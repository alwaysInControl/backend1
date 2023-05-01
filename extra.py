movies = {
    "Django": {
        "John": 10,
        "Jack": 9
    },

    "backend": {}
}


def find_movie(movie_title):
    if movie_title in movies.keys():
        return movie_title
    else:
        return False


def add_movie():
    movie_title = input('Movie title to add: ').title()
    if find_movie(movie_title):
        print('This movie already exists!')
    else:
        movies[movie_title] = {}
        print('Movie added successfully!')


def add_rating():
    movie_title = input('Movie title to rate: ').title()
    if not find_movie(movie_title):
        print("This movie doesn't exist!")
    else:
        while True:
            person_name = input('Name of person: ').title()
            if person_name in movies[movie_title].keys():
                print('This user already exists!')
                continue
            break
        while True:
            try:
                rate = int(input('Rate for movie(0-10): '))
                if not 0 <= rate <= 10:
                    print('Rate from 0 to 10!')
                    continue
                break
            except ValueError:
                print('Use numbers to rate!')
        movies[movie_title].update({person_name: rate})
        print(f'A rating has been added for {movie_title}: {person_name} rated it {rate}')


def show_rating():
    for movie in movies:
        values = movies[movie].values()
        if not values:
            print(f'Rating is not yet available for {movie}.')
        else:
            aver = round(sum(values) / len(values), 1)
            print(f'{movie} is rated {aver}')


while True:
    try:
        command = int(input('Choose command:\n1.Add movie\n2.Add rating\n3.Show rating\n0.Exit\n=> '))
        if command == 0:
            print('Program finished!')
            break
        elif command == 1:
            add_movie()
        elif command == 2:
            add_rating()
        elif command == 3:
            show_rating()
        else:
            print('Invalid, choose again!')
        print('---List of movies---')
        for k, v in movies.items():
            print(f'* {k}: {v}')
    except ValueError:
        print('Choose from given numbers!')
