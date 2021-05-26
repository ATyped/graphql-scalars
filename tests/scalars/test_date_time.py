from datetime import date, datetime, timezone

from arrow import Arrow

from graphql_scalars.scalars.date_time import GraphQLDateTime
from tests.utils import do_test


def test_input():
    do_test(
        GraphQLDateTime.parse_value,
        [
            (
                '2077-07-07T07:07:07.123+07:07',
                datetime(2077, 7, 7, 0, 0, 7, 123 * 1000, timezone.utc),
            ),
            (
                '1999-09-09T09:09:09.456+09:09',
                datetime(1999, 9, 9, 0, 0, 9, 456 * 1000, timezone.utc),
            ),
            (
                '2020-02-20T20:20:20.789-02:20',
                datetime(2020, 2, 20, 22, 40, 20, 789 * 1000, timezone.utc),
            ),
            ('2020-02-02T20:20:20+00:00', datetime(2020, 2, 2, 20, 20, 20, tzinfo=timezone.utc)),
            ('2008-08-08T08:08:08Z', datetime(2008, 8, 8, 8, 8, 8, tzinfo=timezone.utc)),
            ('2020', datetime(2020, 1, 1, tzinfo=timezone.utc)),
            (123, TypeError),
            (True, TypeError),
            (False, TypeError),
            (123.321, TypeError),
            ('2020-02-02T20:20:20', ValueError),
        ],
    )


def test_output():
    do_test(
        GraphQLDateTime.serialize,
        [
            ('2077-07-07T07:07:07.123+07:07', '2077-07-07T00:00:07.123000+00:00'),
            ('2008-08-08T08:08:08Z', '2008-08-08T08:08:08+00:00'),
            ('2021', '2021-01-01T00:00:00+00:00'),
            ('2077-07-07', '2077-07-07T00:00:00+00:00'),
            ('1997-07', '1997-07-01T00:00:00+00:00'),
            (datetime(1945, 5, 4), '1945-05-04T00:00:00+00:00'),
            (date(2033, 6, 1), '2033-06-01T00:00:00+00:00'),
            (Arrow(1989, 12, 31, 12, 31, 24), '1989-12-31T12:31:24+00:00'),
            (123, TypeError),
            (True, TypeError),
            (123.456, TypeError),
        ],
    )
