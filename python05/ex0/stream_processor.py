from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def format_output(self, result: str) -> str:
        return "Output: " + result


class NumericProcessor(DataProcessor):
    def process(self, data: list[int]) -> str:
        data_len: int = len(data)
        result: str = f"Processed {data_len} numeric values, "
        result += f"sum={sum(data)}, "
        if data_len > 0:
            result += f"avg={sum(data)/data_len}"
        else:
            result += "avg=0"
        return result

    def validate(self, data: list[int]) -> bool:
        for element in data:
            if element.__class__.__name__ != "int":
                return False
        print("Numeric data verified")
        return True

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class TextProcessor(DataProcessor):
    def process(self, data: str) -> str:
        chars_count: int = len(data)
        words_count: int = len(data.split(' '))
        return f"Processed text: {chars_count} characters, {words_count} words"

    def validate(self, data: str) -> bool:
        if data.__class__.__name__ == "str":
            print("Text data verified")
            return True
        return False

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class LogProcessor(DataProcessor):
    def process(self, data: str) -> str:
        log_type, log_msg = data.split(":", 1)
        result: str = ""
        if log_type == "ERROR":
            result += "[ALERT] "
        else:
            result += f"[{log_type}] "
        return result + f"{log_type} level detected:{log_msg}"

    def validate(self, data: str) -> bool:
        log_type, _ = data.split(":", 1)
        if log_type in ["ERROR", "INFO", "WARNING"]:
            print("Log entry verified")
            return True
        return False

    def format_output(self, result: str) -> str:
        return super().format_output(result)


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    print("\nInitializing Numeric Processor...")
    np: NumericProcessor = NumericProcessor()
    data_np: list[int] = [1, 2, 3, 4, 5]
    print(f"Processing data: {data_np}")
    np_output: str = np.process(data_np)
    print("Validation: ", end="")
    if np.validate(data_np):
        print(np.format_output(np_output))

    print("\nInitializing Text Processor...")
    tp: TextProcessor = TextProcessor()
    data_tp: str = "Hello Nexus World"
    print(f"Processing data: \"{data_tp}\"")
    tp_output: str = tp.process(data_tp)
    print("Validation: ", end="")
    if tp.validate(data_tp):
        print(tp.format_output(tp_output))

    print("\nInitializing Log Processor...")
    lp: LogProcessor = LogProcessor()
    data_lp: str = "ERROR: Connection timeout"
    print(f"Processing data: \"{data_lp}\"")
    lp_output: str = lp.process(data_lp)
    print("Validation: ", end="")
    if lp.validate(data_lp):
        print(lp.format_output(lp_output))

    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    specialized: list[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor()
    ]
    datas: list[Any] = [
        [0, 2, 4],
        "Hello World",
        "INFO: System Ready"
    ]
    for i in range(3):
        data_processor: DataProcessor = specialized[i]
        print(f"Result {i + 1}: {data_processor.process(datas[i])}")
    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
