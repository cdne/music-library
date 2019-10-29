from collections import defaultdict

# read file and place lines in a dictionary


def read_file():
    d = {}
    with open("file.txt", "r") as file:
        for line in file:
            items = line.strip().split(',')
            key, values = items[1], items[:]
            d[str(key)] = values
    return d


def sort_by_genre(temp_dict):  # requirement 2
    genre = []
    for key in temp_dict:
        genre.append([key, temp_dict[key][3]])
    print(genre)
    genre.sort(key=lambda x: x[1])
    print('sorted by genre', genre)
    for i in genre:
        print(f'{temp_dict[i[0]]}\n')

# def time_range_album(): # requirement 3
#     input('')
#     return


def convert_to_seconds(minsec):  # required in shortest_longest
    list_minutes = []
    for i in minsec:
        if i != ':':
            list_minutes.append(i)
        else:
            break
    minutes = ''.join(list_minutes)
    return int(minutes) * 60 + int((minsec[-2:]))


def shortest_longest(what_album):  # requireent 4
    dict_from_file = read_file()
    albums_list = []
    for key in dict_from_file:
        albums_list.append([key, dict_from_file[key][4]])
    for i in albums_list:
        i[1] = convert_to_seconds(i[1])
    albums_list.sort(key=lambda x: x[1])
    if what_album == 'shortest':
        return dict_from_file[albums_list[0][0]]
    elif what_album == 'longest':
        return dict_from_file[albums_list[-1][0]]


# print('Requested album is', shortest_longest('shortest'))
# print('Requested album is', shortest_longest('longest'))



# def artist_albums(): #requirement 5
#     input('artist')
#     return


# def sort_by_album_name(): # requirement 6
#     input('album name')
#     return


def oldest_album():  # requirement 7.1 oldest album
    dict_from_file = read_file()
    album_years = []
    for key in dict_from_file:
        album_years.append([key, dict_from_file[key][2]])
    album_years.sort(key=lambda x: int(x[1]))
    return dict_from_file[album_years[0][0]]


# print('The oldest album is: ', oldest_album())


def youngest_album():  # requirement 7.2 youngest album
    dict_from_file = read_file()
    album_years = []
    for key in dict_from_file:
        album_years.append([key, dict_from_file[key][2]])
    album_years.sort(key=lambda x: int(x[1]))
    return dict_from_file[album_years[-1][0]]


# print('The youngest album is: ', youngest_album())


def count_all_albums():  # requirement 7.3 total no. of albums
    dict_from_file = read_file()
    return len(dict_from_file)


# print('Total number of albums: ', count_all_albums())


def how_many_given_genre():  # requirement 7.4 how many albums based on genre
    dict_from_file = read_file()
    genres_list = []
    for key in dict_from_file:
        genres_list.append(dict_from_file[key][3])
    valid_input = False
    while valid_input is False:
        selected_genre = input('Please select the genre: ')
        if selected_genre in genres_list:
            valid_input = True
        elif selected_genre == 'exit()':
            print('Thanks for using our product. Have a nice day!')
            exit()
        else:
            print('There are no albums of this genre in the music library.'
                  ' Please select another genre or type "exit()" to quit '
                  'the program.')
    how_many_albums_by_genre = 0
    for key in dict_from_file:
        if selected_genre in dict_from_file[key]:
            how_many_albums_by_genre += 1
    return how_many_albums_by_genre


# print('Your selected genre returned ', how_many_given_genre())

# def suggested_albums(): # requirement 8
#     input('album name')
#     # suggest albums with the same genre
#     return


# def add_new_album(): # requirement 9
#     return


def edit_album():  # requirement 10, needs mistake proof
    dict_from_file = read_file()
    valid_album_name = False
    while valid_album_name is False:
        album_to_edit = input('Please name the album you want to edit:')
        if album_to_edit in dict_from_file:
            valid_album_name = True
        elif album_to_edit == 'exit()':
            print('Thanks for using our product. Have a nice day!')
            exit()
        else:
            print('There are no albums with this name in the music library.'
                  ' Please select another album or type "exit()" to quit '
                  'the program.')
    edited_list = []
    edited_album_name = input('Please enter new album name: ')
    edited_album_artist = input('Please enter the artist: ')
    edited_list.append(edited_album_artist)
    edited_list.append(edited_album_name)
    edited_album_year = input('Please enter the album year: ')
    edited_list.append(edited_album_year)
    edited_album_genre = input('Please enter the album genre: ')
    edited_list.append(edited_album_genre)
    edited_album_length = input('Please enter the album length: ')
    edited_list.append(edited_album_length)
    dict_from_file[edited_album_name] = dict_from_file.pop(album_to_edit)
    dict_from_file[edited_album_name] = edited_list
    print('Please be careful, the edited album is only saved in this session.'
          ' If you would like to keep teh album in the list for longer, '
          ' please consider exporting the current session library.')
    print(dict_from_file)
    # return


edit_album()

# def export_new_to_file(): # requirement 11
