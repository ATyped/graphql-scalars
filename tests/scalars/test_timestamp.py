from datetime import date, datetime, timedelta, timezone

from graphql_scalars.scalars.timestamp import GraphQLTimestamp
from tests.utils import do_test


def test_input():
    do_test(
        GraphQLTimestamp.parse_value,
        [
            (3392841607123, datetime(2077, 7, 7, 0, 0, 7, 123 * 1000, timezone.utc)),
            (936835209456, datetime(1999, 9, 9, 0, 0, 9, 456 * 1000, timezone.utc)),
            ('2020-02-20T20:20:20.789-02:20', TypeError),
            ('2020-02-02T20:20:20+00:00', TypeError),
            ('2008-08-08T08:08:08Z', TypeError),
            (True, TypeError),
            (False, TypeError),
        ],
    )


def test_output():
    do_test(
        GraphQLTimestamp.serialize,
        [
            (datetime(2077, 7, 7, 0, 0, 7, 123 * 1000, timezone.utc), 3392841607123),
            (datetime(1999, 9, 9, 8, 0, 9, 456 * 1000, timezone(timedelta(hours=8))), 936835209456),
            ('2008-08-08T08:08:08Z', 1218182888000),
            (date(2020, 1, 1), 1577836800000),
            (123, TypeError),
            (True, TypeError),
            (123.456, TypeError),
        ],
    )
