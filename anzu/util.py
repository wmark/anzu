#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2009-2010 W-Mark Kubacki; wmark@hurrikane.de
#

__all__ = ['baseN']

base_representation_chars = "0123456789abcdefghijklmnopqrstuvwxyz"

def baseN(num, b):
    """Converts the unsigned integer 'num' into its string representation
    in positional numeral system with base 'b'.

    Use this to get a short string representation of an otherwise long
    integer, e.g. hashes.

    Examples::

        >>> baseN(300, 36)
        '8c'
        >>> baseN(300, 10)
        '300'
        >>> baseN(300, 16)
        '12c'
        >>> baseN(300, 8)
        '454'
        >>> baseN(300, 5)
        '2200'
        >>> baseN(300, 2)
        '100101100'
        >>> baseN(0, 14)
        '0'
        >>> n = 2189753199
        >>> baseN(n, 36)
        '107q0dr'
        >>> n
        2189753199
    """
    assert num >= 0, "'num' must be positive"
    assert 0 < b <= len(base_representation_chars), \
        "radix 'b' must be greater than 0 and less or equal than 36"
    if num == 0:
        return "0"
    else:
        r = ''
        while num > 0:
            r += base_representation_chars[num % b]
            num = num // b
        return r[::-1]