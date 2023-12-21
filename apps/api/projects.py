from fastapi import HTTPException, Header, Depends
import httpx
from fastapi import APIRouter
from fastapi.security.api_key import APIKeyHeader
from fastapi.responses import JSONResponse
from fastapi import status


router = APIRouter()

backend_url = 'http://127.0.0.1:8001/api/'
projects_api_url = backend_url+'monitoring/projects/'
scenarios_api_url = backend_url+'project_calculations/variants_kits/'

token_header = APIKeyHeader(name="Token")

@router.get("/projects/")
async def get_projects(token: str = Depends(token_header)):

    headers = {
        "Authorization": token
    }

    async with httpx.AsyncClient(timeout=httpx.Timeout(timeout=30.0)) as client:
        response = await client.get(projects_api_url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            error_message = f"Ошибка при запросе: Статус код {response.status_code}"
            error_details = response.text
            return {"error": error_message, "error_details": error_details}

@router.get("/project_scenarios/{project_id}")
async def get_project_scenarios(project_id: int, authorization: str = Header(None, convert_underscores=False)):
    if authorization is None:
        raise HTTPException(status_code=401, detail="Не предоставлен токен авторизации")

    headers = {
        "Authorization": authorization
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(scenarios_api_url+'?project='+project_id, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            return {"project_id": project_id, "scenarios": data}
        elif response.status_code == 404:
            raise HTTPException(status_code=404, detail="Проект не найден")
        else:
            raise HTTPException(status_code=500, detail="Не удалось получить сценарии из внешнего API")
