from fastapi import FastAPI
from src.app.router.tracker_router import router as tracker_router
import uvicorn

app = FastAPI()
app.include_router(tracker_router)

if __name__ == '__main__':
    uvicorn.run(app , port=8080, host="0.0.0.0")
