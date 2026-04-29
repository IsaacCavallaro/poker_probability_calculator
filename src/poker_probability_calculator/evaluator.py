"""Poker hand classification logic."""

from __future__ import annotations

from collections import Counter
from enum import StrEnum

from .cards import RANK_TO_VALUE, SUITS, Card


class HandRank(StrEnum):
    ROYAL_FLUSH = "royal_flush"
    STRAIGHT_FLUSH = "straight_flush"
    FOUR_OF_A_KIND = "four_of_a_kind"
    FULL_HOUSE = "full_house"
    FLUSH = "flush"
    STRAIGHT = "straight"
    THREE_OF_A_KIND = "three_of_a_kind"
    TWO_PAIR = "two_pair"
    ONE_PAIR = "one_pair"
    HIGH_CARD = "high_card"
    OTHER = "high_card"


def _validate_hand(hand: list[Card]) -> None:
    if len(hand) != 5:
        raise ValueError("A five-card hand is required.")

    if len(set(hand)) != 5:
        raise ValueError("A hand cannot contain duplicate cards.")

    for suit, rank in hand:
        if suit not in SUITS:
            raise ValueError(f"Unsupported suit: {suit}.")
        if rank not in RANK_TO_VALUE:
            raise ValueError(f"Unsupported rank: {rank}.")


def _rank_values(hand: list[Card]) -> list[int]:
    return sorted(RANK_TO_VALUE[rank] for _, rank in hand)


def _is_flush(hand: list[Card]) -> bool:
    return len({suit for suit, _ in hand}) == 1


def _is_straight(hand: list[Card]) -> bool:
    values = _rank_values(hand)
    if len(set(values)) != 5:
        return False

    if values == [2, 3, 4, 5, 14]:
        return True

    return values == list(range(values[0], values[0] + 5))


def classify_hand(hand: list[Card]) -> HandRank:
    """Return the poker classification for a five-card hand."""
    _validate_hand(hand)

    counts = sorted(Counter(rank for _, rank in hand).values(), reverse=True)
    is_flush = _is_flush(hand)
    is_straight = _is_straight(hand)
    values = set(_rank_values(hand))

    if is_flush and values == {10, 11, 12, 13, 14}:
        return HandRank.ROYAL_FLUSH
    if is_flush and is_straight:
        return HandRank.STRAIGHT_FLUSH
    if counts == [4, 1]:
        return HandRank.FOUR_OF_A_KIND
    if counts == [3, 2]:
        return HandRank.FULL_HOUSE
    if is_flush:
        return HandRank.FLUSH
    if is_straight:
        return HandRank.STRAIGHT
    if counts == [3, 1, 1]:
        return HandRank.THREE_OF_A_KIND
    if counts == [2, 2, 1]:
        return HandRank.TWO_PAIR
    if counts == [2, 1, 1, 1]:
        return HandRank.ONE_PAIR
    return HandRank.HIGH_CARD
