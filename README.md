# Homework 2: Functions and Their Properties + Pytest

In this assignment, you’ll explore key concepts from mathematics and computer science related to **functions**, including:

- Domains, codomains, and ranges
- Total vs. partial functions
- Valid vs. invalid function definitions
- How the definition of mathematical functions relates to the methods of an object, with an emphasis on an important programming concept called **side effects**

You’ll write and evaluate unit tests to validate whether a **set of ordered pairs** represents a function, partial function, or neither. You'll also rewrite a piece of code that has side effects so that it uses functions that avoid side effects.

---

## 🧠 Learning Goals

By the end of this assignment, you should be able to:

- Understand the definitions of **functions**, **partial functions**, and **not functions** using mappings, domains, and codomains
- Represent functions using sets of ordered pairs in Python
- Model side effects and pure functions using mathematical function notation
- Review how to write and interpret unit tests:
  - ✅ Positive tests: verify correct behavior
  - ❌ Negative tests: catch incorrect behavior
  - ⚠️ Type-checking tests: verify input/output type constraints and membership in domain/codomain
- Recognize how object methods can hide the inputs and outputs in a mathematical function and learn how to rewrite methods functionally
- Review how to use `pytest` to run and organize tests from the terminal and VS Code testing panel
- Review how to set up and manage Python projects using `pyproject.toml` and virtual environments (`venv`)
- Review how to tell VS Code to use the Python interpreter from the virtual environment
- **New:** Understand what **mypy** (a static type checker) does, why we use it to reduce the number of runtime type-checking tests, and how to run it.

---

## 1.0 Project Structure

```
homework2/
├── pyproject.toml
├── README.md
├── src/
│   └── homework2/
│       ├── __init__.py
│       └── classify_function.py
└── tests/
    └── test_classify_function.py
```

---

## 2 Setup Instructions

1. Clone your starter repo into the `CS236/` folder.

2. **Deactivate Conda (if active)**  
   If your terminal prompt starts with `(base)` or another environment name in parentheses, you’re likely in a conda environment. To deactivate conda:

   ```bash
   conda deactivate
   ```

3. **Create a Virtual Environment**

   - **On Windows**:
     ```bash
     python -m venv .venv
     ```

   - **On macOS/Linux**:
     ```bash
     python3 -m venv .venv
     ```

   This creates a local `.venv/` directory in your project folder.

4. **Activate the Virtual Environment**

   - **On Windows (PowerShell)**:
     ```bash
     .venv\Scripts\Activate.ps1
     ```

   - **On macOS/Linux**:
     ```bash
     source .venv/bin/activate
     ```

   Once activated, your prompt should now start with `(.venv)` — this means your virtual environment is working.

5. **Install your project locally** (with dependencies):

   - **On Windows**:
     ```bash
     pip install --editable ".[dev]"
     ```

   - **On macOS/Linux**:
     ```bash
     pip3 install --editable ".[dev]"
     ```

This project’s `pyproject.toml` installs `pytest` automatically. It also installs a tool called `mypy` that we'll use so that we don't have to write so many type-checking tests.

---

## 3 Definitions: Function vs. Partial Function

Let:

- $D$ be the **domain** (a set of inputs),
- $C$ be the **codomain** (a set of possible outputs), and
- $f$ be a **mapping** represented as a set of ordered pairs $ f \subseteq D \times C $

**Interpreting ordered pairs.** We represent a mapping as a **set of tuples** like `{(x, y)}` where each `x` is an element of the domain and each `y` is an element of the codomain. For example, with `D = {1,2}` and `C = {'a','b'}`, the relation `f = {(1,'a'), (2,'b')}` maps `1 → 'a'` and `2 → 'b'`.

---

### 3.1 Function

A mapping $ f $ is a **function** if:

1. Every element in the domain $D$ appears exactly once as the first element of a pair in $ f $
2. Each domain element maps to **exactly one** codomain element

> In other words, **every input has one and only one output**

---

### 3.2 Partial Function

A mapping $ f $ is a **partial function** if:

1. Some elements in $D$ may not appear in the mapping  
2. Every input that **is** mapped still has **exactly one** output

> That is, **some inputs might not be used**, but **none are duplicated**

---

### 3.3 Not a Function

A mapping is **not a function** if:

- Any input in the domain appears more than once in the mapping with different outputs
- That is, a single input maps to multiple values

---

### Example:

Let:
- $ D = \{1, 2, 3 \} $
- $ C = \{a, b, c \} $

- **Function**: $ f = \{(1, a), (2, b), (3, c) \} $
- **Partial function**: $ f = \{(1, a), (3, c) \}$
- **Not a function**: $ f = \{(1, a), (1, b), (2, c)\} $

---

## 4. Tests

**How to run tests from the terminal**

```bash
pytest
```

**How to run tests in VS Code**

- Open the **Testing** panel (beaker icon).
- If prompted, choose **Python: Configure Tests** → **pytest** → test folder `tests/`.
- Click **Run All Tests**.

---

## 5. Your Task

Implement the function `classify_function(...)` in `src/homework2/classify_function.py`. The first input to the function is a **set of tuples** — each tuple represents a pair `(input, output)`.

Return one of the following strings:

- `"function"` if the relation maps each domain element to exactly one codomain element
- `"partial function"` if the relation maps some (but not all) domain elements to codomain elements, without duplication
- `"not a function"` if any domain element maps to more than one codomain element

Run tests with:

```bash
pytest
```

or use the **Testing panel** in VS Code. 

---

## 6. Methods, Side Effects, and Mathematical Functions

In this course, we’ll emphasize writing code that behaves like **mathematical functions**: inputs go in, outputs come out — without hidden behavior (side effects). But most Python objects use **methods**, which can hide both inputs and outputs inside the object.

### 6.1 Example: Method with a Side Effect

```python
class Logger:
    def __init__(self):
        self.history = []

    def log_and_return_length(self, message: str) -> int:
        self.history.append(message)
        return len(message)
```

Mathematically, this method’s transformation is:

```
(history, message) ↦ (history', length)
```

- **Domain**: pairs `(history, message)`  
- **Codomain**: pairs `(updated_history, length)`

### 6.2 Why This Matters

Hidden state changes can cause bugs (especially across multiple calls or shared objects).

### 6.3 Functional Design Alternative

```python
def pure_log_and_return_length(history: list[str], message: str) -> tuple[list[str], int]:
    new_history = history + [message]
    return new_history, len(message)
```

This makes the full input and output explicit and testable.

---

## 7. Testing Methods that Use Object State

When testing methods that modify object state **and** return values, you need to check both the explicit and implicit outputs.

Example:

```python
class ScoreKeeper:
    def __init__(self):
        self.total_score = 0
        self.last_added = None

    def add_points(self, points: int) -> int:
        self.total_score += points
        self.last_added = points
        return points
```

Test:

```python
def test_add_points() -> None:
    # Step 1: Instantiate
    sk = ScoreKeeper()
    # Step 2: Set state if needed
    sk.total_score = 10
    # Step 3: Call method
    returned = sk.add_points(5)
    # Step 4: Check return value
    assert returned == 5
    # Step 5: Check modified state
    assert sk.total_score == 15
    assert sk.last_added == 5
```

---

## 8. mypy: Static Type Checking

`mypy` is a **static type checker** for Python. Instead of waiting for tests to fail at runtime, `mypy` analyzes your code and flags type errors **before** execution. In this course, we use `mypy` so you can write *fewer* runtime type-checking tests while still getting strong guarantees about your code.

### 8.1 Why use mypy?

- Catches type mismatches early (e.g., wrong element types in a set of tuples)
- Documents code intent with type hints
- Reduces the need for many runtime type-checking tests
- Plays well with editors (inline diagnostics, quick jumps)

### 8.2 How to run mypy

From the project root (with your virtual environment activated):

```bash
mypy .
```

(If your `pyproject.toml` configures mypy to ignore tests, it won’t type-check files in `tests/`.)

### 8.3 Example: What mypy reports without type hints

```python
def classify_function(mapping, domain, codomain):
    raise NotImplementedError("Function not yet implemented.")
```

Running `mypy .` might produce:

```
src/homework2/classify_function.py:1: error: Function is missing a type annotation for one or more arguments  [no-untyped-def]
src/homework2/classify_function.py:1: note: Use "-> None" if function does not return a value
Found 1 error in 1 file (checked 1 source file)
```

With the typed version:

```python
def classify_function(
    mapping: set[tuple[int | str, int | str]],
    domain: set[int | str],
    codomain: set[int | str],
) -> str:
    raise NotImplementedError("Function not yet implemented.")
```

`mypy` can then validate the structure of the mapping and ensure that all tuple elements and set elements match the declared types.
