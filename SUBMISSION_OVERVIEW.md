# Submission Overview

## Elevator pitch
HFX enables secure interplanetary trading despite extreme delays, using local asset locks, one-time settlement, safe retries, and Ceres-based clearing to make solar-system markets reliable.

## Inspiration
We were inspired by a simple question: how could financial markets work across planets when communication takes hours? That challenge pushed us to redesign trading around space itself.

## Design thesis
Earth financial infrastructure often assumes low-latency communication. HFX instead treats latency, loss, duplication, orbital motion, geometry outages and temporary isolation as normal operating conditions. Safety is maintained locally and durably; communication determines when progress happens, not whether balances remain valid.

## Institutions
Nine settlement operators plus Ceres Clearing House use ten chartered institutions, below the 12-institution limit described in the submission. Institutions begin with zero assets; client accounts remain principals.

## Core protocol
A cross-settlement action receives a durable transaction ID. Assets are encumbered before commitment. Repeated messages are idempotent. A transfer changes authority only through a signed durable transfer certificate, preventing the same balance from becoming spendable at two locations.

## Derivatives
Capped futures are fully funded at Ceres at opening. In the reported example, Ceres Mining and Mars Foundry each lock $30,000 against a maximum $30,000 loss. The $60,000 collateral pool is exclusive to the position.

## Stress case
The chosen incident isolates the Ceres gateway from h478 to h550, beginning two hours before derivative maturity. Price copies cannot reach CCH during the incident, so no unfunded payout is attempted. Collateral remains locked. After connectivity returns, CCH requests the final signed observation and safely resumes settlement.
