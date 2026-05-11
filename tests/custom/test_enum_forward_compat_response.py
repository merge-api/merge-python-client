import typing

import httpx

from merge import Merge
from merge.core.unchecked_base_model import UncheckedBaseModel, construct_type
from merge.resources.hris.types.employment import Employment
from merge.resources.hris.types.pay_period_enum import PayPeriodEnum


def test_construct_type_bare_enum_unknown_value_returns_raw_string():
    out = construct_type(object_="FUTURE_VALUE_NOT_IN_SDK", type_=PayPeriodEnum)
    assert out == "FUTURE_VALUE_NOT_IN_SDK"
    assert isinstance(out, str)
    assert not isinstance(out, PayPeriodEnum)


def test_construct_type_bare_enum_known_value_returns_raw_string():
    out = construct_type(object_="HOUR", type_=PayPeriodEnum)
    assert out == "HOUR"
    assert out == PayPeriodEnum.HOUR
    assert not isinstance(out, PayPeriodEnum)


def test_construct_type_bare_enum_none_value_short_circuits():
    assert construct_type(object_=None, type_=PayPeriodEnum) is None


def test_construct_type_union_enum_str_unknown_value_returns_raw_string():
    union_type = typing.Union[PayPeriodEnum, str]
    out = construct_type(object_="UNKNOWN_PERIOD_42", type_=union_type)
    assert out == "UNKNOWN_PERIOD_42"


def test_construct_type_union_enum_str_known_value_returns_raw_string():
    union_type = typing.Union[PayPeriodEnum, str]
    out = construct_type(object_="HOUR", type_=union_type)
    assert out == "HOUR"
    assert out == PayPeriodEnum.HOUR


def test_construct_type_optional_union_unknown_value():
    optional_union = typing.Optional[typing.Union[PayPeriodEnum, str]]
    assert construct_type(object_="UNKNOWN", type_=optional_union) == "UNKNOWN"


def test_construct_type_optional_union_none_value():
    optional_union = typing.Optional[typing.Union[PayPeriodEnum, str]]
    assert construct_type(object_=None, type_=optional_union) is None


def test_construct_type_list_of_enums_with_mixed_values():
    list_type = typing.List[PayPeriodEnum]
    out = construct_type(object_=["HOUR", "TOTALLY_NEW_VALUE", "DAY"], type_=list_type)
    assert out == ["HOUR", "TOTALLY_NEW_VALUE", "DAY"]


def test_construct_type_dict_with_enum_value_type():
    dict_type = typing.Dict[str, PayPeriodEnum]
    out = construct_type(object_={"a": "HOUR", "b": "UNRELEASED_VALUE"}, type_=dict_type)
    assert out == {"a": "HOUR", "b": "UNRELEASED_VALUE"}


def test_employment_construct_with_unknown_pay_period_does_not_raise():
    e = Employment.construct(id="emp-1", pay_period="FUTURE_VALUE_NOT_IN_SDK")
    assert e.pay_period == "FUTURE_VALUE_NOT_IN_SDK"


def test_employment_construct_with_known_pay_period_str_equality():
    e = Employment.construct(id="emp-1", pay_period="HOUR")
    assert e.pay_period == "HOUR"
    assert e.pay_period == PayPeriodEnum.HOUR


def test_employment_construct_with_none_pay_period():
    e = Employment.construct(id="emp-1")
    assert e.pay_period is None


def test_employment_extra_unknown_field_preserved():
    e = Employment.construct(id="emp-1", brand_new_server_field="present")
    assert getattr(e, "brand_new_server_field", None) == "present"


class _BareEnumModel(UncheckedBaseModel):
    period: typing.Optional[PayPeriodEnum] = None


def test_bare_enum_field_model_unknown_value():
    m = _BareEnumModel.construct(period="UNRELEASED")
    assert m.period == "UNRELEASED"


def test_bare_enum_field_model_known_value():
    m = _BareEnumModel.construct(period="HOUR")
    assert m.period == "HOUR"
    assert m.period == PayPeriodEnum.HOUR


def test_bare_enum_field_model_none():
    m = _BareEnumModel.construct(period=None)
    assert m.period is None


class _NestedModel(UncheckedBaseModel):
    inner: typing.Optional[_BareEnumModel] = None
    items: typing.Optional[typing.List[_BareEnumModel]] = None


def test_nested_model_with_unknown_enum_inside():
    parent = _NestedModel.construct(
        inner={"period": "BRAND_NEW"},
        items=[{"period": "HOUR"}, {"period": "STILL_NEW"}],
    )
    assert parent.inner.period == "BRAND_NEW"
    assert parent.items[0].period == "HOUR"
    assert parent.items[1].period == "STILL_NEW"


def _client_with_response(response: httpx.Response) -> Merge:
    def handler(request: httpx.Request) -> httpx.Response:
        return response

    return Merge(
        account_token="test-token",
        api_key="test-key",
        httpx_client=httpx.Client(transport=httpx.MockTransport(handler)),
    )


def _pay_period(item):
    return item["pay_period"] if isinstance(item, dict) else item.pay_period


def test_e2e_list_response_with_unknown_enum_does_not_raise():
    body = {
        "next": None,
        "previous": None,
        "results": [
            {"id": "1", "pay_period": "HOUR"},
            {"id": "2", "pay_period": "FUTURE_PAY_PERIOD"},
            {"id": "3", "pay_period": None},
        ],
    }
    client = _client_with_response(httpx.Response(200, json=body))
    response = client.hris.employments.list()
    assert len(response.results) == 3
    assert _pay_period(response.results[0]) == "HOUR"
    assert _pay_period(response.results[0]) == PayPeriodEnum.HOUR
    assert _pay_period(response.results[1]) == "FUTURE_PAY_PERIOD"
    assert _pay_period(response.results[2]) is None


def test_e2e_retrieve_response_with_unknown_enum_does_not_raise():
    body = {"id": "emp-1", "pay_period": "NEWLY_ADDED_PERIOD"}
    client = _client_with_response(httpx.Response(200, json=body))
    employment = client.hris.employments.retrieve("emp-1")
    assert employment.pay_period == "NEWLY_ADDED_PERIOD"


def test_e2e_response_with_extra_unknown_top_level_field():
    body = {
        "id": "emp-1",
        "pay_period": "HOUR",
        "newly_added_server_field": {"nested": "value"},
    }
    client = _client_with_response(httpx.Response(200, json=body))
    employment = client.hris.employments.retrieve("emp-1")
    assert employment.pay_period == "HOUR"
    assert getattr(employment, "newly_added_server_field", None) == {"nested": "value"}
