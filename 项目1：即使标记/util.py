# -*- coding=utf-8 -*-
def lines(file):
    for line in file:
        yield line
    yield '\n'

def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():    #不是空行则加入当前块中
            block.append(line)
        elif block:    #当前块不为空[]，则将当前的块返回
            yield ''.join(block).strip()
            block = []

