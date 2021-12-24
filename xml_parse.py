import xmlschema
from lxml import etree as ET
import json

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

def convert_para_type(data, para_type):
    if para_type == 'ECUC-NUMERICAL-PARAM-VALUE':
        return int(data)
    else:
        print('data type [%s] not supported'%para_type)
        return data

def sub_container_recurrsive():
    pass

arxml_file = 'arxml/MCAL_config.arxml'

if validate_arxml(arxml_file):
    print('[OK] Validation pass: %s'%arxml_file)
else:
    exit()


tree = ET.parse(arxml_file)
root = tree.getroot()
nsmap = root.nsmap

mod_pkg = get_target_ARPackage('Dio')
DioInfo = {}
Dio = {}

if mod_pkg != None:
    elements = mod_pkg.find('.//ELEMENTS/', nsmap)
    for el in elements:
        if len(el) == 0:
            DioInfo[el.tag[el.tag.rfind('}')+1:]] = el.text

    containers = mod_pkg.findall('.//CONTAINERS/ECUC-CONTAINER-VALUE', nsmap)
    for container in containers:
        cont_name = container.find('./SHORT-NAME', nsmap).text

        if cont_name == 'DioGeneral':
            paras = container.findall('./PARAMETER-VALUES/', nsmap)
            if len(paras) > 0:
                Dio[cont_name] = {}
                for para in paras:
                    para_type = para.tag[para.tag.rfind('}')+1:]
                    key, value = para.findall('./')
                    Dio[cont_name][key.text[key.text.rfind('/')+1:]] = convert_para_type(value.text, para_type)
        elif cont_name == 'DioConfig':
            DioPorts = container.findall('./SUB-CONTAINERS/ECUC-CONTAINER-VALUE', nsmap)
            Dio[cont_name] = []
            for DioPort in DioPorts:
                PortDict = {}
                PortDict['name'] = DioPort.find('./SHORT-NAME', nsmap).text
                PortDict['DioPortId'] = int(DioPort.find('./PARAMETER-VALUES/ECUC-NUMERICAL-PARAM-VALUE/VALUE', nsmap).text)
                
                DioChannels = DioPort.find('./SUB-CONTAINERS', nsmap)
                PortDict['DioChannel'] = []
                PortDict['DioChannelGroup'] = []

                for DioChannel in DioChannels:
                    DefRef = DioChannel.find('./DEFINITION-REF', nsmap).text.split('/')
                    ChannelDict = {}
                    ChannelDict['name'] = DioChannel.find('./SHORT-NAME', nsmap).text
                    ChannelParas = DioChannel.find('./PARAMETER-VALUES', nsmap)
                    for ChannelPara in ChannelParas:
                        ParaType = ChannelPara.tag[ChannelPara.tag.find('}')+1:]
                        ParaName = ChannelPara.find('./DEFINITION-REF', nsmap).text.split('/')[-1]
                        ParaValue = ChannelPara.find('./VALUE', nsmap).text
                        if ParaType == 'ECUC-TEXTUAL-PARAM-VALUE':
                            ChannelDict[ParaName] = ParaValue
                        elif ParaType == 'ECUC-NUMERICAL-PARAM-VALUE':
                            ChannelDict[ParaName] = int(ParaValue)

                    PortDict[DefRef[-1]].append(ChannelDict)
                Dio[cont_name].append(PortDict)
 
        else:
            paras = container.findall('./PARAMETER-VALUES/', nsmap)
            if len(paras) > 0:
                Dio[cont_name] = {}
                for para in paras:
                    para_type = para.tag[para.tag.rfind('}')+1:]
                    key, value = para.findall('./')
                    Dio[cont_name][key.text[key.text.rfind('/')+1:]] = convert_para_type(value.text, para_type)

        

#print(json.dumps(DioInfo, indent=4, sort_keys=True) )
print(json.dumps(Dio, indent=4, sort_keys=True) )
