'''
Created on Jun 22, 2014

@author: haazee

Netfilter log analyzer

'''
import re


class LogIterator(object):
    
    '''
    Konstruktor - a paraméterek többsége remélem, öndokumentáló, a "parserObject" egy olyan
    függvény vagy metódus, amely inputként kap egy a "filterExpression" által kiszűrt sort
    és ebből visszaad egy előfeldolgozott objektumot. A "str" csak a példa kedvéért szerepel
    defaultként, ha eljutok odáig, akkor egy a log bejegyzések feldolgozására képes objektum
    lesz helyette. Csak azt még ki kell találni. :)
    '''
    def __init__(self, fileObject, parserObject=str, filterExpression='.*kernel: (DROP|ACCEPT) '):
        if(not isinstance(fileObject,file)):
            raise TypeError(fileObject)
        self.__logfile=fileObject
        self.__filterExpression=filterExpression
        self.__parserObject=parserObject
 
    # Python iterator osztály sajátosság. Kell és kész. :)       
    def __iter__(self):
        return self
    
    def next(self):
        
        nextLine=self.__logfile.readline()
        while nextLine and not re.match(self.__filterExpression, nextLine):
            nextLine=self.__logfile.readline()
        if not nextLine:
            raise StopIteration

        return self.__parserObject(nextLine)
    
    
