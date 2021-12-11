[!NOCODE!][!//
/**
*   @file    Dio_VersionCheck_Src.m
*   @version 1.0.2
*
*   @brief   AUTOSAR Dio - version check macro.
*   @details Version checks.
*
*   @addtogroup DIO
*   @{
*/
/*==================================================================================================
*   Project              : AUTOSAR 4.2 MCAL
*   Platform             : ARM
*   Peripheral           : GPIO
*   Dependencies         : none
*
*   Autosar Version      : 4.2.2
*   Autosar Revision     : ASR_REL_4_2_REV_0002
*   Autosar Conf.Variant :
*   SW Version           : 1.0.2
*   Build Version        : S32K14xS32K14X_MCAL_1_0_2_RTM_ASR_REL_4_2_REV_0002_20190426
*
*   (c) Copyright 2006-2016 Freescale Semiconductor, Inc. 
*       Copyright 2017-2019 NXP
*   All Rights Reserved.
==================================================================================================*/
/*==================================================================================================
==================================================================================================*/

[!/* avoid multiple inclusion */!]
[!IF "not(var:defined('DIO_VERSIONCHECK_SRC_M'))"!]
[!VAR "DIO_VERSIONCHECK_SRC_M"="'true'"!]
[!VAR "DIO_AR_RELEASE_MAJOR_VERSION_TEMPLATE"="4"!][!//
[!VAR "DIO_AR_RELEASE_MINOR_VERSION_TEMPLATE"="2"!][!//
[!VAR "DIO_AR_RELEASE_REVISION_VERSION_TEMPLATE"="2"!][!//
[!VAR "DIO_SW_MAJOR_VERSION_TEMPLATE"="1"!][!//
[!VAR "DIO_SW_MINOR_VERSION_TEMPLATE"="0"!][!//
[!VAR "DIO_SW_PATCH_VERSION_TEMPLATE"="2"!][!//

[!SELECT "CommonPublishedInformation"!][!//

[!IF "not(num:i(ArReleaseMajorVersion) = num:i($DIO_AR_RELEASE_MAJOR_VERSION_TEMPLATE))"!]
    [!ERROR!]
        "AUTOSAR release major version number of the Basic Software Module Description file (Dio.epd version [!"ArReleaseMajorVersion"!]) and the Code template file (Dio_Cfg.c version [!"num:i($DIO_AR_RELEASE_MAJOR_VERSION_TEMPLATE)"!]) are different"
    [!ENDERROR!]
[!ENDIF!]
[!IF "not(num:i(ArReleaseMinorVersion)  = num:i($DIO_AR_RELEASE_MINOR_VERSION_TEMPLATE))"!]
    [!ERROR!]
        "AUTOSAR release minor version number of the Basic Software Module Description file (Dio.epd version [!"ArReleaseMinorVersion"!]) and the Code template file (Dio_Cfg.c version [!"num:i($DIO_AR_RELEASE_MINOR_VERSION_TEMPLATE)"!]) are different"
    [!ENDERROR!]
[!ENDIF!]
[!IF "not(num:i(ArReleaseRevisionVersion)  = num:i($DIO_AR_RELEASE_REVISION_VERSION_TEMPLATE))"!]
    [!ERROR!]
        "AUTOSAR release revision version number of the Basic Software Module Description file (Dio.epd version [!"ArReleaseRevisionVersion"!]) and the Code template file (Dio_Cfg.c version [!"num:i($DIO_AR_RELEASE_REVISION_VERSION_TEMPLATE)"!]) are different"
    [!ENDERROR!]
[!ENDIF!]
[!IF "not(num:i(SwMajorVersion) = num:i($DIO_SW_MAJOR_VERSION_TEMPLATE))"!]
    [!ERROR!]
        "The software major number of the Basic Software Module Description file (Dio.epd version [!"SwMajorVersion"!]) and the Code template file (Dio_Cfg.c version [!"num:i($DIO_SW_MAJOR_VERSION_TEMPLATE)"!]) are different"
    [!ENDERROR!]
[!ENDIF!]
[!IF "not(num:i(SwMinorVersion) = num:i($DIO_SW_MINOR_VERSION_TEMPLATE))"!]
    [!ERROR!]
        "The software minor number of the Basic Software Module Description file (Dio.epd version [!"SwMinorVersion"!]) and the Code template file (Dio_Cfg.c version [!"num:i($DIO_SW_MINOR_VERSION_TEMPLATE)"!]) are different"
    [!ENDERROR!]
[!ENDIF!]
[!IF "not(num:i(SwPatchVersion) = num:i($DIO_SW_PATCH_VERSION_TEMPLATE))"!]
    [!ERROR!]
        "The software patch number of the Basic Software Module Description file (Dio.epd version [!"SwPatchVersion"!]) and the Code template file (Dio_Cfg.c version [!"num:i($DIO_SW_PATCH_VERSION_TEMPLATE)"!]) are different"
    [!ENDERROR!]
[!ENDIF!]
[!ENDSELECT!][!//

[!ENDIF!][!// avoid multiple inclusion ENDIF
[!ENDNOCODE!][!//
