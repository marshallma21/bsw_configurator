import xmlschema
from lxml import etree as ET
import glob

xmlschema.limits.MAX_MODEL_DEPTH = 100
xsd_path = 'AUTOSAR_MMOD_XMLSchema/AUTOSAR_4-2-2.xsd'
my_schema = xmlschema.XMLSchema(xsd_path)


def validate_arxml(arxml_file):
    try:
        my_schema.validate(arxml_file)
        return [True, 'Validation passed!']
    except xmlschema.XMLSchemaValidationError as e:
        return [False, str(e)]


def get_target_ARPackage(mod_name):
    global root, nsmap
    mod_list = []
    for mod_package in root.findall('./AR-PACKAGES/AR-PACKAGE', nsmap):
        if mod_package.find('./SHORT-NAME', nsmap).text == mod_name:
            return mod_package

    return None

arxml_file = 'arxml/MCAL_config.arxml'

if validate_arxml(arxml_file):
    print('[OK] Validation pass: %s'%arxml_file)
else:
    exit()


tree = ET.parse(arxml_file)
root = tree.getroot()
nsmap = root.nsmap

mod_pkg = get_target_ARPackage('Dio')

if mod_pkg != None:
    containers = mod_pkg.findall('.//CONTAINERS/ECUC-CONTAINER-VALUE', nsmap)
    for container in containers:
        print(container.find('./SHORT-NAME', nsmap).text)
