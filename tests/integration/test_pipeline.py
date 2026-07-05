import unittest
from packages.core import Frame, Scene, TemporalCoherenceEngine, VideoMetadata
from packages.services import Orchestrator


class TestPipeline(unittest.TestCase):
    def test_pipeline(self):
        engine = TemporalCoherenceEngine(None, None, None)
        orchestrator = Orchestrator(engine)
        video_metadata = VideoMetadata(100, 100, 100)
        scenes = orchestrator.process_video(video_metadata)
        self.assertIsInstance(scenes, list)

if __name__ == '__main__':
    unittest.main()
