from typing import Dict
from functools import lru_cache
from typing import Generator


memo: Dict[int, int] = {0:0, 1:1}

def fib1(n:int) -> int:
    return fib1(n - 1) + fib1(n - 2)

def fib2(n:int) -> int:
    if n<2:
        return n
    return fib2(n-2) + fib2(n-1)

def fib3(n:int) -> int:
    if n not in memo:
        memo[n] = fib3(n-1) + fib3(n-2)
    return memo[n]

@lru_cache(maxsize=None)
def fib4(n:int) -> int:
    if n<2:
        return n
    return fib4(n-2) + fib4(n-1)

def fib5(n:int) -> int:
    if n == 0: return n
    last: int = 0
    next_num: int = 1

    for _ in range(1, n):
        last, next_num = next_num, last + next_num
    return next_num

def fib6(n:int) -> Generator[int, None, None]:
    yield 0

    if n > 0: yield 1

    last: int = 0
    next_num: int = 1

    for _ in range(1, n):
        last, next_num = next_num, last+next_num
        yield next_num
    

if __name__ == "__main__":
    # prints results
    try:
        print(fib1(5))
    except RecursionError as e:
        print(f"Erro: {e.args}")

    print(fib2(10))
    print(fib3(50))
    print(fib4(50))
    print(fib5(50))
    print([i for i in fib6(10)])
