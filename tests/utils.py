from typing import Any, Callable, Type, Union

import pytest
from graphql import GraphQLScalarType, GraphQLSchema


def register_scalar(schema: GraphQLSchema, scalar: GraphQLScalarType):
    schema.type_map[scalar.name] = scalar


def do_test(testee: Callable[[Any], Any], data: list[tuple[Any, Union[Any, Type[Exception]]]]):
    for input_value, expect_value in data:
        if isinstance(expect_value, type) and issubclass(expect_value, Exception):
            with pytest.raises(expect_value):
                actual_value = testee(input_value)
                assert (input_value, actual_value) is None
        else:
            actual_value = testee(input_value)
            assert actual_value == expect_value
