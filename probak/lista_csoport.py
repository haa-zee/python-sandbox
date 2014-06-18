#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Feladat innen: http://hup.hu/node/133324
(azóta, hogy nekiestem, picit változott)
'''



lista1=["\n","random","valami","\n","\n","\n","masik","harmadik","\n","\n","ujabb","csoport","szoveg"]
lista2=["\n","random","valami","\n","\n","\n","masik","harmadik","\n","\n","ujabb","csoport","szoveg","\n","\n"]


def group_iterator(lista, separator="\n"):
	next_group=[]
	for i in lista:
		if i=="\n":
			if len(next_group)>0:
				yield next_group
			next_group=[]	
		else:
			next_group.append(i)
	if len(next_group)>0: yield next_group



elso=[ n for n in group_iterator(lista1) ]
masodik=[ n for n in group_iterator(lista1) ]


print elso
print masodik
