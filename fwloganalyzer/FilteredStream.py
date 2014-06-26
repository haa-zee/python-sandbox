# -*- coding: utf-8 -*-
'''
Created on Jun 22, 2014

@author: haazee

Netfilter log analyzer

'''
import re


class FilteredStream(object):
    
    '''
    Konstruktor
        readableObject = egy objektum, ami rendelkezik readline metódussal. A readline-tól elvárt működés,
            visszaad egy stringet (illetve bármely olyan objektumot, amiben re modul - regexp - segítségével keresni lehet),
            None-t, ha elfogytak az adatok. (tehát e tekintetben úgy műjödik, mintha egy fájlból olvasnék)
        filterExpression = regexp, amit a re modul keresőkifejezésként képes használni
        
    '''
    def __init__(self, readableObject, filterExpression=r".*kernel: (DROP|ACCEPT) "):
        self.__readableObject=readableObject
        self.__filterExpression=filterExpression
         
    # Python iterator osztály sajátosság. Kell és kész. :)       
    def __iter__(self):
        return self
    
    def next(self):
        
        nextLine=self.__readableObject.readline()
        while nextLine and not re.match(self.__filterExpression, nextLine):
            nextLine=self.__readableObject.readline()
        if not nextLine:
            raise StopIteration
        return nextLine
    
    
