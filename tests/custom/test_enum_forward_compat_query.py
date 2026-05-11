import typing

import httpx

from merge import Merge
from merge.core.query_encoder import (
    encode_query,
    single_query_encoder,
    traverse_query_dict,
)
from merge.resources.hris.resources.employments.types.employments_list_request_order_by import (
    EmploymentsListRequestOrderBy,
)


def test_single_query_encoder_with_known_enum_string():
    assert single_query_encoder("order_by", "effective_date") == [
        ("order_by", "effective_date")
    ]


def test_single_query_encoder_with_unknown_string_does_not_raise():
    assert single_query_encoder("order_by", "future_field_value") == [
        ("order_by", "future_field_value")
    ]


def test_single_query_encoder_with_descending_unknown_string():
    assert single_query_encoder("order_by", "-future_field_value") == [
        ("order_by", "-future_field_value")
    ]


def test_single_query_encoder_with_empty_string():
    assert single_query_encoder("order_by", "") == [("order_by", "")]


def test_single_query_encoder_with_enum_instance_str_equality():
    member = EmploymentsListRequestOrderBy.EFFECTIVE_DATE_ASCENDING
    result = single_query_encoder("order_by", member)
    assert result == [("order_by", member)]
    assert result[0][1] == "effective_date"


def test_single_query_encoder_with_descending_enum_instance():
    member = EmploymentsListRequestOrderBy.EFFECTIVE_DATE_DESCENDING
    result = single_query_encoder("order_by", member)
    assert result[0][1] == "-effective_date"


def test_single_query_encoder_with_list_of_unknown_strings():
    assert single_query_encoder("order_by", ["alpha", "beta_gamma"]) == [
        ("order_by", "alpha"),
        ("order_by", "beta_gamma"),
    ]


def test_single_query_encoder_with_mixed_known_and_unknown_strings():
    assert single_query_encoder("order_by", ["effective_date", "made_up_value"]) == [
        ("order_by", "effective_date"),
        ("order_by", "made_up_value"),
    ]


def test_single_query_encoder_with_list_of_enum_instances():
    members = [
        EmploymentsListRequestOrderBy.EFFECTIVE_DATE_ASCENDING,
        EmploymentsListRequestOrderBy.EFFECTIVE_DATE_DESCENDING,
    ]
    assert single_query_encoder("order_by", members) == [
        ("order_by", members[0]),
        ("order_by", members[1]),
    ]


def test_encode_query_with_unknown_enum_value():
    assert encode_query({"order_by": "totally_made_up"}) == [
        ("order_by", "totally_made_up")
    ]


def test_encode_query_returns_none_for_none():
    assert encode_query(None) is None


def test_encode_query_mixed_params_with_enum_instance():
    result = encode_query(
        {
            "order_by": EmploymentsListRequestOrderBy.EFFECTIVE_DATE_ASCENDING,
            "page_size": 50,
            "remote_id": "abc-123",
        }
    )
    assert (
        "order_by",
        EmploymentsListRequestOrderBy.EFFECTIVE_DATE_ASCENDING,
    ) in result
    assert ("page_size", 50) in result
    assert ("remote_id", "abc-123") in result


def test_encode_query_with_unknown_enum_alongside_known_filters():
    result = encode_query({"order_by": "novel_field", "page_size": 10})
    assert ("order_by", "novel_field") in result
    assert ("page_size", 10) in result


def test_traverse_query_dict_with_enum_string_in_nested_filter():
    assert traverse_query_dict({"order_by": "future_value"}, "filter") == [
        ("filter[order_by]", "future_value")
    ]


def _capture_client() -> typing.Tuple[Merge, typing.List[httpx.Request]]:
    captured: typing.List[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        captured.append(request)
        return httpx.Response(
            200,
            json={"next": None, "previous": None, "results": []},
        )

    client = Merge(
        account_token="test-token",
        api_key="test-key",
        httpx_client=httpx.Client(transport=httpx.MockTransport(handler)),
    )
    return client, captured


def test_e2e_unknown_order_by_string_is_sent_through():
    client, captured = _capture_client()
    client.hris.employments.list(order_by="completely_made_up_field")  # type: ignore[arg-type]
    assert len(captured) == 1
    assert "order_by=completely_made_up_field" in str(captured[0].url)


def test_e2e_unknown_descending_order_by_string_is_sent_through():
    client, captured = _capture_client()
    client.hris.employments.list(order_by="-novel_field")  # type: ignore[arg-type]
    assert len(captured) == 1
    assert "order_by=-novel_field" in str(captured[0].url)


def test_e2e_enum_instance_ascending_serializes_to_value():
    client, captured = _capture_client()
    client.hris.employments.list(
        order_by=EmploymentsListRequestOrderBy.EFFECTIVE_DATE_ASCENDING,
    )
    assert len(captured) == 1
    assert "order_by=effective_date" in str(captured[0].url)


def test_e2e_enum_instance_descending_serializes_to_value():
    client, captured = _capture_client()
    client.hris.employments.list(
        order_by=EmploymentsListRequestOrderBy.EFFECTIVE_DATE_DESCENDING,
    )
    assert len(captured) == 1
    assert "order_by=-effective_date" in str(captured[0].url)
