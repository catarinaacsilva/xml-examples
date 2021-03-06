# coding: utf-8


__author__ = 'Catarina Silva'
__version__ = '0.1'
__email__ = 'c.alexandracorreia@ua.pt'
__status__ = 'Development'

from valid_schema import validate
from xml_proc import read_xml, valid_doc

def menu():
    print("******************** MENU ********************")
    print("1 - Read xml file")
    print("2 - Validate xml file")
    print("0 - Sair")
    return input('Opção: ')

def main():
    file_xml = input("Insert name of file xml:")
    file_schema = input("Insert name of file schema:")

    op = menu()

    if op == '1':
        read_xml(file_xml)
    if op == '2':
        valid_doc(file_xml, file_schema)

main()