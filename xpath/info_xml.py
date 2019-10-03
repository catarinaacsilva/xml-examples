# coding: utf-8


__author__ = 'Catarina Silva'
__version__ = '0.1'
__email__ = 'c.alexandracorreia@ua.pt'
__status__ = 'Development'

import xml.etree.ElementTree as ET

def info_cursos_xml(xml_file: str):
    lista = []
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for curso in root.findall('curso'):
        lista.append(curso.find('nome').text)
    return lista
        

print(info_cursos_xml('cursos.xml'))




