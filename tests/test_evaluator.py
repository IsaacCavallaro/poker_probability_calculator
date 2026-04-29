import pytest

from poker_probability_calculator.evaluator import HandRank, classify_hand


def test_classify_royal_flush() -> None:
    hand = [
        ("hearts", "10"),
        ("hearts", "jack"),
        ("hearts", "queen"),
        ("hearts", "king"),
        ("hearts", "ace"),
    ]

    assert classify_hand(hand) == HandRank.ROYAL_FLUSH


def test_classify_full_house() -> None:
    hand = [
        ("hearts", "ace"),
        ("diamonds", "ace"),
        ("clubs", "ace"),
        ("spades", "king"),
        ("hearts", "king"),
    ]

    assert classify_hand(hand) == HandRank.FULL_HOUSE


def test_classify_ace_low_straight() -> None:
    hand = [
        ("hearts", "ace"),
        ("diamonds", "2"),
        ("clubs", "3"),
        ("spades", "4"),
        ("hearts", "5"),
    ]

    assert classify_hand(hand) == HandRank.STRAIGHT


def test_classify_other() -> None:
    hand = [
        ("hearts", "ace"),
        ("diamonds", "2"),
        ("clubs", "4"),
        ("spades", "8"),
        ("hearts", "jack"),
    ]

    assert classify_hand(hand) == HandRank.HIGH_CARD


def test_classify_one_pair() -> None:
    hand = [
        ("hearts", "9"),
        ("diamonds", "9"),
        ("clubs", "2"),
        ("spades", "7"),
        ("hearts", "queen"),
    ]

    assert classify_hand(hand) == HandRank.ONE_PAIR


def test_duplicate_cards_raise_error() -> None:
    hand = [
        ("hearts", "ace"),
        ("hearts", "ace"),
        ("clubs", "4"),
        ("spades", "8"),
        ("diamonds", "jack"),
    ]

    with pytest.raises(ValueError, match="duplicate cards"):
        classify_hand(hand)


def test_invalid_rank_raises_error() -> None:
    hand = [
        ("hearts", "1"),
        ("diamonds", "2"),
        ("clubs", "4"),
        ("spades", "8"),
        ("hearts", "jack"),
    ]

    with pytest.raises(ValueError, match="Unsupported rank"):
        classify_hand(hand)
