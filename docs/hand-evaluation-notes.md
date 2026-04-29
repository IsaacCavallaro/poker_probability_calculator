# Hand Evaluation Notes

The project evaluates standard five-card poker hands with a deterministic classifier.

Supported ranked outcomes:

- royal flush
- straight flush
- four of a kind
- full house
- flush
- straight
- three of a kind
- two pair
- one pair
- high card

Implementation notes:

- Straights support the ace-low wheel (`A-2-3-4-5`).
- Royal flush is treated as a distinct result from straight flush.
- Hands are validated to reject duplicate cards and unsupported suit/rank values.
- Exact probability mode uses standard five-card combinatoric counts.
- Monte Carlo mode draws random five-card hands from a standard 52-card deck.
