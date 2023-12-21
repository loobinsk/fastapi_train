##
Мониторинг и сравнение фактических данных с планом

## Инструкции по установке
1. Склонируйте репозиторий.
2. Установите зависимости: `pip install -r requirements.txt`
3. Обновите схему базы данных: `alembic upgrade head`
4. Запуск:`uvicorn main:app` можно добавить свои параметры по желанию: --workers (количество ядер cpu) --port --host
5. переменные для env: DATABASE_URL, MAIN_SERVICE_URL
