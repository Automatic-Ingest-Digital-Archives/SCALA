# SCALA SIP Structure

A SCALA/RODA-In SIP has the following general folder structure:

```
SIP
├───documentation
├───metadata
│   └───descriptive
├───representations
│   ├───rep1
│   |   └───data
|   └───...
└───schemas
```

**Documentation** - Additional files with information related to, but not part of the IP itself.

**Representations** - Rep1 (the ‘original representation’ of the IP) records the structure and contains all data files of the digital archive as it was originally submitted to the repository. There may be additional representations present in the SIP. These contain data and metadata representing the current/actual preservation state of the SIP.

**Schemas** - Contains documentation and validation information for all fields potentially used in any of the metadata files.

**METS.xml** - Contains data about the SIP' contents.

Example METS:
	
```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<mets xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:sip="https://DILCIS.eu/XML/METS/SIPExtensionMETS" xmlns="http://www.loc.gov/METS/" xmlns:csip="https://DILCIS.eu/XML/METS/CSIPExtensionMETS" xmlns:xlink="http://www.w3.org/1999/xlink" OBJID="uuid-a739678b-0cbc-44f9-871a-a17e1515ef25" LABEL="" TYPE="Mixed" csip:CONTENTINFORMATIONTYPE="MIXED" PROFILE="https://earkcsip.dilcis.eu/profile/E-ARK-CSIP.xml" xsi:schemaLocation="http://www.loc.gov/METS/ schemas/mets1_12.xsd http://www.w3.org/1999/xlink schemas/xlink.xsd https://dilcis.eu/XML/METS/CSIPExtensionMETS schemas/DILCISExtensionMETS.xsd https://dilcis.eu/XML/METS/SIPExtensionMETS schemas/DILCISExtensionSIPMETS.xsd">
    <metsHdr CREATEDATE="2022-02-07T11:30:51.270+01:00" LASTMODDATE="2022-02-07T11:30:51.270+01:00" RECORDSTATUS="NEW" csip:OAISPACKAGETYPE="SIP">
        <agent ROLE="CREATOR" TYPE="OTHER" OTHERTYPE="SOFTWARE">
            <name>RODA-in</name>
            <note csip:NOTETYPE="SOFTWARE VERSION">2.4.2</note>
        </agent>
        <agent ROLE="CREATOR" TYPE="INDIVIDUAL">
            <name>yo</name>
            <note csip:NOTETYPE="IDENTIFICATIONCODE">lo</note>
        </agent>
    </metsHdr>
    <dmdSec ID="uuid-01D02A51-4FED-4CB8-B04D-425490DBF46C" CREATED="2022-02-07T11:30:51.277+01:00" STATUS="CURRENT">
        <mdRef ID="scala.xml" LOCTYPE="URL" MDTYPE="EAD" MDTYPEVERSION="2002" xlink:type="simple" xlink:href="metadata/descriptive/scala.xml" MIMETYPE="text/xml" SIZE="820" CREATED="2022-02-07T11:30:51.277+01:00" CHECKSUM="13FA9ED8E6E14A285D7930DD366D9FF2491B538EE2AAC1AF50C2A046BCFED1BF" CHECKSUMTYPE="SHA-256"/>
    </dmdSec>
    <amdSec ID="uuid-7DE3A8CB-6307-4362-861D-9F1812083B10"/>
    <fileSec ID="uuid-89C1A210-76BC-4AB3-9A84-81A04E941A4D">
        <fileGrp ID="uuid-59295022-33ED-4E7A-98CA-A93E45BF3BA5" USE="Schemas">
            <file ID="ID-598A0278-3579-47EE-AD75-A392DDB439C9" MIMETYPE="application/octet-stream" SIZE="126644" CREATED="2022-02-07T11:30:51.290+01:00" CHECKSUM="2E35653E73A9B66E8796C3DBD24FE32B5037C055840126D9DB792752AC31080B" CHECKSUMTYPE="SHA-256">
                <FLocat xlink:type="simple" xlink:href="schemas/ead2002.xsd" LOCTYPE="URL"/>
            </file>
            <file ID="ID-066C83CC-44B2-41FF-9F92-25AA6652D7D7" MIMETYPE="application/octet-stream" SIZE="2038" CREATED="2022-02-07T11:30:51.290+01:00" CHECKSUM="B4A13747DDE7644122DC14DC7F7333FC51B12DE43039A73BA111A6E0E8204FCC" CHECKSUMTYPE="SHA-256">
                <FLocat xlink:type="simple" xlink:href="schemas/DILCISExtensionMETS.xsd" LOCTYPE="URL"/>
            </file>
            <file ID="ID-0FA4D90C-ED19-45EC-8700-B07DC082D436" MIMETYPE="application/octet-stream" SIZE="499" CREATED="2022-02-07T11:30:51.291+01:00" CHECKSUM="43AC3F08DBECB74C069D1687187A1AEAED800E77581FE0D418468AE3AD20EF86" CHECKSUMTYPE="SHA-256">
                <FLocat xlink:type="simple" xlink:href="schemas/DILCISExtensionSIPMETS.xsd" LOCTYPE="URL"/>
            </file>
            <file ID="ID-62AE9794-7924-4FDA-8251-C45076F81D17" MIMETYPE="application/octet-stream" SIZE="137125" CREATED="2022-02-07T11:30:51.291+01:00" CHECKSUM="5D18B2751C52D87A92D2D947F1FC7974C034E9B1CBB9869B48C138755CBA12DE" CHECKSUMTYPE="SHA-256">
                <FLocat xlink:type="simple" xlink:href="schemas/mets1_12.xsd" LOCTYPE="URL"/>
            </file>
            <file ID="ID-2522B182-C48B-47CC-A88D-95BD74DB68E7" MIMETYPE="application/octet-stream" SIZE="3180" CREATED="2022-02-07T11:30:51.291+01:00" CHECKSUM="F1F5BB6003165CDD8F6C1FCC32F8FD1F965E1681010F3B9806D9460BCFFA8A3C" CHECKSUMTYPE="SHA-256">
                <FLocat xlink:type="simple" xlink:href="schemas/xlink.xsd" LOCTYPE="URL"/>
            </file>
        </fileGrp>
        <fileGrp ID="uuid-2243526B-0162-4B26-A991-5A28BBCE7451" USE="Documentation">
            <file ID="ID-E397CAD3-6B24-4C5E-A7E7-2F2934F11A6F" MIMETYPE="text/plain" SIZE="666368" CREATED="2022-02-07T11:30:51.291+01:00" CHECKSUM="A90F3BE0FD953122DE37A1827293474CDC5E35595CB8CD46624089F0CF0212F8" CHECKSUMTYPE="SHA-256">
                <FLocat xlink:type="simple" xlink:href="documentation/PowerShell_transcript.LAPTOP-1R19714J.fA51FJDU.20210902142714.txt" LOCTYPE="URL"/>
            </file>
        </fileGrp>
        <fileGrp ID="uuid-0B4EA483-7DD5-4C27-84A9-F1E8298B78F6" USE="Representations/rep1">
            <file ID="ID-5FDF7FDF-AC72-4A22-BC8B-D1E3120685F7" MIMETYPE="text/xml" SIZE="4089" CREATED="2022-02-07T11:30:51.503+01:00" CHECKSUM="282B5600306A37CF83F14966839D95B05B7421B931FEBD32B05D028D1E802EA3" CHECKSUMTYPE="SHA-256">
                <FLocat xlink:type="simple" xlink:href="representations/rep1/METS.xml" LOCTYPE="URL"/>
            </file>
        </fileGrp>
    </fileSec>
    <structMap ID="uuid-586E5B7E-5CAA-4D79-B85C-BC4E9BF856A7" TYPE="PHYSICAL" LABEL="CSIP">
        <div ID="uuid-E6559315-1F5C-4766-BA4F-4A3208218929" LABEL="uuid-a739678b-0cbc-44f9-871a-a17e1515ef25">
            <div ID="uuid-77FE4DBB-3925-4EC6-A0A5-3BF98CD52F22" DMDID="uuid-01D02A51-4FED-4CB8-B04D-425490DBF46C" LABEL="Metadata"/>
            <div ID="uuid-CC70ACA1-AAEC-4AB5-8D4F-C299E63E363E" LABEL="Schemas">
                <fptr FILEID="uuid-59295022-33ED-4E7A-98CA-A93E45BF3BA5"/>
            </div>
            <div ID="uuid-CF7F638B-4229-4F2E-8C21-5D82DE5E3697" LABEL="Documentation">
                <fptr FILEID="uuid-2243526B-0162-4B26-A991-5A28BBCE7451"/>
            </div>
            <div ID="uuid-3036978E-78E9-4188-8377-236FAB128C77" LABEL="Representations/rep1">
                <mptr xlink:type="simple" xlink:href="representations/rep1/METS.xml" xlink:title="uuid-0B4EA483-7DD5-4C27-84A9-F1E8298B78F6" LOCTYPE="URL"/>
            </div>
        </div>
    </structMap>
</mets>
```
