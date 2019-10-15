import xml.etree.ElementTree as ET
import lxml.etree as LET
import requests
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
    template = loader.get_template('show_cursos_grau.html')
    grau = request.GET.get('grau_nome')

    graus=[]

    tree = ET.parse('cursos.xml')
    root = tree.getroot()
    for c in root.findall('curso'):
        if c.find('grau').text == grau:
            graus.append(c.find('nome').text)

    return HttpResponse(template.render({'graus':graus}, request))

def show_departamento(request):
    template = loader.get_template('show_cursos_dep.html')
    departamento = request.GET.get('departamento_nome')
    departamentos = []

    tree = ET.parse('cursos.xml')
    root = tree.getroot()
    for c in root.findall('curso'):
        for d in c.find('departamentos').findall("departamento"):
            if d.text == departamento:
                departamentos.append(c.find('nome').text)

    return HttpResponse(template.render({'departamento': departamentos}, request))


def show_areacientifica(request):
    template = loader.get_template('show_cursos_areas.html')
    areacientifica = request.GET.get('areaCientifica_nome')
    areascientificas = []

    tree = ET.parse('cursos.xml')
    root = tree.getroot()
    for c in root.findall('curso'):
        for a in c.find('areascientificas').findall("areacientifica"):
            if a.text == areacientifica:
                areascientificas.append(c.find('nome').text)

    return HttpResponse(template.render({'areacientifica': areascientificas}, request))

def show_local(request):
    template = loader.get_template('show_cursos_local.html')
    local = request.GET.get('local_nome')

    locais=[]

    tree = ET.parse('cursos.xml')
    root = tree.getroot()
    for c in root.findall('curso'):
        if c.find('local').text == local:
            locais.append(c.find('nome').text)

    return HttpResponse(template.render({'locais':locais}, request))

def all_departamentos(request):
    template = loader.get_template('all_information.html')

    lista = []
    tree = ET.parse('cursos.xml')
    root = tree.getroot()
    for d in root.findall('curso/departamentos'):
        lista.append(d.find('departamento').text)

    context = {
        'all': lista
    }

    return HttpResponse(template.render(context, request))

#TODO remove repeated elements
def all_areascientificas(request):
    template = loader.get_template('all_information.html')

    lista = []
    tree = ET.parse('cursos.xml')
    root = tree.getroot()
    for d in root.findall('curso/areascientificas'):
        lista.append(d.find('areacientifica').text)
        #for i in lista:
            #elem = d.find('areacientifica').text
            #remove repeated elements
            #if not i == elem:
                #lista.append(elem)

    context = {
        'all': lista
    }

    return HttpResponse(template.render(context, request))


#TODO remove repeated elements
def all_locals(request):
    template = loader.get_template('all_information.html')

    lista = []
    tree = ET.parse('cursos.xml')
    root = tree.getroot()
    for d in root.findall('curso'):
        lista.append(d.find('local').text)

    context = {
        'all': lista
    }

    return HttpResponse(template.render(context, request))

# after show info about curso is possible to see more about it
def more_info_curso(request):
    response = requests.get('http://acesso.ua.pt/xml//cursos.v5.asp?')
    if response.status_code == 200:
        receive = LET.fromstring(response.content)
        xslt = LET.parse('xslt_file.xsl')
        transform = LET.XSLT(xslt)
        newreceive = transform(receive)
        content = LET.tostring(newreceive, pretty_print=True)
        return HttpResponse(content)

    return HttpResponse("Error")

