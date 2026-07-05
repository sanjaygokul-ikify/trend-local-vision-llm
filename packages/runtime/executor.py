import logging
from typing import List
from packages.core.engine import TemporalCoherenceEngine
from packages.core.types import VideoMetadata


class RuntimeExecutor:
    def __init__(self, engine: TemporalCoherenceEngine):
        self.engine = engine

    def execute(self, video_metadata: VideoMetadata) -> List[Scene]:
        try:
            scenes = self.engine.process_video(video_metadata)
            return scenes
        except VideoProcessingError as e:
            logging.error(f"Error executing video: {e}")
            raise


def main():
    # Create a TemporalCoherenceEngine instance
    engine = TemporalCoherenceEngine(None, None, None)
    # Create a RuntimeExecutor instance
    executor = RuntimeExecutor(engine)
    # Execute the video
    video_metadata = VideoMetadata(100, 1920, 1080)
    scenes = executor.execute(video_metadata)
    # Print the results
    for scene in scenes:
        print(f"Scene {scene.scene_id}: {len(scene.frames)} frames")
