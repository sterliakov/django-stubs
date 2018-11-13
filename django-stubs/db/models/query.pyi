from collections import OrderedDict
from datetime import date, datetime
from typing import Generic, TypeVar, Optional, Any, Type, Dict, Union, overload, List, Iterator, Tuple, Callable

from django.db import models

_T = TypeVar('_T', bound=models.Model)


class QuerySet(Generic[_T]):
    def __init__(
            self,
            model: Optional[Type[models.Model]] = ...,
            query: Optional[Any] = ...,
            using: Optional[str] = ...,
            hints: Optional[Dict[str, models.Model]] = ...,
    ) -> None: ...
    @classmethod
    def as_manager(cls): ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[_T]: ...
    def __bool__(self) -> bool: ...
    @overload
    def __getitem__(self, k: slice) -> QuerySet[_T]: ...
    @overload
    def __getitem__(self, k: int) -> _T: ...
    @overload
    def __getitem__(self, k: str) -> Any: ...
    def __and__(self, other: QuerySet) -> QuerySet: ...
    def __or__(self, other: QuerySet) -> QuerySet: ...

    def iterator(self, chunk_size: int = ...) -> Iterator[_T]: ...
    def aggregate(
            self, *args: Any, **kwargs: Any
    ) -> Dict[str, Optional[Union[datetime, float]]]: ...
    def count(self) -> int: ...
    def get(
            self, *args: Any, **kwargs: Any
    ) -> _T: ...
    def create(self, **kwargs: Any) -> _T: ...
    def bulk_create(
            self,
            objs: Union[Iterator[Any], List[models.Model]],
            batch_size: Optional[int] = ...,
    ) -> List[_T]: ...

    def get_or_create(
            self,
            defaults: Optional[Union[Dict[str, date], Dict[str, models.Model]]] = ...,
            **kwargs: Any
    ) -> Tuple[_T, bool]: ...

    def update_or_create(
            self,
            defaults: Optional[
                Union[
                    Dict[str, Callable],
                    Dict[str, date],
                    Dict[str, models.Model],
                    Dict[str, str],
                ]
            ] = ...,
            **kwargs: Any
    ) -> Tuple[_T, bool]: ...

    def earliest(
            self, *fields: Any, field_name: Optional[Any] = ...
    ) -> _T: ...

    def latest(
            self, *fields: Any, field_name: Optional[Any] = ...
    ) -> _T: ...

    def first(self) -> Optional[Union[Dict[str, int], _T]]: ...

    def last(self) -> Optional[_T]: ...

    def in_bulk(
            self, id_list: Any = ..., *, field_name: str = ...
    ) -> Union[Dict[int, models.Model], Dict[str, models.Model]]: ...

    def delete(self) -> Tuple[int, Dict[str, int]]: ...

    def update(self, **kwargs: Any) -> int: ...

    def exists(self) -> bool: ...

    def explain(
            self, *, format: Optional[Any] = ..., **options: Any
    ) -> str: ...

    def raw(
            self,
            raw_query: str,
            params: Any = ...,
            translations: Optional[Dict[str, str]] = ...,
            using: None = ...,
    ) -> RawQuerySet: ...

    def values(self, *fields: Any, **expressions: Any) -> QuerySet: ...

    def values_list(
            self, *fields: Any, flat: bool = ..., named: bool = ...
    ) -> QuerySet: ...

    def dates(
            self, field_name: str, kind: str, order: str = ...
    ) -> QuerySet: ...

    def datetimes(
            self, field_name: str, kind: str, order: str = ..., tzinfo: None = ...
    ) -> QuerySet: ...

    def none(self) -> QuerySet[_T]: ...

    def all(self) -> QuerySet[_T]: ...

    def filter(self, *args: Any, **kwargs: Any) -> QuerySet[_T]: ...

    def exclude(self, *args: Any, **kwargs: Any) -> QuerySet[_T]: ...

    def complex_filter(
            self,
            filter_obj: Any,
    ) -> QuerySet[_T]: ...

    def union(self, *other_qs: Any, all: bool = ...) -> QuerySet[_T]: ...

    def intersection(self, *other_qs: Any) -> QuerySet[_T]: ...

    def difference(self, *other_qs: Any) -> QuerySet[_T]: ...

    def select_for_update(
            self, nowait: bool = ..., skip_locked: bool = ..., of: Tuple = ...
    ) -> QuerySet: ...

    def select_related(self, *fields: Any) -> QuerySet[_T]: ...

    def prefetch_related(self, *lookups: Any) -> QuerySet[_T]: ...

    def annotate(self, *args: Any, **kwargs: Any) -> QuerySet[_T]: ...

    def order_by(self, *field_names: Any) -> QuerySet[_T]: ...

    def distinct(self, *field_names: Any) -> QuerySet[_T]: ...

    def extra(
            self,
            select: Optional[
                Union[Dict[str, int], Dict[str, str], OrderedDict]
            ] = ...,
            where: Optional[List[str]] = ...,
            params: Optional[Union[List[int], List[str]]] = ...,
            tables: Optional[List[str]] = ...,
            order_by: Optional[Union[List[str], Tuple[str]]] = ...,
            select_params: Optional[Union[List[int], List[str], Tuple[int]]] = ...,
    ) -> QuerySet[_T]: ...

    def reverse(self) -> QuerySet[_T]: ...

    def defer(self, *fields: Any) -> QuerySet[_T]: ...

    def only(self, *fields: Any) -> QuerySet[_T]: ...

    def using(self, alias: Optional[str]) -> QuerySet[_T]: ...

    @property
    def ordered(self) -> bool: ...

    @property
    def db(self) -> str: ...

    def resolve_expression(self, *args: Any, **kwargs: Any) -> Any: ...


class RawQuerySet:
    pass


class RawQuery(object):
    pass


class Query(object):
    pass