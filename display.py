from music_reports import *
import os

os.system('clear')
empty_table = '''
    *               LEMONIFY                 *
    * Artist * Album * Year * Genre * Length *
    *                                        *
    *                                        *
'''
# print(empty_table)
# print('1. View all albums.')
# print('2. Arrange all albums by genre.')
# print('3. Display albums in time range (Ex: 1967 - 1980).')
# print('4. Display the shortest/longest album.')
# print('5. Display all albums by given artist.')
# print('6. Display all albums by album name.')
# print('7. Library statistics report.')
# print('8. View suggestions based on album.')
# print('9. Add new album.')
# print('10. Edit album.')
# print('11. Export library.')

 
def print_formatted(dictionary):
    SPACES_IN_FORMATTING = 20
    TOP_LINE = ['Artist', 'Album', 'Year', 'Genre', 'Length']
    max_character_length = 0
    max_artist_length = 0
    max_album_length = 0
    max_year_length = 0
    max_genre_length = 0
    max_time_length = 0
    for value in dictionary.values():
        length = 0
        for i in value:
            length += len(i)
        if length > max_character_length:
            max_character_length = length
        if len(value[0]) > max_artist_length:
            max_artist_length = len(value[0])
        if len(value[1]) > max_album_length:
            max_album_length = len(value[1])
        if len(value[2]) > max_year_length:
            max_year_length = len(value[2])
        if len(value[3]) > max_genre_length:
            max_genre_length = len(value[3])
        if len(value[4]) > max_time_length:
            max_time_length = len(value[4])
    print(max_character_length)
    line_length = max_character_length + SPACES_IN_FORMATTING
    print('*' * line_length)
    print('{:{align}{width}}'.format('LEMONFY', align='^', width=str(line_length)))
    print('*' * line_length)
    print(f'%{max_artist_length + 2}s' % TOP_LINE[0], f'%{max_album_length + 2}s' % TOP_LINE[1], f'%{max_year_length + 2}s' % TOP_LINE[2], f'%{max_genre_length + 2}s' % TOP_LINE[3], f'%{max_time_length + 2}s' % TOP_LINE[4])
    print('*' * line_length)
    for j in dictionary.values():
        print(f'%{max_artist_length + 2}s' % j[0], f'%{max_album_length + 2}s' % j[1], f'%{max_year_length + 2}s' % j[2], f'%{max_genre_length + 2}s' % j[3], f'%{max_time_length + 2}s' % j[4])
    print('*' * line_length)

running = True
while running is True:
    
    print_formatted(all_albums)
    print('1. View all albums.')
    print('2. Arrange all albums by genre.')
    print('3. Display albums in time range (Ex: 1967 - 1980).')
    print('4. Display the shortest/longest album.')
    print('5. Display all albums by given artist.')
    print('6. Display all albums by album name.')
    print('7. Library statistics report.')
    print('8. View suggestions based on album.')
    print('9. Add new album.')
    print('10. Edit album.')
    print('11. Export library.')
    print('12. Exit.')

    command = input('Input command:')


    if command == '1':
        os.system("clear")
        print_formatted(all_albums)
        input("Press enter to continue...") 
        os.system("clear") 
    elif command == '2':
        os.system("clear")
        print_formatted(sort_by_genre(all_albums))
        input("Press enter to continue...")
        os.system("clear")
    elif command == '3':
        os.system("clear")
        print_formatted(time_range_album(all_albums))
        input("Press enter to continue...")
        os.system("clear")
    elif command == '4':
        os.system("clear")
        print(shortest_longest(all_albums))
        input("Press enter to continue...")
        os.system("clear")
    elif command == '5':
        os.system("clear")
        print(artist_albums(all_albums))
        input("Press enter to continue...")
        os.system("clear")
    elif command == '6':
        os.system("clear")
        print(sort_by_album_name(all_albums))
        input("Press enter to continue...")
        os.system("clear")
    elif command == '7':
        os.system("clear")
        print('Under construction.')
        input("Press enter to continue...")
        os.system("clear")   
    elif command == '8':
        os.system("clear")
        print(all_albums)
        print(suggested_albums(all_albums))
        input("Press enter to continue...")
        os.system("clear")       
    elif command == '9':
        os.system("clear")
        print(add_new_album())
        input("Press enter to continue...")
        os.system("clear")     
    elif command == '10':
        os.system("clear")
        print(edit_album())
        input("Press enter to continue...")
        os.system("clear")      
    elif command == '11':
        os.system("clear")
        print(export_new_to_file())
        input("Press enter to continue...")
        os.system("clear")      
    elif command == '12':
        print('bye')
        exit()

