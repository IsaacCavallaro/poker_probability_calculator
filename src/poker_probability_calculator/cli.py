"""Command-line interface for the poker probability calculator."""

from __future__ import annotations

import argparse
import random

from .evaluator import HandRank
from .odds import (
    exact_probability,
    expected_frequency,
    monte_carlo_probability,
)

HAND_CHOICES: dict[str, HandRank] = {
    "royal-flush": HandRank.ROYAL_FLUSH,
    "straight-flush": HandRank.STRAIGHT_FLUSH,
    "four-of-a-kind": HandRank.FOUR_OF_A_KIND,
    "full-house": HandRank.FULL_HOUSE,
    "flush": HandRank.FLUSH,
    "straight": HandRank.STRAIGHT,
    "three-of-a-kind": HandRank.THREE_OF_A_KIND,
    "two-pair": HandRank.TWO_PAIR,
    "one-pair": HandRank.ONE_PAIR,
    "high-card": HandRank.HIGH_CARD,
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="poker-probability",
        description=(
            "Calculate exact or Monte Carlo probabilities for common five-card poker hands."
        ),
    )
    parser.add_argument("--hand", required=True, choices=sorted(HAND_CHOICES))
    parser.add_argument("--mode", choices=("exact", "monte-carlo"), default="exact")
    parser.add_argument("--simulations", type=int, default=100_000)
    parser.add_argument(
        "--seed",
        type=int,
        help="Optional random seed for reproducible Monte Carlo runs.",
    )
    return parser


def _format_label(value: str) -> str:
    return value.replace("_", " ").title()


def render_result(
    hand_rank: HandRank,
    mode: str,
    probability: float,
    simulations: int | None = None,
    seed: int | None = None,
) -> str:
    frequency = expected_frequency(probability)
    lines = [
        f"Hand: {_format_label(hand_rank.value)}",
        f"Mode: {_format_label(mode.replace('-', '_'))}",
        f"Probability: {probability:.8f}",
        f"Percentage: {probability:.6%}",
        f"Expected frequency: {frequency:,} hands",
    ]

    if simulations is not None:
        lines.append(f"Simulations: {simulations:,}")
    if seed is not None:
        lines.append(f"Seed: {seed}")

    return "\n".join(lines)


def main() -> int:
    args = build_parser().parse_args()
    hand_rank = HAND_CHOICES[args.hand]

    if args.mode == "exact":
        probability = exact_probability(hand_rank)
        print(render_result(hand_rank, args.mode, probability))
    else:
        probability = monte_carlo_probability(
            hand_rank,
            args.simulations,
            rng=random.Random(args.seed),
        )
        print(
            render_result(
                hand_rank,
                args.mode,
                probability,
                simulations=args.simulations,
                seed=args.seed,
            )
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
