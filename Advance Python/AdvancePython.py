friends_last_seen = {
    "Rolf": 31,
    "Jen": 1,
    "Anne" : 7
}

#print(id(friends_last_seen))

friends_last_seen = {
    "Rolf": 31,
    "Jen": 1,
    "Anne" : 7
}

#print(id(friends_last_seen))

friends_last_seen["Rolf"] = 0

#print(id(friends_last_seen))

my_int = 5

#print(id(my_int))

my_int = my_int + 1

#print(id(my_int))

friends = ["Ganesh", "Harshada"]

#print(id(friends))

friends.append("Pillu")

#print(id(friends))

def see_friends(friends, name):
    #print(id(friends))
    friends[name] = 0

#print(id(friends_last_seen))
#print(id(friends_last_seen["Rolf"]))

see_friends(friends_last_seen, "Rolf")

#print(id(friends_last_seen))
#print(id(friends_last_seen["Rolf"]))


age = 20

def increaseAge(current_age):
    current_age = current_age + 1
    #print(id(current_age))

#print(id(age))
increaseAge(age)
#print(id(age))

##########################################################################################################
# Mutable default argument
##########################################################################################################

def CreateAccount(name: str, holder: str, account_holders: list = None):

    if not account_holders:
        account_holders = []

    account_holders.append(holder)

    return {
        'name': name,
        'main_account_holder': holder,
        'account_holders': account_holders
    }


a1 = CreateAccount('Checking','Rolf')
a2 = CreateAccount('Savings', 'Jen')

print(a2)


###############################################################################################################
# Argument Unpacking
###############################################################################################################

class User: 
    def __init__(self, username, password):
        self.username = username
        self.password = password

users = [
    {'username': 'rolf', 'password': '123'},
    {'username': 'jen', 'password': 'test'}
]

user_objects = [User(username = data['username'], password= data['password']) for data in users]

# for data in user_objects:
#     print(data.username)
#     print(data.password)

user_objects = [User(**data) for data in users]

# for data in user_objects:
#     print(data.username)
#     print(data.password)

users = [
    ('rolf', '123'),
    ('jen', 'test')
]

user_objects = [User(*data) for data in users]

# for data in user_objects:
#     print(data.username)
#     print(data.password)


#########################################################################################################
# Some interesting collection in python
# counter
# defaultdict
# ordereddict
# namedtuple
# deque
#########################################################################################################

from collections import Counter

device_temp = [13.5, 12.3, 12.5, 10, 10.25, 11.45, 10.25, 9.52, 12.3]

temp_counter = Counter(device_temp)

print(temp_counter[12.3])


from collections import defaultdict

my_company = 'Aptify'

coworkers = ['ganesh', 'rolf', 'charlie', 'reena']
other_workers = [('harshu', 'sagitec'), ('ankita', 'firserv')]

coworkers_company = defaultdict(lambda : my_company)

for person, company in other_workers:
    coworkers_company[person] = company

print(coworkers_company[coworkers[0]])
print(coworkers_company['harshu'])

from collections import OrderedDict

ordered = OrderedDict()

ordered['rolf'] = 6
ordered['jen'] = 12
ordered['jose'] = 3

print(ordered)

ordered.move_to_end('rolf')

print(ordered)

ordered.move_to_end('jose', last=False)

print(ordered)

ordered.popitem()

print(ordered)

from collections import namedtuple

account = ('checking', 1850.50)

Account = namedtuple('Account', ['name', 'balance'])

accountNamedTuple = Account(*account)

print(accountNamedTuple._asdict()['balance'])


from collections import deque

firendsdeque = deque(('Rolf', 'Çharlie', 'Jen', 'Anna'))

firendsdeque.append('Jose')

firendsdeque.appendleft('Anthony')

print(firendsdeque)

firendsdeque.pop()
firendsdeque.popleft()

print(firendsdeque)


##########################################################################################################
# DateTime 
##########################################################################################################

from datetime import datetime, timezone, timedelta

import time

print(datetime.now())

print(datetime.now(timezone.utc))

today = datetime.now(timezone.utc)

tommorow = today + timedelta(days=1)

print(today)
print(tommorow)

print(today.strftime('%d-%m-%Y %H:%M:%S'))

#user_date = input('Enter date in YYYY-mm-dd format: ')

#user_date = datetime.strptime(user_date,  '%Y-%m-%d')

#print(user_date)

def measure_runtime(func):
    start = time.time()
    func()
    end = time.time()
    print(start - end)

def power(limit):
    return [x**2 for x in range(limit)]

measure_runtime(lambda : power(500000))

import timeit

print(timeit.timeit("[x**2 for x in range(10)]"))
print(timeit.timeit("list(map(lambda x: x**2, range(10)))"))


##########################################################################################################
# Logging in Python
##########################################################################################################

import logging

logging.basicConfig(format='%(asctime)s %(levelname) -8s [%(filename)s:%(lineno)d] : %(message)s', 
level=logging.DEBUG,
datefmt='%d-%m-%Y %H:%M:%S',
filename='test.txt')

logger = logging.getLogger(__name__)

logger.info("This will not show up.")

logger.warning("This will")

logger.debug('This is debug message.')

logger.critical('Critical erro occured.')

"""
DEBUG
INFO
WARNING
ERROR
CRITICAL
"""

