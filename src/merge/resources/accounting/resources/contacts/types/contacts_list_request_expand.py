# This file was auto-generated by Fern from our API Definition.

import typing

ContactsListRequestExpand = typing.Union[
    typing.Literal[
        "addresses",
        "addresses,company",
        "addresses,phone_numbers",
        "addresses,phone_numbers,company",
        "company",
        "phone_numbers",
        "phone_numbers,company",
    ],
    typing.Any,
]
