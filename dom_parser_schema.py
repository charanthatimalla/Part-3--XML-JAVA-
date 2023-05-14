


import xml.dom.minidom
import xml.dom
import xml.sax

def validate(xml_str, schema_file_path):
    try:
        schema_doc = xml.dom.minidom.parse(schema_file_path)
        schema = xml.dom.minidom.DocumentType(schema_doc.documentElement.tagName, '', '')
        schema.entities = schema_doc.entities
        schema_notation = schema_doc.notations
        handler = xml.sax.make_parser()
        handler.setFeature(xml.sax.handler.feature_namespaces, 1)
        validator = xml.sax.handler.ContentHandler()
        handler.setContentHandler(validator)
        handler.setEntityResolver(xml.sax.handler.EntityResolver())
        handler.setDTDHandler(xml.sax.handler.DTDHandler())
        handler.setErrorHandler(xml.sax.handler.ErrorHandler())
        handler.parse(xml_str)
        return True
    except Exception as e:
        print("Error: {}".format(e))
        return False









                                                                                                                                                                                                                                                                                   

