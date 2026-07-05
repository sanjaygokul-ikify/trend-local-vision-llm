import unittest
from packages.core import Frame, Scene, TemporalCoherenceEngine, VideoMetadata


class TestCore(unittest.TestCase):
    def test_frame(self):
        frame = Frame(1, 100, 100, 1, 0.5)
        self.assertEqual(frame.frame_id, 1)
        self.assertEqual(frame.width, 100)
        self.assertEqual(frame.height, 100)
        self.assertEqual(frame.scene_id, 1)
        self.assertEqual(frame.score, 0.5)

    def test_scene(self):
        scene = Scene(1, [])
        self.assertEqual(scene.scene_id, 1)
        self.assertEqual(scene.frames, [])

    def test_video_metadata(self):
        video_metadata = VideoMetadata(100, 100, 100)
        self.assertEqual(video_metadata.frame_count, 100)
        self.assertEqual(video_metadata.width, 100)
        self.assertEqual(video_metadata.height, 100)

    def test_temporal_coherence_engine(self):
        engine = TemporalCoherenceEngine(None, None, None)
        video_metadata = VideoMetadata(100, 100, 100)
        scenes = engine.process_video(video_metadata)
        self.assertIsInstance(scenes, list)

if __name__ == '__main__':
    unittest.main()
