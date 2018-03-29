# -*- coding: utf-8 -*-
# @Filename: functions.py
# @Author: Yee
# @Email:  rlk002@gmail.com
# @Link: https://wj.pe
# @Date:   2018-03-27 10:59:14
# @Copyright: :copyright: (c)2018
# @Last Modified by:   Yee
# @Last Modified time: 2018-03-29 12:01:14

import sys
import os
import time
import string
import random
from yee.settings import env
from yee.libs import logsys

b62chars = string.digits + string.ascii_letters
b62base = len(b62chars)


def b62encode(num):
    if num < 0:
        raise ValueError('cannot encode negative numbers')

    if num == 0:
        return b62chars[0]

    digits = []
    while num:
        rem = num % b62base
        num = num // b62base
        digits.append(b62chars[rem])
    return ''.join(reversed(digits))


def b62decode(string):
    loc = b62chars.index
    size = len(string)
    num = 0

    for i, ch in enumerate(string, 1):
        num += loc(ch) * (b62base ** (size - i))

    return num


def load_class(s):
    path, klass = s.rsplit('.', 1)
    __import__(path)
    mod = sys.modules[path]
    return getattr(mod, klass)


def debug(string):
    lf = time.strftime("%Y-%m-%d", time.localtime())
    log_file_dir = env.LOG_PATH + 'debug/'
    mkdir(log_file_dir)
    log = logsys.Logsys('FA', log_file_dir + 'debug_' + lf)
    log.w('DEBUG', string)


def valid_email(email):
    email_re = re.compile(
        r"(^[-!#$%&'*+/=?^_`{}|~0-9A-Z]+(\.[-!#$%&'*+/=?^_`{}|~0-9A-Z]+)*"  # dot-atom
        r'|^"([\001-\010\013\014\016-\037!#-\[\]-\177]|\\[\001-011\013\014\016-\177])*"'  # quoted-string
        r')@(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?$', re.IGNORECASE)
    return bool(email_re.search(email))


def mkdir(path, relative=True):
    #currentPath = os.getcwd().replace("\\", '/')
    currentPath = ""
    path = path.strip().replace("\\", '/').rstrip('/')
    if not os.path.isdir(path):
        os.makedirs(path)
        return True
    else:
        return False


def random_string(length):
    from random import choice
    from string import digits, letters
    return ''.join(choice(digits + letters) for i in xrange(length))


def random_number(length):
    from random import choice
    from string import digits
    return ''.join(choice(digits) for i in xrange(length))


def md5(strings):
    import hashlib
    m = hashlib.md5()
    m.update(strings)
    return m.hexdigest()


def get_filename(file_path):
    head, tail = os.path.split(file_path)
    return tail


def parse_int(value):
    if isinstance(value, int):
        return value
    if isinstance(value, (float, Decimal)):
        return int(value)
    if isinstance(value, bytes):
        value = value.decode('ascii', 'replace')
    if isinstance(value, str_types):
        if validate_hex_string(value):
            return int(value[2:], 16)
        if validate_int_string(value):
            return int(value)
        if validate_decimal_string(value):
            return int(float(value))
    return None


def parse_boolean(b):
    if isinstance(b, bool):
        return b
    elif isinstance(b, str):
        b = b.lower()
        if b == 'true':
            return True
        elif b == 'false':
            return False
        else:
            return None
    elif isinstance(b, int):
        return bool(b)
    return None
