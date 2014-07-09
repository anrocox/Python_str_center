#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 9, 2014

@author: anroco

How to working the center method of a python str?

¿Como funciona el metodo center de un str python?
'''

#create a str
s = 'example center string'
print(s)

#generates a string of length defined, focusing 's' inside of the new string.
s_center = s.center(30)
print(s_center)
print(s)

#can specify the padding character
s_center = s.center(30, '-')
print(s_center)
