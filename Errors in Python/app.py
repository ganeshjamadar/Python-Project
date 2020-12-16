##################################################################
# Errors in Python
##################################################################

print(f'\n\nErrors in Python')

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f'<Car {self.make}{self.model}>'

class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)
    
    def add_car(self, car):
        if not isinstance(car, Car):
            raise ValueError(f'Tried to add a {car.__class__.__name__} to the garage.')
        self.cars.append(car)
        print(f'\nCar Added Successfully')

hundia = Garage()
creata = Car('Hundia', 'Creata')
hundia.add_car(creata)

# hundia.add_car('Test')  #raise TypeError(f'Tried to add a {car.__class__.__name__} to the garage.')

print(len(hundia))

##################################################################
# Custom Errors in Python
##################################################################

print(f'\n\nCustom Errors in Python')

class MyCustomError(TypeError):
    """
My Custom Error Class
    """
    def __init__(self, message, code):
        super().__init__(f'Error Code: {code} {message}')
        self.code = code


class Cars:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f'<Car {self.make}{self.model}>'

class Garages:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)
    
    def add_car(self, car):
        if not isinstance(car, Cars):
            raise MyCustomError(f'Tried to add a {car.__class__.__name__} to the garage.', 555)
        self.cars.append(car)
        print(f'\nCar Added Successfully')

hundia = Garages()
creata = Cars('Hundia', 'Creata')
hundia.add_car(creata)

#hundia.add_car('Test')  #raise TypeError(f'Tried to add a {car.__class__.__name__} to the garage.')

print(len(hundia))

err = MyCustomError('Ohh!! An error happenrd', 500)

print(err.__doc__)

try:
    hundia1 = Garage()
    creata1 = Car('Hundia', 'Creata')
    hundia1.add_car(creata1)
    hundia.add_car('Tata')
except TypeError:
    print('Your car was not a Car!')
except ValueError:
    print(f'Something Wierd happened')
except Exception:
    print(f'This base Exception')
finally:
    print(f'Finally Garage')

# raise MyCustomError('Ohh!! An error happenrd', 500)

class User:
    def __init__(self, name, engagement):
        self.name = name
        self.engagement = engagement
        self.score = 0
    
    def __repr__(self):
        return f'<User {self.name}>'
    
def get_user_score(user):
    try:
        user.score = perform_calculation(user.engagement)
        print(f'User Score: {my_user.score}')
    except KeyError:
        print('Incorrect value provided to our calculation function.')
        raise
    else:
        send_notification(user)
    finally:
        print(f'Finally get_user_score')

def perform_calculation(metrixes):
    return metrixes['click'] * 5 + metrixes['hits'] * 2

def send_notification(user):
    print(f'Notification sent to {user}')

my_user = User('Ganesh', {'click': 64, 'hits': 411})

get_user_score(my_user)
