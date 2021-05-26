from graphql import StringValueNode

from graphql_scalars.scalars.void import GraphQLVoid
from tests.utils import do_test


def test_output():
    do_test(
        GraphQLVoid.serialize,
        [
            (1, None),
            (2.0, None),
            ('3', None),
            (True, None),
            ({}, None),
        ],
    )


def test_variable_input():
    do_test(
        GraphQLVoid.parse_value,
        [
            (4, None),
            (5.0, None),
            ('6', None),
            (False, None),
            ({}, None),
        ],
    )


def test_literal_input():
    do_test(
        GraphQLVoid.parse_literal,
        [
            (StringValueNode(value='hello'), None),
        ],
    )
