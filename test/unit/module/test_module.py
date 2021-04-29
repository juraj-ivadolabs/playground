from module.module import add_one

def test_wrong_answer():
    assert add_one(3) == 5

def test_correct_answer():
    assert add_one(1) == 2
