from jinja2 import Environment, FileSystemLoader

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

Dio = {
    "CommonPublishedInformation": {
        "ArReleaseMajorVersion": 4,
        "ArReleaseMinorVersion": 2,
        "ArReleaseRevisionVersion": 2,
        "ModuleId": 120,
        "SwMajorVersion": 1,
        "SwMinorVersion": 0,
        "SwPatchVersion": 2,
        "VendorId": 43
    },
    "DioConfig": [
        {
            "DioChannel": [
                {
                    "DioChannelId": 13,
                    "name": "Dio_SWT_CCW"
                },
                {
                    "DioChannelId": 12,
                    "name": "Dio_SWT_CW"
                }
            ],
            "DioChannelGroup": [
                {
                    "DioChannelGroupIdentification": "DioChannelGroup",
                    "DioPortBitNumber": 1,
                    "DioPortMask": 1,
                    "DioPortOffset": 0,
                    "name": "DioChannelGroup_0"
                }
            ],
            "DioPortId": 2,
            "name": "DioPort_PortC"
        },
        {
            "DioChannel": [
                {
                    "DioChannelId": 0,
                    "name": "Dio_RelayA"
                },
                {
                    "DioChannelId": 15,
                    "name": "Dio_RelayB"
                }
            ],
            "DioChannelGroup": [
                {
                    "DioChannelGroupIdentification": "DioChannelGroup2",
                    "DioPortBitNumber": 1,
                    "DioPortMask": 1,
                    "DioPortOffset": 0,
                    "name": "DioChannelGroup_1"
                },
                {
                    "DioChannelGroupIdentification": "DioChannelGroup3",
                    "DioPortBitNumber": 1,
                    "DioPortMask": 1,
                    "DioPortOffset": 0,
                    "name": "DioChannelGroup_2"
                }
            ],
            "DioPortId": 3,
            "name": "DioPort_PortD"
        }
    ],
    "DioGeneral": {
        "DioDevErrorDetect": 0,
        "DioEnableUserModeSupport": 0,
        "DioFlipChannelApi": 0,
        "DioMaskedWritePortApi": 0,
        "DioReadZeroForUndefinedPortPins": 0,
        "DioReversePortBits": 0,
        "DioVersionInfoApi": 0
    }
}


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

file_name = 'Dio_Cfg.h'
template = env.get_template(file_name)
template.globals['inttohex'] = inttohex
template.globals['get_ChannelGroupIndex'] = get_ChannelGroupIndex
template.globals['get_numChannelGroupsInConfig'] = get_numChannelGroupsInConfig
template.globals['get_mask_offset'] = get_mask_offset




with open('generate/%s'%file_name, 'w') as f:
    f.write(template.render(DioInfo=DioInfo, Dio=Dio))