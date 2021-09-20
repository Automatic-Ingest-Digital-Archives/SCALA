# RODA AIP analysis

Let's first look at the general structure of a RODA AIP. Afterwards, we'll go through some metadata examples of such an AIP.

## RODA AIP

A RODA AIP has the following general folder/file structure:

```
AIP
    Documentation
    Metadata (AIP level)
        Descriptive
            Description.xml
        Preservation
            PREMIS.xml
    Representations
        Rep1
            Data
            Metadata (representation/file level)
                Other
                Preservation
                    PREMIS.xml
        …
    Schemas
    Aip.json
```

Let's see what each section contains:

**Documentation** - Additional files with information related to, but not part of the IP itself.

**Description.xml** - Provided information about the archives contained in the AIP. Tags include:

- *CP* - Content provider.
- *CP_id* - Content provider ID.
- *dc_title* - IP title.
- *dc_description* - IP description.
- *dc_identifier_localid* - IP identifier used by the archiver.
- *dc_identifier_localids* - List of other IDs, such as SCALA ID; RODA-In SIP ID, ...
- *dc_titles* - List of names of the archive. (?)
- *dc_creators* - List of people/institutions who made the archive.
- *dc_contributors*
- *dc_rights_licenses*
- *dc_rights_comment*
- *dcterms_created* - Creation date of the IP.
- *md5* - MD5 checksum value.

**PREMIS.xml (AIP level)** - All PREMIS files of events/processes that were run on the AIP's data. Such events include:

- Check if digital signatures are valid and/or strip them.
- Check that the received SIP is well formed, complete and that no unexpected files were included.
- Identify the object's file formats and versions using Siegfried.
- Scan package for malicious programs using ClamAV.
- Start of the ingest process.
- End of the ingest process.
- Check whether the descriptive metadata is included in the SIP and if this metadata is valid according to the established policy.
- Extract technical metadata using Apache Tika.
- Add package to the inventory. After this point, the responsibility for the digital content’s preservation is passed on to the repository.
- Check if PDF files are veraPDF valid.
- Extract objects from package in E-ARK SIP 2 format.
- Create base PREMIS objects with file original name and file fixity information (SHA-256).
- Check user permissions to ensure that they has sufficient authorization to store the AIP under the desired node of the classification scheme.

**Representations** - Rep1 (the ‘original representation’ of the IP) records the structure and contains all data files of the digital archive as it was originally submitted to the repository. There may be additional representations present in the AIP. These contain data and metadata representing the current/actual preservation state of the AIP.

**PREMIS.xml (representation/file level)** - Structural information about all files, like their names and relationships between files. At file level, it stores fixity information, format, size, …

**Other (representation/file level metadata)** - File level information by plugins like ApacheTika, Siegfried and VeraPDF.

**Schemas** - Contains documentation and validation information for all fields potentially used in any of the metadata files.

**Aip.json** - Contains data about the AIP ingest, its contents and any updates it has had.

## Examples/exercises

Check out [this example AIP](https://github.com/Automatic-Ingest-Digital-Archives/SCALA/tree/main/RODA/AIP%20Interpretation%20Manual/VoorbeeldAIP) and see if you can find all sections discussed above.

Now let's take a closer look at some of the metadata files.

### [Example AIP level PREMIS](https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/RODA/AIP%20Interpretation%20Manual/VoorbeeldAIP/metadata/preservation/urn_roda_premis_event_06079fd0-aa57-4931-922e-1df092a09183.xml)

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

See if you can find the following information in the PREMIS above:

- What type of event is this PREMIS about?
- Is there more detailed information about the event available?
- Was the outcome of the event a success or a failure?
- Can you find two linkingAgentIdentifier tags?
- Who are the agents involved in this event? Hint: one agent is a user, one is a piece of software.
- Can you find a linkingObjectIdentifier tag? Can you see that the object it refers to, is the AIP itself?

### [Example representation/file level PREMIS](https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/RODA/AIP%20Interpretation%20Manual/VoorbeeldAIP/representations/rep1/metadata/preservation/Dossier_met_mappen/urn_roda_premis_file_Stuk1_Tekstdocument.docx.xml)

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

See if you can make an educated guess as to the information contained in each tag.

### [Example description.xml](https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/RODA/AIP%20Interpretation%20Manual/SCALA_sample_descriptive_metadata.xml)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<VIAA xmlns:xs="http://www.w3.org/2001/XMLSchema"
      xmlns:dc="http://purl.org/dc/elements/1.1/"
      xmlns:dcterms="http://purl.org/dc/terms/">
   <CP>AMSAB-IG</CP>
   <CP_id>OR-jq0st8z<!--21-09-16 for now we use the generic APA OR-iD; later we will use the OR-ID's of the individual CP's--></CP_id>
   <dc_title>aanwinst van ABVV</dc_title>
   <dc_description>collectie van een aantal digitale dragers uit de bureau's van een aantal medewerkers</dc_description>
   <dc_identifier_localid>collectie12345</dc_identifier_localid>
   <dc_identifier_localids type="list">      
      <ScalaID>UUID12345<!--UUID of SIP produced by Roda-In?--></ScalaID>
   </dc_identifier_localids>
   <dc_titles type="list">
      <archief>144: Archief van Algemeen Belgisch Vakverbond (ABVV)</archief>
   </dc_titles>
   <dc_creators type="list">
         <Archiefvormer>ABVV</Archiefvormer>
   </dc_creators>
   <dc_contributors type="list">
      <Producer>SCALA<!--aim is to be able to filter out Scala content, still looking into this--></Producer>
   </dc_contributors>
   <dc_rights_licenses/> 
   <dc_rights_comment>niet-raadpleegbaar</dc_rights_comment>
   <dcterms_created>2021-09-13<!--creation date of AIP?--></dcterms_created>
   <md5>582925fef639c663e0abf9c47cad0727</md5>
</VIAA>
```
