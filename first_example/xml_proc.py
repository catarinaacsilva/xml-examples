# coding: utf-8


__author__ = 'Catarina Silva'
__version__ = '0.1'
__email__ = 'c.alexandracorreia@ua.pt'
__status__ = 'Development'


from valid_schema import validate


def read_xml(file_xml: str):
    xml_file = open(file_xml, 'r')
    xml_file.read()

def valid_doc(file_xml: str, file_schema: str):
    validate(file_xml, file_schema)
