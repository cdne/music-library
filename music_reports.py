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
        print(key)
        # genre.append([values,key])
        # genre.sort()
        


sort_by_genre(g)