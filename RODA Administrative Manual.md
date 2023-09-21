# RODA Administrative Manual

[RODA](https://roda-community.org/#welcome) is a browser tool where you can upload SIPs and transform them to AIPs.

## Table of contents
- [Plugins](#plugins)
  * [Siegfried configuration](#siegfried-configuration)
  * [Unoconv configuration](#unoconv-configuration)
  * [Mandatory vs. optional ingest plugins](#mandatory-vs-optional-ingest-plugins)
  * [Remove unwanted files](#remove-unwanted-files)
  * [Meemoo descriptive metadata](#meemoo-descriptive-metadata)
  * [AIDA specific preservation actions](#aida-specific-preservation-actions)
    + [Create E-ARK AIP 2.0 manifest files (METS.xml)](#create-e-ark-aip-20-manifest-files--metsxml-)
    + [Image conversion (ImageMagick)](#image-conversion--imagemagick-)
    + [Office documents conversion (unoconv)](#office-documents-conversion--unoconv-)
  * [All commercial plugins](#all-commercial-plugins)
- [Data Management](#data-management)
  * [RODA API documentation](#roda-api-documentation)
  * [Solr querying](#solr-querying)
- [Features](#features)
  * [RODA AIP storage](#roda-aip-storage)
  * [RODA AIP editing](#roda-aip-editing)
  * [RODA AIP searching](#roda-aip-searching)
  * [RODA AIP plugins](#roda-aip-plugins)
  * [Activating full-text search](#activating-full-text-search)
  * [AIDA default ingest workflow](#aida-default-ingest-workflow)
  * [AIP pruning](#aip-pruning)
  * [Orphaned IPs](#orphaned-ips)
  * [Internal actions](#internal-actions)
  * [Preservation actions](#preservation-actions)
  * [IP meemoo status data](#ip-meemoo-status-data)
  * [Meemoo sync](#meemoo-sync)
    + [Submit to meemoo](#submit-to-meemoo)
    + [Prune](#prune)
    + [Restore from meemoo](#restore-from-meemoo)
  * [Access features](#access-features)
- [API examples](#api-examples)
  * [Change descriptive metadata](#change-descriptive-metadata)
- [SOLR examples](#solr-examples)
  * [Learn the number of files of each partner institution](#learn-the-number-of-files-of-each-partner-institution)

## Plugins

### Siegfried configuration

We normally use the Siegfried REST API, as the command bootstrap time per file is huge. We do an /identify/%s?base64=true&format=json and will keep the original Siegfried information under the representation other metadata. From it, we take the mime type, pronom, and format name and version if of the most prominent match. We currently don't use the basis, warning or other matches to record them in PREMIS.

Example:
```
{
  "filename": "/roda/data/storage/aip/3b6aeb0d-4c01-4c9b-a4fe-7541660dc8d5/representations/5c75eb81-84e4-498a-93a2-4551c25f6a3b/data/DILCISBOARD_E-ARK_AIP_1_0.pdf",
  "filesize": 2547324,
  "modified": "2021-09-14T03:20:22Z",
  "errors": "",
  "matches": [
    {
      "ns": "pronom",
      "id": "fmt/95",
      "format": "Acrobat PDF/A - Portable Document Format",
      "version": "1a",
      "mime": "application/pdf",
      "basis": "extension match pdf; byte match at [[0 8] [2461063 44] [2461112 69]]",
      "warning": ""
    }
  ]
}
```



### Unoconv configuration
  
By default, unoconv will pick files with the selected file name extension OR MIME types OR PRONOM IDs.
  
For additional formats (not in default configuration), you can add them via extension and it will still select the file even if the file does not have that extension if there is a mapping between the extension and the pronom identifier and the file without extension is identified with that pronom identifier.
  
The starting configuration for the unoconv plugin is:
  
```properties
##########################################################################
# Conversion plugins' supported INPUT formats (whitelist)
#
# If a conversion plugin does not specify its supported input formats
# it will accept all the formats provided via the UI
##########################################################################
core.tools.unoconvconvert.inputFormatExtensions = txt doc xls ppt html odt ods odp odg docx xlsx pptx csv xml png jpg jpeg wpd
core.tools.unoconvconvert.inputFormatMimetypes = image/gif image/tiff image/png image/jpeg text/plain text/csv text/html application/xml text/xml application/msword application/vnd.ms-excel   application/vnd.openxmlformats-officedocument.spreadsheetml.sheet application/vnd.ms-powerpoint application/vnd.openxmlformats-officedocument.presentationml.presentation application/vnd.oasis.opendocument.text application/vnd.oasis.opendocument.spreadsheet application/vnd.oasis.opendocument.presentation application/vnd.oasis.opendocument.graphics application/vnd.openxmlformats-officedocument.wordprocessingml.document application/vnd.openxmlformats-officedocument.spreadsheetml.sheet application/vnd.openxmlformats-officedocument.presentationml.presentation application/vnd.wordperfect
core.tools.unoconvconvert.inputFormatPronoms = x-fmt/111 fmt/101 x-fmt/394  
```
  
You can use the mapped values to specify which filetype you want to convert to which filetype. Current mappings between MIME types and extension and PRONOM identifiers and extensions for unoconv are:
  
```properties
##########################################################################
# Mappings between PRONOM Ids and file format extensions
#
# For each Pronom ID used in this file, a mapping line should be provided.
# This helps the conversion applications to better specify its input and
# output formats
##########################################################################
core.tools.pronom.fmt/14 = pdf
core.tools.pronom.fmt/15 = pdf
core.tools.pronom.fmt/16 = pdf
core.tools.pronom.fmt/17 = pdf
core.tools.pronom.fmt/18 = pdf
core.tools.pronom.fmt/19 = pdf
core.tools.pronom.fmt/20 = pdf
core.tools.pronom.fmt/558 = pdf
core.tools.pronom.fmt/559 = pdf
core.tools.pronom.fmt/560 = pdf
core.tools.pronom.fmt/561 = pdf
core.tools.pronom.fmt/562 = pdf
core.tools.pronom.fmt/563 = pdf
core.tools.pronom.fmt/564 = pdf
core.tools.pronom.fmt/565 = pdf
core.tools.pronom.fmt/276 = pdf
core.tools.pronom.fmt/95 = pdf
core.tools.pronom.fmt/354 = pdf
core.tools.pronom.fmt/476 = pdf
core.tools.pronom.fmt/477 = pdf
core.tools.pronom.fmt/478 = pdf
core.tools.pronom.fmt/479 = pdf
core.tools.pronom.fmt/480 = pdf
core.tools.pronom.fmt/481 = pdf
core.tools.pronom.fmt/493 = pdf
core.tools.pronom.fmt/144 = pdf
core.tools.pronom.fmt/145 = pdf
core.tools.pronom.fmt/146 = pdf
core.tools.pronom.fmt/147 = pdf
core.tools.pronom.fmt/148 = pdf
core.tools.pronom.fmt/157 = pdf
core.tools.pronom.fmt/158 = pdf
core.tools.pronom.fmt/488 = pdf
core.tools.pronom.fmt/489 = pdf
core.tools.pronom.fmt/490 = pdf
core.tools.pronom.fmt/491 = pdf
core.tools.pronom.fmt/492 = pdf

core.tools.pronom.fmt/101 = xml
core.tools.pronom.x-fmt/111 = txt
core.tools.pronom.x-fmt/394 = wpd


##########################################################################
# Mappings between Mimetypes and file format extensions
#
# For each mimetype used in this file, a mapping line should be provided.
# This helps the conversion applications to better specify its input and
# output formats
##########################################################################
core.tools.mimetype.application/pdf = pdf
core.tools.mimetype.text/plain = txt
core.tools.mimetype.application/msword = doc
core.tools.mimetype.application/vnd.ms-excel = xls
core.tools.mimetype.application/vnd.ms-powerpoint = ppt
core.tools.mimetype.text/html = html
core.tools.mimetype.application/vnd.oasis.opendocument.text = odt
core.tools.mimetype.application/vnd.oasis.opendocument.spreadsheet = ods
core.tools.mimetype.application/vnd.oasis.opendocument.presentation = odp
core.tools.mimetype.application/vnd.oasis.opendocument.graphics = odg
core.tools.mimetype.application/vnd.openxmlformats-officedocument.wordprocessingml.document = docx
core.tools.mimetype.application/vnd.openxmlformats-officedocument.spreadsheetml.sheet = xlsx
core.tools.mimetype.application/vnd.openxmlformats-officedocument.presentationml.presentation = pptx
core.tools.mimetype.application/rtf = rtf
core.tools.mimetype.application/vnd.wordperfect = wpd
core.tools.mimetype.image/gif = gif
core.tools.mimetype.image/png = png
core.tools.mimetype.image/tiff = tiff
core.tools.mimetype.image/jpeg = jpeg
```
  
If there are mappings missing between certain extension(s) and PRONOM identifiers and MIME type identifiers, you can choose to add them as a parameter.
  


### Mandatory vs. optional ingest plugins
  
Mandatory plugins have to run and if they fail they will stop fail the ingestion. Optional plugins will not fail ingestion if they fail.
	
For AIDA ingest workflow (1.0) the plugin optionality is as follows:
	
| Plugin                                          | Optionality |
|-------------------------------------------------|-------------|
| E-ARK SIP 2                                     | Mandatory   |
| Remove unwanted files                           | Optional    |
| AIP Virus check                                 | Optional    |
| Metadata validation                             | Mandatory   |
| Fixity information computation                  | Mandatory   |
| File format identification (Siegfried)          | Optional    |
| Verify user authorization                       | Mandatory   |
| Disposal schedule association via disposal rule | Optional    |
| Meemoo descriptive metadata                     | Mandatory   |
| Auto accept                                     | Mandatory   |



### Remove unwanted files
  
The following information is taken from the [AIDA Administrative Operations Manual](https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Referenced%20Files/MU221844%20-%20AIDA%20Administrative%20Operations%20Manual.pdf) by KEEPS.
	
This plugin checks through predetermined rules, if the AIP has any unwanted files. The rules configuration is under config named ingest.ignore, and contains the following default ones:
![image](https://user-images.githubusercontent.com/87436774/153424300-ee9b8ff0-424d-4aad-85bb-61f2eb470788.png)
  


### Meemoo descriptive metadata
  
The following information is taken from the [AIDA Administrative Operations Manual](https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Referenced%20Files/MU221844%20-%20AIDA%20Administrative%20Operations%20Manual.pdf) by KEEPS.
	
This plugin creates a descriptive metadata with information for __Meemoo__ API integration. After the execution of this plugin the AIP has a new descriptive metadata file named meemoo.xml.
![image](https://user-images.githubusercontent.com/87436774/153424457-2a30e994-4aaf-4854-8fcb-b1aab95f45cf.png)

This plugin will create a descriptive metadata file with the information represented above, such as the auto submission flag, if the AIP is pruned or not, the initial synchronization AIP status **“on_roda”** and the notification email.
  


### AIDA specific preservation actions
	
The following information is taken from the [AIDA Administrative Operations Manual](https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Referenced%20Files/MU221844%20-%20AIDA%20Administrative%20Operations%20Manual.pdf) by KEEPS.
	
The following additional plugins with preservation actions were added to the digital preservation repository solution for AIDA.
	
#### Create E-ARK AIP 2.0 manifest files (METS.xml)

Plugin that generates E-ARK AIP 2.0 manifest files ("METS.xml") from existing AIP information in the storage layer. This plugin only works with filesystem as the storage service.
	
#### Image conversion (ImageMagick)

ImageMagick is a tool that can read and write images in a variety of formats (over 200) including PNG, JPEG, JPEG-2000, GIF, TIFF, DPX, EXR, WebP, Postscript, PDF, and SVG. ImageMagick can also be used to resize, flip, mirror, rotate, distort, shear and transform images, adjust image colours, apply various special effects, or draw text, lines, polygons, ellipses and Bézier curves (e.g. set Command arguments to “ -resample 90” to resize the image to 90 dpi). The results of conversion will be placed on a new representation under the same Archival Information Package (AIP) where the files were originally found. A PREMIS event is also recorded after the task is run. For a full list of supported formats, please visit http://www.imagemagick.org/script/formats.php.
	
#### Office documents conversion (unoconv)
	
Converts office files using the “unoconv” (Universal Office Converter), which uses LibreOffice to convert Office files. The results of conversion will be placed on a new representation under the same Archival Information Package (AIP) where the files were originally found. A PREMIS event is also recorded after the task is run. “unoconv” is a tool that converts between any document format that OpenOffice understands. It uses OpenOffice's UNO bindings for non-interactive conversion of documents. Supported document formats include Open Document Format (odt), MS Word (doc), MS Office Open/MS OOXML (ooxml), Portable Document Format (pdf), HTML (html), XHTML (xhtml), RTF (rtf), Docbook (docbook), and more. The outcome of this task is the creation of a new OpenOffice (and thus unoconv) that supports various import and export formats. Not all formats that can be imported can be exported and vice versa. For a full list of supported formats, please visit - http://dag.wiee.rs/home-made/unoconv/.
	


### All commercial plugins
  
Info and documentation [here](https://github.com/Automatic-Ingest-Digital-Archives/SCALA/tree/main/Referenced%20Files/RODA%20plugins.pdf).
  


## Data Management

### RODA API documentation
  
[API documentation](https://demo.roda-community.org/api-docs/).
  


### Solr querying
  
URL: https://scala.meemoo.be/solr/#/.
  
Documentation: https://solr.apache.org/guide/7_7/index.html. For the standard operations, see https://solr.apache.org/guide/6_6/the-standard-query-parser.html
  
KEEP training Solr use cases and exercises: https://github.com/Automatic-Ingest-Digital-Archives/SCALA/tree/main/Referenced%20Files/Training%20Solr%20use%20cases.pdf.
  
KEEP training Solr answers: https://github.com/Automatic-Ingest-Digital-Archives/SCALA/tree/main/Referenced%20Files/Solr%20exercises%20answers.txt.



## Features

### RODA AIP storage
	
|Task||
|----|-----|
| Store AIP on meemoo | ![](https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Referenced%20Files/Pictures/meemoo.png)|
| Check AIP synchronization status |![image](https://user-images.githubusercontent.com/87436774/138085154-5db47ed5-c4f0-4396-99d7-8d5a180b0225.png)|
| Prune AIP in RODA|Pruning an AIP includes removing PREMIS files and other technical metadata. This results in pruned AIPs having less information for reporting. Therefore, pruning should generally not be done.</br>![image](https://user-images.githubusercontent.com/87436774/138085338-43ad9e04-92d5-424b-90fc-f5ef338734ce.png)|
| Restore pruned AIP representations from meemoo to in RODA|![image](https://user-images.githubusercontent.com/87436774/138085445-8f54ec7f-75f2-4563-bd16-19c03fc360da.png)|
		


### RODA AIP editing

|Task||
|----|-----|
| Start new process on IP | ![](https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Referenced%20Files/Pictures/conversion%20plugin%201.png)|
| File conversion | ![](https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Referenced%20Files/Pictures/conversion%20plugin%202.png)|
| Start new process on representation | ![](https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Referenced%20Files/Pictures/representation%201.png)|
| Create new representation manually ||
| Create new representation automatically after running plugin | ![](https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Referenced%20Files/Pictures/representation%202.png)</br>Deselect "Create dissemination".|
| Set status of representation | ![](https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Referenced%20Files/Pictures/representation%203.png)</br> ![](https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Referenced%20Files/Pictures/representation%204.png)|
	


### RODA AIP searching

|Task||
|----|-----|
| Catalogue | ![image](https://user-images.githubusercontent.com/87436774/138086822-128b2adc-c401-483c-a3bc-7180655b9415.png)|
| Assessment tab | ![image](https://user-images.githubusercontent.com/87436774/138086883-73410974-fccd-4df9-8ff0-19dfb341c96f.png)|
| Search facets | ![image](https://user-images.githubusercontent.com/87436774/138086934-89630095-3e7c-4363-a1c9-801ed48cc13a.png)|
| Search field | ![image](https://user-images.githubusercontent.com/87436774/138086973-c0cb4230-cce4-493b-a074-efe077477438.png)|
| Advanced search field | ![image](https://user-images.githubusercontent.com/87436774/138087110-fea88151-0a69-4704-874c-e0607ceb4759.png)|
	


### RODA AIP plugins
	
| Workflow| Details|
|---------|--------|
| AIP Virus check (ClamAV 0.103.3/26312/Mon Oct 4 09:03:30 2021)| Scans Information Package(s) for malicious software using the Antivirus application ClamAV. Clam AntiVirus (ClamAV) is a free and open-source, cross-platform antivirus software toolkit able to detect many types of malicious software, including viruses.If malicious software is detected a report will be generated and a PREMIS event will record this occurrence.Categories: validation, characterization |
| AIP batch export (1.0)| Exports selected AIP(s) to a ZIP file or folder on the server file system. To retrieve the results of the export action you must have access to the server file system.NOTE: This action can potentially generate a large amount of data. Make sure you select a destination folder that has enough storage space to accommodate the results of the export action.Categories: management |
| AIP corruption risk assessment (1.0)| Computes the fixity/checksum information of files inside an Archival Information Package (AIP) and verifies if this information differs from the information stored in the preservation metadata (i.e. PREMIS objects). If so, it creates a new risk called “File(s) corrupted due to hardware malfunction or human intervention“ and assigns the corrupted file to that risk in the Risk register.It also creates an incidence linked to the representation if a PREMIS file exists but the associated file does not. Within the repository, fixity checking is used to ensure that digital files have not been affected by data rot or other digital preservation dangers. By itself, fixity checking does not ensure the preservation of a digital file. Instead, it allows a repository to identify which corrupted files to replace with a clean copy from the producer or from a backup.Categories: risk management|
| Create E-ARK AIP manifest files (METS.xml) (1.0)| Plugin that generates E-ARK AIP manifest files ("METS.xml") from existing AIP information in the storage layer. This plugin only works with filesystem as the storage service.Categories: misc |
| Create E-ARK DIP manifest files (METS.xml) (1.0)| Plugin that generates E-ARK DIP manifest files ("METS.xml") from existing AIP information in the storage layer. This plugin only works with filesystem as the storage service.Categories: dissemination|
| File format identification (Siegfried) (1.9.1 w/ DROID_SignatureFile_V97) | Identifies the file format and version of data files included in Information Packages using the Siegfried tool (a signature-based file format identification tool that supports PRONOM identifiers and Mimetypes).The task updates PREMIS objects metadata in the Information Package to store the results of format identification. A PREMIS event is also recorded after the task is run.Categories: format identification, characterization |
| Fixity information computation (1.0)| Computes file fixity information (also known as checksum) for all data files within an AIP, representation or file and stores this information in PREMIS objects within the corresponding entity. This task uses SHA-256 as the default checksum algorithm, however, other algorithms can be configured in “roda-core.properties”.File fixity is the property of a digital file being fixed, or unchanged. “AIP corruption risk assessment” is the process of validating that a file has not changed or been altered from a previous state. In order to validate the fixity of an AIP or file, fixity information has to be generated beforehand.Categories: characterization|
| Image conversion (imagemagick) (6.9.11-60)| ImageMagick is a tool that can read and write images in a variety of formats (over 200) including PNG, JPEG, JPEG-2000, GIF, TIFF, DPX, EXR, WebP, Postscript, PDF, and SVG.ImageMagick can also be used to resize, flip, mirror, rotate, distort, shear and transform images, adjust image colours, apply various special effects, or draw text, lines, polygons, ellipses and Bézier curves (e.g. set Command arguments to “ -resample 90” to resize the image to 90 dpi).The results of conversion will be placed on a new representation under the same Archival Information Package (AIP) where the files were originally found. A PREMIS event is also recorded after the task is run.For a full list of supported formats, please visit http://www.imagemagick.org/script/formats.phpCategories: conversion, dissemination|
| Inventory report (1.0)| Creates a report in CSV format that includes a listing of all AIP and its inner files (data and metadata) which also includes some of their technical properties (e.g. sipId, aipId, representationId, filePath, SHA-256, MD5, SHA-1). The report will be stored in a folder on the server side as defined by the user. To obtain the report, one needs access to the storage layer of the repository server.This report may be used to validate the completeness and correctness of an ingest process.Categories: management|
| Metadata validation (1.0) | Checks if the descriptive metadata included in the Information Package is present, and if it is valid according to the XML Schemas installed in the repository. A validation report is generated indicating which Information Packages have valid and invalid metadata.Categories: validation, characterization|
| Move orphan(s) to a parent node (1.0) | Moves selected AIP(s) that are also orphans, i.e. AIPs whose direct ancestor in the catalogue hierarchy does not exist (except root level nodes) to a new parent node defined by the user.This task aims to fix problems that may occur when SIPs are ingested but not all the necessary items to construct the catalogue hierarchy have been received or properly ingested.Categories: management |
| Office documents conversion (unoconv) (7.0.4.2) | Converts office files using the “unoconv” (Universal Office Converter). The results of conversion will be placed on a new representation under the same Archival Information Package (AIP) where the files were originally found. A PREMIS event is also recorded after the task is run.“unoconv” is a tool that converts between any document format that OpenOffice understands. It uses OpenOffice's UNO bindings for non-interactive conversion of documents.Supported document formats include Open Document Format (odt), MS Word (doc), MS Office Open/MS OOXML (ooxml), Portable Document Format (pdf), HTML (html), XHTML (xhtml), RTF (rtf), Docbook (docbook), and more.The outcome of this task is the creation of a new OpenOffice (and thus unoconv) support various import and export formats. Not all formats that can be imported can be exported and vice versa. For a full list of supported formats, please visit - http://dag.wiee.rs/home-made/unoconv/Categories: conversion, dissemination |
| Prune AIP representations (1.0) | This plugin will remove all representations from the AIPCategories: Meemoo |
| Rebuild AIP index (1.0) | Clears the index and recreates it from actual physical data that exists on the storage. This task aims to fix inconsistencies between what is shown in the graphical user interface of the repository and what is actually kept at the storage layer. Such inconsistencies may occur for various reasons, e.g. index corruption, ungraceful shutdown of the repository, etc.Categories: reindex|
| Rebuild preservation AIP event index (1.0)| Clears the index and recreates it from actual physical data that exists on the storage. This task aims to fix inconsistencies between what is shown in the graphical user interface of the repository and what is actually kept at the storage layer. Such inconsistencies may occur for various reasons, e.g. index corruption, ungraceful shutdown of the repository, etc.Categories: reindex|
| Restore pruned representations from Meemoo (1.0)| Fetch the representations from Meemoo API and restores back to RODA. A PREMIS event is recorded after the task is run.Categories: Meemoo |
| Risk association (1.0)| Associates selected items to existing risks in the Risk registry (as risk incidences).This task is convenient when the preservation expert wants to associate a set of items (e.g. AIPs, representations or files) to a risk to be mitigated in the near future.As an example, if the designated community of the repository provides feedback that a given format under a certain collection is not being displayed properly on the graphical user interface of the repository, then the preservation expert may want to mark these files to be targeted by a preservation action (e.g. generate new representations for access purposes).Categories: risk management |
| Submit AIP to Meemoo (1.0)| AIP submission plugin for MEEMOO integrated serviceCategories: Meemoo|
| Verify user authorization (1.0) | Checks if the user has enough permissions to place the AIP under the desired node in the classification schemeCategories: validation |
	


### Activating full-text search
  
You need to activate the full-text by running the full-text plugin, either on ingest or afterwards (e.g. restore from meemoo). The plugin is called "Feature extraction (Apache Tika)" and runs Apache Tika to perform, optionally:

* Feature extraction: Perform feature extraction from files. This will extract properties such as number of pages, width, height, colour space, etc.
* Full text extraction: Extracts full text from document/textual files. Extracted text is used to perform full-text searching on the catalogue.

Please note that extracting full text will require much more index size capabilities.
  


### AIDA default ingest workflow
  
The AIDA ingest workflow (1.0) runs the following plugins in order:
	
![image](https://user-images.githubusercontent.com/87436774/148739625-e2563688-5a28-4e7b-a7a5-9ffb5a5d7131.png)



### AIP pruning

Pruning is the process of removing all representations from an AIP. The aim is to save storage space while still leaving searchable metadata. Later one can unprune an AIP to restore all representations.

However, in RODA, pruning also removes representation level PREMIS files and other technical metadata. This results in pruned AIPs having less information for reporting. Therefore, pruning in RODA should generally not be done.
  


### Orphaned IPs

If a child IP (IP with reference to a parent IP) is accepted in the catalogue, but its parent is not (or not yet), it will be an orphan IP. Orphaned IPs appear under a ghost node in the organization repository.
  
![image](https://user-images.githubusercontent.com/87436774/145191783-931fe3d9-ccd2-42fe-83f9-eb5d3c990c49.png)

It is currently unclear who you can easily search/retrieve all orphaned IPs.
  


### Internal actions
  
Internal actions are complex tasks performed by the repository as background jobs that enhance the user experience by not blocking the user interface during long lasting operations. Examples of such operations are: moving AIPs, reindexing parts of the repository, or deleting a large number of files. Each operation is called a job, and each job leads to one or more reports (one report per AIP).

Job example:
  
![image](https://user-images.githubusercontent.com/87436774/145371252-1d7524a7-38be-4ead-a3d1-c4b2d5e1ea76.png)
  
Report example:
  

| id                                                                                                             | jobId                                | jobName       | sourceObjectId                       | sourceObjectOriginalName    | sourceObjectLabel            | sourceObjectClass | sourceObjectOriginalIds              | outcomeObjectId             | outcomeObjectLabel           | outcomeObjectClass | outcomeObjectState                 | title                        | dateCreated                  | dateUpdated | completionPercentage | stepsCompleted | totalSteps                                             | plugin                             | pluginName | pluginVersion | pluginState                                                                      | pluginDetails | htmlPluginDetails | successfulPlugins | unsuccessfulPlugins | reports |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------|---------------|--------------------------------------|-----------------------------|------------------------------|-------------------|--------------------------------------|-----------------------------|------------------------------|--------------------|------------------------------------|------------------------------|------------------------------|-------------|----------------------|----------------|--------------------------------------------------------|------------------------------------|------------|---------------|----------------------------------------------------------------------------------|---------------|-------------------|-------------------|--------|---------|
| 189796fb-007a-465d-9ac3-723a73705036-c084632a-5e66-4ccd-a9be-6ab01cf5950e-c084632a-5e66-4ccd-a9be-6ab01cf5950e | 189796fb-007a-465d-9ac3-723a73705036 | AIP appraisal | c084632a-5e66-4ccd-a9be-6ab01cf5950e | ingenium18[047]05 (kopie) 2 | org.roda.core.data.v2.ip.AIP | []                | c084632a-5e66-4ccd-a9be-6ab01cf5950e | ingenium18[047]05 (kopie) 2 | org.roda.core.data.v2.ip.AIP | CREATED            | Update AIP permissions recursively | Wed Dec 08 07:59:22 UTC 2021 | Wed Dec 08 07:59:23 UTC 2021 | 100         | 1                    | 1              | org.roda.core.plugins.plugins.internal.AppraisalPlugin | Update AIP permissions recursively | 1.0        | SUCCESS       | The AIP 'c084632a-5e66-4ccd-a9be-6ab01cf5950e' was accepted into the repository. | FALSE         | []                | []                | [Report [id=189796fb-007a-465d-9ac3-723a73705036-c084632a-5e66-4ccd-a9be-6ab01cf5950e-c084632a-5e66-4ccd-a9be-6ab01cf5950e, jobId=189796fb-007a-465d-9ac3-723a73705036, sourceObjectId=c084632a-5e66-4ccd-a9be-6ab01cf5950e, sourceObjectClass=org.roda.core.data.v2.ip.AIP, sourceObjectOriginalIds=[], outcomeObjectId=c084632a-5e66-4ccd-a9be-6ab01cf5950e, outcomeObjectClass=org.roda.core.data.v2.ip.AIP, outcomeObjectState=CREATED, title=Update AIP permissions recursively, dateCreated=Wed Dec 08 07:59:22 UTC 2021, dateUpdated=Wed Dec 08 07:59:23 UTC 2021, completionPercentage=0, stepsCompleted=0, totalSteps=1, plugin=org.roda.core.plugins.plugins.internal.AppraisalPlugin, pluginName=Update AIP permissions recursively, pluginVersion=1.0, pluginState=SUCCESS, pluginIsMandatory=true, pluginDetails=The AIP 'c084632a-5e66-4ccd-a9be-6ab01cf5950e' was accepted into the repository., htmlPluginDetails=false, reports=[]]] |         |
| 189796fb-007a-465d-9ac3-723a73705036-5590bdbf-332f-4965-8918-c77740d22459-5590bdbf-332f-4965-8918-c77740d22459 | 189796fb-007a-465d-9ac3-723a73705036 | AIP appraisal | 5590bdbf-332f-4965-8918-c77740d22459 | ingenium18[047]05 (kopie)   | org.roda.core.data.v2.ip.AIP | []                | 5590bdbf-332f-4965-8918-c77740d22459 | ingenium18[047]05 (kopie)   | org.roda.core.data.v2.ip.AIP | CREATED            | Update AIP permissions recursively | Wed Dec 08 07:59:22 UTC 2021 | Wed Dec 08 07:59:22 UTC 2021 | 100         | 1                    | 1              | org.roda.core.plugins.plugins.internal.AppraisalPlugin | Update AIP permissions recursively | 1.0        | SUCCESS       | The AIP '5590bdbf-332f-4965-8918-c77740d22459' was accepted into the repository. | FALSE         | []                | []                | [Report [id=189796fb-007a-465d-9ac3-723a73705036-5590bdbf-332f-4965-8918-c77740d22459-5590bdbf-332f-4965-8918-c77740d22459, jobId=189796fb-007a-465d-9ac3-723a73705036, sourceObjectId=5590bdbf-332f-4965-8918-c77740d22459, sourceObjectClass=org.roda.core.data.v2.ip.AIP, sourceObjectOriginalIds=[], outcomeObjectId=5590bdbf-332f-4965-8918-c77740d22459, outcomeObjectClass=org.roda.core.data.v2.ip.AIP, outcomeObjectState=CREATED, title=Update AIP permissions recursively, dateCreated=Wed Dec 08 07:59:22 UTC 2021, dateUpdated=Wed Dec 08 07:59:22 UTC 2021, completionPercentage=0, stepsCompleted=0, totalSteps=1, plugin=org.roda.core.plugins.plugins.internal.AppraisalPlugin, pluginName=Update AIP permissions recursively, pluginVersion=1.0, pluginState=SUCCESS, pluginIsMandatory=true, pluginDetails=The AIP '5590bdbf-332f-4965-8918-c77740d22459' was accepted into the repository., htmlPluginDetails=false, reports=[]]] |         |
  


### Preservation actions
  
Preservation actions are tasks performed on the contents of the repository that aim to enhance the accessibility of archived files or to mitigate digital preservation risks. Within RODA, preservation actions are handled by a job execution module. The job execution module allows the repository manager to run actions over a given set of data (AIPs, representations or files). Preservation actions include format conversions, checksum verifications, reporting (e.g. to automatically send SIP acceptance/rejection emails), virus checks, etc. Each operation is called a job, and each job leads to one or more reports (one report per AIP).
  
- Some actions are presented as preservation actions although they are not strictly for preservation, like re-index actions, and these do not create a preservation event.
- Other actions, which might be construed as preservation actions, or at least accessory to preservation actions, like the inventory report, also do not create preservation events.
- Mainly, we create preservation events for actions that change the data (like conversions that create representations) or for actions that enrich the metadata (like generation of fixity information and file format identification) or for actions that validate the data (fixity checks, file format validation).
  
Report export example:
  
| id | jobId | jobName | sourceObjectId | sourceObjectOriginalName | sourceObjectLabel | sourceObjectClass | sourceObjectOriginalIds | outcomeObjectId | outcomeObjectLabel | outcomeObjectClass | outcomeObjectState | title | dateCreated | dateUpdated | completionPercentage | stepsCompleted | totalSteps | plugin | pluginName | pluginVersion | pluginState | pluginDetails | htmlPluginDetails | successfulPlugins | unsuccessfulPlugins | reports |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|----|-----|-----|-----|----|-----|-----|-------|-------|---|--|-----|--------|------|------------|----|
| c0ed7762-1f11-4ec6-9461-23d0dde7a0f5-40bdb2ff-f314-3178-87c2-35005e9b6137-40bdb2ff-f314-3178-87c2-35005e9b6137 | c0ed7762-1f11-4ec6-9461-23d0dde7a0f5 | Office documents conversion (unoconv) (7.0.4.2) | 40bdb2ff-f314-3178-87c2-35005e9b6137 |                          | PV INSCH.DOC                        | org.roda.core.data.v2.ip.File | []                      | 40bdb2ff-f314-3178-87c2-35005e9b6137 |                    | org.roda.core.data.v2.ip.DIP | ACTIVE             | Office documents conversion (unoconv) | Tue Nov 23 16:37:05 UTC 2021 | Tue Nov 23 16:37:05 UTC 2021 | 100                  | 1              | 1          | org.roda.core.plugins.external.UnoconvConvertPlugin | Office documents conversion (unoconv) | 7.0.4.2       | SUCCESS     | This file was ignored. | FALSE             | []                | []                  | [Report   [id=c0ed7762-1f11-4ec6-9461-23d0dde7a0f5-40bdb2ff-f314-3178-87c2-35005e9b6137-40bdb2ff-f314-3178-87c2-35005e9b6137,   jobId=c0ed7762-1f11-4ec6-9461-23d0dde7a0f5,   sourceObjectId=40bdb2ff-f314-3178-87c2-35005e9b6137,   sourceObjectClass=org.roda.core.data.v2.ip.File, sourceObjectOriginalIds=[],   outcomeObjectId=40bdb2ff-f314-3178-87c2-35005e9b6137,   outcomeObjectClass=org.roda.core.data.v2.ip.DIP, outcomeObjectState=ACTIVE,   title=Office documents conversion (unoconv), dateCreated=Tue Nov 23 16:37:05   UTC 2021, dateUpdated=Tue Nov 23 16:37:05 UTC 2021, completionPercentage=0,   stepsCompleted=0, totalSteps=1,   plugin=org.roda.core.plugins.external.UnoconvConvertPlugin, pluginName=Office   documents conversion (unoconv), pluginVersion=7.0.4.2, pluginState=SUCCESS,   pluginIsMandatory=true, pluginDetails=This file was ignored.,   htmlPluginDetails=false, reports=[]]] |
| c0ed7762-1f11-4ec6-9461-23d0dde7a0f5-56fa195f-fc2a-39a6-b113-45eebd46c72f-56fa195f-fc2a-39a6-b113-45eebd46c72f | c0ed7762-1f11-4ec6-9461-23d0dde7a0f5 | Office documents conversion (unoconv) (7.0.4.2) | 56fa195f-fc2a-39a6-b113-45eebd46c72f |                          | PV_INSCH.DOC                        | org.roda.core.data.v2.ip.File | []                      | 56fa195f-fc2a-39a6-b113-45eebd46c72f |                    | org.roda.core.data.v2.ip.DIP | ACTIVE             | Office documents conversion (unoconv) | Tue Nov 23 16:37:05 UTC 2021 | Tue Nov 23 16:37:05 UTC 2021 | 100                  | 1              | 1          | org.roda.core.plugins.external.UnoconvConvertPlugin | Office documents conversion (unoconv) | 7.0.4.2       | SUCCESS     | This file was ignored. | FALSE             | []                | []                  | [Report   [id=c0ed7762-1f11-4ec6-9461-23d0dde7a0f5-56fa195f-fc2a-39a6-b113-45eebd46c72f-56fa195f-fc2a-39a6-b113-45eebd46c72f,   jobId=c0ed7762-1f11-4ec6-9461-23d0dde7a0f5,   sourceObjectId=56fa195f-fc2a-39a6-b113-45eebd46c72f,   sourceObjectClass=org.roda.core.data.v2.ip.File, sourceObjectOriginalIds=[],   outcomeObjectId=56fa195f-fc2a-39a6-b113-45eebd46c72f,   outcomeObjectClass=org.roda.core.data.v2.ip.DIP, outcomeObjectState=ACTIVE,   title=Office documents conversion (unoconv), dateCreated=Tue Nov 23 16:37:05   UTC 2021, dateUpdated=Tue Nov 23 16:37:05 UTC 2021, completionPercentage=0,   stepsCompleted=0, totalSteps=1,   plugin=org.roda.core.plugins.external.UnoconvConvertPlugin, pluginName=Office   documents conversion (unoconv), pluginVersion=7.0.4.2, pluginState=SUCCESS,   pluginIsMandatory=true, pluginDetails=This file was ignored.,   htmlPluginDetails=false, reports=[]]] |
  


### IP meemoo status data
  
RODA keeps track of the following data about IPs in regards to their status on meemoo.

![image](https://user-images.githubusercontent.com/87436774/145192766-db9de476-1742-4c56-8866-029c5f809476.png)
  
1. AIP Version - The version of the IP at meemoo.
2. Identifier - The organization's identifier in the meemoo repository.
3. Synchronization AIP Status (On RODA / On meemoo)
4. Last synchronization date into Meemoo (datetime stamp)
5. Pruned (Yes / No)
6. Archive status (None / On disk)
7. Automatically submitted after ingestion (Yes / No)
  


### Meemoo sync
	
The following information is taken from the [AIDA Administrative Operations Manual](https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Referenced%20Files/MU221844%20-%20AIDA%20Administrative%20Operations%20Manual.pdf) by KEEPS.
  
Operations relative to submitting or updating records into meemoo storage on E-ARK AIP 2.0.4 format, or to restore all records from AIPs archived in meemoo.
	
![image](https://user-images.githubusercontent.com/87436774/153422062-0bab245d-2419-4107-a995-4ebde604256a.png)

This figure depicts all metadata changes during the tasks after the AIP ingest process. During the ingest process the meemoo descriptive metadata file is created. This file has the Synchronization AIP status with the value **“on_roda”**, during the submission to meemoo, if prune representations are activated, the meemoo metadata changes the Synchronization AIP status to **“on_meemoo”**, and add the submission date and prune date to the metadata file.
	
If prune representations are deactivated, the file only adds the submission date to the metadata file. When the status of the AIP is **“on_meemoo”** the Restore operation, as it can be seen above, changes the status again to **“on_roda”** and adds a restore date to the metadata file, and the prune flag is set to false, because the representations of the AIP are again available in RODA.
	
If the submission date of the AIP is after the last update date and the AIP has representations, we can prune the representations from RODA, which changes the metadata of the AIP to **“on_meemoo”**.
	
Preservation action should only be executed when the AIP is **“on_roda”**, as this is when the information is available. A preservation action might change the AIP, which should then be re-submitted to RODA.
	
#### Submit to meemoo
	
The first check when submitting the AIP to Meemoo is to check if the AIP has representations. If the AIP has representations the next step is check if it is possible to submit the AIP to meemoo, in this check it is verified if the AIP has already been submitted and if the AIP is still being processed by meemoo.
	
After checking that the AIP can be submitted, it is checked if it is possible to create the sidecar, for it to be possible it is necessary if the AIP metadata has the mandatory fields, being them:
	
* ead/archdesc/did/repository/corpname
* ead/archdesc/did/unittitle
* ead/archdesc/did/unitid@label='localId'
* ead/archdesc/did/origination@label='creator'/name
* ead/archdesc/did/origination@label='producer'/name
	
![image](https://user-images.githubusercontent.com/87436774/153422777-322dc4e8-d35f-4dd5-9c71-4c6a11e95a4a.png)

The code above shows the meemoo sidecar and the rules to create the sidecar, as well as the mandatory fields described above.
	
After these verifications the “Create METS” plugin is run, this plugin will create or update the METS file in AIP making it according to the E-ARK AIP 2.0.4 specification. If the creation was successful the submission will continue, if the creation fails the submission also fails.
	
Like was explained above, initially the state is **"on_roda"** when AIP is submitted with the pruning option enabled the state is changed to **"on_meemoo"** because the AIP representations are removed from RODA. If the prune option is disabled, RODA keeps the AIP representations and for this reason the state remains **"on_roda"**. This plugin creates after submission a preservation event of the type **“Transfer”** at the repository level.
	
#### Prune
	
The Pruning Representations only can execute if the aip is already on meemoo and the last update date is lower than the submission date of the AIP. If passes this two conditions this plugin will check if the AIP has representations, if it has representations it removes these representations from the AIP and changes the meemoo metadata with the new state of the AIP which is pruned.
![image](https://user-images.githubusercontent.com/87436774/153423290-2d65a613-12fa-4183-9164-6e859f76111b.png)

Before the process of Prune, the tag **<prune>** on meemoo.xml file has the value false, the AIP synchronization status is **“on_roda”** and doesn't exist as a prune date tag as can be seen in code above. After that the value of the tag **<prune>** will be true, the synchronization AIP status changes to **“on_meemoo”** and is added to the meemoo.xml file the prune date of the AIP as can be seen in code below.
![image](https://user-images.githubusercontent.com/87436774/153423497-502b5509-f0c0-4019-b3df-608c64a773bd.png)

This plugin creates a preservation event of the type **“Destruction”** at the repository level.
	
#### Restore from meemoo
	
The Restore Pruned Representations plugin checks if the AIP is saved on Meemoo, if the AIP has been found it looks for the last version of it and starts the process of restoring the representations of the AIP. This process replaces the old AIP with the AIP with representations.
	
The initial state as explained above is **“on_meemoo”**, after the process of restoring the state is changed to **“on_roda”** and is added a restore date to the metadata file and the prune tag changes to false. This change occurs because the RODA has the AIP representations stored again in the system, and for this reason the state is **“on_roda”**.
	
After this process of restore is complete the plugin executes three additional plugins being them:

* Fixity Check plugin
* File Format Identification Plugin
* Virus check Plugin

This plugin like the submission plugin creates a preservention event of the type **“Transfer”** at the repository level.
	


### Access features
	
The following information is taken from the [AIDA Administrative Operations Manual](https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Referenced%20Files/MU221844%20-%20AIDA%20Administrative%20Operations%20Manual.pdf) by KEEPS.
	
The advanced search and facets have been customized for this project, adding search for the following additional attributes:
	
* Meemoo AIP version
* Meemoo Identifier
* Meemoo Archive Status
* Producer

In terms of facets, the attributes added are the following:

* Meemoo prune
* Meemoo archive status
	

	
## API examples
	
### Get descriptive metadata

Example: https://scala.meemoo.be/api/v1/aips/4e222850-4322-43d2-96d6-1b5a49751bd6/descriptive_metadata/scala.xml?metadataType=EAD&metadataVersion=2002&acceptFormat=bin&lang=en_US
	
acceptFormat=bin ensures you get the contents of the scala.xml file for the AIP.

### Change descriptive metadata
Descriptive metadata can be changed by executing a PUT-request on the RODA API. You cannot change one metadata-element. You need to update a complete descriptive metadata file.

Impact on the AIP:
* The old metadata file is deleted and replaced with the new metadata file
* An updateAIPDescriptiveMetadataFile log entry is created
* NO preservation metadata are created --> This is bad and must be changed in future
	
Changing metadata files by API means that these won't go through a validation process! You need to know what you are doing. Always preserve an original copy of them.
Do not really use this until an 'update' preservation event is being generated after changing descriptive metadata.
	
**method**

```python
import requests

'''user input about the new metadata file'''
metadata_file_name = 'scala_update.xml' # This does not affect name of the file in the AIP. This remains scala.xml 
metadata_file_object = open(r'C:\Users\Wim Lo\Downloads\scala_update.xml','rb')
content_type = 'text/xml' # optional (probably)

'''user input about the AIP that is affected, that will be used in the request URL'''
aip_id = "350e4deb-e9ad-46cd-8673-9aab6c5776b0"
metadata_id = "scala.xml" # This will be unchanged after PUT-request
metadataType = "EAD"
metadataVersion = "2002"
acceptFormat = 'json'

'''Creation of all the request information for the API-call'''
url_form = "https://scala.meemoo.be/api/v1/aips/{aip_id}/descriptive_metadata/{metadata_id}?metadataType={metadataType}&metadataVersion={metadataVersion}&acceptFormat={acceptFormat}"
url = url_form.format(aip_id = aip_id, 
                      metadata_id = metadata_id, 
                      metadataType = metadataType, 
                      metadataVersion = metadataVersion,
                      acceptFormat = acceptFormat
                     )
# Roda's API only supports files sent in formData or a Multipart Encoded file
# See: https://docs.python-requests.org/en/latest/user/quickstart/#post-a-multipart-encoded-file
# See also second response in https://stackoverflow.com/questions/12385179/how-to-send-a-multipart-form-data-with-requests-in-python
files = {'file': (metadata_file_name,metadata_file_object,content_type)}

headers = {
  'Authorization': 'Some Base 64 encoded credentials', #alternatively, use Requests' Auth parameter
}

'''Call to the API'''
response = requests.request("PUT", url, headers=headers, files=files)

print(response)
print(response.text)
```
## SOLR examples

### Learn the number of files of each partner institution
You can search by 
* the main AIP UUID (field 'ancestors'), not safe since this excludes AIPs with ghost nodes/unknown ancestors, like https://scala.meemoo.be/#browse/837e4fb8-c18c-4846-815a-de761612ccc5
* permission group (field: 'permission_groups_READ'), safest

On main AIP UUID (example of AMVB main AIP): 
https://scala.meemoo.be/solr/File/select?indent=true&q.op=AND&q=ancestors%3Aed3964e1-d8a7-4786-a594-8f87c08a90f5&useParams=

```json
"response":{
  "numFound":86091,
  "start":0,
  "maxScore":1.2225661,
  "numFoundExact":true,
  "docs":['list of files']
```

On permission group (example of Group 'Curator-AMVB'): 
https://scala.meemoo.be/solr/File/select?indent=true&q.op=AND&q=permission_groups_READ%3ACurator-AMVB&useParams=

```json
"response":{
  "numFound":86091,
  "start":0,
  "maxScore":1.2225661,
  "numFoundExact":true,
  "docs":['list of files']
```
