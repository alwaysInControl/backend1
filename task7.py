ten = [i for i in range(1, 11)]
evens = list(filter(lambda x: x % 2 == 0, ten))
evensSquare = list(map(lambda x: x ** 2, evens))
print(f'{ten}\n{evens}\n{evensSquare}')


def get_value(lst: list = ten):
    while True:
        try:
            index = int(input('Index (Enter 999 to exit): '))
            if index == 999:
                print('Program finished!')
                break
            if index < 0 or index >= len(lst):
                raise IndexError('Invalid index!')
            print(lst[index])
        except ValueError:
            print('Invalid index, enter a number!')
        except IndexError as e:
            print(e)


get_value(evens)
