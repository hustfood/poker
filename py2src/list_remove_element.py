# -*- coding: utf8 -*-

"""--------------------------------------------------------------
Author:
food
gzfujianfeng@corp.netease.com

Date:
2019/03/02

Description:

History:
2017/09/14, create file.
--------------------------------------------------------------"""

_list = [1, 2, 3, 4, 5, 6]


def _ff(_v):
	return _v in [3, 4]


# error try below
for v in _list:
	print v
	if _ff(v):
		_list.remove(v)
print _list

# right try below
_list = [v for v in _list if not _ff(v)]
print _list
