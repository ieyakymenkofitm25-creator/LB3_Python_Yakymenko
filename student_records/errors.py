"""Domain exceptions for the student records application."""
class StudentAppError(Exception):
    """Base domain error for all student-record failures."""

class GradeValidationError(StudentAppError):
    """Invalid grade.

    Args:
        field (str): Name of invalid field.
        value (object): Invalid input.
    """
    def __init__(self, field: str, value: object) -> None:
        self.field, self.value = field, value
        super().__init__(str(self))
    def __str__(self) -> str:
        return f"Invalid {self.field}: {self.value!r}; expected integer 0..100"

class RecordNotFoundError(StudentAppError):
    """Requested student record does not exist.

    Args:
        resource (str): Missing resource path or name.
    """
    def __init__(self, resource: str) -> None:
        self.resource = resource
        super().__init__(str(self))
    def __str__(self) -> str:
        return f"Student resource not found: {self.resource}"

class DuplicateStudentError(StudentAppError):
    """Duplicate student detected.

    Args:
        student_id (str): Duplicate student identifier.
    """
    def __init__(self, student_id: str) -> None:
        self.student_id = student_id
        super().__init__(str(self))
    def __str__(self) -> str:
        return f"Duplicate student ID: {self.student_id}"
