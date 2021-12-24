from jinja2 import Environment, FileSystemLoader
from xml_parse import *

ChannelGroupIndex = 0

DioInfo = {
    "DEFINITION-REF": "/TS_T40D2M10I2R0/Dio",
    "IMPLEMENTATION-CONFIG-VARIANT": "VARIANT-PRE-COMPILE",
    "SHORT-NAME": "Dio",
    'AvailablePortPinsForWrite': ['0x0003FFFF', '0x0003FFFF', '0x0003FFFF', '0x0003FFFF', '0x0001FFFF'],
    'AvailablePortPinsForRead': ['0x0003FFFF', '0x0003FFFF', '0x0003FFFF', '0x0003FFFF', '0x0001FFFF'],
    'AvailablePortPinsForReadReversedBits': ['0xFFFFC000', '0xFFFFC000', '0xFFFFC000', '0xFFFFC000', '0xFFFF8000'],
    'AvailablePortPinsForWriteReversedBits': ['0xFFFFC000', '0xFFFFC000', '0xFFFFC000', '0xFFFFC000', '0xFFFF8000'],
    'InOutConfigSupported': False
}

Dio = load_DIO_config('arxml/MCAL_config.arxml')


def inttohex(num, zfillnum=0):
    return '0x' + ('%x'%num).zfill(zfillnum)

def get_ChannelGroupIndex():
    global ChannelGroupIndex
    ret = ChannelGroupIndex
    ChannelGroupIndex += 1
    return ret

def get_numChannelGroupsInConfig():
    global Dio
    ret = 0
    for port in Dio['DioConfig']:
        ret += len(port['DioChannelGroup'])
    return ret

def get_mask_offset(ChannelGroup):
    global Dio
    Orig_mask = ChannelGroup['DioPortMask']
    Orig_offset = ChannelGroup['DioPortOffset']
    if Dio['DioGeneral']['DioReversePortBits']:
        pass
    else:
        ret_mask = ChannelGroup['DioPortMask']
    ret_offset = ChannelGroup['DioPortOffset']
    return ret_offset, ret_mask

    


file_loader = FileSystemLoader('templates')
env = Environment(autoescape=True, loader=file_loader)


env.trim_blocks = True
env.lstrip_blocks = True
env.rstrip_blocks = True
env.filters['inttohex'] = inttohex


file_names = ['Dio_Cfg.h', 'Dio_Cfg.c']
for file_name in file_names:
    ChannelGroupIndex = 0
    template = env.get_template(file_name)
    template.globals['inttohex'] = inttohex
    template.globals['get_ChannelGroupIndex'] = get_ChannelGroupIndex
    template.globals['get_numChannelGroupsInConfig'] = get_numChannelGroupsInConfig
    template.globals['get_mask_offset'] = get_mask_offset

    with open('generate/%s'%file_name, 'w') as f:
        f.write(template.render(DioInfo=DioInfo, Dio=Dio))
        print('[OK] Generate %s'%file_name)