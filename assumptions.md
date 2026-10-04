# Assumptions

- Sun-centered geometric J2000 ecliptic coordinates, AU.
- Continuous 86,400-second days.
- Fixed supplied orbital elements are propagated using Keplerian motion.
- Kepler's equation solved by Newton iteration.
- Moving-receiver light time solved by fixed-point iteration.
- Solar obstruction radius: 0.10 AU in the submission model.
- Relay A/B: supplied circular 8 AU orbits, phases 45° and 135°.
- Financial correctness does not rely on transport acknowledgements.
- Application-level transaction state is durable and idempotent.
- Common incidents are not treated as independent packet-loss events.
- Institutions themselves begin with zero assets; client assets fund obligations.
