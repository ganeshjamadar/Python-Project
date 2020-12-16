############################################################################
# Files in Python
############################################################################
# import utils.file_operations as fileOpps
from utils.common.file_operations import read_from_file, save_to_file
from utils.find import find_in

print('\n\nFiles in Python')

# print(__name__)

# with open('data.txt', 'r') as my_file:
#     file_content = my_file.read()

# file_content = fileOpps.read_from_file('data.txt')

file_content = read_from_file('data.txt')

print(file_content)

write_file_content = input('Enter content to write to file: ')

# with open('data.txt', 'w') as my_file_writing:
#     my_file_writing.write(write_file_content)

# fileOpps.save_to_file('data.txt',write_file_content)

save_to_file('data.txt',write_file_content)
