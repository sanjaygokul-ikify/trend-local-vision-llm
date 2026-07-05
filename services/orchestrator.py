from packages.core import TemporalCoherenceEngine
from packages.utils import logger


class Orchestrator:
    def __init__(self, engine: TemporalCoherenceEngine):
        self.engine = engine

    def process_video(self, video_metadata: TemporalCoherenceEngine.VideoMetadata) -> list:
        try:
            scenes = self.engine.process_video(video_metadata)
            logger.info('Video processed successfully')
            return scenes
        except Exception as e:
            logger.error(f'Error processing video: {e}')
            raise
