"""File I/O helpers using context managers."""
from pathlib import Path
from ..errors import RecordNotFoundError

def read_records(path: str) -> list[str]:
    """Read lines from a UTF-8 student record file.

    Args:
        path (str): File path.
    Returns:
        list[str]: Nonempty trimmed file lines.
    Raises:
        RecordNotFoundError: If the file cannot be found.
        UnicodeError: If its content is not valid UTF-8.
    """
    try:
        with open(path, 'r', encoding='utf-8') as stream:
            return [line.strip() for line in stream if line.strip()]
    except FileNotFoundError as exc:
        raise RecordNotFoundError(path) from exc

def write_records(path: str, lines: list[str]) -> None:
    """Write student records to a UTF-8 file.

    Args:
        path (str): Output file path.
        lines (list[str]): Lines to write.
    Returns:
        None: File is written and automatically closed.
    Raises:
        OSError: If the destination cannot be written.
    """
    with open(path, 'w', encoding='utf-8') as stream:
        stream.write('\n'.join(lines) + '\n')
