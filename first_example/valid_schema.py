# coding: utf-8


__author__ = 'Catarina Silva'
__version__ = '0.1'
__email__ = 'c.alexandracorreia@ua.pt'
__status__ = 'Development'


import sys
from lxml import etree
from io import StringIO

def validate(file_xml: str, file_schema: str):
    #parsing xsd 
    with open(file_schema, 'r') as schema_file:
        xmlschema_doc = etree.parse(schema_file)
        xmlschema = etree.XMLSchema(xmlschema_doc)
    
        #parsing xml
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

    
        
        #validate schema
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
    

    

validate("mect.xml", "curso.xsd")




