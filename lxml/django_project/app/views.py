# coding: utf-8


__author__ = 'Catarina Silva'
__version__ = '0.1'
__email__ = 'c.alexandracorreia@ua.pt'
__status__ = 'Development'

import xml.etree.ElementTree as ET
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from lxml import etree

def index(request):
    return render(request, 'index.html')

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


def validate(file_xml: str, file_schema: str):
    # parsing xsd
    with open(file_schema, 'r') as schema_file:
        xmlschema_doc = etree.parse(schema_file)
        xmlschema = etree.XMLSchema(xmlschema_doc)

        # parsing xml
        with open(file_xml, 'r') as xml_file:
            try:
                doc = etree.parse(xml_file)
                return 'OK'

            # check for file IO error
            except IOError:
                return 'NOK'

            # check for XML syntax errors
            except etree.XMLSyntaxError as err:
                print('XML Syntax Error, see error_syntax.log')
                with open('error_syntax.log', 'w') as error_log_file:
                    error_log_file.write(str(err.error_log))
                return 'NOK'

            except:
                print('Unknown error, exiting.')
                return 'NOK'



def show_departamento(request):
    template = loader.get_template('validate.html')
    return HttpResponse(template.render({'validate': validate('cursos.xml', 'curso.xsd')}, request))
