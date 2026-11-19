# ЛБ №3 — Python: винятки, модулі, документація

Виконавець: Якименко Іван Едуардович. Група: БІКСб-2-25-4.0д.

## Вимоги
Python 3.10+; сторонніх залежностей немає.

## Запуск
Відкрийте термінал у корені репозиторію та виконайте:

```bash
python -m student_records
```

## Перевірка
```bash
python -m compileall -q student_records
```

## Структура
- `student_records/errors.py` — власні виключення.
- `student_records/services/registry.py` — реєстр студентів.
- `student_records/utils/validation.py` — перевірка оцінок.
- `student_records/utils/files.py` — читання/запис файлів через `with`.
- `student_records/__main__.py` — демонстрація чотирьох завдань.

Для здачі завантажте цей каталог у **власний GitHub-репозиторій** та передайте викладачу URL. PDF-звіт додається окремо.
