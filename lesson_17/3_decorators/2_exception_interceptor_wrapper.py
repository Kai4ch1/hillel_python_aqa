def error_handler_n_tries(n : int, error_type = Exception):
    def decorator(func):
        def wrapper(*args, **kwargs):
            repeater = 0
            if n > 0:
                while repeater < n:
                    try:
                        return func(*args, **kwargs)
                    except error_type:
                        repeater += 1
            else:
                raise ValueError(f"The 'n' should be > 0, but got {n}")
            return f"Tried {repeater} times, but every time received and error= {error_type.__name__}"
        return wrapper
    return decorator

@error_handler_n_tries(n=15, error_type=ZeroDivisionError)
def error_handler_call(value):
    return value / 0

result = error_handler_call(7)
print(result)