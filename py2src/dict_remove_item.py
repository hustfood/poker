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

_dict = {
	'a': 1,
	'b': 2,
	'c': 3,
	'd': 4,
	'e': 5
}


def _ff_k(_k):
	return _k in ['c', 'd']


def _ff_v(_v):
	return _v in [3, 4]


# by key
for k in _dict.keys():
	if _ff_k(k):
		del _dict[k]
print _dict

# by value
for k, v in _dict.items():
	if _ff_v(v):
		del _dict[k]
print _dict
