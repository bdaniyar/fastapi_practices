# FastAPI Project

Простой проект FastAPI с правильной структурой и Poetry.

## Структура проекта

```
project/
├── app/                          # Основной пакет приложения
│   ├── __init__.py              # Инициализация пакета
│   ├── main.py                  # Точка входа (главный файл)
│   ├── models/                  # Модели данных
│   │   ├── __init__.py
│   │   └── user.py
│   ├── schemas/                 # Pydantic schemas (валидация)
│   │   ├── __init__.py
│   │   └── user.py
│   └── routes/                  # API маршруты
│       ├── __init__.py
│       ├── items.py
│       └── users.py
├── tests/                        # Тесты
│   ├── __init__.py
│   └── test_main.py
├── pyproject.toml               # Конфигурация Poetry
├── .gitignore
└── README.md
```

## Установка

1. Установите зависимости с Poetry:
```bash
poetry install
```

2. Активируйте виртуальное окружение:
```bash
poetry shell
```

## Запуск

### Локальный сервер
```bash
poetry run uvicorn app.main:app --reload
```

Сервер будет доступен по адресу: `http://localhost:8000`

### Документация API
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Тесты

```bash
poetry run pytest
```

## API Endpoints

### Items
- `GET /items` - Получить все items
- `GET /items/last` - Получить последний item
- `GET /items/{item_id}` - Получить item по ID

### Users
- `POST /users` - Создать нового пользователя

### Root
- `GET /` - Hello World
