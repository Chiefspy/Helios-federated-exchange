# Architecture

## Asset states
`AVAILABLE -> ENCUMBERED -> OUTBOUND -> SPENDABLE`

Transitions are durable and transaction-ID scoped. A financial action cannot be applied twice.

## Equity exchange
1. Validate buyer cash and seller shares at their authoritative operators.
2. Lock the required assets.
3. Exchange durable prepare/commit state across the backbone.
4. Commit once both sides have valid prepared state.
5. Transfer authority using signed certificates.
6. Activate destination balances exactly once.

## NeoDollar transfer
The source marks value OUTBOUND under a durable transaction ID. The destination activates the signed certificate once. Duplicate deliveries return existing state rather than creating another credit.

## Derivatives
CCH is authoritative for derivative collateral and settlement. Capped loss makes the maximum obligation known at opening, allowing full prefunding. If final-price communication is unavailable, the position remains OPEN and collateral remains locked until a valid observation arrives.

## Routing
Inter-exchange traffic uses the backbone. Each new session chooses the fastest valid simple route of at most three links. Routes are recomputed at handshake because orbital motion changes propagation delay.
