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


# def shortest(): # requireent 4
#     return


# def longest(): # requirement 4
#     return


# def artist_albums(): #requirement 5
#     input('artist')
#     return


# def sort_by_album_name(): # requirement 6
#     input('album name')
#     return


# def oldest_album(): # requirement 7
#     return


# def youngest_album(): # requirement 7
#     return


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
