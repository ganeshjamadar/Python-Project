# Ask the user for a list of 3 friends
# For each friend, we'll tell the user wheather they are nearby 
# For each nearby friend, We''ll save their name to nearby_friends.txt
import utils.common.file_operations as fileOprations

friends = [friend.capitalize() for friend in  input('Enter three friend names, separated by commas (no spaces, Please):').split(',')]

people_content = [line.strip().capitalize() for line in fileOprations.read_from_file('people.txt')]

friends_set = set(friends)

people_content_set = set(people_content)

friends_nearby_set = friends_set.intersection(people_content_set)

for friend in friends_nearby_set:
    print(f'{friend} is nearby, meet up with them.')
    fileOprations.save_to_file('nearby_friends.txt', f'{friend}\n')

