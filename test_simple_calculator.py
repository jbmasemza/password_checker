from addtion import add
from addtion import multiply


def test_add():
 assert add(0,0) == 0
 assert add(-1,-1) == -2
 assert add(4,5) == 9
 assert add(1,2,3,4) == 10

def test_multiply():
 assert multiply(1,2) == 2
 assert multiply(1,2,3,4) == 24
