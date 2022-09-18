import os
# print(os.getcwd())
# print(os.listdir(r'c:\Users\hp\Documents\GitHub'))
# import shutil
# shutil.move('textfile.txt',r'c:\Users\hp\Documents\GitHub\PythonsFiles\advancepython')
for folder,sub_folder,file in os.walk(r'c:\Users\hp\Documents\GitHub\PythonsFiles\advancepythonsfiles'):
    print(f"folder are {folder}")
    print("\n")
    print('the subfolder are:')
    for sub_fold in sub_folder:
        print(f'\t the subfolder are{sub_fold}')
    print('\n')
    print('the files are')
    for f in file:
        print(f'\t files are:{f}')
    print('\n')
