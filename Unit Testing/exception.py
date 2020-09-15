class NotIntegerError(Exception):  # a developer defined an exceptioin.
    pass


def test_divide():
    integers = [10, 20, 30]

    try:
        idx, num = input("type 2 numbers: ").split()
        if int != isinstance(idx, int):
            raise NotIntegerError("typed none integer for idx")

        if int != isinstance(num, int):
            raise NotIntegerError("typed none integer for num")

        result = integers[idx] / num
    except ZeroDivisionError as e:
        result = -1
        print(e)
    except IndexError as e:
        result = -1
        print(e)
    except Exception as e:
        raise RuntimeError("exception occurred in test_divide(): ", e)
    else:
        print("result = ", result)
    finally:
        return result


quotient = test_divide()
print(quotient)
