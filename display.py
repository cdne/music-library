from music_reports import *
import os

empty_table = '''
    *               LEMONIFY                 *
    * Artist * Album * Year * Genre * Length *
    *                                        *
    *                                        *
'''
print(empty_table)

running = True
while running is True:

    command = input('Input command:')
    if command == '1':
        os.system("clear")
        print(empty_table)
        add_new_album()
        export_new_to_file()
    elif command == '2':
        print(all_albums)
    elif command == '3':
        edit_album()
    elif command == 'exit()':
        print('bye')
        exit()