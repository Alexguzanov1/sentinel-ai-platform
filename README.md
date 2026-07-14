# Project sentinel-ai-platform

## Описание проекта

Проект следит за табличными данными производства и определяет аномалии, анализирует процессы с помощью компьютерного зрения, также работает агентная система.

## Структура папок
```text
├───docs
│   └───architechture
├───src
│   └───sentinel
│       ├───common
│       ├───config
│       ├───data
│       ├───features
│       ├───inference
│       └───training
└───tests
    ├───integration
    └───unit
```
## Local development

Requirements:

- Python 3.12 or 3.13
- uv

Install the project environment:

```powershell
uv sync
```

Run tests:

```powershell
uv run pytest
```

## Текущий статус

Проект находится в начале разработки. Созданы основные директории.

## В планах

Планируется разработка основных модулей, тестов
Следующим шагом является разработка классификатора аномалий на основе табличных данных
