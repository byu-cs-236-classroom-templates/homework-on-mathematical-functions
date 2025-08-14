def classify_function(
    mapping: set[tuple[int | str, int | str]],
    domain: set[int | str],
    codomain: set[int | str]
) -> str:
    """
    Classifies the mapping as 'function', 'partial function', or 'not a function'
    based on the provided domain and codomain.

    Args:
        mapping (set[tuple[int | str, int | str]]): A set of ordered pairs (input, output).
        domain (set[int | str]): The full set of possible inputs.
        codomain (set[int | str]): The full set of possible outputs.

    Returns:
        str: 'function' if the mapping is a function, 
             'partial function' if it is a partial function,
             'not a function' if it does not satisfy the criteria of a function.
    """
    raise NotImplementedError("Function not yet implemented.")
