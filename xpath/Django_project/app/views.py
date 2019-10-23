# coding: utf-8


__author__ = 'Catarina Silva'
__version__ = '0.1'
__email__ = 'c.alexandracorreia@ua.pt'
__status__ = 'Development'

import xml.etree.ElementTree as ET
import lxml.etree as LET #to use on xslt
import requests
import sys
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from lxml import etree
from io import StringIO


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
# Use xslt to transform xml in html page
#input:xml --> xslt generate html template --> show information
def more_info_curso():
    response = requests.get('http://acesso.ua.pt/xml//cursos.v5.asp?')
    if response.status_code == 200:
        receive = LET.fromstring(response.content)
        xslt = LET.parse('xslt_file.xsl')
        transform = LET.XSLT(xslt)
        newreceive = transform(receive)
        content = LET.tostring(newreceive, pretty_print=True)
        return HttpResponse(content)

    return HttpResponse("Error")

#validate a xml file with xml schema
def validate(file_xml: str, file_schema: str):
    # parsing xsd
    with open(file_schema, 'r') as schema_file:
        xmlschema_doc = etree.parse(schema_file)
        xmlschema = etree.XMLSchema(xmlschema_doc)

        # parsing xml
        with open(file_xml, 'r') as xml_file:
            try:
                doc = etree.parse(xml_file)
                print('XML well formed, syntax ok.')

            # check for file IO error
            except IOError:
                print('Invalid File')

            # check for XML syntax errors
            except etree.XMLSyntaxError as err:
                print('XML Syntax Error, see error_syntax.log')
                with open('error_syntax.log', 'w') as error_log_file:
                    error_log_file.write(str(err.error_log))
                quit()

            except:
                print('Unknown error, exiting.')
                quit()

        # validate against schema
        try:
            xmlschema.assertValid(doc)
            print('XML valid, schema validation ok.')

        except etree.DocumentInvalid as err:
            print('Schema validation error, see error_schema.log')
            with open('error_schema.log', 'w') as error_log_file:
                error_log_file.write(str(err.error_log))
            quit()

        except:
            print('Unknown error, exiting.')
            quit()

        # validate schema
        try:
            xmlschema.assertValid(doc)
            print('XML valid, schema validation ok.')

        except etree.DocumentInvalid as err:
            print('Schema validation error, see error_schema.log')
            with open('error_schema.log', 'w') as error_log_file:
                error_log_file.write(str(err.error_log))
            quit()

        except:
            print('Unknown error, exiting.')
            quit()



def write_info_xml(request):
    pass




