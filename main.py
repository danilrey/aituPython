import threading
import time
from functools import wraps

def timeout(seconds: int):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = [None]

            def target():
                try:
                    result[0] = func(*args, **kwargs)
                except Exception as e:
                    result[0] = e

            thread = threading.Thread(target=target)
            thread.start()
            thread.join(seconds)
            if thread.is_alive():
                raise TimeoutError(f"Function '{func.__name__}' timed out after {seconds} seconds")
            if isinstance(result[0], Exception):
                raise result[0]
            return result[0]
        return wrapper
    return decorator

@timeout(3)
def slow_function():
    time.sleep(5)
    return "Finished"

try:
    print(slow_function())
except TimeoutError as e:
    print(e)