#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 14:23:14 2020

@author: marianam
"""
from FuncionesGrafo import *
import networkx as nx
  
on=1
IngresarGrafo()
while on==1:
    op=int(input('Menu\n1. Buscar la ruta más corta entre dos ciudades\n2. Buscar las ciudades que quedan en el centro\n3. Modificar el grafo\n4.Finalizar el programa'))
    if op==1:
        c1=input('Ingrese el nombre de la ciudad de origen')
        c2=input('Ingrese el nombre de la ciudad de destino')
        if c1 in nx.nodes(g) and c2 in nx.nodes(g):
            r,d=RutaCorta(c1,c2,g)  
            print('La distancia más corta entre ',c1,' y ',c2,' es de ',d,'por la siguiente ruta ',r)  
        else:
            print('Las ciudades que ingreso no son parte del grafo')        
    elif op==2:
        c=Centro(g)
        print('las ciudades en el centro son: ',c)
    elif op==3:
        op2=int(input('1. Informar de interrupción de tráfico entre un par de ciudades\n2. Establecer conexión entre dos ciudades'))
        if op2==1:
            c1=input('Ingrese el nombre de la ciudad de origen')
            c2=input('Ingrese el nombre de la ciudad de destino')
            if c1 in nx.nodes(g) and c2 in nx.nodes(g):
                g=InterTraf(c1,c2,g)
                print('Se ha eliminado la ruta entre ',c1,' y ',c2)
            else:
                print('Las ciudades que ingreso no son parte del grafo')        
        elif op2==2:
            c1=input('Ingrese el nombre de la ciudad de origen')
            c2=input('Ingrese el nombre de la ciudad de destino')
            d=int(input('Ingrese la distancia entre las dos ciudades'))
            AgregConex(c1,c2,d,g)
            print('Se ha ingresado la ruta entre ',c1,' y ',c2)
        else:
            print('Ingrese una opción valida')
    elif op==4:
        on=0
    else:
        print('Ingrese una opción valida')
