from fastapi import FastAPI
from app.router.tracker_router import router as tracker_router
import uvicorn

app = FastAPI()

# @app.on_event("startup")
# async def on_startup():
#     await init_db()

app.include_router(tracker_router)

if __name__ == '__main__':
    uvicorn.run(app , port=8080, host="0.0.0.0")
