# Третья домашка

## Схемы событий

### Функциональное событие: Задание выполнено

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",

  "title": "ExerciseCompleted",
  "description": "Initial json schema for exercise completed event",

  "definitions": {
    "payload": {
      "type": "object",
      "properties": {
        "exercise_id":           { "type": "string" },
        "title":                 { "type": "string" },
        "author_id":             { "type": "string" },
        "candidate_id":          { "type": "string" },
        "completed_at":          { "type": "string" },
      },
      "required": [
        "exercise_id",
        "title",
        "author_id",
        "candidate_id",
        "completed_at"
      ]
    }
  },

  "type": "object",

  "properties": {
    "event_id":      { "type": "string" },
    "event_version": { "enum": [0] },
    "event_name":    { "enum": ["ExerciseCompleted"] },
    "produced_at":   { "type": "string" },
    "payload": { "$ref": "#/definitions/payload" }
  },

  "required": [
    "event_id",
    "event_version",
    "event_name",
    "produced_at",
    "payload"
  ]
}
```

## Процессы миграции

### Sync -> ED Async (form)

1. Создадим topic `datarep.<topicname>`
2. Создадим консумер[ы], опишем схему, раскатим
3. Создадим продьюсер на стороне источника, раскатим под FF [^1]
4. Убедимся, что это работает
5. Переключим на асинхронную коммуникацию
6. Очистим код от синхронного вызова

### ED Async -> Sync (form)

1. Создадим API endpoint `/api/v0/epname`
2. Создадим логику вызова со стороны потребления
3. Убедимся, что это работает
4. Переключим на синхронную коммуникацию
5. Погасим продьюсер
6. После исчерпания топика, погасим консумеры.

### Sync -> ED Async (func)

1. Создадим topic `datarep.<topicname>`
2. Создадим консумер[ы], опишем схему, раскатим
3. Создадим продьюсер на стороне источника, раскатим под FF [^1]
4. Убедимся, что это работает
5. Переключим на асинхронную коммуникацию
6. Очистим код от синхронного вызова

### ED Async -> Sync (func)

1. Создадим API endpoint `/api/v0/epname`
2. Создадим логику вызова со стороны потребления
3. Убедимся, что это работает
4. Переключим на синхронную коммуникацию
5. Погасим продьюсер
6. После исчерпания топика, погасим консумеры.

## Миграция по новым требованиям

### US-160

### US-170


## Проблемы зачисления/списания

[^1]: Feature Flag


## Мемы
