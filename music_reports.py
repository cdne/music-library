from collections import defaultdict

d = defaultdict(list)


with open ("text_albums_data.txt", "r") as file:
        for line in file: 
            items = line.split(",")
            key, values = items[1], items[:]
            d[str(key)] = values
        
print(d)