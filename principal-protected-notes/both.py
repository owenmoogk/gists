from datetime import date

import matplotlib.pyplot as plt


def year_fraction(start_date: date, end_date: date) -> float:
    return (end_date - start_date).days / 365.25


def interpolate(start: float, end: float, progress: float) -> float:
    return start + (end - start) * progress


def after_tax_capital_gain(gross_gain: float, marginal_tax_rate: float) -> float:
    """
    Canadian capital gains treatment:
    only 50% of the capital gain is taxable.
    """
    capital_gains_inclusion_rate = 0.50
    tax = gross_gain * capital_gains_inclusion_rate * marginal_tax_rate
    return gross_gain - tax


def after_tax_income_gain(gross_gain: float, marginal_tax_rate: float) -> float:
    """
    PPN gains are assumed to be taxed as regular income.
    """
    tax = gross_gain * marginal_tax_rate
    return gross_gain - tax


def simulate_since_november():
    # ----------------------------
    # Dates
    # ----------------------------
    start_date = date(2025, 11, 1)
    end_date = date(2026, 5, 4)

    elapsed_years = year_fraction(start_date, end_date)

    # ----------------------------
    # Tax assumptions
    # ----------------------------
    marginal_tax_rate = 0.40

    # ----------------------------
    # PPN assumptions
    # ----------------------------
    ppn_participation_rate = 1.55
    annual_index_point_deduction = 120.0

    starting_index_level = 2_500.0
    ending_index_level_input = 3_000.0

    # IMPORTANT:
    # True  = 2,500 -> 3,000 is BEFORE the 120-point deduction.
    # False = 2,500 -> 3,000 is already the official adjusted PPN index.
    index_levels_are_before_deduction = True

    # ----------------------------
    # VFV assumption
    # ----------------------------
    # Replace this with the actual VFV return over the same period.
    #
    # Example:
    # 0.12 = VFV gained 12% before tax over the same period.
    vfv_return_over_period = 0.12

    # ----------------------------
    # Build graph data
    # ----------------------------
    num_steps = 100

    x_years = []
    vfv_after_tax_percent_gain_history = []
    ppn_after_tax_percent_gain_history = []

    for step in range(num_steps + 1):
        progress = step / num_steps
        years_elapsed_at_step = elapsed_years * progress

        # VFV after-tax percentage gain
        current_vfv_gross_return = vfv_return_over_period * progress
        current_vfv_after_tax_return = after_tax_capital_gain(
            current_vfv_gross_return,
            marginal_tax_rate,
        )

        # PPN index path
        index_before_deduction = interpolate(
            starting_index_level,
            ending_index_level_input,
            progress,
        )

        if index_levels_are_before_deduction:
            index_after_deduction = (
                index_before_deduction
                - annual_index_point_deduction * years_elapsed_at_step
            )
        else:
            index_after_deduction = index_before_deduction

        adjusted_index_return = (
            index_after_deduction - starting_index_level
        ) / starting_index_level

        ppn_gross_return = max(
            0.0,
            adjusted_index_return * ppn_participation_rate,
        )

        ppn_after_tax_return = after_tax_income_gain(
            ppn_gross_return,
            marginal_tax_rate,
        )

        x_years.append(years_elapsed_at_step)
        vfv_after_tax_percent_gain_history.append(current_vfv_after_tax_return * 100)
        ppn_after_tax_percent_gain_history.append(ppn_after_tax_return * 100)

    # ----------------------------
    # Print summary
    # ----------------------------
    final_vfv_after_tax_percent_gain = vfv_after_tax_percent_gain_history[-1]
    final_ppn_after_tax_percent_gain = ppn_after_tax_percent_gain_history[-1]

    total_point_deduction = annual_index_point_deduction * elapsed_years

    if index_levels_are_before_deduction:
        final_ppn_index_level = ending_index_level_input - total_point_deduction
    else:
        final_ppn_index_level = ending_index_level_input

    print("=" * 70)
    print("SINCE NOVEMBER 2025")
    print("=" * 70)
    print(f"Start Date: {start_date}")
    print(f"End Date: {end_date}")
    print(f"Elapsed Years: {elapsed_years:.3f}")
    print()
    print(f"Starting PPN Index Level: {starting_index_level:,.2f}")
    print(f"Input Ending Index Level: {ending_index_level_input:,.2f}")
    print(f"Point Deduction Over Period: {total_point_deduction:,.2f}")
    print(f"Final PPN Index Level Used: {final_ppn_index_level:,.2f}")
    print()
    print(f"VFV After-Tax Gain: {final_vfv_after_tax_percent_gain:.2f}%")
    print(f"PPN After-Tax Gain: {final_ppn_after_tax_percent_gain:.2f}%")
    print("=" * 70)
    print()

    return (
        x_years,
        vfv_after_tax_percent_gain_history,
        ppn_after_tax_percent_gain_history,
    )


def simulate_last_40_years():
    # ----------------------------
    # Tax assumptions
    # ----------------------------
    marginal_tax_rate = 0.40

    # ----------------------------
    # PPN terms
    # ----------------------------
    ppn_participation_rate = 1.55
    ppn_term_length = 3
    annual_index_point_deduction = 120.0

    # This is just the assumed starting index level for each rolling PPN term.
    # A lower starting index makes 120 points more costly in percentage terms.
    # A higher starting index makes 120 points less costly in percentage terms.
    ppn_starting_index_level = 3_000.0

    # Historical S&P 500 Total Returns proxy for VFV from 1984 to 2023
    market_returns = [
        0.0627,
        0.3173,
        0.1867,
        0.0525,
        0.1661,
        0.3169,
        -0.0310,
        0.3047,
        0.0762,
        0.1008,
        0.0132,
        0.3758,
        0.2296,
        0.3336,
        0.2858,
        0.2104,
        -0.0910,
        -0.1189,
        -0.2210,
        0.2868,
        0.1088,
        0.0491,
        0.1579,
        0.0549,
        -0.3849,
        0.2646,
        0.1506,
        0.0211,
        0.1600,
        0.3239,
        0.1369,
        0.0138,
        0.1196,
        0.2183,
        -0.0438,
        0.3149,
        0.1840,
        0.2871,
        -0.1811,
        0.2423,
    ]

    # ----------------------------
    # VFV buy-and-hold
    # ----------------------------
    vfv_gross_value = 1.0
    vfv_gross_value_history = [vfv_gross_value]
    vfv_after_tax_percent_gain_history = [0.0]

    for r in market_returns:
        vfv_gross_value *= 1 + r
        vfv_gross_value_history.append(vfv_gross_value)

        gross_gain = vfv_gross_value - 1.0

        if gross_gain > 0:
            after_tax_gain = after_tax_capital_gain(gross_gain, marginal_tax_rate)
        else:
            # No tax benefit modeled for capital losses.
            after_tax_gain = gross_gain

        vfv_after_tax_value = 1.0 + after_tax_gain
        vfv_after_tax_percent_gain_history.append((vfv_after_tax_value - 1.0) * 100)

    # ----------------------------
    # Rolling 3-year PPN
    # ----------------------------
    ppn_after_tax_value = 1.0
    ppn_after_tax_percent_gain_history = [0.0]

    # This tracks during-term value visually.
    # The actual PPN only pays the variable return at maturity.
    for i in range(0, len(market_returns), ppn_term_length):
        term_returns = market_returns[i : i + ppn_term_length]
        actual_term_length = len(term_returns)

        starting_index_level = ppn_starting_index_level
        ending_index_level = starting_index_level

        for r in term_returns:
            ending_index_level *= 1 + r
            ending_index_level -= annual_index_point_deduction

        adjusted_index_return = (
            ending_index_level - starting_index_level
        ) / starting_index_level

        ppn_gross_return_for_term = max(
            0.0,
            adjusted_index_return * ppn_participation_rate,
        )

        ppn_after_tax_return_for_term = after_tax_income_gain(
            ppn_gross_return_for_term,
            marginal_tax_rate,
        )

        start_value = ppn_after_tax_value
        end_value = ppn_after_tax_value * (1 + ppn_after_tax_return_for_term)

        # Interpolate during the term for graphing only.
        for year in range(1, actual_term_length + 1):
            progress = year / actual_term_length
            interpolated_value = interpolate(start_value, end_value, progress)
            ppn_after_tax_percent_gain_history.append((interpolated_value - 1.0) * 100)

        ppn_after_tax_value = end_value

    years = list(range(len(vfv_after_tax_percent_gain_history)))

    print("=" * 70)
    print("LAST 40 YEARS")
    print("=" * 70)
    print(f"VFV Final After-Tax Gain: {vfv_after_tax_percent_gain_history[-1]:.2f}%")
    print(f"PPN Final After-Tax Gain: {ppn_after_tax_percent_gain_history[-1]:.2f}%")
    print("=" * 70)
    print()

    return (
        years,
        vfv_after_tax_percent_gain_history,
        ppn_after_tax_percent_gain_history,
    )


def plot_results():
    (
        nov_years,
        nov_vfv_after_tax_percent_gain,
        nov_ppn_after_tax_percent_gain,
    ) = simulate_since_november()

    (
        years_40,
        vfv_40_after_tax_percent_gain,
        ppn_40_after_tax_percent_gain,
    ) = simulate_last_40_years()

    # ----------------------------
    # Graph 1: Since November
    # ----------------------------
    plt.figure(figsize=(10, 6))
    plt.plot(
        nov_years,
        nov_vfv_after_tax_percent_gain,
        label="VFV After-Tax Gain",
    )
    plt.plot(
        nov_years,
        nov_ppn_after_tax_percent_gain,
        label="PPN After-Tax Gain",
    )
    plt.title("After-Tax Percentage Gain Since November 2025")
    plt.xlabel("Years Since November 2025")
    plt.ylabel("After-Tax Gain (%)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

    # ----------------------------
    # Graph 2: Last 40 years
    # ----------------------------
    plt.figure(figsize=(10, 6))
    plt.plot(
        years_40,
        vfv_40_after_tax_percent_gain,
        label="VFV Buy-and-Hold After-Tax Gain",
    )
    plt.plot(
        years_40,
        ppn_40_after_tax_percent_gain,
        label="Rolling 3-Year PPN After-Tax Gain",
    )
    plt.title("After-Tax Percentage Gain Over 40 Years")
    plt.xlabel("Years")
    plt.ylabel("After-Tax Gain (%)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    plot_results()
