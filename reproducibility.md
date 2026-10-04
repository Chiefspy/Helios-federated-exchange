# Reproducibility

## Orbital propagation
For each body, propagate mean anomaly using

`M(t) = M0 + n t`

Solve Kepler's equation

`E - e sin(E) = M`

by Newton iteration, form orbital-plane coordinates, then rotate by argument of periapsis, inclination and longitude of ascending node into the Sun-centered J2000 ecliptic frame.

## Moving light time
Propagation is not computed using only simultaneous endpoint positions. The receiver moves while the signal travels. Iterate arrival time until the light-time solution changes by less than 1 ms.

## Geometry
Test the closest point of the sender-at-emission to receiver-at-arrival segment against the 0.10 AU solar exclusion sphere.

## Sampling
- S3 24-hour access windows: 5-minute samples.
- E4 long-horizon scan: 1-day samples with bisection refinement near boundaries.
- Long-horizon evaluation: 200 years.

## Reported checks
At h0 and h300, all nine settlements had a route to CCH in the evaluated 24-hour windows. The 200-year daily scan reported a viable best route to Ceres at every sampled instant for every settlement.
