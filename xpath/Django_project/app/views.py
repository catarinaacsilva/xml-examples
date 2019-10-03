from django.shortcuts import render

import xml.etree.ElementTree as ET
from django.http import HttpRequest, HttpResponse
from django.template import loader


def info_cursos_xml(xml_file: str):
    lista = []
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for curso in root.findall('curso'):
        lista.append(curso.find('nome').text)
    return lista


def show_cursos(request):
    #return HttpResponse(info_cursos_xml('cursos.xml'))
    template = loader.get_template('show_info.html')
    context = {
        'info': info_cursos_xml(('cursos.xml')),
    }
    return HttpResponse(template.render(context, request))

