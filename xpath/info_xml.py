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

def info_cursos_xml_dic(xml_file: str):
    dic = {}
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for curso in root.findall('curso'):
        dic.update({curso.find('nome').text : curso.find('guid').text})
    return dic
        

print(info_cursos_xml_dic('cursos.xml'))




