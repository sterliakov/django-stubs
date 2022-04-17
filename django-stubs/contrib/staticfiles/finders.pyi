import sys
from typing import Any, Dict, Iterable, Iterator, List, Optional, Sequence, Tuple, Type, overload

from django.core.checks.messages import CheckMessage
from django.core.files.storage import FileSystemStorage, Storage
from django.utils._os import _PathCompatible

if sys.version_info < (3, 8):
    from typing_extensions import Literal
else:
    from typing import Literal

searched_locations: Any

class BaseFinder:
    def check(self, **kwargs: Any) -> List[CheckMessage]: ...
    @overload
    def find(self, path: _PathCompatible, all: Literal[False] = False) -> Optional[_PathCompatible]: ...  # type: ignore[misc]
    @overload
    def find(self, path: _PathCompatible, all: Literal[True] = ...) -> List[_PathCompatible]: ...
    def list(self, ignore_patterns: Optional[Iterable[str]]) -> Iterable[Any]: ...

class FileSystemFinder(BaseFinder):
    locations: List[Tuple[str, _PathCompatible]] = ...
    storages: Dict[_PathCompatible, Any] = ...
    def __init__(self, app_names: Sequence[str] = ..., *args: Any, **kwargs: Any) -> None: ...
    def find_location(
        self, root: _PathCompatible, path: str, prefix: Optional[str] = ...
    ) -> Optional[_PathCompatible]: ...
    @overload
    def find(self, path: _PathCompatible, all: Literal[False] = False) -> Optional[_PathCompatible]: ...  # type: ignore[misc]
    @overload
    def find(self, path: _PathCompatible, all: Literal[True] = ...) -> List[_PathCompatible]: ...
    def list(self, ignore_patterns: Optional[Iterable[str]]) -> Iterable[Any]: ...

class AppDirectoriesFinder(BaseFinder):
    storage_class: Type[FileSystemStorage] = ...
    source_dir: str = ...
    apps: List[str] = ...
    storages: Dict[_PathCompatible, FileSystemStorage] = ...
    def __init__(self, app_names: Optional[Iterable[str]] = ..., *args: Any, **kwargs: Any) -> None: ...
    def find_in_app(self, app: str, path: _PathCompatible) -> Optional[_PathCompatible]: ...
    @overload
    def find(self, path: _PathCompatible, all: Literal[False] = False) -> Optional[_PathCompatible]: ...  # type: ignore[misc]
    @overload
    def find(self, path: _PathCompatible, all: Literal[True] = ...) -> List[_PathCompatible]: ...
    def list(self, ignore_patterns: Optional[Iterable[str]]) -> Iterable[Any]: ...

class BaseStorageFinder(BaseFinder):
    storage: Storage = ...
    def __init__(self, storage: Optional[Storage] = ..., *args: Any, **kwargs: Any) -> None: ...
    @overload
    def find(self, path: _PathCompatible, all: Literal[False] = False) -> Optional[_PathCompatible]: ...  # type: ignore[misc]
    @overload
    def find(self, path: _PathCompatible, all: Literal[True] = ...) -> List[_PathCompatible]: ...
    def list(self, ignore_patterns: Optional[Iterable[str]]) -> Iterable[Any]: ...

class DefaultStorageFinder(BaseStorageFinder):
    storage: Storage = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

@overload
def find(path: _PathCompatible, all: Literal[False] = False) -> Optional[_PathCompatible]: ...  # type: ignore[misc]
@overload
def find(path: _PathCompatible, all: Literal[True] = ...) -> List[_PathCompatible]: ...
def get_finders() -> Iterator[BaseFinder]: ...
@overload
def get_finder(
    import_path: Literal["django.contrib.staticfiles.finders.FileSystemFinder"],
) -> FileSystemFinder: ...
@overload
def get_finder(
    import_path: Literal["django.contrib.staticfiles.finders.AppDirectoriesFinder"],
) -> AppDirectoriesFinder: ...
