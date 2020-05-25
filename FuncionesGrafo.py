#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

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