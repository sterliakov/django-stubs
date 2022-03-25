from typing import Any, Optional

from django.db.models.expressions import Func
from django.db import models

class CumeDist(Func):
    output_field: models.FloatField = ...

class DenseRank(Func):
    output_field: models.IntegerField = ...

class FirstValue(Func): ...

class LagLeadFunction(Func):
    def __init__(
        self, expression: Optional[str], offset: int = ..., default: Optional[int] = ..., **extra: Any
    ) -> None: ...

class Lag(LagLeadFunction): ...
class LastValue(Func): ...
class Lead(LagLeadFunction): ...

class NthValue(Func):
    def __init__(self, expression: Optional[str], nth: int = ..., **extra: Any) -> None: ...

class Ntile(Func):
    def __init__(self, num_buckets: int = ..., **extra: Any) -> None: ...
    output_field: models.IntegerField = ...

class PercentRank(Func):
    output_field: models.FloatField = ...

class Rank(Func):
    output_field: models.IntegerField = ...

class RowNumber(Func):
    output_field: models.IntegerField = ...
