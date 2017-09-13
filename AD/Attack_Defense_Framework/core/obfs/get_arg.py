#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 伪造数据需要

import re
import os

def get_content(path):
    return open(path).read()

def find_arg(content, arg):
    p = re.compile(r'\$' + arg + '\[[\'"]\w+[\'"]\]')
    return list(set(p.findall(content)))

def get_all(root, arg):
    all = []
    result = os.walk(root)
    for path,d,filelist in result:
        for file in filelist:
            if file.endswith(".php"):#如果结尾是php的,就加入到伪造攻击的
                full_path = path + "/" + file
                content = get_content(full_path)
                all.append((full_path, find_arg(content, arg)))
    return all

def main():
    root = "../../test"
    print get_all(root, "_GET")
    print get_all(root, "_POST")
    print get_all(root, "_COOKIE")

if __name__ == "__main__":
    main()
