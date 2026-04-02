# 🚀 jjesboard
## jjesboard — это персональный футуристичный дашборд, построенный на базе FastAPI и Tailwind CSS. Проект агрегирует данные о погоде, курсах валют и последних технологических новостях в едином интерфейсе с эффектом Glassmorphism.

## ✨ Особенности
Real-time Weather: Актуальные данные о погоде в Астане (через wttr.in).

Currency Tracker: Оперативные курсы USD, EUR и RUB по отношению к тенге (KZT).

Tech News Feed: Свежие новости из мира IT через интеграцию с NewsAPI.

Modern UI: Полностью адаптивный интерфейс с использованием Tailwind CSS, анимациями и эффектом "стекла".

Secure: Поддержка переменных окружения (.env) для защиты API-ключей.

## 🛠 Стек технологий
Backend: Python 3.10+, FastAPI, HTTPX (асинхронные запросы).

Frontend: HTML5, Tailwind CSS (CDN), Vanilla JavaScript.

API: NewsAPI.org, ExchangeRate-API, Wttr.in.

## ⚙️ Установка и запуск
Клонируйте репозиторий:

Bash

git clone https://github.com/your-username/jjesboard.git
cd jjesboard
Создайте виртуальное окружение и активируйте его:

Bash

python -m venv venv
source venv/bin/activate  # Для Linux/macOS
# или
venv\Scripts\activate     # Для Windows
Установите зависимости:

Bash

pip install fastapi uvicorn httpx python-dotenv
Настройте переменные окружения:
Создайте файл .env в корневой папке и добавьте свой ключ:

Фрагмент кода

NEWS_API_KEY=ваш_ключ_от_newsapi
Запустите сервер:

Bash

uvicorn main:app --reload
После этого дашборд будет доступен по адресу: http://127.0.0.1:8000

## 📁 Структура проекта
Plaintext

├── main.py              # Логика бэкенда (FastAPI)
├── .env                 # Конфиденциальные ключи (игнорируется Git)
├── .gitignore           # Список исключений для Git
├── static/
│   └── index.html       # Фронтенд часть
└── README.md            # Документация проекта
## 📝 Лицензия
Проект создан в учебных целях. Свободен для использования и модификации.

Автор: Serikov Dias (aka **jjestar**)

Статус: В разработке 🚧
