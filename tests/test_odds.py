import random

import pytest

from poker_probability_calculator.evaluator import HandRank
from poker_probability_calculator.odds import (
    exact_probability,
    expected_frequency,
    monte_carlo_probability,
)


def test_exact_probability_for_royal_flush() -> None:
    assert exact_probability(HandRank.ROYAL_FLUSH) == 4 / 2598960


def test_expected_frequency_for_royal_flush() -> None:
    assert expected_frequency(4 / 2598960) == 649740


def test_exact_probability_for_high_card() -> None:
    assert exact_probability(HandRank.HIGH_CARD) == 1302540 / 2598960


def test_monte_carlo_probability_stays_in_range() -> None:
    probability = monte_carlo_probability(
        HandRank.FLUSH,
        simulations=500,
        rng=random.Random(7),
    )

    assert 0 <= probability <= 1


def test_monte_carlo_probability_requires_positive_simulations() -> None:
    with pytest.raises(ValueError, match="greater than zero"):
        monte_carlo_probability(HandRank.FLUSH, simulations=0)
