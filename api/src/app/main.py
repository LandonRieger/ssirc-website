from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import app.utils.uwyoming as uw
import app.utils.b2sap as bp
from pathlib import Path
from app import data_dir

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
    "http://localhost:5174",
    "http://127.0.0.1:5173",
    "http://127.0.0.1:5174",
    "https://ssirc-website.vercel.app",
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
    return uw.get_balloon_flight_times(
        balloon, uw.get_data_folder()
    ) + bp.get_balloon_flight_times(balloon, bp.get_data_folder())


@app.get("/api/balloon/flight")
def get_balloon_flight_data(filename: str, folder: str, campaign: str = "UWyoming"):

    cdir = Path(__file__).parent.parent.parent
    print(cdir)
    base = data_dir() / campaign / "Locations"

    if campaign == "UWyoming":
        numden_folder = Path(folder) / "Nr_Full_Profile/Average_0.5_km"
        size_folder = Path(folder) / "SizeDist_Stratosphere"

        if filename.split(".")[-1] == "500m":
            filename = base / numden_folder / filename
        else:
            filename = base / size_folder / filename
        return uw.read_file(filename)

    else:
        filename = base / folder / filename
        return bp.read_file(filename)


@app.get("/api/balloon/flight/nd_from_sd")
def get_nd_from_sd(filename: str, folder: str):
    return uw.get_corresponding_nd_file(filename, folder, uw.get_data_folder())


@app.get("/api")
def api_return():
    return {"api": "ssirc-api"}


@app.get("/api/data_dir")
def get_data_dir():
    return {"directory": data_dir().as_posix()}


@app.get("/api/data_dir/ls")
def get_data_folders():
    return {"directory": [l.as_posix() for l in data_dir().glob("*")]}
