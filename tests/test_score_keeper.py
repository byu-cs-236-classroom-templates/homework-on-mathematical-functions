from homework2.score_keeper import ScoreKeeper


def test_add_points_updates_score_and_returns_correct_value() -> None:
    # 1. Instantiate the object
    keeper = ScoreKeeper()

    # 2. Set the member variable that is used in the function
    keeper.multiplier = 2

    # 3. Call the function with a test argument
    return_value = keeper.add_points(5)

    # 4. Compare return value to expected value (points added this call)
    expected_added_points = 10  # 5 * multiplier(2)
    assert return_value == expected_added_points

    # 5. Compare modified member variable with expected value
    expected_total_score = 10
    assert keeper.total_score == expected_total_score