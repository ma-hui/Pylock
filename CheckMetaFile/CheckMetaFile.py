# -*- coding:utf-8 -*-
import os
import time

DIR_PATH = "F:\TEST"
FILE_TYPE = ".meta"
ERR_FILE = []
SVN_FILE = ".svn"


def add_err_file(fname):
    ERR_FILE.append(fname)

def show_err_file():
    plen = len(DIR_PATH)
    for name in ERR_FILE:
        print name[plen+1 :]  #优化输出，不输出每个文件的DIR_PATH部分


def is_meta_file(file):
    spos = len(FILE_TYPE)
    if  file.find(FILE_TYPE, -spos) != -1 :
        return True
    else:
        return False

# def check_meta_file(path, names):
#     tb = []
#     for name in names:
#         f  = os.path.join(path, name)
#         if svn_info(f):
#             tb.append(name)
#
#     for name in tb:
#         if name.find(SVN_FILE) == -1:  # 非svn文件，进行meta和文件本体的对照检查
#             if is_meta_file(name):
#                 fname = name[:-5]
#             else:
#                 fname = name + FILE_TYPE
#
#             if not fname in names:
#                 f = os.path.join(path, name)
#                 add_err_file(f)
#         else:
#             return

def check_meta_file(path, names):
    '''
    :param fname: a list of file name in normal file path like [name1, name2, name3, ....]
    :return: none
    '''
    tb = {}
    err = "  Doesn't exist "

    for name in names :
        if tb.has_key(name):
            continue
        else:    #还没有加入字典中的文件名,即还没有判断过的

            ff = os.path.join(path, name)
            if svn_info(ff) and name.find(SVN_FILE) == -1:    #是svn项目中的文件，而且不是svn管理产生的文件，进行meta和文件本体的对照检查

                    if is_meta_file(name):
                        fname = name[:-5]
                    else:
                        fname = name + FILE_TYPE

                    f = os.path.join(path, fname)
                    if not(fname in names and svn_info(f)):
                        add_err_file(f + err)
                    else:
                        tb[name] = True
                        tb[fname] = True

def  svn_info(dirpath):
    return True

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
    check_dir_path(DIR_PATH)
    show_err_file()

if __name__ == '__main__':
    main()
