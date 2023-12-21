

@app.get("/financial_tables/")
async def get_financial_tables(project_id_request: ProjectIDRequest):
    project_id = project_id_request.project_id
    
    api_url = f"{external_api_url}/{project_id}/financial_tables"

    async with httpx.AsyncClient() as client:
        response = await client.get(api_url)
        
        if response.status_code == 200:
            data = response.json()
            return {"project_id": project_id, "financial_tables": data}
        elif response.status_code == 404:
            raise HTTPException(status_code=404, detail="Project not found")
        else:
            raise HTTPException(status_code=500, detail="Failed to fetch financial tables from the external API")