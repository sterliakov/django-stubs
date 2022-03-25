from contextlib import ContextDecorator, contextmanager
from typing import Any, Callable, Iterator, Optional, Type, TypeVar, overload
from types import TracebackType

from django.db import ProgrammingError

class TransactionManagementError(ProgrammingError): ...

def get_connection(using: Optional[str] = ...) -> Any: ...
def get_autocommit(using: Optional[str] = ...) -> bool: ...
def set_autocommit(autocommit: bool, using: Optional[str] = ...) -> Any: ...
def commit(using: Optional[str] = ...) -> None: ...
def rollback(using: Optional[str] = ...) -> None: ...
def savepoint(using: Optional[str] = ...) -> str: ...
def savepoint_rollback(sid: str, using: Optional[str] = ...) -> None: ...
def savepoint_commit(sid: str, using: Optional[str] = ...) -> None: ...
def clean_savepoints(using: Optional[str] = ...) -> None: ...
def get_rollback(using: Optional[str] = ...) -> bool: ...
def set_rollback(rollback: bool, using: Optional[str] = ...) -> None: ...
@contextmanager
def mark_for_rollback_on_error(using: Optional[str] = ...) -> Iterator[None]: ...
def on_commit(func: Callable, using: Optional[str] = ...) -> None: ...

_C = TypeVar("_C", bound=Callable)  # Any callable

# Don't inherit from ContextDecorator, so we can provide a more specific signature for __call__
class Atomic:
    using: Optional[str] = ...
    savepoint: bool = ...
    def __init__(self, using: Optional[str], savepoint: bool, durable: bool) -> None: ...
    # When decorating, return the decorated function as-is, rather than clobbering it as ContextDecorator does.
    def __call__(self, func: _C) -> _C: ...
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: Optional[Type[BaseException]], exc_value: Optional[BaseException], traceback: Optional[TracebackType]) -> None: ...

# Bare decorator
@overload
def atomic(using: _C) -> _C: ...

# Decorator or context-manager with parameters
@overload
def atomic(using: Optional[str] = ..., savepoint: bool = ..., durable: bool = ...) -> Atomic: ...

# Bare decorator
@overload
def non_atomic_requests(using: _C) -> _C: ...

# Decorator with arguments
@overload
def non_atomic_requests(using: Optional[str] = ...) -> Callable[[_C], _C]: ...
