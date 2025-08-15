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
        # ---- basic type checks for containers ----
    if not isinstance(mapping, set) or not isinstance(domain, set) or not isinstance(codomain, set):
        raise TypeError("mapping, domain, and codomain must all be sets")

    # ---- element type checks for domain/codomain ----
    if not all(isinstance(d, (int, str)) for d in domain):
        raise TypeError("All domain elements must be int or str")
    if not all(isinstance(c, (int, str)) for c in codomain):
        raise TypeError("All codomain elements must be int or str")

    # ---- validate mapping pairs and membership ----
    seen: dict[int | str, int | str] = {}
    for pair in mapping:
        if not isinstance(pair, tuple) or len(pair) != 2:
            raise TypeError("Each mapping element must be a 2-tuple (input, output)")
        x, y = pair

        # element type checks
        if not isinstance(x, (int, str)) or not isinstance(y, (int, str)):
            raise TypeError("Tuple elements must be int or str")

        # membership checks
        if x not in domain:
            raise TypeError("Mapping contains an input not in the domain")
        if y not in codomain:
            raise TypeError("Mapping contains an output not in the codomain")

        # functional consistency: an input maps to exactly one output
        if x in seen and seen[x] != y:
            return "not a function"
        seen[x] = y

    # ---- classification based on coverage of the domain ----
    mapped_inputs = set(seen.keys())

    if mapped_inputs == domain:
        return "function"
    else:
        # Strict subset (or empty when domain non-empty) means some inputs unmapped
        return "partial function"
