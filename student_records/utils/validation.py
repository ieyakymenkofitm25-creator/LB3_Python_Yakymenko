"""Validate grades and convert user input to integers."""
from ..errors import GradeValidationError

def parse_grade(value: str | int) -> int:
    """Parse and validate a grade.

    Args:
        value (str | int): Grade to convert.
    Returns:
        int: Grade in the inclusive interval 0..100.
    Raises:
        GradeValidationError: If the grade is malformed or out of range.
    """
    try:
        grade = int(value)
    except (ValueError, TypeError) as exc:
        raise GradeValidationError("grade", value) from exc
    if isinstance(value, float) or not 0 <= grade <= 100:
        raise GradeValidationError("grade", value)
    return grade
