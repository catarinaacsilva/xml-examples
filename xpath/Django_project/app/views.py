import xml.etree.ElementTree as ET

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def index(request):
    return render(request, 'index.html')


# show name of cursos xml file
def show_cursos(request):
    template = loader.get_template('show_info.html')

    dic = {}
    tree = ET.parse('cursos.xml')
    root = tree.getroot()
    for c in root.findall('curso'):
        dic.update({c.find('nome').text: c.find('guid').text})

    context = {
        'info': dic,
    }
    return HttpResponse(template.render(context, request))


def get_curso(xml_file: str, value: str):
    dic = {}
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for c in root.findall('curso'):
        if c.find("guid").text == value:
            #TODO: porque funciona assim...................
            departamentos = []
            for d in c.find('departamentos').findall("departamento"):
                departamentos.append(d.text)
            areasCientificas = []
            for a in c.find('areascientificas').findall("areacientifica"):
                areasCientificas.append(a.text)
            dic = {
                'nome': c.find('nome').text,
                'codigo': c.find('codigo').text,
                'grau': c.find('grau').text,
                'departamento': departamentos,
                'areaCientifica': areasCientificas,
                'local': c.find('local').text
            }
            break
    return dic


def show_details(request):
    template = loader.get_template('details.html')
    value = request.GET.get('item')
    context = get_curso("cursos.xml", value)
    return HttpResponse(template.render(context, request))


def show_grau(request):
    template = loader.get_template('show_cursos_in.html')
    grau = request.GET.get('grau_nome')

    graus=[]

    tree = ET.parse('cursos.xml')
    root = tree.getroot()
    for c in root.findall('curso'):
        if c.find('grau').text == grau:
            graus.append(c.find('nome').text)

    return HttpResponse(template.render({'graus':graus}, request))

