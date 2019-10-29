from collections import defaultdict


# read file and place lines in dictionary

def read_file(): 
    d = {}
    with open ("file.txt", "r") as file:
            for line in file: 
                items = line.strip().split(',')
                key, values = items[1], items[:]
                d[str(key)] = values
    
    return d  



# placeholder for files
hold_lines = read_file()

def sort_by_genre(temp_dict): # requirement 2
    genre = []
    for key in temp_dict:
        genre.append([key, temp_dict[key][3]])
    print(genre)
    genre.sort(key = lambda x: x[1])
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


print('Requested album is', shortest_longest('shortest'))
print('Requested album is', shortest_longest('longest'))



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


print('The oldest album is: ', oldest_album())


def youngest_album():  # requirement 7.2 youngest album
    dict_from_file = read_file()
    album_years = []
    for key in dict_from_file:
        album_years.append([key, dict_from_file[key][2]])
    album_years.sort(key=lambda x: int(x[1]))
    return dict_from_file[album_years[-1][0]]


print('The youngest album is: ', youngest_album())


# def count_all_albums(): # requirement 7
#     return


# def how_many_given_genre(): # requirement 7
#     return


# def suggested_albums(): # requirement 8
#     input('album name')
#     # suggest albums with the same genre
#     return


# def add_new_album(): # requirement 9
#     return


# def edit_ablum(): # requirement 10
#     return


# def export_new_to_file(): # requirement 11
