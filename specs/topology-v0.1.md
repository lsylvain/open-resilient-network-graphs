# Open Resilient Network Graphs (OpenRNG) Topology Specification — Version 0.1 (DRAFT)

## 1. Scope
This document defines the requirements and parameters for quasi-random flat topologies suitable for data center scale (1k–100k+ nodes).

## 2. Terminology
- **ShuffleBox**: Passive optical device that applies a fixed permutation to fiber connections.
- **RRG**: Random Regular Graph (or quasi-random variant).
- **Expansion Factor**: Minimum number of edge-disjoint paths between any two nodes.

## 3. Required Properties
- Diameter ≤ 3–4 hops in steady state
- Bisection bandwidth ≥ 50% of ideal
- Resilience: tolerate k simultaneous link/switch failures with graceful degradation
- Incremental expandability without full recabling

## 4. Mathematical Model
- Base graph: (n, d) quasi-random regular graph
- Construction method: combination of deterministic shuffles + quasi-random inter-box cabling
- Recommended parameters (initial):
  - Switch radix: 64–128 ports
  - Number of ShuffleBox layers: 1–2
  - Target node degree: ...

## 5. Cabling Specification
- MPO-12 / MPO-16 connector recommendations
- Color coding and labeling standard
- Shuffle permutation tables (to be provided as CSV / Python generator)

## 6. Validation Requirements
- Simulation: must achieve ≥ X% of fat-tree performance in Y metric
- Physical: insertion loss < Z dB, return loss < ...

## Open Questions / Next Steps
- Exact permutation algorithms
- Heterogeneity support (mixed switch types)
- ...
