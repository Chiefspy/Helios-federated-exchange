"""Reference state-machine primitives for HFX.

This is an explanatory implementation of the protocol rules documented in the
submission, not a production financial system.
"""
from dataclasses import dataclass, field
from enum import Enum

class State(str, Enum):
    AVAILABLE = "AVAILABLE"
    ENCUMBERED = "ENCUMBERED"
    OUTBOUND = "OUTBOUND"
    SPENDABLE = "SPENDABLE"

@dataclass
class Ledger:
    balances: dict[str, float] = field(default_factory=dict)
    tx_state: dict[str, str] = field(default_factory=dict)
    locked: dict[str, float] = field(default_factory=dict)

    def lock(self, txid: str, account: str, amount: float) -> bool:
        if txid in self.tx_state:
            return self.tx_state[txid] in {"PREPARED", "COMMITTED"}
        if amount < 0 or self.balances.get(account, 0.0) < amount:
            return False
        self.balances[account] -= amount
        self.locked[txid] = amount
        self.tx_state[txid] = "PREPARED"
        return True

    def mark_outbound(self, txid: str) -> bool:
        if self.tx_state.get(txid) == "COMMITTED":
            return True
        if self.tx_state.get(txid) != "PREPARED":
            return False
        self.tx_state[txid] = "COMMITTED"
        return True

    def activate_credit(self, txid: str, account: str, amount: float) -> bool:
        key = f"credit:{txid}"
        if self.tx_state.get(key) == "APPLIED":
            return True
        self.balances[account] = self.balances.get(account, 0.0) + amount
        self.tx_state[key] = "APPLIED"
        return True
