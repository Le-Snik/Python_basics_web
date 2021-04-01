import os
import shutil

HOME = os.path.join(os.path.split(os.path.abspath(__file__))[0], 'my_project')
my_fold = 'templates'
flag = 0
for root, dirs, files in os.walk(HOME):
    copy_to = os.path.join(HOME, my_fold)
    for dirr in dirs:
        if dirr == my_fold:
            flag = 1
            copy_from = os.path.join(root, dirr)
            try:
                for root_und, dirs_und, files_und in os.walk(copy_from):
                    dirr_und = dirs_und[0]
                    break
            except IndexError:
                print(f" Папка {copy_from} пуста")
                continue
            copy_to = os.path.join(copy_to, dirr_und)
            delete = copy_from
            copy_from = os.path.join(copy_from, dirr_und)

            try:
                shutil.copytree(copy_from, copy_to, symlinks=False, ignore=None, copy_function=shutil.copy2,
                                ignore_dangling_symlinks=False)
                shutil.rmtree(delete)
            except FileExistsError:
                print(f" директория {copy_to}  уже существует")



if flag == 0:
    print(f" Папки {my_fold} не наидены")
