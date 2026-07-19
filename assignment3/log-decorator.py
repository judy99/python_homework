import logging

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))

def logger_decorator(func):
    def wrapper_logger_decorator(*args, **kwargs):
        logger.log(logging.INFO, f"function: {func.__name__}") 
        if not args:
            logger.log(logging.INFO, f"positional parameters: None")
        else:
            logger.log(logging.INFO, f"positional parameters: {args}")
        if not kwargs:
            logger.log(logging.INFO, f"keyword parameters: None")
        else:
            logger.log(logging.INFO, f"keyword parameters: {kwargs}")
        logger.log(logging.INFO, f"return: {func(*args, **kwargs)}")
        logger.log(logging.INFO, f"********************************")
    return wrapper_logger_decorator

# tests
# no params, return nothing
@logger_decorator
def greet1():
    print("Hello world!")

# numbers of positional arguments, returns True
@logger_decorator
def greet2(*args):
    return True

# no positional arguments, numbers of keyword arguments
# returns logger_decorator
@logger_decorator
def greet3(**kwargs):
    return logger_decorator

greet1()
greet2("Anna", 30, "CEO")
greet2("Anna", 30, 15, "12345", (1,2,3,4,5))
greet3(name="Anna", age=30, points=(1,2,3,4,5))
greet3(age=30, points=(1,2,3,4,5))
