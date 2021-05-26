from graphql import (
    BooleanValueNode,
    FloatValueNode,
    IntValueNode,
    ListValueNode,
    NameNode,
    NullValueNode,
    ObjectFieldNode,
    ObjectValueNode,
    StringValueNode,
    VariableNode,
)

from graphql_scalars.scalars.json import GraphQLJSON
from graphql_scalars.settings import Settings
from tests.utils import do_test


def test_variable_input():
    do_test(
        GraphQLJSON.parse_value,
        [
            (2, 2),
            (False, False),
            (3.8, 3.8),
            ([6, 7, 8], [6, 7, 8]),
            ([4, '5', True], [4, '5', True]),
            ((7, '9'), (7, '9')),
            ({'Hello': 'World'}, {'Hello': 'World'}),
            (int, TypeError),
        ],
    )


def test_literal_value_input():
    do_test(
        GraphQLJSON.parse_literal,
        [
            (StringValueNode(value='hello'), 'hello'),
            (IntValueNode(value=1), 1),
            (FloatValueNode(value=2.0), 2.0),
            (BooleanValueNode(value=True), True),
            (
                ListValueNode(
                    values=[StringValueNode(value='hello'), StringValueNode(value='world')]
                ),
                ['hello', 'world'],
            ),
            (NullValueNode(), None),
        ],
    )


def test_literal_object_input():
    assert GraphQLJSON.parse_literal(
        ObjectValueNode(
            fields=[
                ObjectFieldNode(name=NameNode(value='true'), value=BooleanValueNode(value=False)),
                ObjectFieldNode(
                    name=NameNode(value='hello'), value=VariableNode(name=NameNode(value='world'))
                ),
                ObjectFieldNode(
                    name=NameNode(value='array'),
                    value=ListValueNode(
                        values=[
                            IntValueNode(value=1),
                            FloatValueNode(value=2.0),
                            StringValueNode(value='3'),
                        ]
                    ),
                ),
                ObjectFieldNode(name=NameNode(value='maybe_null'), value=NullValueNode()),
                ObjectFieldNode(
                    name=NameNode(value='obj'),
                    value=ObjectValueNode(
                        fields=[
                            ObjectFieldNode(
                                name=NameNode(value='test'),
                                value=VariableNode(name=NameNode(value='tenet')),
                            )
                        ]
                    ),
                ),
            ]
        ),
        {
            'world': 'world',
            'tenet': 'tenet',
        },
    ) == {
        'true': False,
        'hello': 'world',
        'array': [1, 2.0, '3'],
        'maybe_null': None,
        'obj': {'test': 'tenet'},
    }


def test_output():
    do_test(
        GraphQLJSON.serialize,
        [
            (1, 1),
            (True, True),
            (1.2, 1.2),
            ([1, 2, 3], [1, 2, 3]),
            ([4, '5', False], [4, '5', False]),
            ((1, 2), (1, 2)),
            ({}, {}),
            (type, TypeError),
        ],
    )


def test_json_serializer():
    Settings.json_serializers[int] = lambda v: v + 1
    Settings.json_serializers[dict] = lambda _: {}

    do_test(GraphQLJSON.serialize, [(1, 2), (2.0, 2.0), ({1: 1}, {})])

    Settings.json_serializers[int] = lambda _: type  # type: ignore[assignment, return-value]

    do_test(GraphQLJSON.serialize, [(1, TypeError)])
