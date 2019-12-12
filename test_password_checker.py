from password_checker import password_is_valid
from password_checker import password_is_ok
import pytest

def test_password_exists():
	with pytest.raises(Exception, match = "password should exist"):
		password_is_valid("")

def test_password_length():
	with pytest.raises(Exception, match = "password should be longer than 8 characters"):
		password_is_valid("Jo13")

def test_password_has_lower():
	with pytest.raises(Exception, match = "password should contain a lowercase character"):
		password_is_valid("JOY12345678")

def test_password_has_upper():
	with pytest.raises(Exception, match = "password should contain an uppercase character"):
		password_is_valid("joy12345678")

def test_password_has_digit():
	with pytest.raises(Exception, match = "password should contain a digit"):
		password_is_valid("Joymasemola")

def test_password_is_ok():
	assert password_is_ok("Jo13") == False
	assert password_is_ok("J") == False
	assert password_is_ok("") == False
	assert password_is_ok("Joyous@123") == True