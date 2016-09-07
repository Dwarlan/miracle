from datetime import datetime, timedelta

from miracle.models import (
    Session,
    URL,
    User,
)
from miracle.scripts import analysis

TEST_START = datetime.utcfromtimestamp(1469400000)


def test_weekly_recurrence(db):
    with db.session() as session:
        url1 = URL(**URL.from_url('http://localhost:80/path'))
        url2 = URL(**URL.from_url('https://localhost/'))
        url3 = URL(**URL.from_url('https://example.com/'))
        url4 = URL(**URL.from_url('https://example.com/other'))
        user1 = User(token='user1')
        user2 = User(token='user2')
        session.add_all([
            # URL visited three times in a week
            Session(user=user1, url=url1, start_time=TEST_START),
            Session(user=user1, url=url1,
                    start_time=TEST_START + timedelta(days=1)),
            Session(user=user1, url=url1,
                    start_time=TEST_START + timedelta(days=2)),
            # URL visited three times, but not in a week
            Session(user=user1, url=url2, start_time=TEST_START),
            Session(user=user1, url=url2,
                    start_time=TEST_START + timedelta(days=1)),
            Session(user=user1, url=url2,
                    start_time=TEST_START + timedelta(days=8)),
            # URL visited less than three times
            Session(user=user1, url=url3, start_time=TEST_START),
            Session(user=user1, url=url3,
                    start_time=TEST_START + timedelta(days=1)),
            # URL visited three times, in two distinct weeks
            Session(user=user1, url=url4, start_time=TEST_START),
            Session(user=user1, url=url4,
                    start_time=TEST_START + timedelta(days=1)),
            Session(user=user1, url=url4,
                    start_time=TEST_START + timedelta(days=2)),
            Session(user=user1, url=url4,
                    start_time=TEST_START + timedelta(days=10)),
            Session(user=user1, url=url4,
                    start_time=TEST_START + timedelta(days=11)),
            Session(user=user1, url=url4,
                    start_time=TEST_START + timedelta(days=12)),
            # Second user with too few sessions
            Session(user=user2, url=url3,
                    start_time=TEST_START + timedelta(days=2)),
        ])
        session.flush()
        assert analysis.weekly_recurrence(db) == [(0, 1), (2, 1)]


def test_main(db, tmp_path):
    assert analysis.main(db, 'weekly_recurrence')
