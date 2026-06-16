# Contributing to OpenRNG

Thank you for your interest in contributing to **OpenRNG**! This is a community-driven project focused on open specifications for quasi-random flat data center networks.

## How to Contribute

### 1. Discussion & Ideas
- Open an **Issue** for questions, suggestions, bug reports, or new ideas.
- Comment on existing Issues or the original X thread.
- Reach out directly if you prefer.

### 2. Spec Contributions
- All specifications live in the `specs/` folder (Markdown files).
- Follow the style of the existing drafts (clear sections: Scope, Requirements, Open Items).
- Create a new branch for your changes and open a **Pull Request**.
- Reference any related Issues in your PR description.

### 3. Code & Tool Contributions
- Python scripts and tools go in the `tools/` folder.
- Keep code compatible with Python 3.8+.
- Include docstrings and example usage at the bottom.
- Update the README if you add major new functionality.

### 4. Sample Data & Outputs
- Generated files (CSV, plots, etc.) should be added to the `examples/` folder.
- Include a short description in the commit message.

### Development Setup
```bash
git clone https://github.com/lsylvain/open-resilient-network-graphs.git
cd open-resilient-network-graphs

# For visualization tools
pip install networkx matplotlib
