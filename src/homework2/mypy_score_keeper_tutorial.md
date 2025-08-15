# Using mypy with `score_keeper.py`

In this part of the tutorial, you'll explore how `mypy` can reveal missing type hints and type mismatches in your code.

## Step 1 — Open `score_keeper.py`

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

## Step 2 — Run `mypy`

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

## Step 3 — Add Type Hints for Attributes

You can fix the warnings by adding explicit annotations:

```python
class ScoreKeeper:
    multiplier: int
    total_score: int

    def __init__(self) -> None:
        self.multiplier = 1
        self.total_score = 0
```

## Step 4 — Introduce a Type Error

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

---

By using `mypy` in this way, you can catch type problems before running your tests, reducing runtime errors and improving code clarity.
