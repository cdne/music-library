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


g = read_file()

def sort_by_genre(temp_dict):
    genre = []
    for key in temp_dict:
        genre.append([key, temp_dict[key][3]])
    print(genre)
    genre.sort(key = lambda x: x[1])
    print('sorted by genre', genre)
    for i in genre:
        print(f'{temp_dict[i[0]]}\n')

# test branch
        


sort_by_genre(g)