import pydantic

from merge.core.query_encoder import encode_query, single_query_encoder
from merge.resources.ticketing.resources.tickets.types.tickets_list_request_expand_item import (
    TicketsListRequestExpandItem,
)


def test_boolean_true_passes_through():
    assert single_query_encoder("include_remote_data", True) == [
        ("include_remote_data", True)
    ]


def test_boolean_false_passes_through():
    assert single_query_encoder("include_remote_data", False) == [
        ("include_remote_data", False)
    ]


def test_none_passes_through():
    assert single_query_encoder("expand", None) == [("expand", None)]


def test_pydantic_model_flattens_with_bracket_keys():
    class Filter(pydantic.BaseModel):
        foo: str = "bar"

    result = single_query_encoder("filter", Filter())
    assert result == [("filter[foo]", "bar")]


def test_pydantic_model_with_multiple_fields_flattens():
    class Filter(pydantic.BaseModel):
        foo: str = "bar"
        baz: int = 42

    result = single_query_encoder("filter", Filter())
    assert sorted(result) == sorted([("filter[foo]", "bar"), ("filter[baz]", 42)])


def test_dict_flattens_with_bracket_keys():
    assert single_query_encoder("filter", {"foo": "bar"}) == [("filter[foo]", "bar")]


def test_nested_dict_flattens_to_double_bracket_keys():
    assert single_query_encoder("filter", {"foo": {"baz": "qux"}}) == [
        ("filter[foo][baz]", "qux")
    ]


def test_encode_query_returns_none_for_none_input():
    assert encode_query(None) is None


def test_expand_list_of_enum_items_joins_as_csv():
    assert single_query_encoder(
        "expand",
        [TicketsListRequestExpandItem.ACCOUNT, TicketsListRequestExpandItem.ASSIGNEES],
    ) == [("expand", "account,assignees")]


def test_expand_list_of_plain_strings_joins_as_csv():
    assert single_query_encoder("expand", ["account", "assignees"]) == [
        ("expand", "account,assignees")
    ]


def test_expand_single_item_list_emits_single_value():
    assert single_query_encoder("expand", [TicketsListRequestExpandItem.ACCOUNT]) == [
        ("expand", "account")
    ]


def test_expand_empty_list_emits_nothing():
    assert single_query_encoder("expand", []) == []


def test_expand_tuple_of_items_joins_as_csv():
    assert single_query_encoder(
        "expand",
        (TicketsListRequestExpandItem.ACCOUNT, TicketsListRequestExpandItem.ASSIGNEES),
    ) == [("expand", "account,assignees")]


def test_non_expand_list_keeps_repeated_tuples():
    assert single_query_encoder("order_by", ["alpha", "beta"]) == [
        ("order_by", "alpha"),
        ("order_by", "beta"),
    ]
