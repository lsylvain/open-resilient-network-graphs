[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
# open-resilient-network-graphs — A project to develop open specifications for Resilient Network Graphs

**Community-driven, vendor-neutral specifications for quasi-random flat data center networks.**

Goal: Produce vendor-neutral, openly licensed specifications for quasi-random/expander-based flat data center networks, including ShuffleBox-style passive optical components, topology parameters, routing behaviors, and testing methodologies.

Inspired by AWS Resilient Network Graphs (RNG) and earlier work on Jellyfish / expander graphs, we aim to produce open specs that accelerate innovation in high-efficiency, low-power data center interconnects.

### Why This Matters
Modern data centers face exploding power, cabling, and cost pressures — especially for AI workloads.  
AWS demonstrated:
- ~69% fewer routers/switches  
- ~40% lower network power  
- Up to 33% higher throughput  
- Simpler cabling via passive optical ShuffleBoxes

We want to make these benefits available to the entire industry through open, collaborative specifications.

### Project Goals
- Produce **clear, implementable specifications** (not full software/hardware)
- Enable commercial ShuffleBox-style products, routing extensions, and test tools
- Lower barriers for hyperscalers, colocation providers, researchers, and enterprises
- Foster interoperability and incremental adoption

### Core Specifications (In Progress)

1. **Topology Specification**  
   Quasi-random graph models, expansion properties, scaling rules, cabling matrices.

2. **Passive Optical ShuffleBox Specification**  
   Port configurations, internal permutation rules, mechanical/form-factor standards, connector recommendations, test criteria.

3. **Routing & Control Plane Specification**  
   Packet-spraying mechanics (inspired by Spraypoint), waypoint selection, failure handling, integration with existing stacks.

4. **Performance & Validation Framework**  
   Simulation benchmarks, power/cost models, interoperability test suites.

5. **Reference Materials**  
   Topology generators, simulator extensions, example cabling patterns.

### How to Contribute
- **Discussion**: Open an Issue or join the [Discord/Slack/Mailing list] (link TBD)
- **Specs**: Submit Pull Requests against the `specs/` folder
- **Governance**: Apache 2.0 license. Lightweight steering group (open to volunteers)
- **First step**: Review the [Topology v0.1 Draft](specs/topology-v0.1.md)

### Getting Started
```bash
git clone https://github.com/lsylvain/open-resilient-network-graphs.git
cd open-resilient-network-graphs
