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

 
running = True
while running is True:
    
    print(empty_table)
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
        print(all_albums)
        input("Press enter to continue...") 
        os.system("clear") 
    elif command == '2':
        os.system("clear")
        print(sort_by_genre(all_albums))
        input("Press enter to continue...")
        os.system("clear")
    elif command == '3':
        os.system("clear")
        print(time_range_album(all_albums))
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