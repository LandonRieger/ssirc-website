from pathlib import Path


def get_data_folder(campaign: str):
    cdir = Path(__file__).parent.parent.parent.parent
    return cdir / "data" / campaign / "Locations"
