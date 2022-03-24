from contextlib import contextmanager
from datetime import tzinfo
from typing import (
    Any, Callable, Dict, Generator, Iterator, List, Optional, Set,
    Tuple, Type, TypeVar,
)

from django.db.backends.base.client import BaseDatabaseClient
from django.db.backends.base.creation import BaseDatabaseCreation
from django.db.backends.base.features import BaseDatabaseFeatures
from django.db.backends.base.introspection import BaseDatabaseIntrospection
from django.db.backends.base.operations import BaseDatabaseOperations
from django.db.backends.base.schema import BaseDatabaseSchemaEditor
from django.db.backends.base.validation import BaseDatabaseValidation
from django.db.backends.utils import CursorDebugWrapper, CursorWrapper

NO_DB_ALIAS: str

_T = TypeVar("_T", bound="BaseDatabaseWrapper")
_ExecuteWrapper = Callable[[Callable[[str, Any, bool, Dict[str, Any]], Any], str, Any, bool, Dict[str, Any]], Any]

class BaseDatabaseWrapper:
    data_types: Dict[str, str] = ...
    data_types_suffix: Dict[str, str] = ...
    data_type_check_constraints: Dict[str, str] = ...
    vendor: str = ...
    display_name: str = ...
    SchemaEditorClass: Type[BaseDatabaseSchemaEditor] = ...
    client_class: Type[BaseDatabaseClient] = ...
    creation_class: Type[BaseDatabaseCreation] = ...
    features_class: Type[BaseDatabaseFeatures] = ...
    introspection_class: Type[BaseDatabaseIntrospection] = ...
    ops_class: Type[BaseDatabaseOperations] = ...
    validation_class: Type[BaseDatabaseValidation] = ...
    queries_limit: int = ...
    connection: Any = ...
    settings_dict: Dict[str, Any] = ...
    alias: str = ...
    queries_log: Any = ...
    force_debug_cursor: bool = ...
    autocommit: bool = ...
    in_atomic_block: bool = ...
    savepoint_state: int = ...
    savepoint_ids: List[str] = ...
    commit_on_exit: bool = ...
    needs_rollback: bool = ...
    close_at: Optional[float] = ...
    closed_in_transaction: bool = ...
    errors_occurred: bool = ...
    run_on_commit: List[Tuple[Set[str], Callable[[], None]]] = ...
    run_commit_hooks_on_set_autocommit_on: bool = ...
    execute_wrappers: List[_ExecuteWrapper] = ...
    client: BaseDatabaseClient = ...
    creation: BaseDatabaseCreation = ...
    features: BaseDatabaseFeatures = ...
    introspection: BaseDatabaseIntrospection = ...
    ops: BaseDatabaseOperations = ...
    validation: BaseDatabaseValidation = ...
    def __init__(self, settings_dict: Dict[str, Any], alias: str = ...) -> None: ...
    def ensure_timezone(self) -> bool: ...
    @property
    def timezone(self) -> Optional[tzinfo]: ...
    @property
    def timezone_name(self) -> str: ...
    @property
    def queries_logged(self) -> bool: ...
    @property
    def queries(self) -> List[Dict[str, str]]: ...
    def get_connection_params(self) -> Dict[str, Any]: ...
    def get_new_connection(self, conn_params: Any) -> Any: ...
    def init_connection_state(self) -> None: ...
    def create_cursor(self, name: Optional[Any] = ...) -> Any: ...
    def connect(self) -> None: ...
    def check_settings(self) -> None: ...
    def ensure_connection(self) -> None: ...
    def cursor(self) -> CursorWrapper: ...
    def commit(self) -> None: ...
    def rollback(self) -> None: ...
    def close(self) -> None: ...
    def savepoint(self) -> Optional[str]: ...
    def savepoint_rollback(self, sid: str) -> None: ...
    def savepoint_commit(self, sid: str) -> None: ...
    def clean_savepoints(self) -> None: ...
    def get_autocommit(self) -> bool: ...
    def set_autocommit(self, autocommit: bool, force_begin_transaction_with_broken_autocommit: bool = ...) -> None: ...
    def get_rollback(self) -> bool: ...
    def set_rollback(self, rollback: bool) -> None: ...
    def validate_no_atomic_block(self) -> None: ...
    def validate_no_broken_transaction(self) -> None: ...
    @contextmanager
    def constraint_checks_disabled(self) -> Iterator[None]: ...
    def disable_constraint_checking(self) -> bool: ...
    def enable_constraint_checking(self) -> None: ...
    def check_constraints(self, table_names: Optional[Any] = ...) -> None: ...
    def is_usable(self) -> bool: ...
    def close_if_unusable_or_obsolete(self) -> None: ...
    @property
    def allow_thread_sharing(self) -> bool: ...
    def inc_thread_sharing(self) -> None: ...
    def dec_thread_sharing(self) -> None: ...
    def validate_thread_sharing(self) -> None: ...
    def prepare_database(self) -> None: ...
    @property
    def wrap_database_errors(self) -> Any: ...
    def chunked_cursor(self) -> CursorWrapper: ...
    def make_debug_cursor(self, cursor: CursorWrapper) -> CursorDebugWrapper: ...
    def make_cursor(self, cursor: CursorWrapper) -> CursorWrapper: ...
    @contextmanager
    def temporary_connection(self) -> Generator[CursorWrapper, None, None]: ...
    def schema_editor(self, *args: Any, **kwargs: Any) -> BaseDatabaseSchemaEditor: ...
    def on_commit(self, func: Callable[[], None]) -> None: ...
    def run_and_clear_commit_hooks(self) -> None: ...
    @contextmanager
    def execute_wrapper(self, wrapper: _ExecuteWrapper) -> Generator[None, None, None]: ...
    def copy(self: _T, alias: Optional[str] = ...) -> _T: ...
