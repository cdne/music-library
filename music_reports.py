from collections import defaultdict
import os


# read file and place lines in a dictionary

def read_file():
    d = {}
    with open("file.txt", "r") as file:
        for line in file:
            items = line.strip().split(',')
            key, values = items[1], items[:]
            d[str(key)] = values
    return d


# all albums in a dictionary with values as a list
# global dictionary because it is used by multiple functions

all_albums = read_file()

# requirement #2 - Arrange the albums by genre


def sort_by_genre(temp_dict):
    genre = []
    new_dict = {}
    for key in temp_dict:
        genre.append([key, temp_dict[key][3]])
    genre.sort(key=lambda x: x[1])
    for i in genre:
        for key in temp_dict:
            if i[1] in temp_dict[key]:
                new_dict[key] = temp_dict[key]
    all_albums = new_dict
    return all_albums


# requirement #3 Find albums inside a user given time range

def time_range_album(temp_dict):
    x = int(input("Please insert a starting year: "))
    y = int(input("Please insert an ending year: "))
    os.system('clear')
    print(f'Displaying albums that came out between {x} and {y}.')
    years = []
    new_dict = {}
    for i in range(x, y):
        for key in temp_dict:
            if int(temp_dict[key][2]) == i:
                years.append([key, temp_dict[key][2]])
            years.sort(key=lambda x: int(x[1]))
    for i in years:
        for key in temp_dict:
            if i[1] in temp_dict[key]:
                new_dict[key] = temp_dict[key]
    return new_dict


# function required in another function, shortest_longest

def convert_to_seconds(minsec):
    list_minutes = []
    for i in minsec:
        if i != ':':
            list_minutes.append(i)
        else:
            break
    minutes = ''.join(list_minutes)
    return int(minutes) * 60 + int((minsec[-2:]))


# requirement #4 Find the shortest and longest album

def shortest_longest(criteria=None):
    if criteria is None:
        choice = input('Please select 1 for shortest or 2 for longest: ')
        os.system('clear')
        print(f'Displaying album based on choice - "{choice}".')
        if choice == '1':
            criteria = 'shortest'
        elif choice == '2':
            criteria = 'longest'
    working_dict = all_albums
    albums_list = []
    temp_dict = {}
    short = ''
    for key in working_dict:
        albums_list.append([key, working_dict[key][4]])
    for i in albums_list:
        i[1] = convert_to_seconds(i[1])
    albums_list.sort(key=lambda x: x[1])
    if criteria == 'shortest':
        temp_dict[albums_list[0][0]] = working_dict[albums_list[0][0]]
        return temp_dict
    elif criteria == 'longest':
        temp_dict[albums_list[-1][0]] = working_dict[albums_list[-1][0]]
        return temp_dict


# requirement #5 - List albums based on artist

def artist_albums(temp_dict):
    get_input = input("Enter the name of the artist: ")
    os.system('clear')
    print(f'Displaying albums by {get_input}')
    artist = []
    new_dict = {}
    i = 0
    for key in temp_dict:
        artist.append([key, temp_dict[key][0]])
        if get_input in artist[i][1]:
            new_dict[key] = temp_dict[key]
        i += 1
    return new_dict


# requirement #6 - After the user inputs an album name, print it

def sort_by_album_name(temp_dict):
    get_album_input = input("Enter album name: ")
    os.system('clear')
    print(f'Displaying results as requested album "{get_album_input}".')
    new_dict = {}
    for keys in temp_dict:
        if get_album_input in keys:
            new_dict[keys] = temp_dict[keys]
            return new_dict


# requirement # 7.1 Print the oldest album

def oldest_album():
    working_dict = all_albums
    album_years = []
    temp_dict = {}
    for key in working_dict:
        album_years.append([key, working_dict[key][2]])
    album_years.sort(key=lambda x: int(x[1]))
    oldest_year = album_years[0][1]
    for i in working_dict:
        if working_dict[i][2] == oldest_year:
            temp_dict[i] = working_dict[i]
    return temp_dict


# requirement #7.2 Displays the youngest album

def youngest_album():
    working_dict = all_albums
    album_years = []
    temp_dict = {}
    for key in working_dict:
        album_years.append([key, working_dict[key][2]])
    album_years.sort(key=lambda x: int(x[1]))
    temp_dict[album_years[-1][0]] = working_dict[album_years[-1][0]]
    return temp_dict


# requirement #7.3 Displays the total no. of albums

def count_all_albums():
    dict_from_file = all_albums
    return f'The total number of albums in the library is {len(dict_from_file)}.'


# requirement #7.4 Display the number of albums based on genre

def how_many_given_genre():
    dict_from_file = all_albums
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
    return f'The number of {selected_genre} albums is {how_many_albums_by_genre}.'


# requirement #8 - suggested albums based on user input album

def suggested_albums(temp_dict):
    get_album_input = input('Enter album name: ')
    os.system('clear')
    print(f'Displaying suggestions based on given album "{get_album_input}".')
    get_genre_from_input = ''
    suggested = []
    new_dict = {}

    def get_genre():
        for keys in temp_dict:
            if get_album_input in keys:
                return temp_dict[keys][3]

    get_genre_from_input = get_genre()
    for keys in temp_dict:
        albums_genre = temp_dict[keys][3]
        if get_genre_from_input in albums_genre or albums_genre in get_genre_from_input:
            new_dict[keys] = temp_dict[keys]
    return new_dict


# requirement #9 - User can add a new album

def add_new_album():
    global all_albums
    dict_from_file = all_albums
    new_album_list = []
    new_album_name = input('Please enter new album name: ')
    new_album_artist = input('Please enter new album artist: ')
    new_album_list.append(new_album_artist)
    new_album_list.append(new_album_name)
    new_album_year = input('Please enter the album year: ')
    new_album_list.append(new_album_year)
    new_album_genre = input('Please enter the album genre: ')
    new_album_list.append(new_album_genre)
    new_album_length = input('Please enter the album length: ')
    new_album_list.append(new_album_length)
    dict_from_file[new_album_name] = new_album_list
    print('Note: Please be careful, the new album is only saved in this '
          'session. If you would like to keep teh album in the list for '
          'longer, please consider exporting the current session library.')
    all_albums = dict_from_file
    return all_albums


# requirement #10 - User can edit an album

def edit_album():
    global all_albums
    dict_edit = all_albums
    valid_album_name = False
    while valid_album_name is False:
        album_to_edit = input('Please name the album you want to edit:')
        if album_to_edit in dict_edit:
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
    dict_edit[edited_album_name] = dict_edit.pop(album_to_edit)
    dict_edit[edited_album_name] = edited_list
    print('Note: Please be careful, the edited album is only saved in this '
          'session. If you would like to keep the album in the list for '
          'longer, please consider exporting the current session library.')
    all_albums = dict_edit
    return all_albums


# requirement #11 - User can export the current session library

def export_new_to_file():
    global all_albums
    temp_dict = all_albums
    list_of_albums = []
    for value in temp_dict.values():
        list_of_albums.append(','.join(value))
    with open("file.txt", 'w') as file:
        for i in list_of_albums:
            file.write(i + '\n')
    return 'Library successfully exported.'
