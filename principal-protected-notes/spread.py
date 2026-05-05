from datetime import date
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np


# ---------------------------------------------------------
# Utility & Tax Functions
# ---------------------------------------------------------
def after_tax_capital_gain_tax(gross_gain: float, marginal_tax_rate: float) -> float:
    """
    Canadian capital gains treatment:
    Only 50% of the capital gain is taxable.

    Returns the TAX owing, not the after-tax gain.
    """
    if gross_gain <= 0:
        return 0.0

    capital_gains_inclusion_rate = 0.50
    return gross_gain * capital_gains_inclusion_rate * marginal_tax_rate


def after_tax_income_gain(gross_gain: float, marginal_tax_rate: float) -> float:
    """
    Income gain after ordinary income tax.
    Used for PPN gains and VFV foreign-income-style distributions.
    """
    if gross_gain <= 0:
        return gross_gain

    tax = gross_gain * marginal_tax_rate
    return gross_gain - tax


# ---------------------------------------------------------
# Global Assumptions
# ---------------------------------------------------------
MARGINAL_TAX_RATE = 0.40
PPN_TERM_LENGTH = 3

# Assumed annual VFV cash distribution yield.
# VFV distributions are simplified here as foreign income taxed at ordinary income rates.
# This is a modeling assumption. Change this if you want to use actual historical yields.
VFV_DISTRIBUTION_YIELD = 0.015

# Calendar-year total returns proxy.
# Interpreted as returns for 1984 through 2023.
START_RETURN_YEAR = 1984

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
def split_total_return_into_price_and_distribution(
    total_return: float,
    distribution_yield: float,
) -> float:
    """
    Given a total return and an assumed distribution yield, infer the price return.

    If:
        total return = (1 + price return) * (1 + distribution yield) - 1

    Then:
        price return = (1 + total return) / (1 + distribution yield) - 1

    This keeps the total-return series intact before dividend tax.
    """
    return (1 + total_return) / (1 + distribution_yield) - 1


def simulate_vfv_buy_and_hold_estate_value():
    """
    Simulates direct VFV investment.

    Important:
    - Unrealized capital gains are NOT taxed during compounding.
    - Distributions are taxed annually and reinvested after tax.
    - Reinvested after-tax distributions increase ACB.
    - The plotted value is after-tax estate/liquidation value:
        market value minus capital gains tax that would be owing on deemed sale.
    """
    market_value = 1.0
    adjusted_cost_base = 1.0

    after_tax_estate_value_history = [1.0]

    for total_return in MARKET_RETURNS:
        price_return = split_total_return_into_price_and_distribution(
            total_return=total_return,
            distribution_yield=VFV_DISTRIBUTION_YIELD,
        )

        # Price appreciation happens tax-deferred.
        market_value *= 1 + price_return

        # Distribution is paid at year-end, taxed, then reinvested.
        gross_distribution = market_value * VFV_DISTRIBUTION_YIELD
        after_tax_distribution = after_tax_income_gain(
            gross_gain=gross_distribution,
            marginal_tax_rate=MARGINAL_TAX_RATE,
        )

        market_value += after_tax_distribution

        # Reinvested after-tax distributions increase ACB.
        adjusted_cost_base += after_tax_distribution

        # Estate/liquidation value:
        # tax is calculated but not removed from the compounding value.
        unrealized_gain = market_value - adjusted_cost_base
        capital_gains_tax_owing = after_tax_capital_gain_tax(
            gross_gain=unrealized_gain,
            marginal_tax_rate=MARGINAL_TAX_RATE,
        )

        after_tax_estate_value = market_value - capital_gains_tax_owing
        after_tax_estate_value_history.append(after_tax_estate_value)

    return after_tax_estate_value_history


def simulate_ppn_full_rollover(leverage: float, annual_fee: float):
    """
    Simulates investing 100% of capital into one PPN at a time.

    Behavior:
    - Invests all available after-tax value into a 3-year PPN.
    - Calculates payoff at maturity only.
    - Does not interpolate or mark to secondary-market value.
    - Rolls the full after-tax maturity value into the next PPN.
    - This is NOT a 1/3-per-year ladder.

    Fee treatment:
    - annual_fee is modeled as a percentage drag on the linked asset value:
        linked asset multiple *= (1 + annual return) * (1 - annual_fee)

    Principal protection:
    - Negative linked returns do not reduce principal.
    - Fees reduce the linked upside, but do not directly erode protected principal.
    """
    ppn_after_tax_value = 1.0
    ppn_after_tax_value_history = [1.0]

    for i in range(0, len(MARKET_RETURNS), PPN_TERM_LENGTH):
        term_returns = MARKET_RETURNS[i : i + PPN_TERM_LENGTH]
        actual_term_length = len(term_returns)

        start_value = ppn_after_tax_value

        linked_asset_multiple_after_fees = 1.0
        for r in term_returns:
            linked_asset_multiple_after_fees *= (1 + r) * (1 - annual_fee)

        adjusted_index_return = linked_asset_multiple_after_fees - 1.0

        ppn_gross_return_for_term = max(
            0.0,
            adjusted_index_return * leverage,
        )

        ppn_after_tax_return_for_term = after_tax_income_gain(
            gross_gain=ppn_gross_return_for_term,
            marginal_tax_rate=MARGINAL_TAX_RATE,
        )

        end_value = start_value * (1 + ppn_after_tax_return_for_term)

        # No secondary-market marking:
        # value stays flat during the term, then jumps at maturity.
        for year_in_term in range(1, actual_term_length + 1):
            if year_in_term < actual_term_length:
                ppn_after_tax_value_history.append(start_value)
            else:
                ppn_after_tax_value_history.append(end_value)

        ppn_after_tax_value = end_value

    return ppn_after_tax_value_history


# ---------------------------------------------------------
# Plotting
# ---------------------------------------------------------
def plot_results():
    # Initial point is end of the year before the first return.
    # Then each following point is after that calendar year's return.
    years = [START_RETURN_YEAR - 1] + list(
        range(START_RETURN_YEAR, START_RETURN_YEAR + len(MARKET_RETURNS))
    )

    vfv_base_history = simulate_vfv_buy_and_hold_estate_value()

    # ====== GRAPH 1: Varying Leverage (Fixed 2% Fee) ======
    leverages = np.arange(1.0, 2.01, 0.1)
    fixed_fee = 0.02

    colors_lev = cm.turbo(np.linspace(0.1, 0.95, len(leverages)))

    plt.figure(figsize=(12, 7))
    plt.plot(
        years,
        vfv_base_history,
        label="VFV Buy & Hold After-Tax Estate Value",
        color="black",
        linewidth=4,
        zorder=10,
    )

    for lev, color in zip(leverages, colors_lev):
        ppn_history = simulate_ppn_full_rollover(
            leverage=lev,
            annual_fee=fixed_fee,
        )

        plt.step(
            years,
            ppn_history,
            where="post",
            label=f"PPN ({lev * 100:.0f}% Lev)",
            color=color,
            linewidth=2,
        )

    plt.title(
        f"After-Tax Estate Value of $1: Varying PPN Leverage "
        f"(Fixed {fixed_fee * 100:.0f}% Annual Fee)",
        fontsize=14,
        fontweight="bold",
    )
    plt.xlabel("Calendar Year", fontsize=12)
    plt.ylabel("After-Tax Estate Value of $1 Initial Investment", fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")
    plt.tight_layout()
    plt.show()

    # ====== GRAPH 2: Varying Fees (Fixed 150% Leverage) ======
    fixed_leverage = 1.50
    fees = np.arange(0.0, 0.081, 0.01)

    colors_fee = cm.turbo(np.linspace(0.1, 0.95, len(fees)))

    plt.figure(figsize=(12, 7))
    plt.plot(
        years,
        vfv_base_history,
        label="VFV Buy & Hold After-Tax Estate Value",
        color="black",
        linewidth=4,
        zorder=10,
    )

    for fee, color in zip(fees, colors_fee):
        ppn_history = simulate_ppn_full_rollover(
            leverage=fixed_leverage,
            annual_fee=fee,
        )

        plt.step(
            years,
            ppn_history,
            where="post",
            label=f"PPN ({fee * 100:.0f}% Fee)",
            color=color,
            linewidth=2,
        )

    plt.title(
        f"After-Tax Estate Value of $1: Varying PPN Fees "
        f"(Fixed {fixed_leverage * 100:.0f}% Leverage)",
        fontsize=14,
        fontweight="bold",
    )
    plt.xlabel("Calendar Year", fontsize=12)
    plt.ylabel("After-Tax Estate Value of $1 Initial Investment", fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    plot_results()
