from datetime import datetime


def logger(file_path):
    def decorator(func):
        def wrapper(*args, **kwargs):
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(file_path, 'a') as file:
                log_message = f"[{now}] Calling function {func.__name__} with args: {args}, kwargs: {kwargs}\n"
                file.write(log_message)
            return func(*args, **kwargs)
        return wrapper
    return decorator