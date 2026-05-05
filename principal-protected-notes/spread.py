from datetime import date
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np


# ---------------------------------------------------------
# Utility & Tax Functions
# ---------------------------------------------------------
def interpolate(start: float, end: float, progress: float) -> float:
    return start + (end - start) * progress


def after_tax_capital_gain(gross_gain: float, marginal_tax_rate: float) -> float:
    """
    Canadian capital gains treatment:
    Only 50% of the capital gain is taxable.

    If marginal_tax_rate is 0.40, the effective tax applied here
    is 0.40 * 0.50 = 0.20 (20%).
    """
    capital_gains_inclusion_rate = 0.50
    tax = gross_gain * capital_gains_inclusion_rate * marginal_tax_rate
    return gross_gain - tax


def after_tax_income_gain(gross_gain: float, marginal_tax_rate: float) -> float:
    """
    PPN gains are assumed to be taxed as regular income.

    If marginal_tax_rate is 0.40, the effective tax applied here
    is a flat 40%.
    """
    tax = gross_gain * marginal_tax_rate
    return gross_gain - tax


# ---------------------------------------------------------
# Global Assumptions
# ---------------------------------------------------------
MARGINAL_TAX_RATE = 0.40
PPN_TERM_LENGTH = 3

# Historical S&P 500 Total Returns proxy for VFV from 1984 to 2023
MARKET_RETURNS = [
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


# ---------------------------------------------------------
# Simulation Engines
# ---------------------------------------------------------
def simulate_vfv_buy_and_hold():
    """Simulates direct VFV investment, taxing unrealized capital gains."""
    vfv_gross_value = 1.0
    vfv_after_tax_percent_gain_history = [0.0]

    for r in MARKET_RETURNS:
        vfv_gross_value *= 1 + r
        gross_gain = vfv_gross_value - 1.0

        if gross_gain > 0:
            after_tax_gain = after_tax_capital_gain(gross_gain, MARGINAL_TAX_RATE)
        else:
            # No tax benefit modeled for capital losses.
            after_tax_gain = gross_gain

        vfv_after_tax_value = 1.0 + after_tax_gain
        vfv_after_tax_percent_gain_history.append((vfv_after_tax_value - 1.0) * 100)

    return vfv_after_tax_percent_gain_history


def simulate_ppn(leverage: float, annual_fee: float):
    """Simulates rolling PPN terms with varying leverage and fees."""
    ppn_after_tax_value = 1.0
    ppn_after_tax_percent_gain_history = [0.0]

    # Process in 3-year rolling blocks
    for i in range(0, len(MARKET_RETURNS), PPN_TERM_LENGTH):
        term_returns = MARKET_RETURNS[i : i + PPN_TERM_LENGTH]
        actual_term_length = len(term_returns)

        # Apply annual fee drag to the fund's return
        fund_gross_multiple = 1.0
        for r in term_returns:
            fund_gross_multiple *= 1 + r - annual_fee

        adjusted_index_return = fund_gross_multiple - 1.0

        # PPN protects downside (floor at 0), applies leverage to upside
        ppn_gross_return_for_term = max(
            0.0,
            adjusted_index_return * leverage,
        )

        ppn_after_tax_return_for_term = after_tax_income_gain(
            ppn_gross_return_for_term,
            MARGINAL_TAX_RATE,
        )

        start_value = ppn_after_tax_value
        end_value = ppn_after_tax_value * (1 + ppn_after_tax_return_for_term)

        # Interpolate during the term for graphing purposes only
        for year in range(1, actual_term_length + 1):
            progress = year / actual_term_length
            interpolated_value = interpolate(start_value, end_value, progress)
            ppn_after_tax_percent_gain_history.append((interpolated_value - 1.0) * 100)

        # Reset start for next term
        ppn_after_tax_value = end_value

    return ppn_after_tax_percent_gain_history


# ---------------------------------------------------------
# Plotting
# ---------------------------------------------------------
def plot_results():
    years = list(range(len(MARKET_RETURNS) + 1))
    vfv_base_history = simulate_vfv_buy_and_hold()

    # ====== GRAPH 1: Varying Leverage (Fixed 2% Fee) ======
    leverages = np.arange(1.0, 2.01, 0.1)  # 100% to 200%
    fixed_fee = 0.02

    # Use 'turbo' colormap for highly distinct, rainbow-like contrast
    colors_lev = cm.turbo(np.linspace(0.1, 0.95, len(leverages)))

    plt.figure(figsize=(12, 7))
    plt.plot(
        years,
        vfv_base_history,
        label="Base VFV (Buy & Hold)",
        color="black",
        linewidth=4,
        zorder=10,
    )

    for lev, color in zip(leverages, colors_lev):
        ppn_history = simulate_ppn(leverage=lev, annual_fee=fixed_fee)
        plt.plot(
            years,
            ppn_history,
            label=f"PPN ({lev * 100:.0f}% Lev)",
            color=color,
            linewidth=2,
        )

    plt.title(
        f"After-Tax Gains Over 40 Years: Varying PPN Leverage (Fixed {fixed_fee * 100:.0f}% Fee)",
        fontsize=14,
        fontweight="bold",
    )
    plt.xlabel("Years", fontsize=12)
    plt.ylabel("After-Tax Gain (%)", fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")
    plt.tight_layout()
    plt.show()

    # ====== GRAPH 2: Varying Fees (Fixed 150% Leverage) ======
    fixed_leverage = 1.50
    fees = np.arange(0.0, 0.081, 0.01)  # 0% to 8%

    # Use 'turbo' colormap for highly distinct, rainbow-like contrast
    colors_fee = cm.turbo(np.linspace(0.1, 0.95, len(fees)))

    plt.figure(figsize=(12, 7))
    plt.plot(
        years,
        vfv_base_history,
        label="Base VFV (Buy & Hold)",
        color="black",
        linewidth=4,
        zorder=10,
    )

    for fee, color in zip(fees, colors_fee):
        ppn_history = simulate_ppn(leverage=fixed_leverage, annual_fee=fee)
        plt.plot(
            years,
            ppn_history,
            label=f"PPN ({fee * 100:.0f}% Fee)",
            color=color,
            linewidth=2,
        )

    plt.title(
        f"After-Tax Gains Over 40 Years: Varying PPN Fees (Fixed {fixed_leverage * 100:.0f}% Leverage)",
        fontsize=14,
        fontweight="bold",
    )
    plt.xlabel("Years", fontsize=12)
    plt.ylabel("After-Tax Gain (%)", fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    plot_results()
