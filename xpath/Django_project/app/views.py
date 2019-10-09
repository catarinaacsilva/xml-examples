from django.shortcuts import render

import xml.etree.ElementTree as ET
from django.http import HttpRequest, HttpResponse
from django.template import loader

def index(request):
	return render(request, 'index.html')

# return a dictionary:
#   key : name
#   value: guid
def info_cursos_xml_dic(xml_file: str):
    dic = {}
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for curso in root.findall('curso'):
        dic.update({curso.find('nome').text : curso.find('guid').text})
    return dic

# return a dictionary:
#   key : name
#   value: codigo
def info_codigo_xml_dic(xml_file: str):
    dic = {}
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for curso in root.findall('curso'):
        dic.update({curso.find('nome').text : curso.find('codigo').text})
    return dic

# return a dictionary:
#   key : name
#   value: grau
def info_grau_xml_dic(xml_file: str):
    dic = {}
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for curso in root.findall('curso'):
        dic.update({curso.find('nome').text : curso.find('grau').text})
    return dic

#show name of cursos xml file
def show_cursos(request):
    template = loader.get_template('show_info.html')

    context = {
            'info': info_cursos_xml_dic('cursos.xml'),
    }
    return HttpResponse(template.render(context, request))

def show_details(request):
    template = loader.get_template('details.html')

    value = request.GET.get('item')

    context = {
        'nome': ,
        #'codigo': codigo,
        #'grau': grau,
        #'departamento': departamento,
        #'areaCientifica': areaCientifica,
        #'local': local
    }
    return HttpResponse(template.render(context, request))
