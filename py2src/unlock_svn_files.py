#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""-------------------------------------------
Author:
foojamfung
gzfujianfeng@corp.netease.com

Description:
unlock files of svn

History:
2019-04-18, create file
-------------------------------------------"""
import os
import re

def main(local_svn_path):

    os.chdir(local_svn_path)
    cmd_ret = os.popen('svn status --show-updates').readlines()
    ret_re = r'\s+O\s+\d+\s+(\S*)'

    locked_files = []
    for ret in cmd_ret:
        re_ret = re.findall(ret_re, ret)
        if re_ret:
            locked_files.append(re_ret[0])

    print 'locked files count: %s' % len(locked_files)

    for _f in locked_files:
        os.popen('svn unlock --force %s' % _f)

    print 'done'


if __name__ == "__main__":
    svn_path = r''
    if os.path.isdir(svn_path):
        main(svn_path)