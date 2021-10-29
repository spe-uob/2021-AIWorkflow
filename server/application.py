from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from loguru import logger
import uvicorn

app = FastAPI()

origins = ["*"]

app.add_middleware(
	CORSMiddleware,
	allow_origins=origins,
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

@app.get("/hello_world")
def root():
    return JSONResponse({"message": "app is running", "success": True}, 200)

if __name__ == "__main__":
	uvicorn.run("application:app", host="0.0.0.0", port=80, reload=True)