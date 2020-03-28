from datetime import date


def age_calculator(birth_date) -> int:
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    # the last part of the calculation will either return 0(False) or 1(True).
    return age
