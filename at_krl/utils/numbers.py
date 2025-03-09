def to_number_or_str(value: str | int | float) -> int | float | str:
    if isinstance(value, str):
        try:
            return int(value)
        except ValueError:
            try:
                return float(value)
            except ValueError:
                return value
    if int(value) == value:
        return int(value)
    return value
