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
    valid_range = False
    while valid_range is False:
        try:
            valid_range = True
            x = int(input("Please insert a starting year: "))
            y = int(input("Please insert an ending year: "))
            # os.system('clear')
            print(f'Displaying albums that came out between {x} and {y}.')
            years = []
            new_dict = {}
            if x <= y:
                val1 = x
                val2 = y
            else:
                val1 = y
                val2 = x
            for i in range(val1, val2+1):
                for key in temp_dict:
                    if int(temp_dict[key][2]) == i:
                        years.append([key, temp_dict[key][2]])
                    years.sort(key=lambda x: int(x[1]))
            for i in years:
                for key in temp_dict:
                    if i[1] in temp_dict[key]:
                        new_dict[key] = temp_dict[key]
            return new_dict
        except ValueError:
            print("Invalid year.")
            valid_range = False


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
        valid_choice = False
        while valid_choice is False:
            choice = input('Please select 1 for shortest or 2 for longest: ')
            # os.system('clear')
            if choice == '1':
                criteria = 'shortest'
                valid_choice = True
            elif choice == '2':
                criteria = 'longest'
                valid_choice = True
            else:
                valid_choice = False
                print('Invalid choice.')
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
    artist_list = [i[0].title() for i in temp_dict.values()]
    get_input = input("Enter the name of the artist: ").title()
    if get_input == '':
        return {'Invalid Choice': ['Invalid choice.', 'Invalid choice.', '0000', 'Invalid choice.', '00:00']}
    if get_input not in artist_list:
        return {'Invalid Choice': ['Invalid choice.', 'Invalid choice.', '0000', 'Invalid choice.', '00:00']}
    print(f'Displaying albums by {get_input}')
    artist = []
    new_dict = {}
    i = 0
    for key in temp_dict:
        artist.append([key, temp_dict[key][0]])
        if get_input == artist[i][1]:
            new_dict[key] = temp_dict[key]
        elif get_input.lower() == artist[i][1]:
            new_dict[key] = temp_dict[key]
        i += 1
    return new_dict


# requirement #6 - After the user inputs an album name, print it

def sort_by_album_name(temp_dict):
    flag = True
    while flag:
        try:
            get_album_input = input("Enter album name: ").title()
            if get_album_input == '':
                return {'Invalid Choice': ['Invalid choice.', 'Invalid choice.', '0000', 'Invalid choice.', '00:00']}
            print(f'Displaying results as requested album "{get_album_input}".')
            new_dict = {}
            for keys in temp_dict:
                if get_album_input in keys:
                    new_dict[keys] = temp_dict[keys]
                    flag = False
                    return new_dict
            lower = get_album_input.lower()
            for z in temp_dict:
                if lower in z:
                    new_dict[z] = temp_dict[z]
                    flag = False
                    return new_dict
        except:
            print("Album was not found try again")
        else:
            print("Album was not found try again")


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
    flag = True
    while flag:
        try:
            get_album_input = input('Enter album name: ').title()

            if get_album_input == '':
                return {'Invalid Choice': ['Invalid choice.', 'Invalid choice.', '0000', 'Invalid choice.', '00:00']}
            flag = False
            get_genre_from_input = ''
            new_dict = {}

            def get_genre():
                for keys in temp_dict:
                    if get_album_input in keys:
                        return temp_dict[keys][3]
                for z in temp_dict:
                    if get_album_input.lower() in z:
                        return temp_dict[z][3]

            get_genre_from_input = get_genre()
            for keys in temp_dict:
                albums_genre = temp_dict[keys][3]
                if get_genre_from_input in albums_genre or albums_genre in get_genre_from_input:
                    new_dict[keys] = temp_dict[keys]
            print(f'Displaying suggestions based on given album "{get_album_input}".')
            return new_dict
        except:
            print(f"Album {get_album_input} was not found try again")
            flag = True


# time validator function required in the next functions

def time_validator():
    valid_time = False
    while valid_time is False:
        time_string = input('Please enter the album length: ')
        if len(time_string) < 4:
            print('Invalid time. Input too short.')
            valid_time = False
            continue
        if len(time_string) > 3 and time_string[-3] != ':':
            print('Invalid time format. Must have : to delimit seconds eg: 56:22, 42:00.')
            valid_time = False
            continue
        temp_time = time_string.replace(':', '', 1)
        if temp_time.isdigit():
            valid_time = True
            continue
        if not temp_time.isdigit():
            print('Invalid time. Uncertain digits. Please input delimited digits eg: 56:22, 42:00')
            valid_time = False
            continue
    return time_string


# requirement #9 - User can add a new album

def add_new_album():
    global all_albums
    dict_addition = all_albums
    new_album_list = []
    albums_list = [i.title() for i in dict_addition.keys()]
    valid_album_name = False
    while valid_album_name is False:
        new_album_name = input('Please name the album you want to add: ')
        t_new_album_name = new_album_name.title()
        if t_new_album_name in albums_list:
            print('The library already has that album.')
        else:
            valid_album_name = True
    t_new_album_name = new_album_name.title()
    new_album_artist = input('Please enter new album artist: ')
    t_new_album_artist = new_album_artist.title()
    new_album_list.append(t_new_album_artist)
    new_album_list.append(t_new_album_name)
    valid_year = False
    while valid_year is False:
        new_album_year = input('Please enter the album year: ')
        if new_album_year.isdigit():
            valid_year = True
        else:
            print('The year must be a valid number (integer).')
    new_album_list.append(new_album_year)
    new_album_genre = input('Please enter the album genre: ')
    l_new_album_genre = new_album_genre.lower()
    new_album_list.append(l_new_album_genre)
    new_album_length = time_validator()
    new_album_list.append(new_album_length)
    dict_addition[t_new_album_name] = new_album_list
    print('Note: Please be careful, the new album is only saved in this '
          'session. If you would like to keep teh album in the list for '
          'longer, please consider exporting the current session library.')
    all_albums = dict_addition
    return all_albums


# requirement #10 - User can edit an album

def edit_album():
    global all_albums
    dict_edit = all_albums
    albums_list = [i.title() for i in dict_edit.keys()]
    valid_album_name = False
    while valid_album_name is False:
        album_to_edit = input('Please name the album you want to edit: ')
        t_album_to_edit = album_to_edit.title()
        if t_album_to_edit in albums_list:
            valid_album_name = True
        else:
            print('There are no albums with this name in the music library.'
                  ' Please select another album.')
    edited_list = []
    edited_album_name = input('Please enter new album name: ')
    t_edited_album_name = edited_album_name.title()
    edited_album_artist = input('Please enter the artist: ')
    t_edited_album_artist = edited_album_artist.title()
    edited_list.append(t_edited_album_artist)
    edited_list.append(t_edited_album_name)
    valid_year = False
    while valid_year is False:
        edited_album_year = input('Please enter the album year: ')
        if edited_album_year.isdigit():
            valid_year = True
        else:
            print('The year must be a valid number (integer).')
    edited_list.append(edited_album_year)
    edited_album_genre = input('Please enter the album genre: ')
    l_edited_album_genre = edited_album_genre.lower()
    edited_list.append(l_edited_album_genre)

    edited_album_length = time_validator()

    edited_list.append(edited_album_length)
    try:
        if album_to_edit[0] in 'abcdefghijklmnopqrstuvxzyw':
            dict_edit[t_edited_album_name] = dict_edit.pop(album_to_edit)
        else:
            dict_edit[t_edited_album_name] = dict_edit.pop(t_album_to_edit)
    except IndexError:
        dict_edit[t_edited_album_name] = dict_edit.pop(t_album_to_edit)
    dict_edit[t_edited_album_name] = edited_list
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
