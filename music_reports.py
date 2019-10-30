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

# all albums in a dictionary with values as a list
# global dictionary because it is used by multiple functions

all_albums = read_file()


def sort_by_genre(temp_dict):  # requirement 2
    genre = []
    new_dict = {}
    for key in temp_dict:
        genre.append([key, temp_dict[key][3]])
    # print(genre)
    genre.sort(key=lambda x: x[1])
    # print('sorted by genre', genre)
    # for i in genre:
    #     print(f'{temp_dict[i[0]]}\n')
    for i in genre:
        for key in temp_dict:
            if i[1] in temp_dict[key]:
                new_dict[key] = temp_dict[key]
    return new_dict   


# TO DO
# output all values in list
def time_range_album(temp_dict): # requirement 3
    x = int(input("Please insert a starting year: "))
    y = int(input("Please insert an ending year: "))
    years = []
    new_dict = {}
    for i in range(x, y):
        for key in temp_dict:
            if int(temp_dict[key][2]) == i:
                years.append([key, temp_dict[key][2]])
            years.sort(key = lambda x: int(x[1]))
    for i in years:
        for key in temp_dict:
            if i[1] in temp_dict[key]:
                new_dict[key] = temp_dict[key]
    return new_dict
   

def convert_to_seconds(minsec):  # required in shortest_longest
    list_minutes = []
    for i in minsec:
        if i != ':':
            list_minutes.append(i)
        else:
            break
    minutes = ''.join(list_minutes)
    return int(minutes) * 60 + int((minsec[-2:]))

# make input inside function 'shortest' and 'longest'
def shortest_longest(what_album):  # requireent 4
    dict_from_file = all_albums
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

def artist_albums(temp_dict): #requirement 5

    get_input = input("Enter the name of the artist: ")
    artist = []
    albums_from_artist = []
    i = 0
    for key in temp_dict:
        artist.append([key, temp_dict[key][0]])
        if get_input in artist[i][1]:
             albums_from_artist.append(temp_dict[key])
        i += 1 
    return albums_from_artist

def sort_by_album_name(temp_dict): # requirement 6
    get_album_input = input("Enter album name: ")
    album_details = []
    for keys in temp_dict:
        if get_album_input in keys:
            return temp_dict[keys]
            
# TO DO
# print all of the same year
def oldest_album():  # requirement 7.1 oldest album
    dict_from_file = all_albums
    album_years = []
    for key in dict_from_file:
        album_years.append([key, dict_from_file[key][2]])
    album_years.sort(key=lambda x: int(x[1]))
    return dict_from_file[album_years[0][0]]


def youngest_album():  # requirement 7.2 youngest album
    dict_from_file = all_albums
    album_years = []
    for key in dict_from_file:
        album_years.append([key, dict_from_file[key][2]])
    album_years.sort(key=lambda x: int(x[1]))
    return dict_from_file[album_years[-1][0]]


def count_all_albums():  # requirement 7.3 total no. of albums
    dict_from_file = all_albums
    return len(dict_from_file)

def suggested_albums(temp_dict): # requirement 8

    get_album_input = input('Enter album name: ')
    get_genre_from_input = ''
    suggested = []
    
    def get_genre():
        for keys in temp_dict:
            if get_album_input in keys:
              return temp_dict[keys][3]
                             
    get_genre_from_input = get_genre()
    for keys in temp_dict:
       
        albums_genre = temp_dict[keys][3]

        if get_genre_from_input in albums_genre or albums_genre in get_genre_from_input:
            suggested.append(temp_dict[keys])
  
    return suggested
    

# print('Total number of albums: ', count_all_albums())


def how_many_given_genre():  # requirement 7.4 how many albums based on genre
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
    return how_many_albums_by_genre


# requirement 9, what if edit and add in the same session,
# without exporting


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
    print('Please be careful, the new album is only saved in this session.'
          ' If you would like to keep teh album in the list for longer, '
          ' please consider exporting the current session library.')
    all_albums = dict_from_file 
    return all_albums



# requirement 10, needs mistake proof,
# what if edit and add in the same session


def edit_album():
    global all_albums
    dict_from_file = all_albums
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
    all_albums = dict_from_file
    return all_albums

# export
def export_new_to_file():  # requirement 11
    global all_albums
    temp_dict = all_albums
    list_of_albums = []
    for value in temp_dict.values():
        list_of_albums.append(','.join(value))
    print(list_of_albums)
    with open("file.txt", 'w') as file:
        for i in list_of_albums:
            file.write(i + '\n')