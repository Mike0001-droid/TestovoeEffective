# TestovoeEffective
API Разработка системы управления заказами в кафе
![GitHub top language](https://img.shields.io/github/languages/top/Mike0001-droid/TestovoeEffective)

<!--Установка-->
## Установка 
У вас должны быть установлены [зависимости проекта](https://github.com/Mike0001-droid/TestovoeEffective/blob/main/requirements.txt)

1. Клонирование репозитория 

```git clone https://github.com/Mike0001-droid/TestovoeEffective.git```

2. Переход в директорию TestovoeEffective

```cd TestovoeEffective```

3. Создание виртуального окружения

```python -m venv venv```

4. Активация виртуального окружения

```cd venv/scripts/activate```

5. Установка зависимостей

```pip install -r requirements.txt```

6. Запуск миграций

```python manage.py migrate```

7. Создание админа

```python manage.py createsuperuser```

8. Запуск сервера

```python manage.py runserver```

## Возможности сервиса

1. Создание, удаление, изменение статуса у заказа

2. Создание блюд

3. Реализован API для управления заказами (получение всех заказов, создание, удаление, редактирование блюд и статуса)

4. Реализована система авторизации и аутентификации на основе JWT токенов
