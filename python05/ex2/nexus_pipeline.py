from typing import Any, List, Optional, Dict, Union, Protocol
from abc import ABC, abstractmethod


class ProcessingPipeline(ABC):
    pass


class ProcessingStage(Protocol):
    def process(data: Any) -> Any:
        pass


def main() -> None:
    pass


# useful https://dev.to/shameerchagani/what-is-a-protocol-in-python-3fl1
if __name__ == "__main__":
    main()
