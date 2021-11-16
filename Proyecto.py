import os
from typing import Text
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, Comment, ElementTree

def prettify(elem):
    from xml.etree import ElementTree
    from xml.dom import minidom
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

def leerXML(fichero):
    arbol = ET.parse(fichero)
    root = arbol.getroot()
    return root

def buscar(lib,tit):
    pos = 0
    for libro in lib:
        if(libro[0].text==tit):
            return pos
        pos += 1
    return -1

def alta():
    if(os.path.exists('Libreria.xml')):
        tree = leerXML("Libreria.xml")
    else:
        tree = Element("Libreria")

    titulo = input("Titulo\n")
    autor = input("Autor\n")
    generoAutor = input("H/M\n")
    edad = input("Edadn")
    genero = input("Genero\n")
    anio = input("Año de publicacion\n")

    libro = ET.Element('libro')
    tit = ET.SubElement(libro, 'titulo')
    tit.text = titulo
    aut = ET.SubElement(libro, 'autor',{'Genero':generoAutor,'Edad':edad})
    aut.text = autor
    gen = ET.SubElement(libro, 'genero')
    gen.text = genero
    a = ET.SubElement(libro, 'anio')
    a.text = anio
    tree.append(libro)

    salida = prettify(tree)
    file = open("Libreria.xml","w")
    file.write(salida)
    file.close()

def modificar():
    tree = leerXML("Libreria.xml")
    libro = input("Titulo del libro a modificar")
    anio = input("Introduce el nuevo año de publicacion:\n")
    pos = buscar(tree,libro)
    if(pos!=-1):
	    tree[pos][3].text = str(anio)
    else:
	    print("Libro no encontrado")
    salida = prettify(tree)
    file = open("Libreria.xml","w")
    file.write(salida)
    file.close()

print("EMPEZAMOS")

alta()

print("FIN")
