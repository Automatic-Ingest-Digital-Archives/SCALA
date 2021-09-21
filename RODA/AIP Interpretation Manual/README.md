# Structure

A RODA AIP has the following general folder/file structure:

```
AIP
├───documentation
├───metadata
│   ├───descriptive
│   └───preservation
├───representations
│   └───rep1
│       ├───data
│       └───metadata
│           ├───other
│           └───preservation
|   └───...
└───schemas
```

**Documentation** - Additional files with information related to, but not part of the IP itself.

**Representations** - Rep1 (the ‘original representation’ of the IP) records the structure and contains all data files of the digital archive as it was originally submitted to the repository. There may be additional representations present in the AIP. These contain data and metadata representing the current/actual preservation state of the AIP.

**Schemas** - Contains documentation and validation information for all fields potentially used in any of the metadata files.

**Aip.json / METS.xml** - Contains data about the AIP ingest process, its contents and any updates it has had.

AIP metadata will be explored in detail in the following segments.

# Descriptive metadata

<details>
  <summary>Click to expand</summary>
    
Description.xml contains provided information about the archives contained in the AIP. The following table contains an overview of all tags considered, including mapping between descriptive metadata standards. It also shows how these standards are then mapped to the meemoo.xml.

<details>
    <summary>Expand table</summary>

| ISAD(G)                                                   | EAD 2002                                                          | RODA-In EAD                                 | DC Elements | RODA-In DC   | sidecar XML                                                                  | SCALA priority | SCALA description                |
|-----------------------------------------------------------|-------------------------------------------------------------------|---------------------------------------------|-------------|--------------|------------------------------------------------------------------------------|----------------|----------------------------------|
| 3.1.1 Reference code(s)                                   | <unitid> with COUNTRYCODE and REPOSITORYCODE attributes           | Identifier                                  | Identifier  | ID           | PID                                                                          | MUST           | id / dcterms:identifier          |
| 3.1.2 Title                                               | <unittitle>                                                       | Title                                       | Title       | Title        | dc_title                                                                     | SHOULD         | originalTitle / dc:title         |
| 3.1.3 Dates                                               | <unitdate>                                                        | Descriptive date                            | Date        | N/A          | dcterms_created                                                              | SHOULD         | date / dcterms:created           |
| 3.1.4 Level of description                                | <archdesc> LEVEL attribute                                        | Description level                           | N/A         | N/A          |                                                                              | SHOULD         |                                  |
| 3.1.5 Extent and medium of the unit                       | <physdesc>, subelement <physfacet>                                | Appearance                                  | N/A         | N/A          |                                                                              | CAN            |                                  |
| 3.1.5 Extent and medium of the unit                       | <physdesc>, subelement <dimensions>                               | Dimensions                                  | N/A         | N/A          | DurationTimecode / ImageSize                                                 | CAN            |                                  |
| 3.1.5 Extent and medium of the unit                       | <physdesc>, subelement <extent>                                   | Extent and medium                           | N/A         | N/A          |                                                                              | CAN            | cld:itemFormat / dcterms: extent |
| 3.1.5 Extent and medium of the unit                       | <physdesc>, subelement <genreform>                                | N/A                                         | Type        | Type         | dc_types                                                                     | CAN            | dcterms:type                     |
| 3.1.5 Extent and medium of the unit                       | <physdesc>                                                        | Physical description                        | Format      | Format       | VideoFormat / VideoTechnical / AudioTechnical / TcInTimecode / TcOutTimecode | SHOULD         |                                  |
| 3.2.1 Name of creator                                     | <origination> label="creator" attribute                           | Name of creator(s)                          | Creator     | Creator      | dc_creator / dc_creators                                                     | SHOULD         | dc:creator                       |
| 3.2.2 Administrative/Biographical history                 | <bioghist>                                                        | Administrative and biographical history     | N/A         | N/A          |                                                                              | CAN            |                                  |
| 3.2.3 Archival history                                    | <custodhist>                                                      | Custodial history                           | N/A         | N/A          | dc_rights_rightsOwners / dc_rights_rightsHolders / dc_rights_credit          | CAN            | marc:owner                       |
| 3.2.4 Immediate source of acquisition                     | <acqinfo>                                                         | Immediate source of acquisition or transfer | N/A         | N/A          |                                                                              | CAN            |                                  |
| 3.3.1 Scope and content                                   | <scopecontent>                                                    | Scope and content                           | Description | Description  | dc_description / dc_description_***                                          | SHOULD         | dc:description                   |
| 3.3.2 Appraisal, destruction and scheduling               | <appraisal>                                                       | Appraisal, destruction and scheduling       | N/A         | N/A          |                                                                              | CAN            |                                  |
| 3.3.3 Accruals                                            | <accruals>                                                        | Accruals                                    | N/A         | N/A          |                                                                              | CAN            |                                  |
| 3.3.4 System of arrangement                               | <arrangement>                                                     | System of arrangement                       | N/A         | N/A          |                                                                              | CAN            |                                  |
| 3.4.1 Conditions governing access                         | <accessrestrict>                                                  | Conditions governing access                 | Rights      | Rights       |                                                                              | SHOULD         | dcterms:accessRights             |
| 3.4.2 Conditions governing reproduction                   | <userestrict>                                                     | Conditions governing reproduction           | Rights      | Rights       | dc_rights_licenses / dc_rights_comment                                       | CAN            |                                  |
| 3.4.3 Language/scripts of material                        | <langmaterial> with <language> LANGCODE and SCRIPTCODE attributes | Language and script notes                   | N/A         | N/A          |                                                                              | CAN            |                                  |
| 3.4.3 Language/scripts of material                        | <langmaterial>                                                    | Language of material                        | Language    | Language     | dc_languages                                                                 | CAN            | dcterms:language                 |
| 3.4.4 Physical characteristics and technical requirements | <phystech>                                                        | Material specification                      | N/A         | N/A          |                                                                              | CAN            |                                  |
| 3.4.5 Finding aids                                        | <otherfindaid>                                                    | Find aid                                    | N/A         | N/A          |                                                                              | CAN            |                                  |
| 3.5.1 Existence and location of originals                 | <originalsloc>                                                    | Existence and location of originals         | N/A         | N/A          |                                                                              | CAN            |                                  |
| 3.5.2 Existence and location of copies                    | <altformavail>                                                    | Existence and location of copies            | N/A         | N/A          |                                                                              | CAN            |                                  |
| 3.5.3 Related units of description                        | <relatedmaterial>                                                 | Related units of description                | Relation    | Relation     | dc_local_id / dc_relations type                                              | CAN/SHOULD     | dcterms:isPartOf                 |
| 3.5.4 Publication note                                    | <bibliography>                                                    | Bibliography                                | N/A         | N/A          |                                                                              | CAN            |                                  |
| 3.6.1 Note                                                | <odd> type="levelOfDetail" attribute                              | Level of detail                             | N/A         | N/A          |                                                                              | CAN            |                                  |
| 3.6.1 Note                                                | <note> type="generalNote" attribute                               | Notes                                       | N/A         | N/A          |                                                                              | CAN            |                                  |
| 3.6.1 Note                                                | <note> type="sourcesDescription" attribute                        | Sources                                     | N/A         | N/A          |                                                                              | CAN            |                                  |
| 3.6.1 Note                                                | <odd> type="statusDescription" attribute                          | Status description                          | N/A         | N/A          |                                                                              | CAN            |                                  |
| 3.7.1 Archivist's note                                    | <processinfo>                                                     | Archivists notes                            | N/A         | N/A          |                                                                              | CAN            |                                  |
| 3.7.2 Rules or conventions                                | <descrules>                                                       | Rules or conventions                        | N/A         | N/A          |                                                                              | CAN            |                                  |
| 3.7.3 Date(s) of descriptions                             | <processinfo>, subelement <date>                                  | Date of creation or revision                | N/A         | N/A          |                                                                              | CAN            |                                  |
| N/A                                                       | <unitid> COUNTRYCODE attribute                                    | Country code                                | N/A         | N/A          | CP_id                                                                        | SHOULD         |                                  |
| N/A                                                       | <unitdate> label="UnitDates" normal=Initialdate/finaldate         | Final date                                  | N/A         | Final date   |                                                                              | CAN            |                                  |
| N/A                                                       | <unitdate> label="UnitDates" normal=Initialdate/finaldate         | Initial date                                | N/A         | Initial date |                                                                              | CAN            |                                  |
| N/A                                                       | N/A                                                               | N/A                                         | Contributor | Contributor  | dc_contributors                                                              | CAN            |                                  |
| N/A                                                       | <controlaccess><geogname>                                         | N/A                                         | Coverage    | Coverage     | dc_coverages                                                                 | CAN            |                                  |
| N/A                                                       | <unittitle><imprint><publisher>                                   | N/A                                         | Publisher   | N/A          | dc_publishers                                                                | CAN/MUST       |                                  |
| N/A                                                       | N/A                                                               | N/A                                         | N/A         | N/A          | md5                                                                          | MUST           |                                  |
| N/A                                                       | N/A                                                               | N/A                                         | N/A         | N/A          |                                                                              | CAN            | edm:dataprovider                 |
| N/A                                                       | N/A                                                               | N/A                                         | Source      | Source       |                                                                              | CAN/SHOULD     |                                  |
| N/A                                                       | <controlaccess><subject>                                          | N/A                                         | Subject     | Subject      | dc_subjects                                                                  | CAN            | dcterms:subject                  |
| N/A                                                       | <origination>                                                     | Origination                                 | N/A         | N/A          |                                                                              | CAN            |                                  |
| N/A                                                       | <origination> label="producer" attribute                          | Producer                                    | N/A         | Producer     |                                                                              | CAN/MUST       | Producer                         |
| N/A                                                       | <prefercite>                                                      | Quote                                       | N/A         | N/A          |                                                                              | CAN            |                                  |
| N/A                                                       | <repository>                                                      | Repository                                  | N/A         | N/A          | CP                                                                           | MUST           | edm:provider                     |
| N/A                                                       | <unitid> REPOSITORYCODE attribute                                 | Repository code                             | N/A         | N/A          |                                                                              | SHOULD         |                                  |

[Table source](https://drive.google.com/file/d/1O1x-21RBuIK6d0WqePyFhu16Czd66J0x/view)

</details>

</details>

# Preservation metadata
    
<details>
  <summary>Click to expand</summary>
    
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
    
Events are saved at the AIP level. An event is a process which is run on the AIP.

An event PREMIS file is a log file about an event. It involves three parts:
- The type of event. Check the full list below.
- The outcome of the event. An event can have a SUCCESS or a FAILURE outcome. Or it can be SKIPPED, meaning the process was considered but not executed.
- The agents involved in the event. Agents can be users or software programs.
- The objects involved in the event. Objects can be files, representations, the AIP and even the ingested SIP.

Here follows a list of event PREMIS metadata per event type.
    
### Wellformedness check

Checked that the received SIP is well formed, complete and that no unexpected files were included.

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

Checked whether the descriptive metadata is included in the SIP and if this metadata is valid according to the established policy.

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

Identified the object's file formats and versions using Siegfried.

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

Scanned package for malicious programs using ClamAV.

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

User permissions have been checked to ensure that he has sufficient authorization to store the AIP under the desired node of the classification scheme.

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

The ingest process has started.

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

The ingest process has ended.

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

Created base PREMIS objects with file original name and file fixity information (SHA-256).

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

Added package to the inventory. After this point, the responsibility for the digital content’s preservation is passed on to the repository.

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

Extracted objects from package in E-ARK SIP 2 format.

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

Checked if digital signatures were valid and/or stripped them.

Agents involved: DigitalSignaturePlugin, user starting ingest process.
    
No objects involved.
    
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
    
# Other metadata

<details>
<summary>Click to expand</summary>
    
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
    
## VeraPDF

</details>
    
