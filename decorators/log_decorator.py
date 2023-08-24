def log_decorator(func):
    def wrap():
        print(f'Calling func {func}')
        func()
        print(f'Func {func} finished its work')
    return wrap

def hello():
    print("Hello, World")

#It's the same value

@log_decorator
def hello():
    print("Hello, World")