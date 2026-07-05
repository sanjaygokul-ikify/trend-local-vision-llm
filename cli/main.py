import argparse
from packages.core import TemporalCoherenceEngine, VideoMetadata
from packages.services import Orchestrator
from packages.utils import logger


def main():
    parser = argparse.ArgumentParser(description='Video Analysis CLI')
    parser.add_argument('--video-metadata', help='Video metadata', required=True)
    args = parser.parse_args()
    video_metadata = VideoMetadata(**eval(args.video_metadata))
    engine = TemporalCoherenceEngine(None, None, None)
    orchestrator = Orchestrator(engine)
    scenes = orchestrator.process_video(video_metadata)
    logger.info('Video processed successfully')

if __name__ == '__main__':
    main()
