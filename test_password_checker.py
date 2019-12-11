#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 11:06:34 2019

@author: joyous
"""

import password_checker
import pytest

#password_is_valid tests
def test_password_exists():
	with pytest.raises(Exception, match = "password should exist"):
		password_checker.password_is_valid("")

def test_password_length():
	with pytest.raises(Exception, match = "password should be longer than 8 characters"):
		password_checker.password_is_valid("Jo13")

def test_password_has_lower():
	with pytest.raises(Exception, match = "password should contain a lowercase character"):
		password_checker.password_is_valid("J12345678")

def test_password_has_upper():
	with pytest.raises(Exception, match = 'password should contain an uppercase character'):
		password_checker.password_is_valid('j12345678')

def test_password_has_digit():
	with pytest.raises(Exception, match = 'password should contain a digit'):
		password_checker.password_is_valid('Joymasemola')

#password_is_ok tests
def test_password_is_ok():
	assert password_checker.password_is_ok('Jo13') == False
	assert password_checker.password_is_ok('J') == False
	assert password_checker.password_is_ok('') == False
	assert password_checker.password_is_ok('Joyous@123') == True