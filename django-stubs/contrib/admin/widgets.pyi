from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple, Union

from django import forms
from django.contrib.admin.sites import AdminSite
from django.core.files.base import File
from django.db.models.fields.reverse_related import (
    ForeignObjectRel, ManyToOneRel, ManyToManyRel
)
from django.forms.models import ModelChoiceIterator
from django.forms.widgets import Media
from django.db.models.fields import _FieldChoices
from django.forms.widgets import _OptAttrs


class FilteredSelectMultiple(forms.SelectMultiple):
    verbose_name: str = ...
    is_stacked: bool = ...
    def __init__(
        self,
        verbose_name: str,
        is_stacked: bool,
        attrs: Optional[_OptAttrs] = ...,
        choices: _FieldChoices = ...
    ) -> None: ...

class AdminDateWidget(forms.DateInput):
    def __init__(self, attrs: Optional[_OptAttrs] = ..., format: Optional[str] = ...) -> None: ...
class AdminTimeWidget(forms.TimeInput):
    def __init__(self, attrs: Optional[_OptAttrs] = ..., format: Optional[str] = ...) -> None: ...

class AdminSplitDateTime(forms.SplitDateTimeWidget):
    template_name: str
    def __init__(self, attrs: Optional[_OptAttrs] = ...) -> None: ...
    def get_context(self, name: str, value: Any, attrs: Optional[_OptAttrs]) -> Dict[str, Any]: ...

class AdminRadioSelect(forms.RadioSelect): ...
class AdminFileWidget(forms.ClearableFileInput): ...

def url_params_from_lookup_dict(lookups: Any) -> Dict[str, str]: ...

class ForeignKeyRawIdWidget(forms.TextInput):
    rel: ManyToOneRel = ...
    admin_site: AdminSite = ...
    db: Optional[str] = ...
    def __init__(self, rel: ManyToOneRel, admin_site: AdminSite, attrs: Optional[_OptAttrs] = ..., using: Optional[str] = ...) -> None: ...
    def base_url_parameters(self) -> Dict[str, str]: ...
    def get_context(self, name: str, value: Any, attrs: Optional[_OptAttrs]) -> Dict[str, Any]: ...
    def url_parameters(self) -> Dict[str, str]: ...
    def label_and_url_for_value(self, value: Any) -> Tuple[str, str]: ...

class ManyToManyRawIdWidget(ForeignKeyRawIdWidget):
    rel: ManyToManyRel = ...  # type: ignore
    def get_context(self, name: str, value: Any, attrs: Optional[_OptAttrs]) -> Dict[str, Any]: ...
    def url_parameters(self) -> Dict[str, str]: ...
    def label_and_url_for_value(self, value: Any) -> Tuple[str, str]: ...
    def format_value(self, value: Any) -> Optional[str]: ...
    def value_from_datadict(self, data: Mapping[str, Any], files: Mapping[str, Iterable[File]], name: str) -> Any: ...

class RelatedFieldWidgetWrapper(forms.Widget):
    template_name: str = ...
    choices: ModelChoiceIterator = ...
    widget: forms.ChoiceWidget = ...
    rel: ManyToOneRel = ...
    can_add_related: bool = ...
    can_change_related: bool = ...
    can_delete_related: bool = ...
    can_view_related: bool = ...
    admin_site: AdminSite = ...
    def __init__(
        self,
        widget: forms.ChoiceWidget,
        rel: ManyToOneRel,
        admin_site: AdminSite,
        can_add_related: Optional[bool] = ...,
        can_change_related: bool = ...,
        can_delete_related: bool = ...,
        can_view_related: bool = ...,
    ) -> None: ...
    @property
    def media(self) -> Media: ...  # type: ignore
    @property
    def is_hidden(self) -> bool: ...
    def get_related_url(self, info: Tuple[str, str], action: str, *args: Any) -> str: ...
    def get_context(self, name: str, value: Any, attrs: Optional[_OptAttrs]) -> Dict[str, Any]: ...
    def value_from_datadict(self, data: Mapping[str, Any], files: Mapping[str, Iterable[File]], name: str) -> Any: ...
    def value_omitted_from_data(self, data: Mapping[str, Any], files: Mapping[str, Iterable[File]], name: str) -> bool: ...
    def id_for_label(self, id_: str) -> str: ...

class AdminTextareaWidget(forms.Textarea):
    def __init__(self, attrs: Optional[_OptAttrs] = ...) -> None: ...

class AdminTextInputWidget(forms.TextInput):
    def __init__(self, attrs: Optional[_OptAttrs] = ...) -> None: ...

class AdminEmailInputWidget(forms.EmailInput):
    def __init__(self, attrs: Optional[_OptAttrs] = ...) -> None: ...

class AdminURLFieldWidget(forms.URLInput):
    template_name: str
    def __init__(self, attrs: Optional[_OptAttrs] = ..., validator_class: Any = ...) -> None: ...
    def get_context(self, name: str, value: Any, attrs: Optional[_OptAttrs]) -> Dict[str, Any]: ...

class AdminIntegerFieldWidget(forms.NumberInput):
    def __init__(self, attrs: Optional[_OptAttrs] = ...) -> None: ...
    class_name: str = ...

class AdminBigIntegerFieldWidget(AdminIntegerFieldWidget):
    class_name: str = ...

class AdminUUIDInputWidget(forms.TextInput):
    def __init__(self, attrs: Optional[_OptAttrs] = ...) -> None: ...

SELECT2_TRANSLATIONS: Dict[str, str] = ...

class AutocompleteMixin:
    url_name: str = ...
    field: Any = ...
    admin_site: AdminSite = ...
    db: Optional[str] = ...
    choices: Any = ...
    attrs: _OptAttrs = ...
    def __init__(
        self,
        field: Any,
        admin_site: AdminSite,
        attrs: Optional[_OptAttrs] = ...,
        choices: Any = ...,
        using: Optional[str] = ...,
    ) -> None: ...
    def get_url(self) -> str: ...
    @property
    def media(self) -> Media: ...
    def build_attrs(
        self, base_attrs: _OptAttrs, extra_attrs: Optional[_OptAttrs] = ...
    ) -> Dict[str, Any]: ...
    # typo in source: `attr` instead of `attrs`
    def optgroups(self, name: str, value: Sequence[str], attr: Optional[_OptAttrs] = ...) -> List[Tuple[Optional[str], List[Dict[str, Any]], Optional[int]]]: ...

class AutocompleteSelect(AutocompleteMixin, forms.Select): ...  # type: ignore
class AutocompleteSelectMultiple(AutocompleteMixin, forms.SelectMultiple): ...  # type: ignore
