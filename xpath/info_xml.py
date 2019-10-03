import xml.etree.ElementTree as ET

def info_cursos_xml(xml_file: str):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for curso in root.findall('curso'):
        nome = curso.find('nome').text
        return nome

