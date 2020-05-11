import os

from pip._vendor.distlib.compat import raw_input

folders = []
print('Welcome to dir2list 0.1v\n')


def main():
    inputpath()


def inputpath():
    path = raw_input('Please Enter the FULL PATH:')
    if os.path.isdir(path):
        print(f'Path: {path}')
        filename = input('Please Enter the Filename:')
        check = dir2list(path, filename)
        if check == 1:
            print(f'File: {filename}.txt succesfully written')
            checkexit()
    else:
        print('Directory not exists.')
        main()


def dir2list(path, filename):
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for folder in d:
            folders.append(os.path.join(r, folder))

    with open(filename + '.txt', 'a') as file:
        for f in folders:
            file.write(f + '\n')
        return 1


def checkexit():
    str_exit = input('Program Exit ?')
    if str_exit == 'y':
        exit()
    else:
        main()


main()
