# from django.test import TestCase
def worker(number, arg2):
    return number, arg2


res = [worker(f"abcd -> 10", [i for i in range(5)])]
print(res)