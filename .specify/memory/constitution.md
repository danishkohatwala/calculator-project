<!--
Sync Impact Report:
- Version change: 1.0.0 → 1.1.0
- Modified principles: None
- Added sections:
  - Code Quality Standards
- Removed sections: None
- Templates requiring updates: None
- Follow-up TODOs: None
-->
# Calculator-Project Constitution

## Core Principles

### I. Test-Driven Development
TDD is mandatory: Tests are written, then code is implemented to make them pass. The Red-Green-Refactor cycle is strictly enforced.

### II. Modern Python
Use Python 3.12+ with type hints for all code. This ensures code is modern, readable, and less prone to runtime errors.

### III. Clean Code
Code must be kept clean, simple, and easy to read.

### IV. Architectural Decision Records
Document all significant architectural decisions using ADRs. This provides a historical record of choices and their rationale.

### V. OOP Principles
Follow essential Object-Oriented Programming principles, including SOLID, DRY (Don't Repeat Yourself), and KISS (Keep It Simple, Stupid).

## Technology Stack

- Python 3.12+
- `uv` for package management
- `pytest` for testing
- All project files must be versioned with `git`.

## Quality Gates

- All tests must pass before merging code.
- Maintain a minimum of 80% code coverage.
- Use `dataclasses` for data structures to ensure immutability and clarity.

## Code Quality Standards

- All functions must include type hints on parameters and return types.
  - Example: `def add(a: float, b: float) -> float:`
- All functions must include docstrings explaining what they do.
  - Example: `"""Add two numbers and return the sum."""`
- Follow PEP 8 naming conventions (lowercase_with_underscores for functions).
- Lines must be under 100 characters.
- No magic numbers; use named constants.
  - Bad: `if x > 10:`
  - Good: `if x > MAX_POWER_EXPONENT:`

## Governance

This Constitution supersedes all other practices. Amendments require documentation, approval, and a migration plan. All PRs and reviews must verify compliance.

**Version**: 1.1.0 | **Ratified**: 2025-11-06 | **Last Amended**: 2025-11-06
