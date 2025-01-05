import pytest
import pytz  # python IANA timezone implementation
from pytz import timezone
from tzlocal import get_localzone
from datetime import datetime

import time
from datetime import datetime, timezone
from unix_epoch import get_epoch, get_datetime


@pytest.fixture
def now_epoch() -> int:
    return int(time.mktime(datetime.now(timezone.utc).timetuple()))


def test_unix_epoch(now_epoch) -> None:
    assert get_epoch(local_time=False) >= now_epoch


@pytest.fixture
def epoch() -> int:
    return int(1734877954)


@pytest.fixture
def iso8601_format() -> str:
    return "%Y-%m-%dT%H:%M:%S%z"


@pytest.fixture
def date_format() -> str:
    return "%Y-%m-%d %H:%M:%S %Z%z"


def test_utc_iso8601_date_from_epoch(epoch, iso8601_format) -> None:
    assert get_datetime(epoch=epoch, date_format=iso8601_format) == '2024-12-22T15:32:34+0000'


def test_utc_date_from_epoch(epoch) -> None:
    assert get_datetime(epoch=epoch) == '2024-12-22 15:32:34 UTC+0000'


def test_local_iso8601_date_from_epoch(epoch, iso8601_format) -> None:
    _dt = datetime.fromtimestamp(epoch).replace(tzinfo=pytz.UTC)
    _tz = str(get_localzone())
    _answer = str(_dt.astimezone(pytz.timezone(_tz)).strftime(iso8601_format))
    assert get_datetime(epoch=epoch, local_time=True, date_format=iso8601_format) == _answer


def test_local_date_from_epoch(epoch, date_format) -> None:
    _dt = datetime.fromtimestamp(epoch).replace(tzinfo=pytz.UTC)
    _tz = str(get_localzone())
    _answer = str(_dt.astimezone(pytz.timezone(_tz)).strftime(date_format))
    assert get_datetime(epoch=epoch, local_time=True) == _answer

# import pytz
# from pytz import timezone
# from datetime import datetime
# _dt = datetime.fromtimestamp(_epoch).replace(tzinfo=pytz.UTC)
# dt_format = "%Y-%m-%d %H:%M:%S %Z%z"
# iso_format="%Y-%m-%dT%H:%M:%S%z"
# print(_dt.strftime(iso_format))                                          # 2024-12-22T15:32:34+0000
# print(_dt.strftime(dt_format))                                           # 2024-12-22 15:32:34 UTC+0000
# tz = str(get_localzone())
# print(_dt.astimezone(pytz.timezone(tz)).strftime(iso_format))    # 2024-12-22T16:32:34+0100
# print(_dt.astimezone(pytz.timezone(tz)).strftime(dt_format))     # 2024-12-22 16:32:34 CET+0100
#
# print(_dt.astimezone(timezone('Europe/Zurich')).strftime(iso_format))    # 2024-12-22T16:32:34+0100
# print(_dt.astimezone(timezone('Europe/Zurich')).strftime(dt_format))     # 2024-12-22 16:32:34 CET+0100
# print(_dt.astimezone(timezone('America/New_York')).strftime(iso_format)) # 2024-12-22T10:32:34-0500
# print(_dt.astimezone(timezone('America/New_York')).strftime(dt_format))  # 2024-12-22 10:32:34 EST-0500
