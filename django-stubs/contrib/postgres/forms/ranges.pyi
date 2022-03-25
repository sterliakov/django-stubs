from psycopg2.extras import Range  # type: ignore
from typing import Any, Optional, Tuple, Type, Union

from django import forms
from django.db.models.fields import _ErrorMessagesT
from django.forms.widgets import MultiWidget
from django.forms.widgets import _OptAttrs


class RangeWidget(MultiWidget):
    def __init__(self, base_widget: Union[forms.Widget, Type[forms.Widget]], attrs: Optional[_OptAttrs] = ...) -> None: ...
    def decompress(self, value: Any) -> Tuple[Optional[Any], Optional[Any]]: ...

class HiddenRangeWidget(RangeWidget):
    def __init__(self, attrs: Optional[_OptAttrs] = ...) -> None: ...

class BaseRangeField(forms.MultiValueField):
    default_error_messages: _ErrorMessagesT
    base_field: Type[forms.Field]
    range_type: Type[Range]
    hidden_widget: Type[forms.Widget]
    def __init__(self, **kwargs: Any) -> None: ...
    def prepare_value(self, value: Any) -> Any: ...
    def compress(self, values: Tuple[Optional[Any], Optional[Any]]) -> Optional[Range]: ...

class IntegerRangeField(BaseRangeField):
    default_error_messages: _ErrorMessagesT
    base_field: Type[forms.Field]
    range_type: Type[Range]

class DecimalRangeField(BaseRangeField):
    default_error_messages: _ErrorMessagesT
    base_field: Type[forms.Field]
    range_type: Type[Range]

class DateTimeRangeField(BaseRangeField):
    default_error_messages: _ErrorMessagesT
    base_field: Type[forms.Field]
    range_type: Type[Range]

class DateRangeField(BaseRangeField):
    default_error_messages: _ErrorMessagesT
    base_field: Type[forms.Field]
    range_type: Type[Range]
