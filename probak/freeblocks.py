#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Aug 3, 2014

@author: haazee
'''
import os


def get_free_space(fs):
    '''
    Mivel a statvfs által visszaadott f_blocks nem tartalmazza a foglalt (reserved) blokkokat, 
    ezért azt az f_bfree és az f_bavail különbségéből kell kiszámítani. Legalábbis ext2/3/4 fájlrendszer
    esetében. Lásd még tune2fs -l /dev/sdx!
    '''
    st=os.statvfs(fs)
    total=float(st.f_blocks)*st.f_frsize+st.f_bfree*st.f_frsize-st.f_bavail*st.f_frsize
    percent=round((total-st.f_bfree*st.f_frsize)*100/total,0)
    return percent

print "%u"%get_free_space('/boot')