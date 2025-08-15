# Homework 2: Functions: Mathematic and Python

In this assignment, you’ll explore key concepts from mathematics and computer science related to **functions**, including:

- Domains, codomains, and ranges
- Total vs. partial functions
- Valid vs. invalid function definitions
- How the definition of mathematical functions relates to the methods of a Python class, with an emphasis on a programming concept called **side effects**
- How to use the `mypy` tool to check for type errors in Python

You’ll write a function that takes a **set of ordered pairs** and says whether the ordered represent a function, partial function, or neither. You'll also review how to run unit tests and how to do passoffs in GitHub Classroom. Finally, you'll learn how to write unit tests when your class has methods that rely on class member variables.

---

## 1.0 Project Structure
Clone the project into VS Code and configure it by doing the following steps:
- install and activate `venv` 
- install the project (e.g., `pip install --editable ".[dev]"`)
- configure VS Code so that it can run tests by
  - Navigating to _View_ -> _Command Palette_ -> _Python: Select Interpreter_ and choosing the interpreter that is running in the virtual environment (e.g., `Python 3.12.5 (.venv)`)
  - Opening the Testing Panel in VS Code (the beaker) and configuring tests to use `pytest` and the `tests` directory.

This homework uses the following project structure.

```
homework2/
├── pyproject.toml
├── README.md
├── src/
│   └── homework2/
│       ├── __init__.py
|       ├── classify_function.py
│       └── score_keeper.py
└── tests/
|   ├── test_classify_function_typechecks
|   ├── test_classify_function.py
|   └── test_score_keeper.py
```

We'll look at both modules in `src/homework2`, and we'll work with all the test modules in `tests`.

---

## 3 Definitions: Function vs. Partial Function

### 3.1 Domain, Codomain, Cartesian Product
Let's begin with a review of the definitions for a function and a partial function.

Let:

- $D$ be the **domain** (a set of inputs),
- $C$ be the **codomain** (a set of possible outputs), and
- $f$ be a **mapping** represented as a set of ordered pairs $ f \subseteq D \times C $


### 3.1 Function

A mapping $ f $ is a **function** if:

1. Every element in the domain $D$ appears exactly once as the first element of a pair in $ f $
2. Each domain element maps to **exactly one** codomain element

> In other words, **every input has one and only one output**

Notice that we are defining the function using a subset of ordered pairs. For example, with $D = \{1,2\}$ and $C = \{'a','b'\}$, we can define a function as $f = \{(1,'a'), (2,'b')\}$ which is a subset of all the possible ordered pairs that could appear in the Cartesian product $D\times C$. This function maps `1 → 'a'` and `2 → 'b'`. You might be most familiar with writing this function as
$$ 
     f(1) = 'a'\\
     f(2) = 'b'
$$
The first element of the ordered pair goes inside the parentheses and the second element of the ordered pair is the value that the function produces, $f($ first element $) = $ second element


### 3.2 Partial Function

A mapping $ f $ is a **partial function** if:

1. Some elements in $D$ may not appear in the mapping  
2. Every input that **is** mapped still has **exactly one** output

> That is, **some inputs might not be used**, but **none are duplicated**


### 3.3 Not a Function

A mapping is **not a function** if:

- Any input in the domain appears more than once in the mapping with different outputs
- That is, a single input maps to multiple values

### 3.4 Examples

Let:
- $ D = \{1, 2, 3 \} $
- $ C = \{a, b, c \} $

- **Function**: $ f = \{(1, a), (2, b), (3, c) \} $
- **Partial function**: $ f = \{(1, a), (3, c) \}$
- **Not a function**: $ f = \{(1, a), (1, b), (2, c)\} $

### 3.5 Edge Cases

You are going to write a Python function that takes a set of ordered pairs and classifies it as a function, partial function, or neither. That Python function needs to handle the following two edge cases.

1. $D=\emptyset$, $C \neq \emptyset$, and $f = \emptyset$. The domain is empty, the codomain is not empty, and the mapping in the tuples is empty. Notice that $f$ has to be the emptyset since $D\times C = \emptyset \times C = \emptyset$, and the only subset of the empty set is the empty set itself. 

    The mapping $f$ in this problem **is a function** because each element of the domain is only appears once in $f$, which is trivially true since both $D$ and $f = \emptyset$. (This reasoning can be a little tricky, but we'll return to this kind of reasoning later in the class when we discuss propositional logic.)
1. $D\neq \emptyset$, $C \neq\emptyset$, $f = \emptyset$. The domain is not empty, the codomain is not empty, but the mapping is empty. 

   The mapping $f$ in this problem **is a partial function** because there are elements of the domain that do not appear in the tuples in $f$ (since there are no tuples in $f$).
    
1. $D\neq \emptyset$, $C =\emptyset$, $f = \emptyset$. The domain is not empty, the codomain is empty, and the mapping $f$ is empty. 
    
    The mapping $f$ in this problem **is a partial function** for the same reason as the example just above.

---

## 4. Unit Tests

The `tests` folder contains two files:
- `test_classify_function.py`
- `test_classify_function_typecheck.py`

The `test_classify_function.py` file provides some positive tests including the edge cases above. The other file does type-checking. We'll have more to say about type-checking shortly. 

---

## 5. Your Task

Implement the function `classify_function(...)` in `src/homework2/classify_function.py`. The first input to the function is a **set of tuples** — each tuple represents a pair `(input, output)`.

Return one of the following strings:

- `"function"` if the relation maps each domain element to exactly one codomain element
- `"partial function"` if the relation maps some (but not all) domain elements to codomain elements, without duplication
- `"not a function"` if any domain element maps to more than one codomain element

The Python function you write must pass each tests. Note that the elements of each set can be either an integer or a string. You can see this in the type hings in the function definition. For example, `domain: set[int | str]`. The vertical `|` represents a logical _or_, so the Python variable `domain` is supposed to be either an integer or a string. 

**Complete the Python function** in `classify_function.py` so that it passes each test. You'll be commiting the function to GitHub Classroom, and all the tests will be run. Don't spend too much time on this problem if you get hung up on it; passing all the tests will only be worth 2 points on the homework.

```bash
pytest
```

or use the **Testing panel** in VS Code. 

**Commit your code to GitHub Classroom** and use the process from Homework 1 to confirm that your code passed the autograding.

---

## 6. mypy: Static Type Checking
One of the experiences the instructors wanted you to have in writing the function above is the problem of doing all the type-checking. We'll now discuss a tool that you can use to check types. 


`mypy` is a **static type checker** for Python. Instead of waiting for tests to fail at runtime, `mypy` analyzes your code and flags type errors **before** execution. In this course, we use `mypy` so you can write *fewer* runtime type-checking tests while still getting strong guarantees about your code.

### 6.1 Why use mypy?

- Catches type mismatches early (e.g., wrong element types in a set of tuples)
- Documents code intent with type hints
- Reduces the need for many runtime type-checking tests
- Plays well with editors (inline diagnostics, quick jumps)

### 6.2 How to run mypy

From the project root (with your virtual environment activated):

```bash
mypy .
```

(If your `pyproject.toml` configures mypy to ignore tests, it won’t type-check files in `tests/`.)

### 6.3 Example: What mypy reports without type hints

In this part of the tutorial, you'll explore how `mypy` can reveal missing type hints and type mismatches in your code.

**1. Open `score_keeper.py`**

The file `score_keeper.py` currently contains:

```python
class ScoreKeeper:
    def __init__(self) -> None:
        self.multiplier = 1  # used in calculation
        self.total_score = 0  # altered in method

    def add_points(self, points: int) -> int:
        """
        Add points multiplied by self.multiplier to total_score.
        Return the amount of points added in this call.
        """
        added_points = points * self.multiplier
        self.total_score += added_points
        return added_points
```

Notice that `self.multiplier` and `self.total_score` do not have explicit type hints.

— **Run `mypy`**

From the root of the project, with your virtual environment activated, run:

```bash
mypy .
```

You should see warnings similar to:

```
src/homework2/score_keeper.py:3: error: Need type annotation for 'multiplier'  [var-annotated]
src/homework2/score_keeper.py:4: error: Need type annotation for 'total_score'  [var-annotated]
Found 2 errors in 1 file (checked 1 source file)
```

These warnings tell you that while the method signatures are typed, `mypy` still wants annotations for class attributes when `strict = true` is set in `pyproject.toml`.

**2. Add Type Hints for Attributes**

You can fix the warnings by adding explicit annotations:

```python
class ScoreKeeper:
    multiplier: int
    total_score: int

    def __init__(self) -> None:
        self.multiplier = 1
        self.total_score = 0
```

**3. Introduce a Type Error**

Now, let's see `mypy` catch a type mismatch. Change:

```python
self.multiplier = 1
```

to:

```python
self.multiplier = 0.0
```

Run `mypy .` again. You should now see:

```
src/homework2/score_keeper.py:6: error: Incompatible types in assignment (expression has type "float", variable has type "int")  [assignment]
Found 1 error in 1 file (checked 1 source file)
```

`mypy` correctly detects that you are assigning a `float` to a variable annotated as an `int`.


By using `mypy` in this way, you can catch type problems before running your tests, reducing runtime errors and improving code clarity.

# TODO
Conclude that this can help us avoid writing all the type checking tests.


---

## 7. Methods, Side Effects, and Mathematical Functions

In this course, we’ll emphasize writing code that behaves like **mathematical functions**: inputs go in, outputs come out — without hidden behavior (side effects). But most Python objects use **methods**, which can hide both inputs and outputs inside the object.

### 7.1 Example: Method with a Side Effect

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

### 7.2 Why This Matters

Hidden state changes can cause bugs (especially across multiple calls or shared objects).

---

## 8. Testing Methods that Use Object State

When testing methods that modify object state **and** return values, you need to check both the explicit and implicit outputs.

Example:

```python
class ScoreKeeper:
    def __init__(self) -> None:
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

