from example import add

def test_add():
	assert add(2, 3) == 5

def test_fail():
	assert subtract(5, 8) == 3
