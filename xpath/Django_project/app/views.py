from django.shortcuts import render

import xml.etree.ElementTree as ET
from django.http import HttpRequest, HttpResponse
from django.template import loader

def index(request):
	return render(request, 'index.html')

# return a dictionary:
#   key : name
#   value: guid
def info_cursos_xml_dic(xml_file: str, a: str, b:str, c: str):
    dic = {}
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for curso in root.findall(a):
        dic.update({curso.find(b).text : curso.find(c).text})
    return dic


# return a dictionary:
#   key : name
#   value: codigo
def info_codigo_xml_dic(xml_file: str):
    dic = {}
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for curso in root.findall('curso'):
        dic.update({curso.find('codigo').text : curso.find('guid').text})
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

    dic_cursos = info_cursos_xml_dic('cursos.xml')
    dic_codigo = info_codigo_xml_dic('cursos.xml')
    dic_grau = info_grau_xml_dic('cursos.xml')

    for i in dic_cursos.keys():
        if dic_cursos.get(i) == value:
            name = i

    for i in dic_codigo.keys():
        if dic_codigo.get(i) == value:
            codigo = i

    for i in dic_grau.keys():
        if dic_grau.get(i) == value:
            grau = i


    context = {
        'nome': name,
        'codigo': codigo,
        'grau': grau,
        #'departamento': departamento,
        #'areaCientifica': areaCientifica,
        #'local': local
    }
    return HttpResponse(template.render(context, request))
