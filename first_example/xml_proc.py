# coding: utf-8


__author__ = 'Catarina Silva'
__version__ = '0.1'
__email__ = 'c.alexandracorreia@ua.pt'
__status__ = 'Development'



def read_xml(file: str):
    path = 'doc_xml/'+file
    xml_file = open(path, 'r')
    xml_file.read()



