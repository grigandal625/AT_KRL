def to_number_or_str(value: bool | str | int | float | None) -> bool | int | float | str | None:
    if value is None:
        return value
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        try:
            return int(value)
        except ValueError:
            try:
                return float(value)
            except ValueError:
                if value.lower() == "true":
                    return True
                if value.lower() == "false":
                    return False
                return value
    if int(value) == value:
        return int(value)
    return value
