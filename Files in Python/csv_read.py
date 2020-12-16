import utils.common.file_operations as fileOperations
    
csv_file_content = fileOperations.read_from_file('csv_data.txt')

csv_file_content = csv_file_content[1:]

csv_data = [line.strip() for line in csv_file_content]

for data in csv_data:
    student = data.split(',')
    name = student[0].title()
    age = student[1]
    university = student[2].upper()
    degree = student[3].capitalize()

    print(f'Student {name} is {age} pursuing {degree} in {university}.')


sample_csv_value = ','.join(['Rolf','14','Cambrige','M.sc'])

print(sample_csv_value)