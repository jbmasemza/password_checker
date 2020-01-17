def test_password_is_ok():
	assert password_is_ok("Jo13") == False
	assert password_is_ok("J") == False
	assert password_is_ok("") == False
	assert password_is_ok("Joyous@123") == True
