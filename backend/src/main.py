from fastapi import FastAPI
from backend.src.user.routes.user_routes import router as user_router

app = FastAPI(
	title="DRPortal Backend API", 
	description="This backend is meant for DrPortal's use only and should not be used by any other party.",
	version="0.0.1"
) 

@app.get("/")
def root():
	return {"Message": "Hello World"}

app.include_router(user_router, prefix="/api/v1", target=["users"])