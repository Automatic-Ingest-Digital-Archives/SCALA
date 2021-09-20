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

**Description.xml** - Provided information about the archives contained in the AIP.

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

## Examples

Check out [this example AIP](https://github.com/Automatic-Ingest-Digital-Archives/SCALA/tree/main/RODA/AIP%20Interpretation%20Manual/VoorbeeldAIP) and see if you can find all sections discussed above.

Now let's take a closer look at some of the metadata files.

[Example package level PREMIS.xml](https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/RODA/AIP%20Interpretation%20Manual/VoorbeeldAIP/metadata/preservation/urn_roda_premis_event_06079fd0-aa57-4931-922e-1df092a09183.xml)
