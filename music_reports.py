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

# placeholder for lines in dictionary format with album as keys and info about album as list
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


# def shortest(): # requireent 4
#     return


# def longest(): # requirement 4
#     return

def artist_albums(temp_dict): #requirement 5
    # read from user name
    # itterate over index 0 with string if is in then show all albums
    get_input = input("Enter the name of the artist: ")
    artist = []
    albums_from_artist = []
    i = 0
    for key in temp_dict:
        artist.append([key, temp_dict[key][0]])
        if get_input in artist[i][1]:
             albums_from_artist.append(artist[i][0])
        i += 1
    
    return albums_from_artist

def sort_by_album_name(temp_dict): # requirement 6
    get_album_input = input("Enter album name: ")
    album_details = []
    for keys in temp_dict:
        if get_album_input in keys:
            return temp_dict[keys]
            

# def oldest_album(): # requirement 7
#     return


# def youngest_album(): # requirement 7
#     return


# def count_all_albums(): # requirement 7
#     return


# def how_many_given_genre(): # requirement 7
#     return


def suggested_albums(temp_dict): # requirement 8
    # TO DO remove input album from created list

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
    

# def add_new_album(): # requirement 9
#     return


# def edit_ablum(): # requirement 10
#     return


# def export_new_to_file(): # requirement 11
