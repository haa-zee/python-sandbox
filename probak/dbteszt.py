#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Dec 29, 2014

@author: haazee

Feladat: van egy sérült firefox profilom, amiben a history is sérült (egyébként is menthetetlen, nem találom, melyik fájl vagy fájlok
miatt fagy le a firefox indításkor, de még safe mode-ban is). Az adatokat a places.sqlite adatbázis tartalmazza. Esetemben a moz_historyvisits nevű tábla
tartalma veszett el. Van egy szeptemberi mentésem, amelyben természetesen kissé eltérő adatok vannak, de az működik.
Mivel a tényleges history adatok a moz_places táblában vannak, ami sértetlennek tűnik, talán össze lehet hozni (GÁNYOLÁS-VESZÉLY!!!), hogy a mentett állapotból
áthozom a moz_historyvisits tartalmát úgy, hogy csak azokat a sorokat töltöm be, amelyek id-je megvan a sérült adatbázisban is.
Az első teszt, hogy a moz_places táblákat egyeztetem: azonos id-hez azonos url tartozik-e? Ezt csinálja ez a program.
'''

import sys,os.path
import sqlite3


def get_ids_and_urls(dbname):
    '''
    Visszaadja a paraméterként kapott adatbázisból a moz_places táblában lévő url-ket, dict formában, kulcsként az id-t használva.
    '''
    if not os.path.isfile(dbname):
        raise IOError("File not found %s"%dbname)
    
    db=sqlite3.connect(dbname)
    cur=db.cursor()
    
    result={ k:v for (k,v) in cur.execute("Select id,url from moz_places")}
    
    return result
    
    
    
def process_db(dbnames):
    print dbnames
    res1=get_ids_and_urls(dbnames[0])
    res2=get_ids_and_urls(dbnames[1])
    
    print len(res1.keys()), len(res2.keys())
    intersect=(set(res1.keys()) & set(res2.keys()))
    
    # A teszt kedvéért kiválasztok egy azonos id-jű párt és átírom a hozzá tartozó értéket (a [::-1] formátum megfordítja a stringet)
    #l=list(intersect)
    #res1[l[10]]=res1[l[10]][::-1]
    
    
    print len(intersect)
    for k in intersect:
        if res1[k] != res2[k]:
            print u"Eltérés: %s %s %s"%(k,res1[k],res2[k])
    print u"---vége---"
    # Úgy tűnik, a két táblában a közös id-k azonos url-t tartalmaznak. :)
    

if __name__ == '__main__':
    print sys.argv[1:3]
    if len(sys.argv)==3:
        process_db(sys.argv[1:])
    else:
        raise Exception("Two arguments needed...")
        