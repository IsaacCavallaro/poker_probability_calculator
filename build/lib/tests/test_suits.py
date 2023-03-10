# pylint: disable=missing-module-docstring,missing-function-docstring, redefined-outer-name, too-many-function-args,singleton-comparison, duplicate-code
from ..src.suits import (
    is_flush,
    is_full_house,
    is_three_of_a_kind,
    is_straight,
    is_straight_flush,
    is_two_pairs,
    is_four_of_a_kind,
    is_royal_flush,
)
from ..src.main import calculate_probability, create_deck


suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = [
    "Ace",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "Jack",
    "Queen",
    "King",
]
deck = [(suit, rank) for suit in suits for rank in ranks]


def test_is_flush():
    hand = [
        ("Hearts", "Ace"),
        ("Hearts", "5"),
        ("Hearts", "7"),
        ("Hearts", "10"),
        ("Hearts", "King"),
    ]
    assert is_flush(hand) == True


def test_is_full_house():
    hand = [
        ("Hearts", "Ace"),
        ("Diamonds", "Ace"),
        ("Clubs", "Ace"),
        ("Hearts", "King"),
        ("Diamonds", "King"),
    ]
    assert is_full_house(hand) == True


def test_is_three_of_a_kind():
    hand = [
        ("Hearts", "Ace"),
        ("Diamonds", "Ace"),
        ("Clubs", "Ace"),
        ("Hearts", "King"),
        ("Diamonds", "10"),
    ]
    assert is_three_of_a_kind(hand) == True


def test_is_straight():
    hand = [
        ("Hearts", "Ace"),
        ("Diamonds", "10"),
        ("Clubs", "Jack"),
        ("Hearts", "Queen"),
        ("Diamonds", "King"),
    ]
    ranks = [
        "Ace",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
    ]
    assert is_straight(hand, ranks) == True


def test_is_straight_flush():
    hand = [
        ("Hearts", "Ace"),
        ("Hearts", "2"),
        ("Hearts", "3"),
        ("Hearts", "4"),
        ("Hearts", "5"),
    ]
    assert is_straight_flush(hand, ranks) == True


def test_is_two_pairs():
    hand = [
        ("Hearts", "Ace"),
        ("Diamonds", "Ace"),
        ("Clubs", "King"),
        ("Hearts", "King"),
        ("Diamonds", "10"),
    ]
    assert is_two_pairs(hand) == True


def test_is_four_of_a_kind():
    hand = [
        ("Hearts", "Ace"),
        ("Diamonds", "Ace"),
        ("Clubs", "Ace"),
        ("Spades", "Ace"),
        ("Diamonds", "10"),
    ]
    assert is_four_of_a_kind(hand) == True


def test_is_royal_flush():
    hand = [
        ("Hearts", "Ace"),
        ("Hearts", "King"),
        ("Hearts", "Queen"),
        ("Hearts", "Jack"),
        ("Hearts", "10"),
    ]
    assert is_royal_flush(hand) == True


def test_calculate_probability():
    # Define the suits and ranks variables
    suits = ["hearts", "diamonds", "clubs", "spades"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    # Test with a flush hand type and 1000 simulations
    result = calculate_probability("flush", 1000, suits, ranks)
    assert 0 <= result <= 1

    # Test with a royal flush hand type and 500 simulations
    result = calculate_probability("royal flush", 500, suits, ranks)
    assert 0 <= result <= 1


def test_create_deck():
    suits = ["hearts", "diamonds", "clubs", "spades"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    deck = create_deck(suits, ranks)
    assert len(deck) == 52
    assert isinstance(deck, list)
