# -*- coding:utf-8 -*-
import os


DIR_PATH = 'F:\TEST'
FILE_TYPE = '.meta'
ERR_FILE = []
SVN_FILE = '.svn'


def  add_err_file(fname):
    ERR_FILE.append(fname)

def  show_err_file():
    plen = len(DIR_PATH)
    for name in ERR_FILE:
        print name[plen+1 :]  #优化输出，不输出每个文件的DIR_PATH部分


def  is_meta_file(file):
    spos = len(FILE_TYPE)
    if  file.find(FILE_TYPE, -spos) != -1 :
        return True
    else:
        return False

def  check_meta_file(path, names):
    '''
    :param fname: a list of file name in normal file path like [name1, name2, name3, ....]
    :return: none
    '''
    for name in names :
        if name.find(SVN_FILE) == -1:    #非svn文件，进行meta和文件本体的对照检查
            if is_meta_file(name):
                fname = name[:-5]
            else:
                fname = name + FILE_TYPE

            if not fname in names:
                f = os.path.join(path, name)
                add_err_file(f)
        else:
            return

def  check_dir_path(dirpath):
    if os.path.exists(dirpath):

        if dirpath.find(SVN_FILE) == -1:    #不是svn创建的目录，才需要判断meta文件
            dirs = os.listdir(dirpath)
            check_meta_file(dirpath ,dirs)

            for file in dirs:
                newpath = os.path.join(dirpath,file)
                if os.path.isdir(newpath):
                    check_dir_path(newpath)
        else:
            return
    else:
        print '%s is not exists' % dirpath


def main():
    path = DIR_PATH
    check_dir_path(path)
    show_err_file()


if __name__ == '__main__':
    main()
