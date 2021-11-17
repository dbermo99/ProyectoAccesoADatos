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

def mostrar():
    tree = leerXML("Libreria.xml")
    cont = 0

    for libro in tree:
        print("Libro:", cont)
        cont += 1
        for elemento in libro:
            print("\t", elemento.tag, ":", elemento.text)
    
def borrar():
    tree = leerXML("Libreria.xml")
    titulo = input("Introduce el titulo del libro que quieres borrar:")
    pos = buscar(tree,titulo)
    if (pos != -1):
        del (tree[pos])
        print(titulo, "borrado")
    else:
        print("Titulo no encontrado")
    opcion = input("Quieres borrar otro titulo?(si/otro)")
    while (opcion.upper() == "SI"):
        titulo = input("Introduce el titulo del libro que quieres borrar:")
        pos = buscar(tree, titulo)
        if (pos != -1):
            del (tree[pos])
            print(titulo, "borrado")
        else:
            print("Titulo no encontrado")
        opcion = input("Quieres borrar otro titulo?(si/otro)")

    salida = prettify(tree)
    file = open("Libreria.xml","w")
    file.write(salida)
    file.close()

def buscarLibro():
    tree = leerXML("Libreria.xml")
    titulo = input("Introduce el titulo del libro que quieres buscar:")
    pos = buscar(tree,titulo)
    for libro in tree:
        if(libro[0].text==titulo):
            print("Libro: ",pos)

def menu():
    op = ""
    while op != "0":
        op = input("Introduce una opcion:\n1-ALTA\n2-BAJA\n3-MODIFICAR\n4-BUSCAR\n5-MOSTRAR TODOS\n0-SALIR\n")
        if op == "1":
            alta()
        elif op == "2":
            borrar()
        elif op == "3":
            modificar()
        elif op == "4":
            buscar()
        elif op == "5":
            mostrar()
            
print("EMPEZAMOS")

menu()

print("FIN")
