from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from .data.uwyoming import get_balloon_flight_times, read_wyoming_file, get_corresponding_nd_file
from pathlib import Path

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
    "http://localhost:5174",
    "http://127.0.0.1:5173",
    "http://127.0.0.1:5174",
    "https://ssirc-website.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/api/balloon/flights")
def get_balloon_flights(balloon: str = "wopc"):
    return get_balloon_flight_times(balloon)


@app.get("/api/balloon/flight")
def get_balloon_flight_data(filename: str, folder: str):

    cdir = Path(__file__).parent.parent.parent
    base = cdir / 'data' / "Locations"
    numden_folder = Path(folder) / "Nr_Full_Profile/Average_0.5_km"
    size_folder = Path(folder) / "SizeDist_Stratosphere"

    if filename.split('.')[-1] == '500m':
        filename = base / numden_folder / filename
    else:
        filename = base / size_folder / filename

    return read_wyoming_file(filename)


@app.get("/api/balloon/flight/nd_from_sd")
def get_balloon_flights(filename: str, folder: str):
    return get_corresponding_nd_file(filename, folder)
