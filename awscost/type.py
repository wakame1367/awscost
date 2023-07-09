from typing import List, Optional
from pydantic import BaseModel

class Metrics(BaseModel):
    UnblendedCost: dict
    # 他のメトリクスをここに追加する

class Group(BaseModel):
    Keys: List[str]
    Metrics: Metrics

class ResultsByTime(BaseModel):
    TimePeriod: dict
    Total: Metrics
    Groups: List[Group]

class CostExplorerResponse(BaseModel):
    ResultsByTime: List[ResultsByTime]
    # 他のフィールドをここに追加する