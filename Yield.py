# -*- coding:utf-8 -*-
def flattern(nested):
    try:
        try:
            nested + ''
        except TypeError:
            pass
        else:
            raise TypeError

        for sublist in nested:
           for element in flattern(sublist):
               yield  element
    except TypeError:
        yield  nested


test = [1,2,3,45,[123,[123,1233,'wdfa','adf'],888], 455]

# test = 1
print list(flattern(test))