from typing import Any, List, Dict, Union, Protocol
from abc import ABC, abstractmethod


class NexusManagerError(Exception):
    pass


class ProcessingStage(Protocol):
    def process(data: Any) -> Any:
        pass


class InputStage:
    def __init__(self) -> None:
        print("Stage 1: Input validation and parsing")

    def process(self, data: Any) -> Dict:
        print(f"Input: {data}")
        if isinstance(data, dict):
            return {"adapter": "JSON", "data": data}
        elif data == "Real-time sensor stream":
            return {"adapter": "STREAM", "data": data}
        else:
            return {"adapter": "CSV", "data": data}


class TransformStage:
    def __init__(self) -> None:
        print("Stage 2: Data transformation and enrichment")

    def process(self, data: Any) -> Dict:
        if data["adapter"] == "JSON":
            pass
        elif data["adapter"] == "CSV":
            pass
        elif data["adapter"] == "STREAM":
            pass


class OutputStage:
    def __init__(self) -> None:
        print("Stage 3: Output formatting and delivery")

    def process(self, data: Any) -> str:
        if data["adapter"] == "JSON":
            pass
        elif data["adapter"] == "CSV":
            pass
        elif data["adapter"] == "STREAM":
            pass


class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id: str) -> None:
        self.stages: List[Union[InputStage,
                                TransformStage,
                                OutputStage
                                ]] = []
        self.pipeline_id: str = pipeline_id

    def add_stage(self, stage: Union[
        InputStage,
        TransformStage,
        OutputStage
         ]) -> None:
        self.stages = self.stages + [stage]

    @abstractmethod
    def process(self, data: Any) -> Any:
        pass


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        temp: dict = self.stages[0].process(data)
        for stage in self.stages[1:]:
            if isinstance(stage, TransformStage):
                temp = stage.process(temp)
            else:
                stage.process(temp)


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        pass


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        pass


class NexusManager:
    def __init__(self) -> None:
        print("Initializing Nexus Manager...")
        self.capacity: int = 1000
        print(f"Pipeline capacity: {self.capacity} streams/second")
        self.pipelines: List[ProcessingPipeline] = []

    def add_pipeline(self, new_pipeline: ProcessingPipeline) -> None:
        if self.capacity <= 0:
            raise NexusManagerError("no more capacity in the manager")
        for pipeline in self.pipelines:
            if pipeline.pipeline_id == new_pipeline.pipeline_id:
                raise NexusManagerError(f"'{new_pipeline.pipeline_id}' already"
                                        " exists")
        self.pipelines = self.pipelines + [new_pipeline]
        self.capacity -= 1

    def process_data(self, adapter: ProcessingPipeline, data: Any) -> None:
        for pipeline in self.pipelines:
            if isinstance(pipeline, adapter):
                try:
                    pipeline.process(data)
                except Exception as e:
                    print(f"[ERROR:{e.__class__.__name__}]: {e}")
                break


def main() -> None:
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")
    nexus: NexusManager = NexusManager()

    print("\nCreating Data Processing Pipeline...")
    stages: List[ProcessingStage] = [
        InputStage(),
        TransformStage(),
        OutputStage()
    ]
    pipelines: List[ProcessingPipeline] = [
        JSONAdapter("JSON_001"),
        CSVAdapter("CSV_001"),
        StreamAdapter("STREAM_001"),
    ]

    for pipeline in pipelines:
        for stage in stages:
            pipeline.add_stage(stage)
        nexus.add_pipeline(pipeline)

    print("\n=== Multi-Format Data Processing ===\n")
    data: dict[str, Any] = {
        "JSON": {"sensor": "temp", "value": 23.5, "unit": "C"},
        "CSV": "user,action,timestamp",
        "STREAM": "Real-time sensor stream"
    }

    for key in data:
        if key == "JSON":
            nexus.process_data(JSONAdapter, data[key])
        elif key == "CSV":
            nexus.process_data(CSVAdapter, data[key])
        elif key == "STREAM":
            nexus.process_data(StreamAdapter, data[key])


if __name__ == "__main__":
    main()
