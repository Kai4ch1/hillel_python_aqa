import logging
import definitions

logging.basicConfig(
    filename='log_wrapper_args_kwargs.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("LOG EVENT")
log_file_storage = definitions.SAVE_DECORATOR_LOG


def log_arguments(func):
    def wrapper(*args, **kwargs):
        try:
            logger.info(f"LOGGING ARGS={args}, KWARGS={kwargs}")

            result = func(*args, **kwargs)

            logger.info(f"Logged result={result}")
            return result
        except TypeError as e:
            print(f"Caught an error{e}")
    return wrapper

@log_arguments
def divide(a, b):
    return a / b

if __name__ == "__main__":
    final = divide(7, 2)
    print(final)
