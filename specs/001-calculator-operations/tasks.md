# Tasks: Basic Calculator Operations

**Input**: Design documents from `/specs/001-calculator-operations/`
**Prerequisites**: plan.md (required), spec.md (required for user stories)

**Tests**: Tests are required for this feature.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create project structure: `src/calculator/` and `tests/` directories.

---

## Phase 2: User Story 1 - Add two numbers (Priority: P1) 🎯 MVP

**Goal**: Implement the `add` function.

**Independent Test**: The `add` function can be tested independently.

### Tests for User Story 1 ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T002 [P] [US1] Create `tests/test_operations.py` and write tests for the `add` function.

### Implementation for User Story 1

- [ ] T003 [US1] Create `src/calculator/operations.py` and implement the `add` function.

---

## Phase 3: User Story 2 - Subtract two numbers (Priority: P1)

**Goal**: Implement the `subtract` function.

**Independent Test**: The `subtract` function can be tested independently.

### Tests for User Story 2 ⚠️

- [ ] T004 [P] [US2] Write tests for the `subtract` function in `tests/test_operations.py`.

### Implementation for User Story 2

- [ ] T005 [US2] Implement the `subtract` function in `src/calculator/operations.py`.

---

## Phase 4: User Story 3 - Multiply two numbers (Priority: P1)

**Goal**: Implement the `multiply` function.

**Independent Test**: The `multiply` function can be tested independently.

### Tests for User Story 3 ⚠️

- [ ] T006 [P] [US3] Write tests for the `multiply` function in `tests/test_operations.py`.

### Implementation for User Story 3

- [ ] T007 [US3] Implement the `multiply` function in `src/calculator/operations.py`.

---

## Phase 5: User Story 4 - Divide two numbers (Priority: P1)

**Goal**: Implement the `divide` function.

**Independent Test**: The `divide` function can be tested independently.

### Tests for User Story 4 ⚠️

- [ ] T008 [P] [US4] Write tests for the `divide` function in `tests/test_operations.py`, including a test for division by zero.

### Implementation for User Story 4

- [ ] T009 [US4] Implement the `divide` function in `src/calculator/operations.py`.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Final touches and project-wide concerns.

- [ ] T010 [P] Create `src/calculator/__init__.py` and `tests/__init__.py`.
- [ ] T011 Run `mypy` and other linters to ensure code quality.
