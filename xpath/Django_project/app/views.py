from django.shortcuts import render

import xml.etree.ElementTree as ET
from django.http import HttpRequest, HttpResponse

def cursos(xml_file: str):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for curso in root.findall('curso'):
        nome = curso.find('nome').text
        return nome

def show_cursos(request):
    assert isinstance(request, HttpRequest)
    if 'xml' in request.POST:
        xml = request.POST['xml']
        if xml:
            return render(request, 'send_results.html',{
                'xml': xml,
                'response': cursos(xml)
            })


