from typing import Any, Callable, Dict, List, Optional, Set, Type

from django.contrib.gis.db.backends.base.operations import BaseSpatialOperations as BaseSpatialOperations
from django.db.backends.mysql.operations import DatabaseOperations as DatabaseOperations
from django.contrib.gis.db.backends.utils import SpatialOperator
from django.contrib.gis.geos.geometry import GEOSGeometryBase

class MySQLOperations(BaseSpatialOperations, DatabaseOperations):
    name: str = ...
    geom_func_prefix: str = ...
    Adapter: Any = ...
    @property
    def mariadb(self) -> bool: ...
    @property
    def mysql(self) -> bool: ...  # type: ignore
    @property
    def select(self) -> str: ...  # type: ignore
    @property
    def from_text(self) -> str: ...  # type: ignore
    @property
    def gis_operators(self) -> Dict[str, SpatialOperator]: ...
    disallowed_aggregates: Any = ...
    @property
    def unsupported_functions(self) -> Set[str]: ...  # type: ignore
    def geo_db_type(self, f: Any) -> Any: ...
    def get_distance(self, f: Any, value: Any, lookup_type: Any) -> List[Any]: ...
    def get_geometry_converter(
        self, expression: Any
    ) -> Callable[[Any, Any, Any], Optional[GEOSGeometryBase]]: ...
