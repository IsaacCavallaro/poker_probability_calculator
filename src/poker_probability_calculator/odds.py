"""Probability helpers for five-card poker hands."""

from __future__ import annotations

import math
import random

from .cards import create_deck
from .evaluator import HandRank, classify_hand

TOTAL_FIVE_CARD_HANDS = math.comb(52, 5)

EXACT_HAND_COUNTS: dict[HandRank, int] = {
    HandRank.ROYAL_FLUSH: 4,
    HandRank.STRAIGHT_FLUSH: 36,
    HandRank.FOUR_OF_A_KIND: 624,
    HandRank.FULL_HOUSE: 3744,
    HandRank.FLUSH: 5108,
    HandRank.STRAIGHT: 10200,
    HandRank.THREE_OF_A_KIND: 54912,
    HandRank.TWO_PAIR: 123552,
    HandRank.ONE_PAIR: 1_098_240,
    HandRank.HIGH_CARD: 1_302_540,
}


def exact_probability(hand_rank: HandRank) -> float:
    """Return the exact probability of the target hand from a random five-card deal."""
    if hand_rank not in EXACT_HAND_COUNTS:
        raise ValueError(f"Exact probability is not defined for {hand_rank}.")

    return EXACT_HAND_COUNTS[hand_rank] / TOTAL_FIVE_CARD_HANDS


def monte_carlo_probability(
    hand_rank: HandRank,
    simulations: int,
    rng: random.Random | None = None,
) -> float:
    """Estimate a hand probability by random simulation."""
    if simulations <= 0:
        raise ValueError("Simulation count must be greater than zero.")

    generator = rng or random.Random()
    deck = create_deck()
    matches = 0

    for _ in range(simulations):
        hand = generator.sample(deck, 5)
        if classify_hand(hand) == hand_rank:
            matches += 1

    return matches / simulations


def expected_frequency(probability: float) -> int:
    """Return the expected number of hands between occurrences."""
    if probability <= 0:
        raise ValueError("Probability must be greater than zero.")

    return round(1 / probability)
