"""This module contains the code required to run the backend application."""
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from routers.routers import user_router, tweet_router, workflow_router

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)
app.include_router(tweet_router)
app.include_router(workflow_router)

@app.get("/")
def root():
    """Root endpoint to check that the application is running."""
    return JSONResponse({"message": "app is running", "success": True}, 200)


if __name__ == "__main__":
    uvicorn.run("application:app", host="0.0.0.0", port=80, reload=True)
