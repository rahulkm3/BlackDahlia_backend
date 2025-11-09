# File: main.py (FastAPI backend)
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
import uvicorn

app = FastAPI()

# Allow CORS so Streamlit can fetch from here
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/get_data")
def get_data(lat: float = Query(...), lon: float = Query(...),
             start: str = Query(...), end: str = Query(...)):
    # Replace this mock logic with GEE or your real transformation
    dummy_response = {
        "NDVI": round(0.4 + lat*0.001 - lon*0.0001, 4),
        "Rainfall": round(50 + lat - lon, 2),
        "NightLights": round(lat * lon % 5, 3),
    }
    return dummy_response

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
