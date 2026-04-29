from poker_probability_calculator.cli import render_result
from poker_probability_calculator.evaluator import HandRank


def test_render_result_contains_expected_summary() -> None:
    output = render_result(HandRank.FULL_HOUSE, "exact", 0.00144058)

    assert "Hand: Full House" in output
    assert "Mode: Exact" in output
    assert "Expected frequency:" in output


def test_render_result_includes_simulation_details_when_present() -> None:
    output = render_result(
        HandRank.ONE_PAIR,
        "monte-carlo",
        0.421,
        simulations=250_000,
        seed=42,
    )

    assert "Hand: One Pair" in output
    assert "Mode: Monte Carlo" in output
    assert "Simulations: 250,000" in output
    assert "Seed: 42" in output
