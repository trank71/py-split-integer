from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    parts = [4, 4, 4, 5]
    value = 17
    assert sum(parts) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    parts = [4, 4, 4, 5]
    assert max(parts) - min(parts) <= 1


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 8
    number_of_parts = 1
    result = [8]
    func = split_integer(value, number_of_parts)
    assert result == func


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    pass


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    pass
