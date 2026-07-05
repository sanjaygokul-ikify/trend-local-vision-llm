import unittest
from packages.core import Frame, Scene, TemporalCoherenceEngine


class TestRuntime(unittest.TestCase):
    def test_temporal_coherence_engine(self):
        engine = TemporalCoherenceEngine(None, None, None)
        frames = [Frame(1, 100, 100, 1, 0.5)]
        scenes = engine.detect_scenes(frames)
        self.assertIsInstance(scenes, list)

if __name__ == '__main__':
    unittest.main()
