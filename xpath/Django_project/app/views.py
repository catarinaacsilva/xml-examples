from django.shortcuts import render

import xml.etree.ElementTree as ET

def cursos(xml_file: str):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for curso in root.findall('curso'):
        nome = curso.find('nome').text
        return nome

def show_cursos(request):
    


