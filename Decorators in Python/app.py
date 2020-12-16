import functools

user = {
    'access_level': 'admin'
}

def user_has_permission(access_level):
    def my_decorator(func):
        @functools.wraps(func)
        def secure_func(*args , **kwargs):
            """
            Hey
            """
            if user.get('access_level') == access_level:
                return func(*args , **kwargs)
        return secure_func
    return my_decorator


@user_has_permission('admin')
def my_function(panel):
    """
    My Function
    """
    return f'Password for {panel} panel id 1234'

@user_has_permission('admin')
def another_function():
    """
    another Function
    """
    print('Hello')

# my_secure_function = user_has_permission(my_function)

print(my_function('admin'))

print(another_function())

# print(my_function.__name__)
# print(another_function.__name__)

def add_all(*args):
    print(args)


def print_prety(**kwargs):
    for k ,v in kwargs.items():
        print(f'For {k} we have {v}')
    

add_all(1,2,5,3,6)

print_prety( username = "ganesh", access_level = "admin")

print_prety(**{'username': 'ganesh', 'access_level': 'admin'})