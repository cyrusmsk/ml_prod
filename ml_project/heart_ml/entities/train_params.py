from dataclasses import dataclass, field


@dataclass()
class TrainingParams:
    model_type: str = field(default="CatBoostClassifier")