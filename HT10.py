#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 14:23:14 2020

@author: marianam
"""
import networkx as nx

g = nx.DiGraph()
def RutaCorta(ciudad1,ciudad2,g):
    dist=0
    predecessors, _ = nx.floyd_warshall_predecessor_and_distance(g)
    ruta=nx.reconstruct_path(ciudad1, ciudad2, predecessors)
    for i in ruta:
        if i==ciudad1:
            j=i
        elif i==ciudad2:
            dist=g.get_edge_data(j,i)['weight']+dist
            return(ruta,dist)
        else:
            dist=g.get_edge_data(j,i)['weight']+dist
            j=i
    
def InterTraf(ciudad1,ciudad2,g):
    g.remove_edge(ciudad1,ciudad2)
    return(g)

def AgregConex(ciudad1,ciudad2,dist,g):
    g.add_edge(ciudad1,ciudad2,weight=dist)    
    return(g)
    
def Centro(g):
    return(nx.center(g))

def IngresarGrafo():
    file = open("guategrafo.txt","r+")
    for linea in file:
        h = linea.split(" ")
        ciudad1 = h[0]
        ciudad2 = h[1]
        dist = float(h[2])
        g.add_edge(ciudad1,ciudad2,weight=dist)
    file.close()     
  
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