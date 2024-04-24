import sched
import time

from src.orchestrator import PipelineOrchestrator

if __name__ == '__main__':
    s = sched.scheduler(time.time, time.sleep)
    orchestrator = PipelineOrchestrator(s)
    orchestrator.start_immediately()
