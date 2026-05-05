import matplotlib.pyplot as plt


def simulate_investments():
    # --- Parameters ---
    initial_investment = 10000.0
    marginal_tax_rate = 0.40
    capital_gains_tax_rate = 0.20

    # For this specific PPN
    ppn_participation_rate = 1.55
    term_length = 3

    # Index assumptions
    # This is the index level from the PPN document as of July 31, 2025.
    # The actual Initial Index Level would be the closing index level on the Initial Valuation Date.
    initial_index_level = 3000

    # This is the synthetic dividend deduction from the PPN document.
    annual_index_point_deduction = 120.0

    # Historical S&P 500 Total Returns (proxy for VFV) from 1984 to 2023 (40 years)
    sp500_returns = [
        0.0627,
        0.3173,
        0.1867,
        0.0525,
        0.1661,
        0.3169,
        -0.0310,
        0.3047,
        0.0762,
        0.1008,  # 1984 - 1993
        0.0132,
        0.3758,
        0.2296,
        0.3336,
        0.2858,
        0.2104,
        -0.0910,
        -0.1189,
        -0.2210,
        0.2868,  # 1994 - 2003
        0.1088,
        0.0491,
        0.1579,
        0.0549,
        -0.3849,
        0.2646,
        0.1506,
        0.0211,
        0.1600,
        0.3239,  # 2004 - 2013
        0.1369,
        0.0138,
        0.1196,
        0.2183,
        -0.0438,
        0.3149,
        0.1840,
        0.2871,
        -0.1811,
        0.2423,  # 2014 - 2023
    ]

    # --- 1. VFV Simulation (Buy and Hold) ---
    vfv_value = initial_investment
    vfv_history = [vfv_value]

    for r in sp500_returns:
        vfv_value *= 1 + r
        vfv_history.append(vfv_value)

    # Calculate capital gains tax at the very end
    vfv_total_gain = vfv_value - initial_investment
    vfv_tax_paid = vfv_total_gain * capital_gains_tax_rate
    vfv_net_final = vfv_value - vfv_tax_paid

    # --- 2. PPN Simulation ---
    ppn_principal = initial_investment
    ppn_history = [ppn_principal]
    total_ppn_tax_paid = 0

    # Process in PPN term chunks
    for i in range(0, len(sp500_returns), term_length):
        term_returns = sp500_returns[i : i + term_length]
        actual_term_length = len(term_returns)

        # Start each new PPN term with the index at the same initial level.
        # This approximates buying a new note at par each term.
        starting_index_level = initial_index_level
        ending_index_level = starting_index_level

        # Apply total return first, then subtract the annual 120-point deduction.
        # The real product calculates this daily, but this annual-return simulation
        # approximates it once per year.
        for r in term_returns:
            ending_index_level *= 1 + r
            ending_index_level -= annual_index_point_deduction

        cumulative_index_return = (
            ending_index_level - starting_index_level
        ) / starting_index_level

        # Apply PPN logic:
        # - If adjusted index return is positive, investor receives participation rate times upside.
        # - If adjusted index return is zero or negative, investor receives no variable return.
        if cumulative_index_return > 0:
            ppn_return = cumulative_index_return * ppn_participation_rate
        else:
            ppn_return = 0.0

        # Calculate earnings and tax
        gross_earnings = ppn_principal * ppn_return
        tax_on_earnings = gross_earnings * marginal_tax_rate
        total_ppn_tax_paid += tax_on_earnings

        net_earnings = gross_earnings - tax_on_earnings

        # Visual interpolation only.
        # The actual PPN pays the variable return only at maturity.
        start_val = ppn_principal
        end_val = ppn_principal + net_earnings

        for year in range(1, actual_term_length + 1):
            current_interpolated_value = start_val + (
                net_earnings * (year / actual_term_length)
            )
            ppn_history.append(current_interpolated_value)

        # Reinvest after-tax proceeds into the next PPN term
        ppn_principal = end_val

    ppn_net_final = ppn_principal

    # --- Results Output ---
    print("=" * 50)
    print("40-YEAR INVESTMENT SIMULATION RESULTS")
    print("=" * 50)
    print(f"Initial Investment: ${initial_investment:,.2f}\n")

    print("OPTION 1: VFV (Buy and Hold)")
    print(f"Gross Final Value: ${vfv_value:,.2f}")
    print(f"Capital Gains Tax Paid (End): ${vfv_tax_paid:,.2f}")
    print(f"NET AFTER-TAX VALUE: ${vfv_net_final:,.2f}\n")

    print("OPTION 2: PPN")
    print(f"Participation Rate: {ppn_participation_rate:.0%}")
    print(f"Term Length: {term_length} years")
    print(f"Starting Index Level Used: {initial_index_level:,.2f}")
    print(f"Annual Index Point Deduction: {annual_index_point_deduction:,.2f}")
    print(f"Total Income Tax Paid Over Simulation: ${total_ppn_tax_paid:,.2f}")
    print(f"NET AFTER-TAX VALUE: ${ppn_net_final:,.2f}\n")

    print("DIFFERENCE:")
    if vfv_net_final > ppn_net_final:
        print(f"VFV outperformed the PPN by ${vfv_net_final - ppn_net_final:,.2f}")
    else:
        print(f"PPN outperformed VFV by ${ppn_net_final - vfv_net_final:,.2f}")
    print("=" * 50)

    # --- Plotting ---
    years = range(len(vfv_history))

    plt.figure(figsize=(10, 6))
    plt.plot(years, vfv_history, label="VFV (Pre-Tax Growth)", color="blue")
    plt.plot(
        range(len(ppn_history)),
        ppn_history,
        label="PPN (After-Tax Growth, With 120-Point Deduction)",
        color="orange",
    )

    # Add a marker for the sudden tax drop at year 40 for VFV
    plt.plot(
        [40, 40],
        [vfv_value, vfv_net_final],
        color="blue",
        linestyle="--",
        label="VFV Cap Gains Tax",
    )
    plt.scatter([40], [vfv_net_final], color="blue", zorder=5)

    plt.title("VFV vs. PPN With 120-Point Annual Index Deduction")
    plt.xlabel("Years")
    plt.ylabel("Portfolio Value ($CAD)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    simulate_investments()
