'''
# This is project to manage the movies

'''

movies = []

def menu():
    user_input =  input('Please enter (a or A): adding movies (l or L): displaying movies (f or F): finding movies (q or Q): quiting: ')

    while user_input.lower() != 'q':
        if user_input.lower() == 'a':
            addMovies()
        elif user_input.lower() == 'l':
            showMovies(movies)
        elif user_input.lower() == 'f':
            findMovies()
        else:
            print('Invalid input!!')
            
        user_input =  input('Please enter (a or A): adding movies (l or L): displaying movies (f or F): finding movies (q or Q): quiting: ')

def addMovies():
    name = input('Please enter movie name: ')
    director = input('Please enter director name: ')
    releaseYear = input('Please enter release year: ')

    movies.append({
        'name': name,
        'director': director,
        'releaseYear': releaseYear
    })

def showMovies(movies):
    for movie in movies:
        showMoviesDetails(movie)
        print('-------------------------------------------------------')

def showMoviesDetails(movie):
    print(f'name : {movie["name"]}')
    print(f'director : {movie["director"]}')
    print(f'release Year : {movie["releaseYear"]}')

def findMovies():
    find_by = input('What property you are looking for?')
    looking_for = input('What are you searching for?')

    found_movies =  find_by_attribute(movies, looking_for , lambda x: x[find_by])

    showMovies(found_movies)

def find_by_attribute(items, expected, finder):
    found= []
    for i in items:
        if finder(i) == expected:
            found.append(i)
    return found

menu()