from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/api/data")
def get_data():
    # This is the data your backend sends back
    return {
        "status": "success",
        "message": "Hello from Render!",
        "items": ["Python", "FastAPI", "Render"]
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
