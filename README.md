# Django menu
'''Для удобства просмотра добавлены стили, БД заполнена и находится в репозитории.'''

Django menu - это тестовое задание на позицию Junior Python Backend Developer. Суть задания состоит в том, чтобы сделать django app, который будет реализовывать древовидное меню, соблюдая следующие условия:
- Меню реализовано через template tag
- Все, что над выделенным пунктом - развернуто. Первый уровень вложенности под
выделенным пунктом тоже развернут
- Хранится в БД
- Редактируется в стандартной админке Django
- Активный пункт меню определяется исходя из URL текущей страницы
- Меню на одной странице может быть несколько. Они определяются по названию
- При клике на меню происходит переход по заданному в нем URL. URL может быть задан
как явным образом, так и через named url
- На отрисовку каждого меню требуется ровно 1 запрос к БД
- Нужен django-app, который позволяет вносить в БД меню (одно или несколько) через
админку, и нарисовать на любой нужной странице меню по названию

## Технологии:

- Python
- Django
- CSS
- CI

## Как это работает?

Склонируйте себе репозиторий проекта, создайте и активируйте виртуальное окружение и установите зависимости с помощью команды "pip install -r requirements.txt".
Создайте и примените миграции с помощью команд:

```Python
python manage.py makemigrations
python manage.py migrate
```
Создайте суперюзера с помощью команды:
```Python
python manage.py createsuperuser
```
Запустите проект командой:
```Python
python manage.py runserver
```
## Лицензия

#### The MIT License (MIT)

Copyright © «2022» «copyright Yasnov Kirill»

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE

## Авторы
#### Яснов Кирилл
https://github.com/YasnovKS