from django.shortcuts import render

import xml.etree.ElementTree as ET
import requests
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
            'info': info_cursos_xml_dic('cursos.xml').keys(),
    }
    return HttpResponse(template.render(context, request))

def show_details(request, xml_file: str):
    template = loader.get_template('details.html')

    #vai buscar o numero da chave do link que foi inserida na url
    #TODO: arranjar uma forma do item associado à chave ser colocado no link

    # inserir o numero do item no link
    nome = request.GET.get('i')

    postData = {
        'j': nome.items()
    }

    requests.post(postData)

    context = {
        'nome': nome,
        #'codigo': codigo,
        #'grau': grau,
        #'departamento': departamento,
        #'areaCientifica': areaCientifica,
        #'local': local
    }
    return HttpResponse(template.render(context, request))
