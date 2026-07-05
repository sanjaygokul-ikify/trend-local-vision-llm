from dataclasses import dataclass
from typing import List

@dataclass
class Frame:
    frame_id: int
    width: int
    height: int
    scene_id: int
    score: float

@dataclass
class Scene:
    scene_id: int
    frames: List[Frame]

@dataclass
class VideoMetadata:
    frame_count: int
    width: int
    height: int
