# Poker Probability Calculator

`poker_probability_calculator` is a modern Python package and CLI for working with five-card poker odds.

It supports:

- exact probabilities for every standard five-card poker hand category
- Monte Carlo simulation when you want an approximate result
- deterministic hand classification with input validation
- reproducible simulation runs with an optional random seed

## Why This Repo Exists

This project is a compact probability and card-logic exercise that demonstrates:

- practical Python package structure
- CLI design
- deterministic testing for probability-related code
- reproducible simulation behavior
- clean separation between hand evaluation and odds calculation

## Quick Start

Create a virtual environment and install the project in editable mode:

```bash
env -u HTTP_PROXY -u HTTPS_PROXY -u http_proxy -u https_proxy python3 -m venv .venv
source .venv/bin/activate
env -u HTTP_PROXY -u HTTPS_PROXY -u http_proxy -u https_proxy python -m pip install --upgrade pip
env -u HTTP_PROXY -u HTTPS_PROXY -u http_proxy -u https_proxy pip install -e ".[dev]"
```

Run the CLI for an exact probability:

```bash
poker-probability --hand royal-flush --mode exact
```

Run a Monte Carlo estimate:

```bash
poker-probability --hand full-house --mode monte-carlo --simulations 200000 --seed 42
```

## Example Output

```text
Hand: Royal Flush
Mode: Exact
Probability: 0.00000154
Percentage: 0.000154%
Expected frequency: 649,740 hands
```

## Supported Hands

- `royal-flush`
- `straight-flush`
- `four-of-a-kind`
- `full-house`
- `flush`
- `straight`
- `three-of-a-kind`
- `two-pair`
- `one-pair`
- `high-card`

## Development

Run linting and tests:

```bash
ruff check .
pytest
```

GitHub Actions validates the project on pushes and pull requests against Python 3.11, 3.12, and 3.13.

## Notes

- Exact probabilities are based on standard five-card poker combinatorics.
- Monte Carlo mode samples random five-card hands from a standard 52-card deck.
- This project intentionally focuses on five-card hands rather than Texas Hold'em board/runout calculations.
