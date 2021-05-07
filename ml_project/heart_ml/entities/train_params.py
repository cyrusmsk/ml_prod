from dataclasses import dataclass, field


@dataclass()
class TrainingParams:
    model_type: str = field(default="CatboostClassifier")
    random_state: int = field(default=31337)