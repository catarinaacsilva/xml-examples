from django.shortcuts import render

import xml.etree.ElementTree as ET
from django.http import HttpRequest, HttpResponse


def info_cursos_xml(xml_file: str):
    lista = []
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for curso in root.findall('curso'):
        lista.append(curso.find('nome').text)
    return lista


def show_cursos(request):
    return HttpResponse(info_cursos_xml('cursos.xml'))

