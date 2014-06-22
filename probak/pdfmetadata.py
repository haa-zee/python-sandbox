#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys
from fnmatch import fnmatch

# a köv. sorhoz szükség van a pdfminer-re, amit ubuntun a python-pdfminer csomag tartalmaz.
# Ha nincs csomagban, akkor a githubról elérhető (talán máshonnan is)
from pdfminer.pdfparser import PDFParser, PDFDocument


def pdfMetadata(pathToPDF):
    '''
        Innen: http://stackoverflow.com/questions/14209214/reading-the-pdf-properties-metadata-in-python
    '''
    with open(pathToPDF,"rb") as pdfFile:
        parser=PDFParser(pdfFile)
        document=PDFDocument()
        parser.set_document(document)
        document.set_parser(parser)
        document.initialize()
    return document.info

def findFiles(fileSpec):
    result={}
    if(os.path.isdir(fileSpec)):
        for (directoryName, directories, files) in os.walk(fileSpec):
            for nextFile in files:
                fullPath=os.path.join(directoryName,nextFile)
                if fnmatch(fullPath,'*.pdf'):
                    result[fullPath]=pdfMetadata(fullPath)
    else:
        result[fileSpec]=pdfMetadata(fileSpec)

    return result


def main(arg):
    metadata=findFiles(arg)
    for filename in metadata:
        print u"%s %s\n"%(filename,metadata[filename])

if __name__ == "__main__":
    args=sys.argv[1:]
    if len(args)<1:
        print "Missing argument..."
        sys.exit(-1)

    map(main,args)
