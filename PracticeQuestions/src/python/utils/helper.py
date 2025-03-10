import time


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)  # Call the original function with its arguments
        print(f"Time Taken by '{func.__name__}': {time.time() - start:.12f} seconds")
        return result

    return wrapper


__all__ = ["timeit"]
