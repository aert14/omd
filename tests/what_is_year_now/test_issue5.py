import json
from unittest.mock import patch

import pytest

from what_is_year_now import what_is_year_now


def test_ymd_format():
    """Test the YEAR.MONTH.DAY format."""
    with patch("urllib.request.urlopen") as mocked_get:
        mocked_get.return_value.__enter__.return_value.read.return_value =\
              json.dumps({"currentDateTime": "2023-01-01"})
        assert what_is_year_now() == 2023
        mocked_get.assert_called_once()

def test_dmy_format():
    """Test the DAY.MONTH.YEAR format."""
    with patch("urllib.request.urlopen") as mocked_get:
        mocked_get.return_value.__enter__.return_value.read.return_value =\
              json.dumps({"currentDateTime": "01.01.2023"}).encode("utf-8")
        assert what_is_year_now() == 2023
        mocked_get.assert_called_once()

def test_invalid_format():
    """Test the invalid format."""
    with patch("urllib.request.urlopen") as mocked_get:
        mocked_get.return_value.__enter__.return_value.read.return_value =\
              json.dumps({"currentDateTime": "01-01-2023"}).encode("utf-8")
        with pytest.raises(ValueError):
            what_is_year_now()
        mocked_get.assert_called_once()

if __name__ == "__main__":
    pass
