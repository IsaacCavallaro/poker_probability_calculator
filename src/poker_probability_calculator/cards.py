"""Card constants and deck helpers."""

from __future__ import annotations

from typing import TypeAlias

Card: TypeAlias = tuple[str, str]

SUITS: tuple[str, ...] = ("hearts", "diamonds", "clubs", "spades")
RANKS: tuple[str, ...] = (
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "jack",
    "queen",
    "king",
    "ace",
)

RANK_TO_VALUE: dict[str, int] = {rank: index + 2 for index, rank in enumerate(RANKS)}
DECK: tuple[Card, ...] = tuple((suit, rank) for suit in SUITS for rank in RANKS)


def create_deck() -> list[Card]:
    """Return a fresh mutable deck."""
    return list(DECK)
