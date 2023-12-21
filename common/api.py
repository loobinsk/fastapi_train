import httpx
from django.conf import settings

async def check_author(scenario_id: int, token: str):

    api_url = f"{settings.MAIN_SERVICE_URL}monitoring/check_author/{scenario_id}/"
    headers = {
        "Authorization": token
    }

    async with httpx.AsyncClient(timeout=httpx.Timeout(timeout=90.0)) as client:
        response = await client.get(api_url, headers=headers)

        # Проверяем статус ответа и возвращаем результат
        if response.status_code == 200:
            return True
        elif response.status_code == 403:
            return False
        elif response.status_code == 401:
            return "Неверный токен авторизации"
        else:
            raise Exception(f"Не удалось выполнить запрос: {response.status_code} {response.text}")