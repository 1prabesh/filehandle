import os
path="C:\\Users\\Dell\\Desktop\\applications\\newfile.txt"
if os.path.exists(path) is True:
    print('Path exist')
elif os.path.exists(path) is False:
    print('File not found')
    user=input('Do you want to create this file:?\t').lower()
    if user in ['Yes','yes','YES']:
        try:
            with open(path,'w') as file:
                file.write('Hello some text has been added')
        except FileNotFoundError:
            print('Something went wrong')
    elif user in ['No','no','NO']:
        print('Process Halted')
else:
    user=input('Do you want to read the file : ?').lower()
    if user == 'ok':
        try:
            with open(path,'r') as file:
                print(file.read())
        except FileExistsError:
            print('Halted')
    else :
        print('Checked')
