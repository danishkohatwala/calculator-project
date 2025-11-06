<!--
Sync Impact Report:
- Version change: 1.1.0 → 1.2.0
- Modified principles:
  - III. Clean Code
  - IV. Architectural Decision Records
  - V. OOP Principles
- Added sections:
  - Error Handling
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
Code must be kept clean, simple, and easy to read. For a concrete set of rules, we will follow the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html).

### IV. Architectural Decision Records
Document all significant architectural decisions using ADRs. A decision is considered "significant" if it:
- Introduces a new third-party dependency.
- Changes the database schema.
- Introduces a new service or component.
- Changes the deployment strategy.

### V. OOP Principles
Follow essential Object-Oriented Programming principles, including SOLID, DRY (Don't Repeat Yourself), and KISS (Keep It Simple, Stupid). For example:
- **Single Responsibility Principle:** A class should have only one reason to change. For instance, a `Calculator` class should perform calculations, but not handle user input.
- **Don't Repeat Yourself:** If you find yourself writing the same code in multiple places, refactor it into a reusable function or class.

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

## Error Handling

- Use exceptions for error handling. Do not return error codes.
- Create custom exception classes for specific error conditions.
- All user-facing errors should be logged with a unique ID that can be used to track the error in the logs.

## Governance

This Constitution supersedes all other practices. Amendments require documentation, approval, and a migration plan. All PRs and reviews must verify compliance.

**Version**: 1.2.0 | **Ratified**: 2025-11-06 | **Last Amended**: 2025-11-06