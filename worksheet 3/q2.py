def test_range(n):
    if (100<=n<1000) or n == 2000:
        return True
    else:
        return False

print(test_range(500))