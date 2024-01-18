import time


def timer(func):
    def calculate(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        runtime = end_time - start_time
        print(f"--> Finished {func.__name__!r} in {runtime:.8f} secs")
        return value
    return calculate
