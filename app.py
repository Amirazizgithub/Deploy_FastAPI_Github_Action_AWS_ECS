import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.routes import routes

app = FastAPI()

# CORS Middleware - Keep if needed, but if serving frontend and backend
# from the same FastAPI app, it might not be strictly necessary.
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the router from routes.py
# This connects the /query_response and /session_history endpoints
app.include_router(routes)

if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
