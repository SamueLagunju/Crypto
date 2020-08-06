import crypto

from crypto.helpers import arg_parser


import pytest

# @pytest.fixture(params=[["--encrypt", "file.txt"], ["--encrypt", "test.txt"]])
def test_parse():
    parser = arg_parser
    result = parser(["--encrypt", "file.txt"])

    assert result.encrypt_file ==  ["file.txt"]