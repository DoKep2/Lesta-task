from functools import wraps
from time import perf_counter


def average_benchmark_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        results = list()
        n_repeats = 3
        for i in range(n_repeats):
            time_start = perf_counter()
            result = func(*args, **kwargs)
            time_end = perf_counter()
            time_duration = time_end - time_start
            results.append(time_duration)
            print(f'>run {i + 1} took {time_duration:.3f} seconds')
        avg_duration = sum(results) / n_repeats
        print(f'Took {avg_duration:.3f} seconds on average')
        return result

    return wrapper
