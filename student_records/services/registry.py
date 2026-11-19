"""Student registration and grade processing services."""
from ..errors import DuplicateStudentError
from ..utils.validation import parse_grade

class StudentRegistry:
    """Maintain unique student IDs and validated grades.

    Args:
        initial (dict[str, int] | None): Optional initial records.
    """
    def __init__(self, initial: dict[str, int] | None = None) -> None:
        self._grades: dict[str, int] = {}
        for student_id, grade in (initial or {}).items():
            self.add(student_id, grade)

    def add(self, student_id: str, grade: str | int) -> None:
        """Add a student with a validated grade.

        Args:
            student_id (str): Unique student identifier.
            grade (str | int): Grade in range 0..100.
        Returns:
            None: The registry is updated.
        Raises:
            DuplicateStudentError: If the ID is already present.
            GradeValidationError: If the grade is invalid.
        """
        if student_id in self._grades:
            raise DuplicateStudentError(student_id)
        self._grades[student_id] = parse_grade(grade)

    def average(self) -> float:
        """Calculate the average grade.

        Args:
            None.
        Returns:
            float: Average grade or 0 for empty registry.
        Raises:
            None.
        """
        return sum(self._grades.values()) / len(self._grades) if self._grades else 0.0
