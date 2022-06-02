import time


def timer_execution(func):
    def wrapper(*args, **kwargs):
        start_time = time.monotonic()
        result_func = func(*args, **kwargs)
        end_time = time.monotonic()
        print(f"Результат {func.__name__}: {end_time - start_time:.5f}")
        return result_func
    return wrapper