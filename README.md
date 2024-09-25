# Новостной сайт

Проект представляет собой веб-приложение для чтения,
редактирования и публикации новостей. Функционал приложения позволяет:

- Создавать и редактировать новостные статьи, включая заголовок и основной текст новости.
- Выбирать категорию для каждой новости.
- Добавлять фотографии к статьям.
- Публиковать новости и, при необходимости, удалять их.

Функционал сайта включает:

- Просмотр главной страницы с актуальными новостями.
- Просмотр новостей по выбранным категориям.
- Просмотр отдельных новостных статей в развернутом виде.

## Установка и запуск

Для удобства используйте принцип copy-paste: копируйте команды из этого README
и вставляйте их в командную строку Git Bash или IDE (например, VSCode или PyCharm).

### Локальный запуск

**Для пользователей Windows:**
Обязательно выполните следующую команду, иначе файл `start.sh` при клонировании будет поврежден:

```
git config --global core.autocrlf false
```

1. **Клонируйте репозиторий с GitHub:**

   ```
   git clone https://github.com/HarutyunDanielyan/django-site.git && cd django-sites
   ```
2. **Создайте и активируйте виртуальное окружение:**

   - Если у вас **Linux/macOS**:
     ```
     python -m venv venv && source venv/bin/activate
     ```
   - Если у вас **Windows**:
     ```
     python -m venv venv && source venv/Scripts/activate
     ```
3. **Установите все необходимые зависимости из файла `requirements.txt`:**

   ```
   python -m pip install --upgrade pip && pip install -testsite/requirements.txt
   ```
4. **Выполните миграции, создайте суперпользователя (потребуется ввод персональных данных) и запустите приложение:**

   ```
   cd yatube && \
   python manage.py makemigrations && \
   python manage.py migrate && \
   python manage.py prepare_load_data && \
   python manage.py loaddata dump.json && \
   python manage.py createsuperuser && \
   python manage.py runserver && cd ..
   ```
5. Сервер запустится локально по адресу: [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

> **Примечание:** Чтобы остановить сервер Django, используйте комбинацию клавиш `Ctrl+C`.

## Вклад

Для значительных изменений, пожалуйста, сначала откройте issue, чтобы обсудить, что вы хотите изменить.

## Лицензия

Этот проект выпущен не под лицензией.

**Автор:** Danielyan Harutyun
