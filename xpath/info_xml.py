import xml.etree.ElementTree as ET

def info_cursos_xml(xml_file: str):
    lista = []
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for curso in root.findall('curso'):
        lista.append(curso.find('nome').text)
    return lista
        

print(info_cursos_xml('cursos.xml'))




