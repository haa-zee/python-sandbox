#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Aug 3, 2014

@author: haazee
'''
import os


def get_free_space(fs):
    st=os.statvfs(fs)
    total=float(st.f_blocks*st.f_frsize)+float(st.f_bfree*st.f_frsize)-float(st.f_bavail*st.f_frsize)
    percent=round((total-float(st.f_bfree*st.f_frsize))*100/total)
    return percent

print get_free_space('/boot')