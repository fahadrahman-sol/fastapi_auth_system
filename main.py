from fastapi import FastAPI
from routes import user, auth

app = FastAPI()

# Include routes
app.include_router(user.router, prefix="/user", tags=["User"])
app.include_router(auth.router, prefix="/auth", tags=["Auth"])

@app.get("/")
def root():
    return {"message": "FastAPI Authentication System"}
