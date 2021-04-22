# API_Survay.
# API для системы опроса пользователей.

## Документация по API

### Алгоритм авторизации пользователей
- Пользователь отправляет запрос с параметрами username и password на /api/v1/token/, в ответе на запрос ему приходит token (JWT-токен) в поле access. Данные из поля refresh необходимы для обновления токена.
- При отправке запроса токен следует передавать в заголовке Authorization: Bearer <токен>
### Добавление опросов (POST)
- Права доступа: Администратор
- URL: /api/v1/surveys/
- QUERY PARAMETERS: title, date_finish, description
### Изменение/удаление опросов (PUT, DELETE)
- Права доступа: Администратор
- URL: /api/v1/surveys/{survey_id}/
### Добавление вопросов к опросу (POST)
- Права доступа: Администратор
- URL: /api/v1/surveys/{survey_id}/questions/
- QUERY PARAMETERS: text, type_question (text / single_value / multi_boxes), survey
### Изменение/удаление вопросов (PUT, DELETE)
- Права доступа: Администратор
- URL: /api/v1/surveys/{survey_id}/questions/
### Добавление и просмотр вариантов ответа к вопросу (POST, GET)
- Права доступа: Администратор
- URL: /api/v1/surveys/{survey_id}/questions/{question_id}/choices/
- QUERY PARAMETERS: title, question
### Получение списка активных опросов (GET)
- Права доступа: Любой пользователь
- URL: /api/v1/active/
### Прохождение опроса (POST)
- Права доступа: Авторизованный пользователь
- URL: /api/v1/surveys/{survey_id}/questions/{question_id}/answers/
### Получение пройденных пользователем опросов (GET)
- Права доступа: Авторизованный пользователь
- URL: /api/v1/passed/
