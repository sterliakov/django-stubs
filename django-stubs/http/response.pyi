import datetime
from io import BytesIO
from json import JSONEncoder
from typing import (
    Any, Dict, Iterable, Iterator, List, Optional, Tuple, Type, TypeVar, Union,
    overload, type_check_only
)

from django.http.cookie import SimpleCookie
from django.utils.datastructures import CaseInsensitiveMapping, _PropertyDescriptor

class BadHeaderError(ValueError): ...

_Z = TypeVar("_Z")

class ResponseHeaders(CaseInsensitiveMapping[str]):
    def __init__(self, data: Dict[str, str]) -> None: ...
    def _convert_to_charset(self, value: Union[bytes, str, int], charset: str, mime_encode: bool = ...) -> str: ...
    def __delitem__(self, key: str) -> None: ...
    def __setitem__(self, key: str, value: Union[str, bytes, int]) -> None: ...
    def pop(self, key: str, default: _Z = ...) -> Union[_Z, Tuple[str, str]]: ...
    def setdefault(self, key: str, value: Union[str, bytes, int]) -> None: ...

class HttpResponseBase:
    status_code: int = ...
    streaming: bool = ...
    cookies: SimpleCookie = ...
    closed: bool = ...
    headers: ResponseHeaders = ...
    def __init__(
        self,
        content_type: Optional[str] = ...,
        status: Optional[int] = ...,
        reason: Optional[str] = ...,
        charset: Optional[str] = ...,
        headers: Optional[Dict[str, str]] = ...,
    ) -> None: ...
    @property
    def reason_phrase(self) -> str: ...
    @reason_phrase.setter
    def reason_phrase(self, value: str) -> None: ...
    @property
    def charset(self) -> str: ...
    @charset.setter
    def charset(self, value: str) -> None: ...
    def serialize_headers(self) -> bytes: ...
    __bytes__ = serialize_headers
    def __setitem__(self, header: str, value: Union[str, bytes, int]) -> None: ...
    def __delitem__(self, header: str) -> None: ...
    def __getitem__(self, header: str) -> str: ...
    def has_header(self, header: str) -> bool: ...
    def items(self) -> Iterable[Tuple[str, str]]: ...
    @overload
    def get(self, header: str, alternate: str) -> str: ...
    @overload
    def get(self, header: str, alternate: None = ...) -> Optional[str]: ...
    def set_cookie(
        self,
        key: str,
        value: str = ...,
        max_age: Optional[int] = ...,
        expires: Optional[Union[str, datetime.datetime]] = ...,
        path: str = ...,
        domain: Optional[str] = ...,
        secure: bool = ...,
        httponly: bool = ...,
        samesite: str = ...,
    ) -> None: ...
    def setdefault(self, key: str, value: str) -> None: ...
    def set_signed_cookie(self, key: str, value: str, salt: str = ..., **kwargs: Any) -> None: ...
    def delete_cookie(
        self, key: str, path: str = ..., domain: Optional[str] = ..., samesite: Optional[str] = ...
    ) -> None: ...
    def make_bytes(self, value: object) -> bytes: ...
    def close(self) -> None: ...
    def write(self, content: Union[str, bytes]) -> None: ...
    def flush(self) -> None: ...
    def tell(self) -> int: ...
    def readable(self) -> bool: ...
    def seekable(self) -> bool: ...
    def writable(self) -> bool: ...
    def writelines(self, lines: Iterable[object]) -> None: ...

    # Fake methods that are implemented by all subclasses
    @type_check_only
    def __iter__(self) -> Iterator[bytes]: ...
    @type_check_only
    def getvalue(self) -> bytes: ...

class HttpResponse(HttpResponseBase, Iterable[bytes]):
    content = _PropertyDescriptor[object, bytes]()
    csrf_cookie_set: bool
    redirect_chain: List[Tuple[str, int]]
    sameorigin: bool
    test_server_port: str
    test_was_secure_request: bool
    xframe_options_exempt: bool
    def __init__(self, content: object = ..., *args: Any, **kwargs: Any) -> None: ...
    def serialize(self) -> bytes: ...
    __bytes__ = serialize
    def __iter__(self) -> Iterator[bytes]: ...
    def getvalue(self) -> bytes: ...

class StreamingHttpResponse(HttpResponseBase, Iterable[bytes]):
    streaming_content = _PropertyDescriptor[Iterable[object], Iterator[bytes]]()
    def __init__(self, streaming_content: Iterable[object] = ..., *args: Any, **kwargs: Any) -> None: ...
    def __iter__(self) -> Iterator[bytes]: ...
    def getvalue(self) -> bytes: ...

class FileResponse(StreamingHttpResponse):
    file_to_stream: Optional[BytesIO]
    block_size: int = ...
    as_attachment: bool = ...
    filename: str = ...
    def __init__(self, *args: Any, as_attachment: bool = ..., filename: str = ..., **kwargs: Any) -> None: ...
    def set_headers(self, filelike: BytesIO) -> None: ...

class HttpResponseRedirectBase(HttpResponse):
    allowed_schemes: List[str] = ...
    def __init__(self, redirect_to: str, *args: Any, **kwargs: Any) -> None: ...
    @property
    def url(self) -> str: ...

class HttpResponseRedirect(HttpResponseRedirectBase): ...
class HttpResponsePermanentRedirect(HttpResponseRedirectBase): ...

class HttpResponseNotModified(HttpResponse):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class HttpResponseBadRequest(HttpResponse): ...
class HttpResponseNotFound(HttpResponse): ...
class HttpResponseForbidden(HttpResponse): ...

class HttpResponseNotAllowed(HttpResponse):
    def __init__(self, permitted_methods: Iterable[str], *args: Any, **kwargs: Any) -> None: ...

class HttpResponseGone(HttpResponse): ...
class HttpResponseServerError(HttpResponse): ...
class Http404(Exception): ...

class JsonResponse(HttpResponse):
    def __init__(
        self,
        data: Any,
        encoder: Type[JSONEncoder] = ...,
        safe: bool = ...,
        json_dumps_params: Optional[Dict[str, Any]] = ...,
        **kwargs: Any
    ) -> None: ...
