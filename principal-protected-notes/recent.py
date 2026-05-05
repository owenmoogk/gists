from datetime import date

import matplotlib.pyplot as plt


def year_fraction(start_date: date, end_date: date) -> float:
    return (end_date - start_date).days / 365.25


def interpolate(start: float, end: float, t: float) -> float:
    return start + (end - start) * t


def simulate_ppn_vs_vfv_since_november():
    # ----------------------------
    # Dates
    # ----------------------------
    start_date = date(2025, 11, 1)
    end_date = date(2026, 5, 4)

    elapsed_years = year_fraction(start_date, end_date)

    # ----------------------------
    # Investment assumptions
    # ----------------------------
    initial_investment = 10_000.00
    marginal_tax_rate = 0.40
    capital_gains_tax_rate = 0.20

    # ----------------------------
    # PPN terms
    # ----------------------------
    participation_rate = 1.55
    annual_index_point_deduction = 120.0

    starting_index_level = 2_500.0
    ending_index_level_input = 3_000.0

    # IMPORTANT:
    # True  = 2,500 -> 3,000 is the gross/underlying index BEFORE the 120-point deduction.
    # False = 2,500 -> 3,000 is already the official adjusted-return PPN index.
    index_levels_are_before_deduction = True

    # ----------------------------
    # VFV assumption
    # ----------------------------
    # Replace this with actual VFV price return / total return over the same period.
    #
    # Example:
    # 0.12 = VFV gained 12% before tax over the same period.
    vfv_return_over_period = 0.12

    # ----------------------------
    # Build monthly-ish paths
    # ----------------------------
    num_steps = 100

    x_years = []
    ppn_index_without_deduction_history = []
    ppn_index_with_deduction_history = []
    ppn_after_tax_gain_history = []
    vfv_after_tax_gain_history = []

    for step in range(num_steps + 1):
        progress = step / num_steps
        years_elapsed_at_step = elapsed_years * progress

        # Gross/index input path
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

        ppn_gross_return = max(0.0, adjusted_index_return * participation_rate)

        ppn_gross_gain = initial_investment * ppn_gross_return
        ppn_tax = ppn_gross_gain * marginal_tax_rate
        ppn_after_tax_gain = ppn_gross_gain - ppn_tax

        # VFV path, linearly interpolated by total return over this period.
        # This is for graphing. For a real chart, replace this with actual daily/monthly VFV prices.
        current_vfv_return = vfv_return_over_period * progress
        vfv_gross_gain = initial_investment * current_vfv_return
        vfv_tax = vfv_gross_gain * capital_gains_tax_rate
        vfv_after_tax_gain = vfv_gross_gain - vfv_tax

        x_years.append(years_elapsed_at_step)
        ppn_index_without_deduction_history.append(index_before_deduction)
        ppn_index_with_deduction_history.append(index_after_deduction)
        ppn_after_tax_gain_history.append(ppn_after_tax_gain)
        vfv_after_tax_gain_history.append(vfv_after_tax_gain)

    # ----------------------------
    # Final values
    # ----------------------------
    total_point_deduction = annual_index_point_deduction * elapsed_years

    if index_levels_are_before_deduction:
        final_ppn_index_level = ending_index_level_input - total_point_deduction
    else:
        final_ppn_index_level = ending_index_level_input

    ppn_adjusted_index_return = (
        final_ppn_index_level - starting_index_level
    ) / starting_index_level

    ppn_gross_return = max(0.0, ppn_adjusted_index_return * participation_rate)
    ppn_gross_gain = initial_investment * ppn_gross_return
    ppn_tax = ppn_gross_gain * marginal_tax_rate
    ppn_after_tax_gain = ppn_gross_gain - ppn_tax

    vfv_gross_gain = initial_investment * vfv_return_over_period
    vfv_tax = vfv_gross_gain * capital_gains_tax_rate
    vfv_after_tax_gain = vfv_gross_gain - vfv_tax

    # ----------------------------
    # Print summary
    # ----------------------------
    print("=" * 70)
    print("VFV VS PPN SINCE NOVEMBER 2025")
    print("=" * 70)
    print(f"Start Date: {start_date}")
    print(f"End Date: {end_date}")
    print(f"Elapsed Years: {elapsed_years:.3f}")
    print()
    print(f"Initial Investment: ${initial_investment:,.2f}")
    print()
    print("PPN INDEX")
    print(f"Starting Index Level: {starting_index_level:,.2f}")
    print(f"Input Ending Index Level: {ending_index_level_input:,.2f}")
    print(f"Annual Point Deduction: {annual_index_point_deduction:,.2f}")
    print(f"Point Deduction Over Period: {total_point_deduction:,.2f}")
    print(f"Final PPN Index Level Used: {final_ppn_index_level:,.2f}")
    print(f"Adjusted Index Return Used: {ppn_adjusted_index_return:.2%}")
    print()
    print("PPN AFTER-TAX RESULT")
    print(f"Participation Rate: {participation_rate:.2%}")
    print(f"Gross PPN Return: {ppn_gross_return:.2%}")
    print(f"Gross PPN Gain: ${ppn_gross_gain:,.2f}")
    print(f"Tax on PPN Gain: ${ppn_tax:,.2f}")
    print(f"After-Tax PPN Gain: ${ppn_after_tax_gain:,.2f}")
    print()
    print("VFV AFTER-TAX RESULT")
    print(f"VFV Return Over Period: {vfv_return_over_period:.2%}")
    print(f"Gross VFV Gain: ${vfv_gross_gain:,.2f}")
    print(f"Capital Gains Tax on VFV Gain: ${vfv_tax:,.2f}")
    print(f"After-Tax VFV Gain: ${vfv_after_tax_gain:,.2f}")
    print()
    print("DIFFERENCE")
    difference = ppn_after_tax_gain - vfv_after_tax_gain
    if difference > 0:
        print(f"PPN after-tax gain is higher by ${difference:,.2f}")
    else:
        print(f"VFV after-tax gain is higher by ${-difference:,.2f}")
    print("=" * 70)

    # ----------------------------
    # Graph 1: index levels
    # ----------------------------
    plt.figure(figsize=(10, 6))
    plt.plot(
        x_years,
        ppn_index_without_deduction_history,
        label="Index Before 120-Point Deduction",
    )
    plt.plot(
        x_years,
        ppn_index_with_deduction_history,
        label="Index After 120-Point Deduction",
    )
    plt.title("PPN Index Level: Effect of 120-Point Annual Deduction")
    plt.xlabel("Years Since November 2025")
    plt.ylabel("Index Level / Points")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

    # ----------------------------
    # Graph 2: after-tax gains
    # ----------------------------
    plt.figure(figsize=(10, 6))
    plt.plot(
        x_years,
        vfv_after_tax_gain_history,
        label="VFV After-Tax Gain",
    )
    plt.plot(
        x_years,
        ppn_after_tax_gain_history,
        label="PPN After-Tax Gain",
    )
    plt.title("After-Tax Gain Comparison: VFV vs PPN")
    plt.xlabel("Years Since November 2025")
    plt.ylabel("After-Tax Gain ($CAD)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    simulate_ppn_vs_vfv_since_november()
