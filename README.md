# Тестовый проект - тестируем книжный веб-магазин
## "Page objects"  - в рамках курса "Автоматизация тестирования с помощью Selenium и Python". (https://stepik.org/course/575)
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

В данном проекте изучался Page Object Model или кратко Page Object — паттерн программирования, который очень популярен в автоматизации тестирования и является одним из стандартов при автоматизации тестирования веб-продуктов. 
Это также один из удобных способов структурировать свой код таким образом, чтобы его было удобно поддерживать, менять и работать с ним.

- ✨Magic ✨Python

## Предусловия
- Использовался интепритатор Python3
- Склонируйте репозиторий
- Создайте и активируйте виртуальное окружение
- Установите зависимости pip install -r requirements.txt
- Установите драйвер для браузера
- - Chrome: chromedriver: https://sites.google.com/chromium.org/driver/
- - Firefox: geckodriver: https://github.com/mozilla/geckodriver/releases
- Добавьте путь к драйверу - в системную переменную PATH (в настройках системы вашего ПК).

## Запуск скрипта
Запустите скрипт в консоли командой:
- pytest -v --tb=line --language=en test_product_page.py
- pytest -v --tb=line --language=en test_maun_page.py
- или используйте подсказки из комментариев по запуску тестов.
- 
____________________________________________________________________________________

# Test project - testing a web bookstore
## "Page objects" - as part of the "Test Automation with Selenium and Python" course. (https://stepik.org/course/575)
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

In this project, we studied Page Object Model or briefly Page Object - a programming pattern that is very popular in test automation and is one of the standards for automating testing of web products.
It's also one of the handy ways to structure your code in a way that makes it easy to maintain, change, and work with.

- ✨Magic ✨Python

## Preconditions
- Used Python3 interpreter
- Clone the repository
- Create and activate virtual environment
- Install dependencies pip install -r requirements.txt
- Install browser driver
- - Chrome: chromedriver: https://sites.google.com/chromium.org/driver/
- - Firefox: geckodriver: https://github.com/mozilla/geckodriver/releases
- Add the path to the driver - to the system PATH variable (in your PC's system settings).

## Run script
Run the script in the console with the command:
- pytest -v --tb=line --language=en test_product_page.py
- pytest -v --tb=line --language=en test_maun_page.py
- or use hints from comments on running tests.
