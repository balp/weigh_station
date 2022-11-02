from dataclasses import dataclass


@dataclass
class StationData:
    lorries: int
    tons: int


seen_passages = StationData(0, 0)
