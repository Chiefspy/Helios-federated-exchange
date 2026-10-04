"""Minimal orbital utilities matching the methodology used by HFX."""
import math

def solve_kepler(M: float, e: float, tol: float = 1e-13, max_iter: int = 50) -> float:
    E = M
    for _ in range(max_iter):
        f = E - e * math.sin(E) - M
        fp = 1.0 - e * math.cos(E)
        step = f / fp
        E -= step
        if abs(step) < tol:
            break
    return E

def orbital_plane_xy(a: float, e: float, E: float):
    return a * (math.cos(E) - e), a * math.sqrt(1 - e*e) * math.sin(E)
