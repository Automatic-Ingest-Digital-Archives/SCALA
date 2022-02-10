# RODA Administrative Manual

## Plugin Documentation

## Data Management

###
<details><summary><b>RODA AIP storage</b></summary>
	
|Task||
|----|-----|
| Store AIP on meemoo | ![](https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Referenced%20Files/Pictures/meemoo.png)|
| Check AIP synchronization status |![image](https://user-images.githubusercontent.com/87436774/138085154-5db47ed5-c4f0-4396-99d7-8d5a180b0225.png)|
| Prune AIP in RODA|Pruning an AIP includes removing PREMIS files and other technical metadata. This results in pruned AIPs having less information for reporting. Therefore, pruning should generally not be done.</br>![image](https://user-images.githubusercontent.com/87436774/138085338-43ad9e04-92d5-424b-90fc-f5ef338734ce.png)|
| Restore pruned AIP representations from meemoo to in RODA|![image](https://user-images.githubusercontent.com/87436774/138085445-8f54ec7f-75f2-4563-bd16-19c03fc360da.png)|
		
</details>

###
<details><summary><b>RODA AIP editing</b></summary>

|Task||
|----|-----|
| Start new process on IP | ![](https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Referenced%20Files/Pictures/conversion%20plugin%201.png)|
| File conversion | ![](https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Referenced%20Files/Pictures/conversion%20plugin%202.png)|
| Start new process on representation | ![](https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Referenced%20Files/Pictures/representation%201.png)|
| Create new representation manually ||
| Create new representation automatically after running plugin | ![](https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Referenced%20Files/Pictures/representation%202.png)</br>Deselect "Create dissemination".|
| Set status of representation | ![](https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Referenced%20Files/Pictures/representation%203.png)</br> ![](https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Referenced%20Files/Pictures/representation%204.png)|
	
</details>

###
<details><summary><b>RODA AIP searching</b></summary>

|Task||
|----|-----|
| Catalogue | ![image](https://user-images.githubusercontent.com/87436774/138086822-128b2adc-c401-483c-a3bc-7180655b9415.png)|
| Assessment tab | ![image](https://user-images.githubusercontent.com/87436774/138086883-73410974-fccd-4df9-8ff0-19dfb341c96f.png)|
| Search facets | ![image](https://user-images.githubusercontent.com/87436774/138086934-89630095-3e7c-4363-a1c9-801ed48cc13a.png)|
| Search field | ![image](https://user-images.githubusercontent.com/87436774/138086973-c0cb4230-cce4-493b-a074-efe077477438.png)|
| Advanced search field | ![image](https://user-images.githubusercontent.com/87436774/138087110-fea88151-0a69-4704-874c-e0607ceb4759.png)|
	
</details>

###
<details><summary><b>RODA AIP plugins</b></summary>
	
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
	
</details>
