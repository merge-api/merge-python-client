import warnings

import pydantic
import pytest

from merge.core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from merge.core.unchecked_base_model import UncheckedBaseModel
from merge.resources.accounting.types.account import Account
from merge.resources.accounting.types.field_mapping_api_instance_response import (
    FieldMappingApiInstanceResponse,
)

pytestmark = pytest.mark.skipif(not IS_PYDANTIC_V2, reason="config deprecation only applies on pydantic v2")

_DEPRECATION_MARKERS = (
    "class-based `config`",
    "allow_population_by_field_name",
    "smart_union",
    "Valid config keys have changed",
)


def _pydantic_config_warnings(records):
    hits = []
    for r in records:
        if not issubclass(r.category, (DeprecationWarning, UserWarning, PendingDeprecationWarning)):
            continue
        text = str(r.message)
        if any(marker in text for marker in _DEPRECATION_MARKERS):
            hits.append(text)
    return hits


def test_defining_a_subclass_emits_no_config_deprecation_warnings():
    with warnings.catch_warnings(record=True) as records:
        warnings.simplefilter("always")

        class _Probe(UncheckedBaseModel):
            name: str = pydantic.Field(default="", alias="Name")

        _Probe(Name="probe")

    hits = _pydantic_config_warnings(records)
    assert hits == [], f"deprecated pydantic config resurfaced (issue #117): {hits}"


def test_instantiating_real_models_emits_no_config_deprecation_warnings():
    with warnings.catch_warnings(record=True) as records:
        warnings.simplefilter("always")
        Account(name="Cash", id="123")
        FieldMappingApiInstanceResponse(account=[])

    hits = _pydantic_config_warnings(records)
    assert hits == [], f"deprecated pydantic config resurfaced (issue #117): {hits}"


def test_base_model_config_has_no_deprecated_v1_keys():
    config = UniversalBaseModel.model_config
    assert "smart_union" not in config
    assert "allow_population_by_field_name" not in config
