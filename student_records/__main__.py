"""Run exception handling, package import, and introspection demonstrations."""
import student_records.errors as errors  # absolute module import
from student_records.services import StudentRegistry  # selective import
from student_records.utils.files import read_records, write_records
from student_records.utils.validation import parse_grade


def demo_basic() -> None:
    """Demonstrate a typed try/except for successful and invalid input.

    Args:
        None.
    Returns:
        None.
    Raises:
        None: Validation errors are caught.
    """
    print('1A. BASIC try/except')
    for value in ('91', 'wrong'):
        try:
            print(f'  {value!r} -> {parse_grade(value)}')
        except errors.GradeValidationError as exc:
            print(f'  ERROR: {exc}')


def demo_full() -> None:
    """Demonstrate try/except/else/finally and guaranteed cleanup.

    Args:
        None.
    Returns:
        None.
    Raises:
        None: Conversion errors are handled.
    """
    print('1B. FULL try/except/else/finally')
    for value in ('4', 'zero'):
        try:
            result = 100 / int(value)
        except (ValueError, ZeroDivisionError) as exc:
            print(f'  ERROR: {type(exc).__name__}')
        else:
            print(f'  ELSE: result={result}')
        finally:
            print('  FINALLY: processing attempt finished')


def demo_multiple() -> None:
    """Handle multiple built-in error types in one except block.

    Args:
        None.
    Returns:
        None.
    Raises:
        None: Type and value errors are handled.
    """
    print('1C. MULTI-TYPE except')
    for value in ('76', None, 'not-a-number'):
        try:
            print(f'  {value!r} -> {int(value)}')
        except (TypeError, ValueError) as exc:
            print(f'  ERROR: {type(exc).__name__}')


def demo_files() -> None:
    """Demonstrate with, chained exceptions, and domain-level catching.

    Args:
        None.
    Returns:
        None.
    Raises:
        None: Missing-file errors are caught.
    """
    print('1D / 2. FILES, DOMAIN ERRORS, CHAINING')
    write_records('sample_students.txt', ['ivan,95', 'olena,87'])
    print('  WITH success:', read_records('sample_students.txt'))
    try:
        read_records('missing_students_123.txt')
    except errors.RecordNotFoundError as exc:
        print('  DOMAIN ERROR:', exc)
        print('  __cause__:', type(exc.__cause__).__name__)


def demo_domain() -> None:
    """Demonstrate concrete domain exceptions and bare re-raise.

    Args:
        None.
    Returns:
        None.
    Raises:
        None: Domain exceptions are caught by caller.
    """
    print('2. DOMAIN EXCEPTIONS / RE-RAISE')
    registry = StudentRegistry()
    registry.add('ivan', 95)
    try:
        registry.add('ivan', 85)
    except errors.DuplicateStudentError as exc:
        print('  SPECIFIC CATCH:', exc)
    try:
        try:
            registry.add('olena', 120)
        except errors.StudentAppError as exc:
            print('  LOGGED:', exc)
            raise
    except errors.StudentAppError as exc:
        print('  BASE CATCH AFTER RE-RAISE:', type(exc).__name__)
    print('  AVERAGE:', registry.average())


def demo_exports() -> None:
    """Show that wildcard import respects package __all__.

    Args:
        None.
    Returns:
        None.
    Raises:
        None.
    """
    print('3. __all__ DEMONSTRATION')
    scope: dict[str, object] = {}
    exec('from student_records import *', scope)
    exported = sorted(key for key in scope if not key.startswith('__'))
    print('  Exported:', exported)


def demo_docs() -> None:
    """Display help and function metadata for introspection.

    Args:
        None.
    Returns:
        None.
    Raises:
        None.
    """
    print('4. INTROSPECTION')
    print('  __name__:', parse_grade.__name__)
    print('  __annotations__:', parse_grade.__annotations__)
    print('  __doc__:', parse_grade.__doc__.strip().splitlines()[0])
    help(parse_grade)


def main() -> None:
    """Run all laboratory demonstrations.

    Args:
        None.
    Returns:
        None.
    Raises:
        OSError: If the example file cannot be written.
    """
    demo_basic()
    demo_full()
    demo_multiple()
    demo_files()
    demo_domain()
    demo_exports()
    demo_docs()


if __name__ == '__main__':
    main()
