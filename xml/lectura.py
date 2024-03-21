from xml.etree.ElementTree import parse, Element

archivo = 'Resultados_XML.xml'
doc_xml = parse(archivo)
raiz = doc_xml.getroot()
print(raiz)


# Remosion de elementos
raiz.remove(raiz.find('pasivos'))

# Insertar un nuevo element
