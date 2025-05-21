from .Operations import suma, product, subs

def test_sum():
    assert suma(1, 2) == 3, "Should be 3"

def test_prod():
    assert product(1, 2) == 2, "Should be 2"

def test_sub():
    assert subs(1, 2) == 0, "Should be 0"
    assert subs(2, 1) == 1, "Should be 1"

if __name__ == "__main__":
    test_sum()
    test_prod()
    test_sub()
    print("Everything passed")