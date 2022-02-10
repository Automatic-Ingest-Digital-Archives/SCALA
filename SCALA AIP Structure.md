# SCALA AIP Structure

A SCALA/RODA AIP has the following general folder structure:

```
AIP
├───documentation
├───metadata
│   ├───descriptive
│   └───preservation
├───representations
│   ├───rep1
│   |   ├───data
│   |   └───metadata
│   |       ├───other
│   |       └───preservation
|   └───...
└───schemas
```

**Documentation** - Additional files with information related to, but not part of the IP itself.

**Representations** - Rep1 (the ‘original representation’ of the IP) records the structure and contains all data files of the digital archive as it was originally submitted to the repository. There may be additional representations present in the AIP. These contain data and metadata representing the current/actual preservation state of the AIP.

**Schemas** - Contains documentation and validation information for all fields potentially used in any of the metadata files.

**Aip.json / METS.xml** - Contains data about the AIP ingest process, its contents and any updates it has had.

AIP metadata will be explored in detail in the following segments.

###
<details><summary><b>METS structure</b></summary>
	
A RODA METS file contains following sections:
	
- **MetsHdr** containing references to all agents involved in making this METS file.
- **DmdSec** containing references to all descriptive metadata files.
- **AmdSec** containing references to digital provenance PREMIS events.
- **FileSec** containing references to all AIP data files and their technical information (e.g. checksum, creationdate, ...).
- **StructMap** containing references to the AIP data files and their original directory structure. Also includes potential references to ancestral AIPs.
	
Example METS:
	
```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<mets xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:sip="https://DILCIS.eu/XML/METS/SIPExtensionMETS" xmlns="http://www.loc.gov/METS/" xmlns:csip="https://DILCIS.eu/XML/METS/CSIPExtensionMETS" xmlns:xlink="http://www.w3.org/1999/xlink" OBJID="a83362bb-fc63-44a1-87e5-c28384f1441c" LABEL="" TYPE="Other" csip:OTHERTYPE="type" csip:CONTENTINFORMATIONTYPE="MIXED" PROFILE="NOT_DEFINED" xsi:schemaLocation="http://www.loc.gov/METS/ schemas/mets1_12.xsd http://www.w3.org/1999/xlink schemas/xlink.xsd https://dilcis.eu/XML/METS/CSIPExtensionMETS schemas/DILCISExtensionMETS.xsd https://dilcis.eu/XML/METS/SIPExtensionMETS schemas/DILCISExtensionSIPMETS.xsd">
    <metsHdr CREATEDATE="2022-01-06T12:35:53.636Z" LASTMODDATE="2022-01-06T12:35:53.636Z" RECORDSTATUS="NEW" csip:OAISPACKAGETYPE="AIP">
        <agent ROLE="CREATOR" TYPE="OTHER" OTHERTYPE="SOFTWARE">
            <name>RODA plugin: Create E-ARK AIP manifest files (METS.xml)</name>
            <note csip:NOTETYPE="SOFTWARE VERSION">1.0</note>
        </agent>
        <agent ROLE="OTHER" OTHERROLE="SUBMITTER" TYPE="INDIVIDUAL">
            <name>jelle</name>
            <note csip:NOTETYPE="IDENTIFICATIONCODE">jelle</note>
        </agent>
    </metsHdr>
    <dmdSec ID="uuid-14A2D5FD-3C4E-4B12-A55D-2AF56AF034FC" CREATED="2022-01-06T12:35:53.641Z" STATUS="CURRENT">
        <mdRef ID="scala.xml" LOCTYPE="URL" MDTYPE="EAD" MDTYPEVERSION="2002" xlink:type="simple" xlink:href="metadata/descriptive/scala.xml" MIMETYPE="application/xml" SIZE="722" CREATED="2022-01-06T12:35:53.641Z" CHECKSUM="0DFD82D617E31003BF8A303F31B67508D9FEB3456656E96FA3D0C84C3FEDEAAE" CHECKSUMTYPE="SHA-256"/>
    </dmdSec>
    <dmdSec ID="uuid-3787E1AD-BD22-4CF0-AED1-1FBCD83BF29F" CREATED="2022-01-06T12:35:53.643Z" STATUS="CURRENT">
        <mdRef ID="meemoo.xml" LOCTYPE="URL" MDTYPE="OTHER" OTHERMDTYPE="meemoo" xlink:type="simple" xlink:href="metadata/descriptive/meemoo.xml" MIMETYPE="application/xml" SIZE="423" CREATED="2022-01-06T12:35:53.643Z" CHECKSUM="10A00A9D53711B9E8783D088724690C6D18AFF4EE37F2C454F47CFEA002C729E" CHECKSUMTYPE="SHA-256"/>
    </dmdSec>
    <amdSec ID="uuid-BD81745F-ECB5-4285-8388-E7603B987830">
        <digiprovMD ID="uuid-C8480DE3-C780-4923-A52B-5A87289A0671" STATUS="CURRENT">
            <mdRef ID="urn_roda_premis_event_2c326297-86f8-4064-a92b-ac1fc882acbf" LOCTYPE="URL" MDTYPE="PREMIS" xlink:type="simple" xlink:href="metadata/preservation/urn:roda:premis:event:2c326297-86f8-4064-a92b-ac1fc882acbf.xml" MIMETYPE="application/xml" SIZE="1806" CREATED="2022-01-06T12:35:53.643Z" CHECKSUM="8DEFBA71679FBA4A390C8DC1ECB1A0DBD56D16A2E4D65AFC2632B216E7972A82" CHECKSUMTYPE="SHA-256"/>
        </digiprovMD>
        <digiprovMD ID="uuid-4DF3FA3D-9F11-4FEB-B59C-86509626430B" STATUS="CURRENT">
            <mdRef ID="urn_roda_premis_event_b0bb9a34-f27e-42a7-a147-152d32086616" LOCTYPE="URL" MDTYPE="PREMIS" xlink:type="simple" xlink:href="metadata/preservation/urn:roda:premis:event:b0bb9a34-f27e-42a7-a147-152d32086616.xml" MIMETYPE="application/xml" SIZE="1606" CREATED="2022-01-06T12:35:53.643Z" CHECKSUM="528A75B1202BB1BC49434F6415C011B83593F6CE4CE6A8F52EAE91150F6B0D3F" CHECKSUMTYPE="SHA-256"/>
        </digiprovMD>
        <digiprovMD ID="uuid-40DB8F69-4291-45DE-A8F0-044548729C89" STATUS="CURRENT">
            <mdRef ID="urn_roda_premis_event_b23d6159-5674-456e-848d-55942f8c187c" LOCTYPE="URL" MDTYPE="PREMIS" xlink:type="simple" xlink:href="metadata/preservation/urn:roda:premis:event:b23d6159-5674-456e-848d-55942f8c187c.xml" MIMETYPE="application/xml" SIZE="1922" CREATED="2022-01-06T12:35:53.643Z" CHECKSUM="90A8A9011A99AE414DC92448A459460B4A57482B89FD7010786C618338B04800" CHECKSUMTYPE="SHA-256"/>
        </digiprovMD>
        <digiprovMD ID="uuid-B3CCD3DE-99C9-4684-8742-2A6523393381" STATUS="CURRENT">
            <mdRef ID="urn_roda_premis_event_0be38b13-0a41-4363-87e7-7d6399097185" LOCTYPE="URL" MDTYPE="PREMIS" xlink:type="simple" xlink:href="metadata/preservation/urn:roda:premis:event:0be38b13-0a41-4363-87e7-7d6399097185.xml" MIMETYPE="application/xml" SIZE="1620" CREATED="2022-01-06T12:35:53.643Z" CHECKSUM="102BADB49B0617330CA75E3EBF135A3E74C819D70D056D9B2224793323958525" CHECKSUMTYPE="SHA-256"/>
        </digiprovMD>
        <digiprovMD ID="uuid-095C3B1B-B5F3-4F9F-BDE3-EA047CF95FDA" STATUS="CURRENT">
            <mdRef ID="urn_roda_premis_event_8494df17-e688-44d6-bfa0-6479479f4d4a" LOCTYPE="URL" MDTYPE="PREMIS" xlink:type="simple" xlink:href="metadata/preservation/urn:roda:premis:event:8494df17-e688-44d6-bfa0-6479479f4d4a.xml" MIMETYPE="application/xml" SIZE="1649" CREATED="2022-01-06T12:35:53.643Z" CHECKSUM="63C4309F7269D348CC531D650194CF8BEDD49B92519AA29AD0A4A451BF7BA7C8" CHECKSUMTYPE="SHA-256"/>
        </digiprovMD>
        <digiprovMD ID="uuid-5B621587-04F3-43FA-A2C2-23C08E38A10E" STATUS="CURRENT">
            <mdRef ID="urn_roda_premis_event_97eb6f0b-069a-44a1-9fc6-4632b7bb89f6" LOCTYPE="URL" MDTYPE="PREMIS" xlink:type="simple" xlink:href="metadata/preservation/urn:roda:premis:event:97eb6f0b-069a-44a1-9fc6-4632b7bb89f6.xml" MIMETYPE="application/xml" SIZE="1844" CREATED="2022-01-06T12:35:53.643Z" CHECKSUM="194CBA2986CAF19442F6306B1C15C8301584AF34A43451632312CF0E7BBA2A94" CHECKSUMTYPE="SHA-256"/>
        </digiprovMD>
        <digiprovMD ID="uuid-9D5FA319-69BD-41E4-82F8-0F6C2C033571" STATUS="CURRENT">
            <mdRef ID="urn_roda_premis_event_5b7031ae-9b1e-4af7-85b8-a7051e930c4b" LOCTYPE="URL" MDTYPE="PREMIS" xlink:type="simple" xlink:href="metadata/preservation/urn:roda:premis:event:5b7031ae-9b1e-4af7-85b8-a7051e930c4b.xml" MIMETYPE="application/xml" SIZE="1848" CREATED="2022-01-06T12:35:53.643Z" CHECKSUM="E009BB909489F17F9FE48190DAABA95E49B5577BFC17A13D8476502CDAF36FAC" CHECKSUMTYPE="SHA-256"/>
        </digiprovMD>
        <digiprovMD ID="uuid-16848C37-61BD-4442-BED8-526AA7E47F31" STATUS="CURRENT">
            <mdRef ID="urn_roda_premis_event_f5a65f78-25bd-4713-bc44-44531aca6530" LOCTYPE="URL" MDTYPE="PREMIS" xlink:type="simple" xlink:href="metadata/preservation/urn:roda:premis:event:f5a65f78-25bd-4713-bc44-44531aca6530.xml" MIMETYPE="application/xml" SIZE="1868" CREATED="2022-01-06T12:35:53.644Z" CHECKSUM="1167D4D27FCE4AD01AF7C39AC294DF8BA811CF867B1F7314DE486655232C3572" CHECKSUMTYPE="SHA-256"/>
        </digiprovMD>
        <digiprovMD ID="uuid-87C42E18-DC9A-46C3-B43E-D365D94D81AF" STATUS="CURRENT">
            <mdRef ID="urn_roda_premis_event_1816c07d-40b9-4315-a637-4cbfcdb4d679" LOCTYPE="URL" MDTYPE="PREMIS" xlink:type="simple" xlink:href="metadata/preservation/urn:roda:premis:event:1816c07d-40b9-4315-a637-4cbfcdb4d679.xml" MIMETYPE="application/xml" SIZE="1810" CREATED="2022-01-06T12:35:53.644Z" CHECKSUM="1A48C0DE71F2816FDCCBA6EDC77E5AACFEAD00AB106DA9CF4D64F6C504F93F42" CHECKSUMTYPE="SHA-256"/>
        </digiprovMD>
        <digiprovMD ID="uuid-196CE71E-632A-490C-A097-4DE24D3BE409" STATUS="CURRENT">
            <mdRef ID="urn_roda_premis_event_6a81f894-df3c-40f9-bcf9-14b4eeaee3f9" LOCTYPE="URL" MDTYPE="PREMIS" xlink:type="simple" xlink:href="metadata/preservation/urn:roda:premis:event:6a81f894-df3c-40f9-bcf9-14b4eeaee3f9.xml" MIMETYPE="application/xml" SIZE="1690" CREATED="2022-01-06T12:35:53.644Z" CHECKSUM="62359A3F01E4653EB960437786B7845C8F6C7F5C2159CB91B73D79FE0DB706C0" CHECKSUMTYPE="SHA-256"/>
        </digiprovMD>
    </amdSec>
    <fileSec ID="uuid-F48ED105-EDAC-4CFF-82C1-72C051A3DCDD">
        <fileGrp ID="uuid-1E47CA67-A6FF-46AC-8E6B-7FE94330FC20" USE="Schemas">
            <file ID="ID-0A902493-C499-44DC-A77F-0D890940C52F" MIMETYPE="application/xml" SIZE="3180" CREATED="2022-01-06T12:35:53.645Z" CHECKSUM="F1F5BB6003165CDD8F6C1FCC32F8FD1F965E1681010F3B9806D9460BCFFA8A3C" CHECKSUMTYPE="SHA-256">
                <FLocat xlink:type="simple" xlink:href="schemas/xlink.xsd" LOCTYPE="URL"/>
            </file>
            <file ID="ID-B612EC18-4583-49D7-9CC5-CEBBA12DE99A" MIMETYPE="application/xml" SIZE="137125" CREATED="2022-01-06T12:35:53.646Z" CHECKSUM="5D18B2751C52D87A92D2D947F1FC7974C034E9B1CBB9869B48C138755CBA12DE" CHECKSUMTYPE="SHA-256">
                <FLocat xlink:type="simple" xlink:href="schemas/mets1_12.xsd" LOCTYPE="URL"/>
            </file>
            <file ID="ID-63013D42-8BA3-4A57-84F6-2049ACBF703C" MIMETYPE="application/xml" SIZE="499" CREATED="2022-01-06T12:35:53.646Z" CHECKSUM="43AC3F08DBECB74C069D1687187A1AEAED800E77581FE0D418468AE3AD20EF86" CHECKSUMTYPE="SHA-256">
                <FLocat xlink:type="simple" xlink:href="schemas/DILCISExtensionSIPMETS.xsd" LOCTYPE="URL"/>
            </file>
            <file ID="ID-E14F8F5C-3954-40D1-B066-1EE0EE9EF815" MIMETYPE="application/xml" SIZE="2038" CREATED="2022-01-06T12:35:53.646Z" CHECKSUM="B4A13747DDE7644122DC14DC7F7333FC51B12DE43039A73BA111A6E0E8204FCC" CHECKSUMTYPE="SHA-256">
                <FLocat xlink:type="simple" xlink:href="schemas/DILCISExtensionMETS.xsd" LOCTYPE="URL"/>
            </file>
            <file ID="ID-962542F3-9B4D-41C2-9469-2714E3F43E41" MIMETYPE="application/xml" SIZE="126644" CREATED="2022-01-06T12:35:53.646Z" CHECKSUM="2E35653E73A9B66E8796C3DBD24FE32B5037C055840126D9DB792752AC31080B" CHECKSUMTYPE="SHA-256">
                <FLocat xlink:type="simple" xlink:href="schemas/ead2002.xsd" LOCTYPE="URL"/>
            </file>
        </fileGrp>
        <fileGrp ID="uuid-45370FF7-C844-46FF-8E2E-3CF7C052EA0E" USE="Representations/rep1">
            <file ID="ID-125EE487-F31B-4B17-97FF-BF11D29521BD" MIMETYPE="application/xml" SIZE="3568" CREATED="2022-01-06T12:35:53.657Z" CHECKSUM="7D7E9F250A0EC639139EB3ECC00E2C9505E8968CC7E088214E8FF75A8729836D" CHECKSUMTYPE="SHA-256">
                <FLocat xlink:type="simple" xlink:href="representations/rep1/METS.xml" LOCTYPE="URL"/>
            </file>
        </fileGrp>
    </fileSec>
    <structMap ID="uuid-CA4DB147-1434-4F2D-94A7-17F4E99A9EF7" TYPE="PHYSICAL" LABEL="CSIP">
        <div ID="uuid-BDD99930-0AF0-47FD-8EDA-62694C223743" LABEL="a83362bb-fc63-44a1-87e5-c28384f1441c">
            <div ID="uuid-EBD9F9A7-1D7F-44BC-A619-A2E0F34E8585" DMDID="uuid-14A2D5FD-3C4E-4B12-A55D-2AF56AF034FC uuid-3787E1AD-BD22-4CF0-AED1-1FBCD83BF29F" ADMID="uuid-C8480DE3-C780-4923-A52B-5A87289A0671 uuid-4DF3FA3D-9F11-4FEB-B59C-86509626430B uuid-40DB8F69-4291-45DE-A8F0-044548729C89 uuid-B3CCD3DE-99C9-4684-8742-2A6523393381 uuid-095C3B1B-B5F3-4F9F-BDE3-EA047CF95FDA uuid-5B621587-04F3-43FA-A2C2-23C08E38A10E uuid-9D5FA319-69BD-41E4-82F8-0F6C2C033571 uuid-16848C37-61BD-4442-BED8-526AA7E47F31 uuid-87C42E18-DC9A-46C3-B43E-D365D94D81AF uuid-196CE71E-632A-490C-A097-4DE24D3BE409" LABEL="Metadata"/>
            <div ID="uuid-E0B51ACD-B6A2-4DF0-A821-DDDD0A8A1E76" LABEL="Schemas">
                <fptr FILEID="uuid-1E47CA67-A6FF-46AC-8E6B-7FE94330FC20"/>
            </div>
            <div ID="uuid-0AD089CC-E193-4228-A95E-30267314AF5F" LABEL="Representations/rep1">
                <mptr xlink:type="simple" xlink:href="representations/rep1/METS.xml" xlink:title="uuid-45370FF7-C844-46FF-8E2E-3CF7C052EA0E" LOCTYPE="URL"/>
            </div>
        </div>
    </structMap>
    <structMap ID="uuid-E6B5BC1C-E66C-41EB-9438-A0A717C5D5A9" LABEL="RODA structural map">
        <div ID="uuid-13CE3726-B227-4A00-872C-56A5821FFBCC" LABEL="RODA">
            <div ID="uuid-8597A700-7B0E-495E-AAC4-EC5403395CCE" LABEL="Ancestors">
                <mptr xlink:type="simple" xlink:href="6c63fb22-ca07-4912-b559-6bc127aa7e1b" LOCTYPE="HANDLE"/>
            </div>
        </div>
    </structMap>
</mets>	
```
	
Parent AIPs are referenced in a structMap element in the METS. It is a little different from [E-ARK's proposition](https://earkaip.dilcis.eu/#childaipreferencesparentaip).
![image](https://user-images.githubusercontent.com/87436774/146341721-1cc44b69-88f6-40aa-9d02-c2a08a929107.png)

</details>
	
##
<details><summary><b>Descriptive metadata in AIP</b></summary>

`description.xml` contains a minimal set of essential metadata to be archived within the AIP. SCALA departs from the assumption that an up to date and more elaborate version of the descriptive metadata is managed and stored within the partners' archives management system. The following EAD-sample gives an overview of all metadatafields. They can be automatically generated or must be provided using Roda-in.
  
```XML
<?xml version="1.0" encoding="UTF-8"?>
<ead xmlns="urn:isbn:1-931666-22-9"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="urn:isbn:1-931666-22-9 http://www.loc.gov/ead/ead.xsd">
    <eadheader>
        <eadid/>
        <filedesc>
            <titlestmt>
                <titleproper/>
            </titlestmt>
        </filedesc>
        <profiledesc>
            <creation>
                Generated by RODA-IN 2.0
            </creation>
        </profiledesc>
    </eadheader>
    <archdesc level="file"> <!-- a description level. Can have different values from a controlled vocab -->
        <did>
		<unittitle>aanwinst van ABVV</unittitle> <!-- the title of the archive -->
		<unitid repositorycode="BE-471084" label="localID">collectie12345</unitid> <!-- repositorycode is an ISIL code, optional | localID is the institution's inventory number -->
		<unitid label="original_filepath">path/to/file.ext</unitid> <!-- If the AIP is on item-level, this contains the relative path relative from the parent AIP https://www.w3schools.com/html/html_filepaths.asp -->
            	<unitdate>1999-08-10/2005-09-30</unitdate> <!-- Roda-in must have a precision on day-level -->
            	<repository>
                	<corpname>AMSAB-ISG</corpname> <!-- The repository name. Can have different values from a controlled vocab -->
            	</repository>
            	<origination label="creator">
                	<name>ABVV</name> <!-- The archive creator -->
            	</origination>
            	<origination label="producer">
                	<name>AIDA</name> <!-- Is always AIDA -->
            	</origination>
        </did>
        <scopecontent>
            <p>collectie van een aantal digitale dragers, uit de bureau's van een aantal medewerkers</p>
        </scopecontent>
        <accessrestrict>
            <p>niet-raadpleegbaar</p> <!-- Information about access restriction. It's just a string -->
        </accessrestrict>
        <dsc type="combined">  
        </dsc>
    </archdesc>
</ead>
```
</details>

###
<details><summary><b>Descriptive metadata in meemoo</b></summary>	

During the AIP's submission to meemoo, a meemoo sidecar XML is generated containing essential descriptive metadata necessary for meemoo. The following XML-sample gives an overview of all metadatafields. It is automatically generated by RODA, but stored in the meemoo MAM. The source of the metadata values is being given in the sample's comments.
	
```XML
<?xml version="1.0" encoding="UTF-8"?>
<VIAA xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/"> <!--meemoo sidecar-->
	<CP>AMSAB-IG</CP> <!--Source: descriptive metadata ead/archdesc/did/repository/corpname-->
	<CP_id>OR-jq0st8z</CP_id> <!--OR-ID (source?)-->
	<dc_title>aanwinst van ABVV</dc_title> <!--Source: descriptive metadata ead/archdesc/did/unittitle-->
	<dc_description>collectie van een digitale dragers</dc_description> <!--Source: descriptive metadata ead/archdesc/did/scopecontent | optional -->
	<dc_identifier_localid>collectie12345</dc_identifier_localid> <!--Source: descriptive metadata ead/archdesc/did/unitid@label='localId'. Local ID. See https://github.com/Automatic-Ingest-Digital-Archives/SCALA/issues/57-->
	<dc_identifier_localids type="list">
		<ScalaID>a84be406-38a5-4002-a20a-188abd83ff83</ScalaID> <!--Source: AIP. AIP ID. See https://github.com/Automatic-Ingest-Digital-Archives/SCALA/issues/54-->
	</dc_identifier_localids>
	<dc_creators type="list">
		<Archiefvormer>ABVV</Archiefvormer> <!--Source: descriptive metadata ead/archdesc/did/origination@label='creator'-->
	</dc_creators>
	<dc_publishers type="list">
		<publisher>AIDA</publisher> <!--Source: descriptive metadata ead/archdesc/did/origination@label='producer'. This field is hardcoded to AIDA in RODA-In.-->
	</dc_publishers>
	<dc_rights_comment>niet-raadpleegbaar</dc_rights_comment> <!--Source: descriptive metadata ead/archdesc/did/accessrestrict | optional-->
	<md5>582925fef639c663e0abf9c47cad0727</md5> <!--Source: AIP-->
</VIAA>
	
```
	
</details>

##
<details><summary><b>Preservation metadata</b></summary>
    
## Object metadata

### File object metadata
    
Contains structural information about each file, like its name, fixity information, format, size, …

The representation folder structure is copied. Then for each data file a file object PREMIS is made. Each file object PREMIS is given the filename of the original file.
    
<details>
  <summary>Example of a file object</summary>
    
```xml
<?xml version="1.0" encoding="UTF-8"?>
<v3:object xsi:type="v3:file" xmlns:v3="http://www.loc.gov/premis/v3" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <v3:objectIdentifier>
    <v3:objectIdentifierType>URN</v3:objectIdentifierType>
    <v3:objectIdentifierValue>urn:roda:premis:file:Stuk1_Tekstdocument.docx</v3:objectIdentifierValue>
  </v3:objectIdentifier>
  <v3:preservationLevel>
    <v3:preservationLevelValue>full</v3:preservationLevelValue>
  </v3:preservationLevel>
  <v3:objectCharacteristics>
    <v3:fixity>
      <v3:messageDigestAlgorithm>MD5</v3:messageDigestAlgorithm>
      <v3:messageDigest>DC5D4F96B81E7453C48664F7CBBE32BF</v3:messageDigest>
      <v3:messageDigestOriginator>RODA</v3:messageDigestOriginator>
    </v3:fixity>
    <v3:size>11803</v3:size>
    <v3:format>
      <v3:formatDesignation>
        <v3:formatName>Microsoft Word for Windows</v3:formatName>
        <v3:formatVersion>2007 onwards</v3:formatVersion>
      </v3:formatDesignation>
    </v3:format>
    <v3:format>
      <v3:formatRegistry>
        <v3:formatRegistryName>pronom</v3:formatRegistryName>
        <v3:formatRegistryKey>fmt/412</v3:formatRegistryKey>
      </v3:formatRegistry>
    </v3:format>
    <v3:format>
      <v3:formatRegistry>
        <v3:formatRegistryName>mime</v3:formatRegistryName>
        <v3:formatRegistryKey>application/vnd.openxmlformats-officedocument.wordprocessingml.document</v3:formatRegistryKey>
      </v3:formatRegistry>
    </v3:format>
  </v3:objectCharacteristics>
  <v3:originalName>Stuk1_Tekstdocument.docx</v3:originalName>
  <v3:storage>
    <v3:contentLocation>
      <v3:contentLocationType/>
      <v3:contentLocationValue/>
    </v3:contentLocation>
  </v3:storage>
</v3:object>
```

</details>
    
### Representation object metadata
    
Contains structural information about a representation, like its contained files and relations between them.

<details>
  <summary>Example of a representation object</summary>
    
```xml
<?xml version="1.0" encoding="UTF-8"?>
<v3:object xsi:type="v3:representation" xmlns:v3="http://www.loc.gov/premis/v3" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <v3:objectIdentifier>
    <v3:objectIdentifierType>URN</v3:objectIdentifierType>
    <v3:objectIdentifierValue>urn:roda:premis:representation:76af487e-7c63-3a1d-9ef2-5eec0b9e139d</v3:objectIdentifierValue>
  </v3:objectIdentifier>
  <v3:preservationLevel>
    <v3:preservationLevelValue/>
  </v3:preservationLevel>
  <v3:relationship>
    <v3:relationshipType>structural</v3:relationshipType>
    <v3:relationshipSubType>hasPart</v3:relationshipSubType>
    <v3:relatedObjectIdentifier>
      <v3:relatedObjectIdentifierType>URN</v3:relatedObjectIdentifierType>
      <v3:relatedObjectIdentifierValue>urn:roda:premis:file:Stuk2_Presentatie.pptx</v3:relatedObjectIdentifierValue>
    </v3:relatedObjectIdentifier>
  </v3:relationship>
  <v3:relationship>
    <v3:relationshipType>structural</v3:relationshipType>
    <v3:relationshipSubType>hasPart</v3:relationshipSubType>
    <v3:relatedObjectIdentifier>
      <v3:relatedObjectIdentifierType>URN</v3:relatedObjectIdentifierType>
      <v3:relatedObjectIdentifierValue>urn:roda:premis:file:Stuk1_Tekstdocument.docx</v3:relatedObjectIdentifierValue>
    </v3:relatedObjectIdentifier>
  </v3:relationship>
</v3:object>
```
    
</details>
    
## Event metadata
    
An event is a process which is run on the AIP. Events are normally run and saved at the AIP level. It is possible to explicitely ask RODA to run certain events at representation or file level. In those cases, the event data will be stored in PREMIS metadata at the respective level.

An event PREMIS file is a log file about an event. It contains the following parts:
- The type of event. Check the full list below.
- The outcome of the event. An event can have a SUCCESS or a FAILURE outcome. Or it can be SKIPPED, meaning the process was considered but not executed.
- The agents involved in the event. Agents can be users or software programs.
- The objects involved in the event. Objects can be files, representations, the AIP and even the ingested SIP.

Here follows a list of event PREMIS metadata per event type.
    
### Wellformedness check

Checks that the received SIP is well formed, complete and that no unexpected files were included.

Agents involved: EARKSIP2ToAIPPlugin, user starting ingest process.
    
Objects involved: SIP, AIP.

<details>
    <summary>Example</summary>
    
```xml
<?xml version="1.0" encoding="UTF-8"?>
<event xmlns="http://www.loc.gov/premis/v3">
  <eventIdentifier>
    <eventIdentifierType>URN</eventIdentifierType>
    <eventIdentifierValue>urn:roda:premis:event:f051d728-5cba-4a4c-b9b2-0ef192c3bc2c</eventIdentifierValue>
  </eventIdentifier>
  <eventType>wellformedness check</eventType>
  <eventDateTime>2021-09-20T10:42:12.80Z</eventDateTime>
  <eventDetailInformation>
    <eventDetail>Checked that the received SIP is well formed, complete and that no unexpected files were included.</eventDetail>
  </eventDetailInformation>
  <eventOutcomeInformation>
    <eventOutcome>SUCCESS</eventOutcome>
    <eventOutcomeDetail>
      <eventOutcomeDetailNote>The SIP was well formed and complete.</eventOutcomeDetailNote>
    </eventOutcomeDetail>
  </eventOutcomeInformation>
  <linkingAgentIdentifier>
    <linkingAgentIdentifierType>URN</linkingAgentIdentifierType>
    <linkingAgentIdentifierValue>urn:roda:premis:agent:org.roda.core.plugins.plugins.ingest.EARKSIP2ToAIPPlugin@1.0</linkingAgentIdentifierValue>
  </linkingAgentIdentifier>
  <linkingAgentIdentifier>
    <linkingAgentIdentifierType>URN</linkingAgentIdentifierType>
    <linkingAgentIdentifierValue>urn:roda:premis:agent:jkleevens</linkingAgentIdentifierValue>
  </linkingAgentIdentifier>
  <linkingObjectIdentifier>
    <linkingObjectIdentifierType>URN</linkingObjectIdentifierType>
    <linkingObjectIdentifierValue>urn:roda:transferred_resource:dossier_met_mappen - uuid-6981ba8e-9d2b-4e8a-912e-6e2a6ad44c3d.zip</linkingObjectIdentifierValue>
    <linkingObjectRole>source</linkingObjectRole>
  </linkingObjectIdentifier>
  <linkingObjectIdentifier>
    <linkingObjectIdentifierType>URN</linkingObjectIdentifierType>
    <linkingObjectIdentifierValue>urn:roda:aip:668b3f2f-51be-4dd7-ace6-d73a41b8526c</linkingObjectIdentifierValue>
    <linkingObjectRole>outcome</linkingObjectRole>
  </linkingObjectIdentifier>
</event>
```

</details>

Checks whether the descriptive metadata is included in the SIP and if this metadata is valid according to the established policy.

Agents involved: DescriptiveMetadataValidationPlugin, user starting ingest process.
    
Objects involved: AIP.

<details>
    <summary>Example</summary>

```xml
<?xml version="1.0" encoding="UTF-8"?>
<event xmlns="http://www.loc.gov/premis/v3">
  <eventIdentifier>
    <eventIdentifierType>URN</eventIdentifierType>
    <eventIdentifierValue>urn:roda:premis:event:5794d4d2-4d8e-4ebc-977e-1f0d3b5d077e</eventIdentifierValue>
  </eventIdentifier>
  <eventType>wellformedness check</eventType>
  <eventDateTime>2021-09-20T10:42:13.39Z</eventDateTime>
  <eventDetailInformation>
    <eventDetail>Checked whether the descriptive metadata is included in the SIP and if this metadata is valid according to the established policy.</eventDetail>
  </eventDetailInformation>
  <eventOutcomeInformation>
    <eventOutcome>SUCCESS</eventOutcome>
    <eventOutcomeDetail>
      <eventOutcomeDetailNote>Descriptive metadata is well formed and complete.
Schemas used on validation: scala-dc (1.0)</eventOutcomeDetailNote>
    </eventOutcomeDetail>
  </eventOutcomeInformation>
  <linkingAgentIdentifier>
    <linkingAgentIdentifierType>URN</linkingAgentIdentifierType>
    <linkingAgentIdentifierValue>urn:roda:premis:agent:org.roda.core.plugins.plugins.base.DescriptiveMetadataValidationPlugin@1.0</linkingAgentIdentifierValue>
  </linkingAgentIdentifier>
  <linkingAgentIdentifier>
    <linkingAgentIdentifierType>URN</linkingAgentIdentifierType>
    <linkingAgentIdentifierValue>urn:roda:premis:agent:jkleevens</linkingAgentIdentifierValue>
  </linkingAgentIdentifier>
  <linkingObjectIdentifier>
    <linkingObjectIdentifierType>URN</linkingObjectIdentifierType>
    <linkingObjectIdentifierValue>urn:roda:aip:668b3f2f-51be-4dd7-ace6-d73a41b8526c</linkingObjectIdentifierValue>
    <linkingObjectRole>outcome</linkingObjectRole>
  </linkingObjectIdentifier>
</event>
```
 
</details>

### Format identification

Identifies the object's file formats and versions using Siegfried.

Agents involved: SiegfriedPlugin, user starting ingest process.
    
Objects involved: all files.
 
<details>
    <summary>Example</summary>

```xml
<?xml version="1.0" encoding="UTF-8"?>
<event xmlns="http://www.loc.gov/premis/v3">
  <eventIdentifier>
    <eventIdentifierType>URN</eventIdentifierType>
    <eventIdentifierValue>urn:roda:premis:event:53c2f0b9-61c9-4088-a4e6-fabc8c6f6f2a</eventIdentifierValue>
  </eventIdentifier>
  <eventType>format identification</eventType>
  <eventDateTime>2021-09-20T10:42:13.89Z</eventDateTime>
  <eventDetailInformation>
    <eventDetail>Identified the object's file formats and versions using Siegfried.</eventDetail>
  </eventDetailInformation>
  <eventOutcomeInformation>
    <eventOutcome>SUCCESS</eventOutcome>
    <eventOutcomeDetail>
      <eventOutcomeDetailNote>File formats were identified and recorded in PREMIS objects.</eventOutcomeDetailNote>
    </eventOutcomeDetail>
  </eventOutcomeInformation>
  <linkingAgentIdentifier>
    <linkingAgentIdentifierType>URN</linkingAgentIdentifierType>
    <linkingAgentIdentifierValue>urn:roda:premis:agent:org.roda.core.plugins.plugins.characterization.SiegfriedPlugin@1.9.1 w/ DROID_SignatureFile_V97</linkingAgentIdentifierValue>
  </linkingAgentIdentifier>
  <linkingAgentIdentifier>
    <linkingAgentIdentifierType>URN</linkingAgentIdentifierType>
    <linkingAgentIdentifierValue>urn:roda:premis:agent:jkleevens</linkingAgentIdentifierValue>
  </linkingAgentIdentifier>
  <linkingObjectIdentifier>
    <linkingObjectIdentifierType>URN</linkingObjectIdentifierType>
    <linkingObjectIdentifierValue>urn:roda:file:07fd0033-d8c4-3e69-83f4-4bd0601efdb9</linkingObjectIdentifierValue>
    <linkingObjectRole>source</linkingObjectRole>
  </linkingObjectIdentifier>
  <linkingObjectIdentifier>
    <linkingObjectIdentifierType>URN</linkingObjectIdentifierType>
    <linkingObjectIdentifierValue>urn:roda:file:e1da121d-9a3a-3a09-bdb4-355c03cf560d</linkingObjectIdentifierValue>
    <linkingObjectRole>source</linkingObjectRole>
  </linkingObjectIdentifier>
  <linkingObjectIdentifier>
    <linkingObjectIdentifierType>URN</linkingObjectIdentifierType>
    <linkingObjectIdentifierValue>urn:roda:file:d775e0e6-66cb-3a76-b7ef-3695de3ec22b</linkingObjectIdentifierValue>
    <linkingObjectRole>source</linkingObjectRole>
  </linkingObjectIdentifier>
  <linkingObjectIdentifier>
    <linkingObjectIdentifierType>URN</linkingObjectIdentifierType>
    <linkingObjectIdentifierValue>urn:roda:file:5d9ee2c8-1dca-38dd-af8e-4ff1df860875</linkingObjectIdentifierValue>
    <linkingObjectRole>source</linkingObjectRole>
  </linkingObjectIdentifier>
</event>
```
  
</details>

### Virus check

Scans package for malicious programs using ClamAV.

Agents involved: AntivirusPlugin, user starting ingest process.
    
Objects involved: AIP.
    
<details>
    <summary>Example</summary>

```xml
<?xml version="1.0" encoding="UTF-8"?>
<event xmlns="http://www.loc.gov/premis/v3">
  <eventIdentifier>
    <eventIdentifierType>URN</eventIdentifierType>
    <eventIdentifierValue>urn:roda:premis:event:06079fd0-aa57-4931-922e-1df092a09183</eventIdentifierValue>
  </eventIdentifier>
  <eventType>virus check</eventType>
  <eventDateTime>2021-09-20T10:42:13.36Z</eventDateTime>
  <eventDetailInformation>
    <eventDetail>Scanned package for malicious programs using ClamAV.</eventDetail>
  </eventDetailInformation>
  <eventOutcomeInformation>
    <eventOutcome>SUCCESS</eventOutcome>
    <eventOutcomeDetail>
      <eventOutcomeDetailNote>The package does not contain any known malicious programs.
/roda/data/storage/aip/668b3f2f-51be-4dd7-ace6-d73a41b8526c: OK

----------- SCAN SUMMARY -----------
Infected files: 0
Time: 0.325 sec (0 m 0 s)
Start Date: 2021:09:20 10:42:13
End Date:   2021:09:20 10:42:13</eventOutcomeDetailNote>
    </eventOutcomeDetail>
  </eventOutcomeInformation>
  <linkingAgentIdentifier>
    <linkingAgentIdentifierType>URN</linkingAgentIdentifierType>
    <linkingAgentIdentifierValue>urn:roda:premis:agent:org.roda.core.plugins.plugins.antivirus.AntivirusPlugin@ClamAV 0.103.2/26261/Thu Aug 12 08:22:34 2021</linkingAgentIdentifierValue>
  </linkingAgentIdentifier>
  <linkingAgentIdentifier>
    <linkingAgentIdentifierType>URN</linkingAgentIdentifierType>
    <linkingAgentIdentifierValue>urn:roda:premis:agent:jkleevens</linkingAgentIdentifierValue>
  </linkingAgentIdentifier>
  <linkingObjectIdentifier>
    <linkingObjectIdentifierType>URN</linkingObjectIdentifierType>
    <linkingObjectIdentifierValue>urn:roda:aip:668b3f2f-51be-4dd7-ace6-d73a41b8526c</linkingObjectIdentifierValue>
    <linkingObjectRole>outcome</linkingObjectRole>
  </linkingObjectIdentifier>
</event>
```
  
</details>

### Authorization check

User permissions are checked to ensure that they have sufficient authorization to store the AIP under the desired node of the classification scheme.

Agents involved: VerifyUserAuthorizationPlugin, user starting ingest process.
    
Objects involved: AIP.
 
<details>
    <summary>Example</summary>

```xml
<?xml version="1.0" encoding="UTF-8"?>
<event xmlns="http://www.loc.gov/premis/v3">
  <eventIdentifier>
    <eventIdentifierType>URN</eventIdentifierType>
    <eventIdentifierValue>urn:roda:premis:event:d9f2207c-53ad-4196-b333-7b881ac676d2</eventIdentifierValue>
  </eventIdentifier>
  <eventType>authorization check</eventType>
  <eventDateTime>2021-09-20T10:42:13.97Z</eventDateTime>
  <eventDetailInformation>
    <eventDetail>User permissions have been checked to ensure that he has sufficient authorization to store the AIP under the desired node of the classification scheme.</eventDetail>
  </eventDetailInformation>
  <eventOutcomeInformation>
    <eventOutcome>SUCCESS</eventOutcome>
    <eventOutcomeDetail>
      <eventOutcomeDetailNote>The user has enough permissions to deposit the AIP under the designated node of the classification scheme
Done with checking user authorization for AIP 668b3f2f-51be-4dd7-ace6-d73a41b8526c</eventOutcomeDetailNote>
    </eventOutcomeDetail>
  </eventOutcomeInformation>
  <linkingAgentIdentifier>
    <linkingAgentIdentifierType>URN</linkingAgentIdentifierType>
    <linkingAgentIdentifierValue>urn:roda:premis:agent:org.roda.core.plugins.plugins.ingest.VerifyUserAuthorizationPlugin@1.0</linkingAgentIdentifierValue>
  </linkingAgentIdentifier>
  <linkingAgentIdentifier>
    <linkingAgentIdentifierType>URN</linkingAgentIdentifierType>
    <linkingAgentIdentifierValue>urn:roda:premis:agent:jkleevens</linkingAgentIdentifierValue>
  </linkingAgentIdentifier>
  <linkingObjectIdentifier>
    <linkingObjectIdentifierType>URN</linkingObjectIdentifierType>
    <linkingObjectIdentifierValue>urn:roda:aip:668b3f2f-51be-4dd7-ace6-d73a41b8526c</linkingObjectIdentifierValue>
    <linkingObjectRole>outcome</linkingObjectRole>
  </linkingObjectIdentifier>
</event>
```
   
</details>

### Ingest start

The ingest process starts.

Agents involved: ConfigurableIngestPlugin, user starting ingest process.
    
Objects involved: SIP, AIP.
    
<details>
    <summary>Example</summary>

```xml
<?xml version="1.0" encoding="UTF-8"?>
<event xmlns="http://www.loc.gov/premis/v3">
  <eventIdentifier>
    <eventIdentifierType>URN</eventIdentifierType>
    <eventIdentifierValue>urn:roda:premis:event:5aebcbb0-dcbd-41e2-b342-08de70fde9a6</eventIdentifierValue>
  </eventIdentifier>
  <eventType>ingest start</eventType>
  <eventDateTime>2021-09-20T10:42:11.97Z</eventDateTime>
  <eventDetailInformation>
    <eventDetail>The ingest process has started.</eventDetail>
  </eventDetailInformation>
  <eventOutcomeInformation>
    <eventOutcome>SUCCESS</eventOutcome>
    <eventOutcomeDetail>
      <eventOutcomeDetailNote>The ingest process has successfully ended.</eventOutcomeDetailNote>
    </eventOutcomeDetail>
  </eventOutcomeInformation>
  <linkingAgentIdentifier>
    <linkingAgentIdentifierType>URN</linkingAgentIdentifierType>
    <linkingAgentIdentifierValue>urn:roda:premis:agent:org.roda.core.plugins.plugins.ingest.v2.ConfigurableIngestPlugin@2.0</linkingAgentIdentifierValue>
  </linkingAgentIdentifier>
  <linkingAgentIdentifier>
    <linkingAgentIdentifierType>URN</linkingAgentIdentifierType>
    <linkingAgentIdentifierValue>urn:roda:premis:agent:jkleevens</linkingAgentIdentifierValue>
  </linkingAgentIdentifier>
  <linkingObjectIdentifier>
    <linkingObjectIdentifierType>URN</linkingObjectIdentifierType>
    <linkingObjectIdentifierValue>urn:roda:transferred_resource:dossier_met_mappen - uuid-6981ba8e-9d2b-4e8a-912e-6e2a6ad44c3d.zip</linkingObjectIdentifierValue>
    <linkingObjectRole>source</linkingObjectRole>
  </linkingObjectIdentifier>
  <linkingObjectIdentifier>
    <linkingObjectIdentifierType>URN</linkingObjectIdentifierType>
    <linkingObjectIdentifierValue>urn:roda:aip:668b3f2f-51be-4dd7-ace6-d73a41b8526c</linkingObjectIdentifierValue>
    <linkingObjectRole>outcome</linkingObjectRole>
  </linkingObjectIdentifier>
</event>
```
 
</details>

### Ingest end

The ingest process ends.

Agents involved: ConfigurableIngestPlugin, user starting ingest process.
    
Objects involved: SIP, AIP.
    
<details>
    <summary>Example</summary>

```xml
<?xml version="1.0" encoding="UTF-8"?>
<event xmlns="http://www.loc.gov/premis/v3">
  <eventIdentifier>
    <eventIdentifierType>URN</eventIdentifierType>
    <eventIdentifierValue>urn:roda:premis:event:8ce4e78f-6f09-40f4-99a5-5c8e7bc835d3</eventIdentifierValue>
  </eventIdentifier>
  <eventType>ingest end</eventType>
  <eventDateTime>2021-09-20T10:42:14.14Z</eventDateTime>
  <eventDetailInformation>
    <eventDetail>The ingest process has ended.</eventDetail>
  </eventDetailInformation>
  <eventOutcomeInformation>
    <eventOutcome>SUCCESS</eventOutcome>
    <eventOutcomeDetail>
      <eventOutcomeDetailNote>The ingest process has successfully ended.</eventOutcomeDetailNote>
    </eventOutcomeDetail>
  </eventOutcomeInformation>
  <linkingAgentIdentifier>
    <linkingAgentIdentifierType>URN</linkingAgentIdentifierType>
    <linkingAgentIdentifierValue>urn:roda:premis:agent:org.roda.core.plugins.plugins.ingest.v2.ConfigurableIngestPlugin@2.0</linkingAgentIdentifierValue>
  </linkingAgentIdentifier>
  <linkingAgentIdentifier>
    <linkingAgentIdentifierType>URN</linkingAgentIdentifierType>
    <linkingAgentIdentifierValue>urn:roda:premis:agent:jkleevens</linkingAgentIdentifierValue>
  </linkingAgentIdentifier>
  <linkingObjectIdentifier>
    <linkingObjectIdentifierType>URN</linkingObjectIdentifierType>
    <linkingObjectIdentifierValue>urn:roda:transferred_resource:dossier_met_mappen - uuid-6981ba8e-9d2b-4e8a-912e-6e2a6ad44c3d.zip</linkingObjectIdentifierValue>
    <linkingObjectRole>source</linkingObjectRole>
  </linkingObjectIdentifier>
  <linkingObjectIdentifier>
    <linkingObjectIdentifierType>URN</linkingObjectIdentifierType>
    <linkingObjectIdentifierValue>urn:roda:aip:668b3f2f-51be-4dd7-ace6-d73a41b8526c</linkingObjectIdentifierValue>
    <linkingObjectRole>outcome</linkingObjectRole>
  </linkingObjectIdentifier>
</event>
```
    
</details>

### Message digest calculation

Creates base PREMIS objects with file original name and file fixity information (like MD5 or SHA-256).

Agents involved: PremisSkeletonPlugin, user starting ingest process.
    
Objects involved: AIP.
   
<details>
    <summary>Example</summary>

```xml
<?xml version="1.0" encoding="UTF-8"?>
<event xmlns="http://www.loc.gov/premis/v3">
  <eventIdentifier>
    <eventIdentifierType>URN</eventIdentifierType>
    <eventIdentifierValue>urn:roda:premis:event:eeb83f9f-97e1-4a01-97b2-baa824f656bc</eventIdentifierValue>
  </eventIdentifier>
  <eventType>message digest calculation</eventType>
  <eventDateTime>2021-09-20T10:42:13.71Z</eventDateTime>
  <eventDetailInformation>
    <eventDetail>Created base PREMIS objects with file original name and file fixity information (SHA-256).</eventDetail>
  </eventDetailInformation>
  <eventOutcomeInformation>
    <eventOutcome>SUCCESS</eventOutcome>
    <eventOutcomeDetail>
      <eventOutcomeDetailNote>PREMIS objects were successfully created.</eventOutcomeDetailNote>
    </eventOutcomeDetail>
  </eventOutcomeInformation>
  <linkingAgentIdentifier>
    <linkingAgentIdentifierType>URN</linkingAgentIdentifierType>
    <linkingAgentIdentifierValue>urn:roda:premis:agent:org.roda.core.plugins.plugins.characterization.PremisSkeletonPlugin@1.0</linkingAgentIdentifierValue>
  </linkingAgentIdentifier>
  <linkingAgentIdentifier>
    <linkingAgentIdentifierType>URN</linkingAgentIdentifierType>
    <linkingAgentIdentifierValue>urn:roda:premis:agent:jkleevens</linkingAgentIdentifierValue>
  </linkingAgentIdentifier>
  <linkingObjectIdentifier>
    <linkingObjectIdentifierType>URN</linkingObjectIdentifierType>
    <linkingObjectIdentifierValue>urn:roda:aip:668b3f2f-51be-4dd7-ace6-d73a41b8526c</linkingObjectIdentifierValue>
    <linkingObjectRole>outcome</linkingObjectRole>
  </linkingObjectIdentifier>
</event>
```
  
</details>

### Accession

Adds the package to the inventory. After this point, the responsibility for the digital content’s preservation is passed on to the repository.

Agents involved: AutoAcceptSIPPlugin, user starting ingest process.
    
Objects involved: AIP.
    
<details>
    <summary>Example</summary>

```xml
<?xml version="1.0" encoding="UTF-8"?>
<event xmlns="http://www.loc.gov/premis/v3">
  <eventIdentifier>
    <eventIdentifierType>URN</eventIdentifierType>
    <eventIdentifierValue>urn:roda:premis:event:08fe7621-5824-456b-8178-952139837fa9</eventIdentifierValue>
  </eventIdentifier>
  <eventType>accession</eventType>
  <eventDateTime>2021-09-20T10:42:14.10Z</eventDateTime>
  <eventDetailInformation>
    <eventDetail>Added package to the inventory. After this point, the responsibility for the digital content’s preservation is passed on to the repository.</eventDetail>
  </eventDetailInformation>
  <eventOutcomeInformation>
    <eventOutcome>SUCCESS</eventOutcome>
    <eventOutcomeDetail>
      <eventOutcomeDetailNote>The AIP was successfully added to the repository's inventory.</eventOutcomeDetailNote>
    </eventOutcomeDetail>
  </eventOutcomeInformation>
  <linkingAgentIdentifier>
    <linkingAgentIdentifierType>URN</linkingAgentIdentifierType>
    <linkingAgentIdentifierValue>urn:roda:premis:agent:org.roda.core.plugins.plugins.ingest.AutoAcceptSIPPlugin@1.0</linkingAgentIdentifierValue>
  </linkingAgentIdentifier>
  <linkingAgentIdentifier>
    <linkingAgentIdentifierType>URN</linkingAgentIdentifierType>
    <linkingAgentIdentifierValue>urn:roda:premis:agent:jkleevens</linkingAgentIdentifierValue>
  </linkingAgentIdentifier>
  <linkingObjectIdentifier>
    <linkingObjectIdentifierType>URN</linkingObjectIdentifierType>
    <linkingObjectIdentifierValue>urn:roda:aip:668b3f2f-51be-4dd7-ace6-d73a41b8526c</linkingObjectIdentifierValue>
    <linkingObjectRole>outcome</linkingObjectRole>
  </linkingObjectIdentifier>
</event>
```
 
</details>

### Unpacking

Extracts objects from the package in E-ARK SIP 2 format.

Agents involved: EARKSIP2ToAIPPlugin, user starting ingest process.
    
Objects involved: SIP, AIP.
    
<details>
    <summary>Example</summary>

```xml
<?xml version="1.0" encoding="UTF-8"?>
<event xmlns="http://www.loc.gov/premis/v3">
  <eventIdentifier>
    <eventIdentifierType>URN</eventIdentifierType>
    <eventIdentifierValue>urn:roda:premis:event:93820350-9ebd-47ba-aed6-71e8801cbf23</eventIdentifierValue>
  </eventIdentifier>
  <eventType>unpacking</eventType>
  <eventDateTime>2021-09-20T10:42:12.78Z</eventDateTime>
  <eventDetailInformation>
    <eventDetail>Extracted objects from package in E-ARK SIP 2 format.</eventDetail>
  </eventDetailInformation>
  <eventOutcomeInformation>
    <eventOutcome>SUCCESS</eventOutcome>
    <eventOutcomeDetail>
      <eventOutcomeDetailNote>The SIP has been successfully unpacked.</eventOutcomeDetailNote>
    </eventOutcomeDetail>
  </eventOutcomeInformation>
  <linkingAgentIdentifier>
    <linkingAgentIdentifierType>URN</linkingAgentIdentifierType>
    <linkingAgentIdentifierValue>urn:roda:premis:agent:org.roda.core.plugins.plugins.ingest.EARKSIP2ToAIPPlugin@1.0</linkingAgentIdentifierValue>
  </linkingAgentIdentifier>
  <linkingAgentIdentifier>
    <linkingAgentIdentifierType>URN</linkingAgentIdentifierType>
    <linkingAgentIdentifierValue>urn:roda:premis:agent:jkleevens</linkingAgentIdentifierValue>
  </linkingAgentIdentifier>
  <linkingObjectIdentifier>
    <linkingObjectIdentifierType>URN</linkingObjectIdentifierType>
    <linkingObjectIdentifierValue>urn:roda:transferred_resource:dossier_met_mappen - uuid-6981ba8e-9d2b-4e8a-912e-6e2a6ad44c3d.zip</linkingObjectIdentifierValue>
    <linkingObjectRole>source</linkingObjectRole>
  </linkingObjectIdentifier>
  <linkingObjectIdentifier>
    <linkingObjectIdentifierType>URN</linkingObjectIdentifierType>
    <linkingObjectIdentifierValue>urn:roda:aip:668b3f2f-51be-4dd7-ace6-d73a41b8526c</linkingObjectIdentifierValue>
    <linkingObjectRole>outcome</linkingObjectRole>
  </linkingObjectIdentifier>
</event>
```
 
</details>

### Digital signature validation

Checks if digital signatures were valid and/or strips them.

Agents involved: DigitalSignaturePlugin, user starting ingest process.
    
Objects involved: AIP.
    
<details>
    <summary>Example</summary>

```xml
<?xml version="1.0" encoding="UTF-8"?>
<event xmlns="http://www.loc.gov/premis/v3">
  <eventIdentifier>
    <eventIdentifierType>URN</eventIdentifierType>
    <eventIdentifierValue>urn:roda:premis:event:909e5fc4-d6e7-4f9d-a750-a9679c3f2dc0</eventIdentifierValue>
  </eventIdentifier>
  <eventType>digital signature validation</eventType>
  <eventDateTime>2021-07-19T07:28:51.56Z</eventDateTime>
  <eventDetailInformation>
    <eventDetail>Checked if digital signatures were valid and/or stripped them.</eventDetail>
  </eventDetailInformation>
  <eventOutcomeInformation>
    <eventOutcome>SKIPPED</eventOutcome>
    <eventOutcomeDetail>
      <eventOutcomeDetailNote>The package skipped the action.
No file was stripped on this aip.</eventOutcomeDetailNote>
    </eventOutcomeDetail>
  </eventOutcomeInformation>
  <linkingAgentIdentifier>
    <linkingAgentIdentifierType>URN</linkingAgentIdentifierType>
    <linkingAgentIdentifierValue>urn:roda:premis:agent:org.roda.core.plugins.external.DigitalSignaturePlugin@1.0</linkingAgentIdentifierValue>
  </linkingAgentIdentifier>
  <linkingAgentIdentifier>
    <linkingAgentIdentifierType>URN</linkingAgentIdentifierType>
    <linkingAgentIdentifierValue>urn:roda:premis:agent:admin</linkingAgentIdentifierValue>
  </linkingAgentIdentifier>
</event>
```
    
</details>

### Metadata extraction

Extraction of technical metadata using Apache Tika.

Agents involved: TikaFullTextPlugin, user starting ingest process.
    
Objects involved: all files.
    
<details>
    <summary>Example</summary>

```xml
<?xml version="1.0" encoding="UTF-8"?>
<event xmlns="http://www.loc.gov/premis/v3">
  <eventIdentifier>
    <eventIdentifierType>URN</eventIdentifierType>
    <eventIdentifierValue>urn:roda:premis:event:1f1fae7e-c9f3-47da-9843-ddb5b200f1bc</eventIdentifierValue>
  </eventIdentifier>
  <eventType>metadata extraction</eventType>
  <eventDateTime>2021-07-19T07:28:50.61Z</eventDateTime>
  <eventDetailInformation>
    <eventDetail>Extraction of technical metadata using Apache Tika.</eventDetail>
  </eventDetailInformation>
  <eventOutcomeInformation>
    <eventOutcome>FAILURE</eventOutcome>
    <eventOutcomeDetail>
      <eventOutcomeDetailNote>Failed to extract technical metadata from file.
Could not create binary</eventOutcomeDetailNote>
    </eventOutcomeDetail>
  </eventOutcomeInformation>
  <linkingAgentIdentifier>
    <linkingAgentIdentifierType>URN</linkingAgentIdentifierType>
    <linkingAgentIdentifierValue>urn:roda:premis:agent:org.roda.core.plugins.external.TikaFullTextPlugin@1.0</linkingAgentIdentifierValue>
  </linkingAgentIdentifier>
  <linkingAgentIdentifier>
    <linkingAgentIdentifierType>URN</linkingAgentIdentifierType>
    <linkingAgentIdentifierValue>urn:roda:premis:agent:admin</linkingAgentIdentifierValue>
  </linkingAgentIdentifier>
  <linkingObjectIdentifier>
    <linkingObjectIdentifierType>URN</linkingObjectIdentifierType>
    <linkingObjectIdentifierValue>urn:roda:file:4a1b6500-8136-3b9f-9bb6-cb1f45d34ff1</linkingObjectIdentifierValue>
    <linkingObjectRole>source</linkingObjectRole>
  </linkingObjectIdentifier>
  <linkingObjectIdentifier>
    <linkingObjectIdentifierType>URN</linkingObjectIdentifierType>
    <linkingObjectIdentifierValue>urn:roda:file:aada1e36-ec4a-3322-bec0-578c77cf97d0</linkingObjectIdentifierValue>
    <linkingObjectRole>source</linkingObjectRole>
  </linkingObjectIdentifier>
  <linkingObjectIdentifier>
    <linkingObjectIdentifierType>URN</linkingObjectIdentifierType>
    <linkingObjectIdentifierValue>urn:roda:file:78852e6c-9b8a-3350-b6eb-0e6755501e57</linkingObjectIdentifierValue>
    <linkingObjectRole>source</linkingObjectRole>
  </linkingObjectIdentifier>
</event>
```
  
</details>

</details>
    
##
<details><summary><b>Other metadata</b></summary>
    
## Siegfried
    
The representation folder structure is copied. Then for each data file a Siegried JSON file is made.
    
<details>
    <summary>Example</summary>

```JSON
{
    "filename": "/roda/data/storage/aip/668b3f2f-51be-4dd7-ace6-d73a41b8526c/representations/rep1/data/Dossier_1/Stuk1_Tekstdocument.docx",
    "filesize": 11803,
    "modified": "2021-09-20T10:42:12Z",
    "errors": "",
    "matches": [{
            "ns": "pronom",
            "id": "fmt/412",
            "format": "Microsoft Word for Windows",
            "version": "2007 onwards",
            "mime": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            "basis": "extension match docx; container name [Content_Types].xml with byte match at 327, 94 (signature 1/3)",
            "warning": ""
        }
    ]
}
```
   
</details>

## ApacheTika
  
The representation folder structure is copied. Then for each data file an ApacheTika XML file is made.
    
<details>
    <summary>Example</summary>

```xml
<?xml version="1.0" encoding="UTF-8"?>
<metadata>
  <field name="X-Parsed-By">org.apache.tika.parser.DefaultParser</field>
  <field name="X-Parsed-By">org.apache.tika.parser.txt.TXTParser</field>
  <field name="Content-Encoding">ISO-8859-1</field>
  <field name="Content-Type">text/plain; charset=ISO-8859-1</field>
</metadata>
```
   
</details>
    
## VeraPDF
  
The representation folder structure is copied. Then for each pdf file a VeraPDF HTML file is made.
  
[Example](https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Referenced%20Files/VeraPDF_Example_Output.pdf.html)
   
</details>

</details>
    
