# SURVEY API

## API для системы опросов пользователей

### Функционал для администратора системы:
- авторизация в системе (без регистрации)
- добавление/изменение/удаление опросов. Атрибуты опроса: название, дата старта, дата окончания, описание. После создания поле "дата старта" у опроса менять нельзя
- добавление/изменение/удаление вопросов в опросе. Атрибуты вопросов: текст вопроса, тип вопроса (ответ текстом, ответ с выбором одного варианта, ответ с выбором нескольких вариантов)

### Функционал для пользователей системы:
- получение списка активных опросов
- прохождение опроса: опросы можно проходить анонимно, в качестве идентификатора пользователя в API передаётся числовой ID, по которому сохраняются ответы пользователя на вопросы; один пользователь может участвовать в любом количестве опросов
- получение пройденных пользователем опросов с детализацией по ответам (что выбрано) по ID уникальному пользователя

### Установка:
- клонируйте репозиторий
- создайте и активируйте в вирутальное окружение
- установите зависимости командой: pip install -r requirements.txt
- примените миграции:
python manage.py makemigrations,
python manage.py migrate
- cоздайте суперпользователя командой: python manage.py createsuperuser
- ознакомьтесь с документацией: через терминал перейдите в папку documentation, выполните команду mkdocs serve и откройте в браузере 'http://127.0.0.1:8000/' , либо ознакомьтесь с файлом docs/index.md непосредственно на GitHub
- перейдите в корневой каталог и запустите сервер разработки командой: python manage.py runserver
