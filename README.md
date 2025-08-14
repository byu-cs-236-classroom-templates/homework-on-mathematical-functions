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
- Review how to tell VSCode to use the Python interpreter from the virtual environment

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

## 2.0 Setup Instructions

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

## 3.0 Definitions: Function vs. Partial Function

Let:

- $D$ be the **domain** (a set of inputs),
- $C$ be the **codomain** (a set of possible outputs), and
- $f$ be a **mapping** represented as a set of ordered pairs $ f \subseteq D \times C $

# TODO
Talk about what these ordered pairs look like and how to interpret them

---

### 3.1 Function

A mapping $ f $ is a **function** if:

1. Every element in the domain $D$ appears exactly once as the first element of a pair in $ f $
2. Each domain element maps to **exactly one** codomain element

> In other words, **every input has one and only one output**

---

### ⚠️ Partial Function

A mapping $ f $ is a **partial function** if:

1. Some elements in $D$ may not appear in the mapping  
2. Every input that **is** mapped still has **exactly one** output

> That is, **some inputs might not be used**, but **none are duplicated**

---

### ❌ Not a Function

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

## 🧪 Tests

Open the file `tests\test_classify_function.py` and look at the tests. The math behind the first five tests is:

- $D=\{1,2,3\}$, $C=\{a, b, c\}$, and $f = \{(1,a), (2,b), (3,c)\}$ is a function.
- $D=\{1,2,3\}$, $C=\{a, b, c\}$, and $f = \{(1,a), (3,c)\}$ is a partial function.
- $D=\{1,2,3\}$, $C=\{a, b, c\}$, and $f = \{(1,a), (1,b), (3,c)\}$ is neither a function nor a partial function.
- $D=\emptyset$, $C=\{a, b\}$, and $f = \emptyset$ is a function.
- $D=\{1, 2, 3\}$, $C=\{a, b, c\}$, and $f = \emptyset$ is a partial function.

Note that the last two examples are edge cases that test what happens when the domain is empty or the mapping is empty.

---
Open the file `tests\test_classify_function_typechecks.py`. We split the tests into two files to make it easier to track the different kinds of tests. This file contains tests that check whether there are elements of the tuples that don't appear in the domain or codomain, which would violate the definitions of functions, partial functions, and even mappings from the domain to the codomain. This file also tests whether the elements of the domain, codomain, and tuples in the mapping are either strings or integers.


---

## 🚀 Your Task

Implement the function `classify_function(...)` in `src/homework2/classify_function.py`. The first input to the function will now be a **set of tuples** — each tuple represents a pair of an input and output.

Return one of the following strings:

- `"function"` if the relation maps each domain element to exactly one codomain element
- `"partial function"` if the relation maps some (but not all) domain elements to codomain elements, without duplication
- `"not a function"` if any domain element maps to more than one codomain element

---

Run tests with:

```bash
pytest
```

or use the **Testing panel** in VS Code. 

---

## 🔄 Methods, Side Effects, and Mathematical Functions

In this course, we’ll emphasize writing code that behaves like **mathematical functions**: inputs go in, outputs come out — without hidden behavior (side effects). But most Python objects use **methods**, which can hide both inputs and outputs inside the object.

---

### ✅ Example: Method with a Side Effect

```python
class Logger:
    def __init__(self):
        self.history = []

    def log_and_return_length(self, message: str) -> int:
        self.history.append(message)
        return len(message)
```

Let’s model this **mathematically**.

- The method takes:
  - `self.history` (hidden input)
  - `message` (explicit input)

- The method returns:
  - `len(message)` (explicit output)
  - but it also changes `self.history` (hidden output)

So the method can be thought of as a function:

```math
f: (history, message) → (history', length)
```

That is:

- **Domain**: pairs `(history, message)`
- **Codomain**: pairs `(updated_history, length)`

Even though Python lets you write:

```python
length = logger.log_and_return_length("hello")
```

The **actual transformation** includes a change to `logger.history`.

---

### ⚠️ Why This Matters

If we care only about outputs, we might miss the fact that the method also modified internal state. This leads to bugs when:

- A method is **called more than once**
- Or different parts of the program depend on the same object

---

### ✅ Functional Design Alternative

We can rewrite this method to avoid side effects by **returning everything that changed**:

```python
def pure_log_and_return_length(history: list[str], message: str) -> tuple[list[str], int]:
    new_history = history + [message]
    return new_history, len(message)
```

Now the function:

```math
f: (history, message) → (history', length)
```

is **explicit**, pure, and testable.

---

### 🧠 Takeaway

When designing methods, use the mathematical definition of a function to make sure that the code is clear about the following:
- What is the full **input**? (Not just the arguments, but also the object state)
- What is the full **output**? (Not just the return value, but also what was modified?)

A **good design** makes this mapping explicit — either through function arguments, return values, or both.

---

## 🧠 What You’ve Practiced

- Cloning and configuring a Python project with a virtual environment
- Installing dependencies (like `pytest`) via `pyproject.toml`
- Understanding how to model functions and partial functions using **sets of tuples**
- Running and analyzing a variety of test types to validate both functional correctness and input constraints
- Rewriting object methods to avoid side effects, using pure function design principles


