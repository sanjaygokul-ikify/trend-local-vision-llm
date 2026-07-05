class VideoProcessingError(Exception):
    pass

class FrameExtractionError(VideoProcessingError):
    pass

class SceneDetectionError(VideoProcessingError):
    pass

class SceneOptimizationError(VideoProcessingError):
    pass
