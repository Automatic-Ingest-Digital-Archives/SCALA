## RODA is a browser tool where you can upload SIPs and transform them to AIPs.

###
<details><summary><b>To use RODA</b></summary>
  
1. Go to https://roda-community.org/#welcome.
  
</details>

##
<details><summary><b>RODA API documentation</b></summary>
  
[API documentation](https://demo.roda-community.org/api-docs/).
  
</details>

##
<details><summary><b>Siegfried configuration</b></summary>

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

</details>

##
<details><summary><b>Unoconv configuration</b></summary>
  
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
  
</details>

##
<details><summary><b>Metadata format configuration</b></summary>

RODA supports any descriptive metadata format (i.e. Descriptive Information as stated in the OAIS) as long as it represented by an XML file. If you have a descriptive metadata format that is not based on XML (e.g. CSV, JSON, MARC21, etc.), you will have to convert it to XML before you can use in RODA. Several tools exist on the Web that allow you to convert most data formats into XML.

Once you have your metadata in XML you are ready to package it into a Submission Information Package (SIP) and ingest it on the repository. Alternatively, you may want to create a metadata file directly on the repository by using the functionality provided by the Catalogue. When the metadata format is new to RODA, the repository will do its best to support without the need to do any reconfiguration of system.
  
[Main documentation](https://scala.meemoo.be/#theme/Metadata_Formats.md).
  
The off-the-shelf configurations for EAD 2002 are:
  
* Validation schema: https://github.com/keeps/roda/blob/master/roda-core/roda-core/src/main/resources/config/schemas/ead_2002.xsd
* Visualization stylesheet: https://github.com/keeps/roda/blob/master/roda-ui/roda-wui/src/main/resources/config/crosswalks/dissemination/html/ead_2002.xslt
* Indexing stylesheet: https://github.com/keeps/roda/blob/master/roda-core/roda-core/src/main/resources/config/crosswalks/ingest/ead_2002.xslt
* Editing template: https://github.com/keeps/roda/blob/master/roda-ui/roda-wui/src/main/resources/config/templates/ead_2002.xml.hbs
* Destruction metadata pruning rules: https://github.com/keeps/roda/blob/master/roda-core/roda-core/src/main/resources/config/disposal/destruction/ead_2002.xslt
* Translations (English, other files for other languages) - Title: https://github.com/keeps/roda/blob/98edeaa80218fc7fd7bdeda7c6d90ed2365c78bb/roda-ui/roda-wui/src/main/resources/config/i18n/ServerMessages.properties#L292
* Translations (English, other files for other languages) - Fields: https://github.com/keeps/roda/blob/98edeaa80218fc7fd7bdeda7c6d90ed2365c78bb/roda-ui/roda-wui/src/main/resources/config/i18n/ServerMessages.properties#L303-L418
* Settings - adding metadata schema: https://github.com/keeps/roda/blob/b302d503400decce9fc6c632e3b03b2b135f2949/roda-ui/roda-wui/src/main/resources/config/roda-wui.properties#L242
 
The specific setting of level and title in the search results, pertains to the "level" and "title" indexed fields, defined at:
  
* Level: https://github.com/keeps/roda/blob/master/roda-core/roda-core/src/main/resources/config/crosswalks/ingest/ead_2002.xslt#L343-L356
* Title: https://github.com/keeps/roda/blob/master/roda-core/roda-core/src/main/resources/config/crosswalks/ingest/ead_2002.xslt#L15-L19

To define advanced search fields and fields of the search results:

* Advanced search fields: https://github.com/keeps/roda/blob/master/roda-ui/roda-wui/src/main/resources/config/roda-wui.properties#L261-L354
* Search and catalogue searching results configuration: https://github.com/keeps/roda/blob/master/roda-ui/roda-wui/src/main/resources/config/roda-wui.properties#L910-L1048
* Facets: https://github.com/keeps/roda/blob/master/roda-ui/roda-wui/src/main/resources/config/roda-wui.properties#L1585-L1650

Other configurations available for other lists that present AIPs either than the Search and Catalogue pages.
  
</details>

##
<details><summary><b>Restart failed/interrupted ingest processes</b></summary>
  
You can go to Ingest > Transfer and search for the content you have uploaded. Then choose "Select all pages" and then "Start new process". There you need to select the same ingest parameters, including Parent node, OR identifier and ingest finished email notification.
  
</details>

##
<details><summary><b>User permissions</b></summary>

#### Top level repository permissions

| Permission | Detail |
|------------|--------|
| Create | Permission to submit or create a new archival package under this one. |
| Read | Permission to search or access this archival package. |
| Update | Permission to change this archival package or any of its sub-components. |
| Delete | Permission to delete this archival package or any of its sub-components. |
| Grant | Permission to change the permissions of this archival package. |
  
#### Lower level IP permissions

| Permission |
|------------|
| Retrieve intellectual entities (AIPs) |
| List and search intellectual entities (AIPs) |
| Accept or reject intellectual entities in assessment |
| Create top intellectual entities |
| Create intellectual entities |
| Update intellectual entities |
| Delete intellectual entities |
| List and search representations and computer files |
| Retrieve representations and computer files |
| Create representations and computer files |
| Update representations and computer files |
| Delete representations and computer files |
| List and retrieve descriptive metadata |
| Create descriptive metadata |
| Update descriptive metadata |
| Delete descriptive metadata |
| List and retrieve preservation metadata |
| Create preservation metadata |
| Delete preservation metadata |
| List and retrieve files in transfer |
| Create files and transfer |
| Update files and transfer |
| Delete files and transfer |
| List and view processes (ingest and action) |
| Manage processes (ingest and action) |
| List and view users and groups |
| Manage users and groups |
| List and view notifications |
| Manage notifications |
| List and view log entries |
| Delete log entries |
| List and view preservation risks |
| Manage preservation risks |
| List and view representation information |
| Manage representation information |
| Read and query about the permissions of other users |
| List and view disposal rule information |
| Manage disposal rule information |
| List and view disposal schedule information |
| Manage disposal schedule information |
| Associate or disassociate disposal schedule from intellectual entities (AIPs) |
| List and view disposal hold information |
| Manage disposal hold information |
| Apply or lift disposal hold from intellectual entities (AIPs) |
| List and view disposal confirmation information |
| Manage disposal confirmation information |
| Destroy intellectual entities (AIPs) according to the disposal confirmation |
| Restore destroyed intellectual entities (AIPs) according to the disposal confirmation |
| Permanently delete destroyed intellectual entities (AIPs) according to the disposal confirmation |
  
</details>

##
<details><summary><b>Repository classification scheme</b></summary>
  
To use the classification scheme, go to RODA menu Ingest>Pre-ingest and download the classification scheme. Then you can for example load it into RODA-in, and then you can drag'n'drop SIPs to a specific node under your organization.
  
</details>

##
<details><summary><b>Activating full-text search</b></summary>
  
You need to activate the full-text by running the full-text plugin, either on ingest or afterwards (e.g. restore from meemoo). The plugin is called "Feature extraction (Apache Tika)" and runs Apache Tika to perform, optionally:

* Feature extraction: Perform feature extraction from files. This will extract properties such as number of pages, width, height, colour space, etc.
* Full text extraction: Extracts full text from document/textual files. Extracted text is used to perform full-text searching on the catalogue.

Please note that extracting full text will require much more index size capabilities.
  
</details>

##
<details><summary><b>Commercial plugins</b></summary>
  
Info and documentation [here](https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/RODA/RODA%20plugins.pdf).
  
</details>

##
<details><summary><b>METS</b></summary>
  
Parent AIPs are referenced in a structMap element in the METS. It is a little different from [E-ARK's proposition](https://earkaip.dilcis.eu/#childaipreferencesparentaip).
![image](https://user-images.githubusercontent.com/87436774/146341721-1cc44b69-88f6-40aa-9d02-c2a08a929107.png)
  
</details>

##
<details><summary><b>AIP pruning</b></summary>

Pruning is the process of removing all representations from an AIP. The aim is to save storage space while still leaving searchable metadata. Later one can unprune an AIP to restore all representations.

However, in RODA, pruning also removes representation level PREMIS files and other technical metadata. This results in pruned AIPs having less information for reporting. Therefore, pruning in RODA should generally not be done.
  
</details>

##
<details><summary><b>Orphaned IPs</b></summary>

If a child IP (IP with reference to a parent IP) is accepted in the catalogue, but its parent is not (or not yet), it will be an orphan IP. Orphaned IPs appear under a ghost node in the organization repository.
  
![image](https://user-images.githubusercontent.com/87436774/145191783-931fe3d9-ccd2-42fe-83f9-eb5d3c990c49.png)

It is currently unclear who you can easily search/retrieve all orphaned IPs.
  
</details>

##
<details><summary><b>Internal actions</b></summary>
  
Internal actions are complex tasks performed by the repository as background jobs that enhance the user experience by not blocking the user interface during long lasting operations. Examples of such operations are: moving AIPs, reindexing parts of the repository, or deleting a large number of files. Each operation is called a job, and each job leads to one or more reports (one report per AIP).

Job example:
  
![image](https://user-images.githubusercontent.com/87436774/145371252-1d7524a7-38be-4ead-a3d1-c4b2d5e1ea76.png)
  
Report example:
  

| id                                                                                                             | jobId                                | jobName       | sourceObjectId                       | sourceObjectOriginalName    | sourceObjectLabel            | sourceObjectClass | sourceObjectOriginalIds              | outcomeObjectId             | outcomeObjectLabel           | outcomeObjectClass | outcomeObjectState                 | title                        | dateCreated                  | dateUpdated | completionPercentage | stepsCompleted | totalSteps                                             | plugin                             | pluginName | pluginVersion | pluginState                                                                      | pluginDetails | htmlPluginDetails | successfulPlugins | unsuccessfulPlugins | reports |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------|---------------|--------------------------------------|-----------------------------|------------------------------|-------------------|--------------------------------------|-----------------------------|------------------------------|--------------------|------------------------------------|------------------------------|------------------------------|-------------|----------------------|----------------|--------------------------------------------------------|------------------------------------|------------|---------------|----------------------------------------------------------------------------------|---------------|-------------------|-------------------|--------|---------|
| 189796fb-007a-465d-9ac3-723a73705036-c084632a-5e66-4ccd-a9be-6ab01cf5950e-c084632a-5e66-4ccd-a9be-6ab01cf5950e | 189796fb-007a-465d-9ac3-723a73705036 | AIP appraisal | c084632a-5e66-4ccd-a9be-6ab01cf5950e | ingenium18[047]05 (kopie) 2 | org.roda.core.data.v2.ip.AIP | []                | c084632a-5e66-4ccd-a9be-6ab01cf5950e | ingenium18[047]05 (kopie) 2 | org.roda.core.data.v2.ip.AIP | CREATED            | Update AIP permissions recursively | Wed Dec 08 07:59:22 UTC 2021 | Wed Dec 08 07:59:23 UTC 2021 | 100         | 1                    | 1              | org.roda.core.plugins.plugins.internal.AppraisalPlugin | Update AIP permissions recursively | 1.0        | SUCCESS       | The AIP 'c084632a-5e66-4ccd-a9be-6ab01cf5950e' was accepted into the repository. | FALSE         | []                | []                | [Report [id=189796fb-007a-465d-9ac3-723a73705036-c084632a-5e66-4ccd-a9be-6ab01cf5950e-c084632a-5e66-4ccd-a9be-6ab01cf5950e, jobId=189796fb-007a-465d-9ac3-723a73705036, sourceObjectId=c084632a-5e66-4ccd-a9be-6ab01cf5950e, sourceObjectClass=org.roda.core.data.v2.ip.AIP, sourceObjectOriginalIds=[], outcomeObjectId=c084632a-5e66-4ccd-a9be-6ab01cf5950e, outcomeObjectClass=org.roda.core.data.v2.ip.AIP, outcomeObjectState=CREATED, title=Update AIP permissions recursively, dateCreated=Wed Dec 08 07:59:22 UTC 2021, dateUpdated=Wed Dec 08 07:59:23 UTC 2021, completionPercentage=0, stepsCompleted=0, totalSteps=1, plugin=org.roda.core.plugins.plugins.internal.AppraisalPlugin, pluginName=Update AIP permissions recursively, pluginVersion=1.0, pluginState=SUCCESS, pluginIsMandatory=true, pluginDetails=The AIP 'c084632a-5e66-4ccd-a9be-6ab01cf5950e' was accepted into the repository., htmlPluginDetails=false, reports=[]]] |         |
| 189796fb-007a-465d-9ac3-723a73705036-5590bdbf-332f-4965-8918-c77740d22459-5590bdbf-332f-4965-8918-c77740d22459 | 189796fb-007a-465d-9ac3-723a73705036 | AIP appraisal | 5590bdbf-332f-4965-8918-c77740d22459 | ingenium18[047]05 (kopie)   | org.roda.core.data.v2.ip.AIP | []                | 5590bdbf-332f-4965-8918-c77740d22459 | ingenium18[047]05 (kopie)   | org.roda.core.data.v2.ip.AIP | CREATED            | Update AIP permissions recursively | Wed Dec 08 07:59:22 UTC 2021 | Wed Dec 08 07:59:22 UTC 2021 | 100         | 1                    | 1              | org.roda.core.plugins.plugins.internal.AppraisalPlugin | Update AIP permissions recursively | 1.0        | SUCCESS       | The AIP '5590bdbf-332f-4965-8918-c77740d22459' was accepted into the repository. | FALSE         | []                | []                | [Report [id=189796fb-007a-465d-9ac3-723a73705036-5590bdbf-332f-4965-8918-c77740d22459-5590bdbf-332f-4965-8918-c77740d22459, jobId=189796fb-007a-465d-9ac3-723a73705036, sourceObjectId=5590bdbf-332f-4965-8918-c77740d22459, sourceObjectClass=org.roda.core.data.v2.ip.AIP, sourceObjectOriginalIds=[], outcomeObjectId=5590bdbf-332f-4965-8918-c77740d22459, outcomeObjectClass=org.roda.core.data.v2.ip.AIP, outcomeObjectState=CREATED, title=Update AIP permissions recursively, dateCreated=Wed Dec 08 07:59:22 UTC 2021, dateUpdated=Wed Dec 08 07:59:22 UTC 2021, completionPercentage=0, stepsCompleted=0, totalSteps=1, plugin=org.roda.core.plugins.plugins.internal.AppraisalPlugin, pluginName=Update AIP permissions recursively, pluginVersion=1.0, pluginState=SUCCESS, pluginIsMandatory=true, pluginDetails=The AIP '5590bdbf-332f-4965-8918-c77740d22459' was accepted into the repository., htmlPluginDetails=false, reports=[]]] |         |
  
</details>

##
<details><summary><b>Preservation actions</b></summary>
  
Preservation actions are tasks performed on the contents of the repository that aim to enhance the accessibility of archived files or to mitigate digital preservation risks. Within RODA, preservation actions are handled by a job execution module. The job execution module allows the repository manager to run actions over a given set of data (AIPs, representations or files). Preservation actions include format conversions, checksum verifications, reporting (e.g. to automatically send SIP acceptance/rejection emails), virus checks, etc. Each operation is called a job, and each job leads to one or more reports (one report per AIP).
  
- Some actions are presented as preservation actions although they are not strictly for preservation, like re-index actions, and these do not create a preservation event.
- Other actions, which might be construed as preservation actions, or at least accessory to preservation actions, like the inventory report, also do not create preservation events.
- Mainly, we create preservation events for actions that change the data (like conversions that create representations) or for actions that enrich the metadata (like generation of fixity information and file format identification) or for actions that validate the data (fixity checks, file format validation).
  
Report export example:
  
| id | jobId | jobName | sourceObjectId | sourceObjectOriginalName | sourceObjectLabel | sourceObjectClass | sourceObjectOriginalIds | outcomeObjectId | outcomeObjectLabel | outcomeObjectClass | outcomeObjectState | title | dateCreated | dateUpdated | completionPercentage | stepsCompleted | totalSteps | plugin | pluginName | pluginVersion | pluginState | pluginDetails | htmlPluginDetails | successfulPlugins | unsuccessfulPlugins | reports |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|----|-----|-----|-----|----|-----|-----|-------|-------|---|--|-----|--------|------|------------|----|
| c0ed7762-1f11-4ec6-9461-23d0dde7a0f5-40bdb2ff-f314-3178-87c2-35005e9b6137-40bdb2ff-f314-3178-87c2-35005e9b6137 | c0ed7762-1f11-4ec6-9461-23d0dde7a0f5 | Office documents conversion (unoconv) (7.0.4.2) | 40bdb2ff-f314-3178-87c2-35005e9b6137 |                          | PV INSCH.DOC                        | org.roda.core.data.v2.ip.File | []                      | 40bdb2ff-f314-3178-87c2-35005e9b6137 |                    | org.roda.core.data.v2.ip.DIP | ACTIVE             | Office documents conversion (unoconv) | Tue Nov 23 16:37:05 UTC 2021 | Tue Nov 23 16:37:05 UTC 2021 | 100                  | 1              | 1          | org.roda.core.plugins.external.UnoconvConvertPlugin | Office documents conversion (unoconv) | 7.0.4.2       | SUCCESS     | This file was ignored. | FALSE             | []                | []                  | [Report   [id=c0ed7762-1f11-4ec6-9461-23d0dde7a0f5-40bdb2ff-f314-3178-87c2-35005e9b6137-40bdb2ff-f314-3178-87c2-35005e9b6137,   jobId=c0ed7762-1f11-4ec6-9461-23d0dde7a0f5,   sourceObjectId=40bdb2ff-f314-3178-87c2-35005e9b6137,   sourceObjectClass=org.roda.core.data.v2.ip.File, sourceObjectOriginalIds=[],   outcomeObjectId=40bdb2ff-f314-3178-87c2-35005e9b6137,   outcomeObjectClass=org.roda.core.data.v2.ip.DIP, outcomeObjectState=ACTIVE,   title=Office documents conversion (unoconv), dateCreated=Tue Nov 23 16:37:05   UTC 2021, dateUpdated=Tue Nov 23 16:37:05 UTC 2021, completionPercentage=0,   stepsCompleted=0, totalSteps=1,   plugin=org.roda.core.plugins.external.UnoconvConvertPlugin, pluginName=Office   documents conversion (unoconv), pluginVersion=7.0.4.2, pluginState=SUCCESS,   pluginIsMandatory=true, pluginDetails=This file was ignored.,   htmlPluginDetails=false, reports=[]]] |
| c0ed7762-1f11-4ec6-9461-23d0dde7a0f5-56fa195f-fc2a-39a6-b113-45eebd46c72f-56fa195f-fc2a-39a6-b113-45eebd46c72f | c0ed7762-1f11-4ec6-9461-23d0dde7a0f5 | Office documents conversion (unoconv) (7.0.4.2) | 56fa195f-fc2a-39a6-b113-45eebd46c72f |                          | PV_INSCH.DOC                        | org.roda.core.data.v2.ip.File | []                      | 56fa195f-fc2a-39a6-b113-45eebd46c72f |                    | org.roda.core.data.v2.ip.DIP | ACTIVE             | Office documents conversion (unoconv) | Tue Nov 23 16:37:05 UTC 2021 | Tue Nov 23 16:37:05 UTC 2021 | 100                  | 1              | 1          | org.roda.core.plugins.external.UnoconvConvertPlugin | Office documents conversion (unoconv) | 7.0.4.2       | SUCCESS     | This file was ignored. | FALSE             | []                | []                  | [Report   [id=c0ed7762-1f11-4ec6-9461-23d0dde7a0f5-56fa195f-fc2a-39a6-b113-45eebd46c72f-56fa195f-fc2a-39a6-b113-45eebd46c72f,   jobId=c0ed7762-1f11-4ec6-9461-23d0dde7a0f5,   sourceObjectId=56fa195f-fc2a-39a6-b113-45eebd46c72f,   sourceObjectClass=org.roda.core.data.v2.ip.File, sourceObjectOriginalIds=[],   outcomeObjectId=56fa195f-fc2a-39a6-b113-45eebd46c72f,   outcomeObjectClass=org.roda.core.data.v2.ip.DIP, outcomeObjectState=ACTIVE,   title=Office documents conversion (unoconv), dateCreated=Tue Nov 23 16:37:05   UTC 2021, dateUpdated=Tue Nov 23 16:37:05 UTC 2021, completionPercentage=0,   stepsCompleted=0, totalSteps=1,   plugin=org.roda.core.plugins.external.UnoconvConvertPlugin, pluginName=Office   documents conversion (unoconv), pluginVersion=7.0.4.2, pluginState=SUCCESS,   pluginIsMandatory=true, pluginDetails=This file was ignored.,   htmlPluginDetails=false, reports=[]]] |
  
</details>

##
<details><summary><b>IP meemoo status data</b></summary>
  
RODA keeps track of the following data about IPs in regards to their status on meemoo.

![image](https://user-images.githubusercontent.com/87436774/145192766-db9de476-1742-4c56-8866-029c5f809476.png)
  
1. AIP Version - The version of the IP at meemoo.
2. Identifier - The organization's identifier in the meemoo repository.
3. Synchronization AIP Status (On RODA)
4. Last synchronization date into Meemoo (datetime stamp)
5. Pruned (Yes / No)
6. Archive status (None / On disk)
7. Automatically submitted after ingestion (Yes / No)
  
</details>
  
##
<details><summary><b>Archiving on meemoo</b></summary>
  
Meemoo keeps its own version of documentation for the project on https://meemoo.atlassian.net/wiki/spaces/SRP/overview?homepageId=3171909795
  
The current strategy is to archive all AIP versions on meemoo. These versions should be documented in the meemoo sidecar xml. RODA will always restore the latest version from meemoo. Obsolete versions are not deleted; it is up to meemoo to develop a way to delete obsolete AIP versions later on.

When archiving to meemoo, a sidecar xml is generated and passed to meemoo for cross platform linking of the IP. Example sidecar xml generated when archiving AIP on meemoo:
  
```xml
AIP successfully preserved in MEEMOO
The following representations were removed from the AIP: 
rep1

sidecar:
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<VIAA>
    <aip_version>1</aip_version>
    <md5>BB096878ED1F765088A85D23C587B482</md5>
    <dc_contributors/>
    <dcterms_created>2021-11-22T14:41:46Z</dcterms_created>
    <dc_creators/>
    <dc_identifier_localid>a7cb55ff-f8de-47ea-9a9f-6d14705d3b97</dc_identifier_localid>
    <dc_identifier_localids>
        <ScalaID>uuid-16c59bcd-b0c7-492f-9c18-89e83ba48604</ScalaID>
    </dc_identifier_localids>
    <CP_id>OR-jq0st8z</CP_id>
    <dc_titles/>
</VIAA>
```
  
</details>

##
<details><summary><b>Meemoo AIP querying</b></summary>
  
Querying the meemoo API for AIPs is based on the key dc_identifier_localidsScalaID. There are two versions of the API (v1 and v2). Make sure you are logged into the meemoo qas.
  
v1</br>
General information about searching items using search fields with REST API v1: https://archief-qas.viaa.be/mediahaven-rest-api/#mediahaven-rest-api-manual-search-for-media-objects-search-on-data-within-specific-fields.</br>
GET call: https://archief-qas.viaa.be/mediahaven-rest-api/resources/media/?q=%2B(dc_identifier_localidsScalaID:"{scala-id}")</br>
Example: https://archief-qas.viaa.be/mediahaven-rest-api/resources/media/?q=%2B(dc_identifier_localidsScalaID:"uuid-fd82992d-169f-44ed-9139-6e1ad4f9e40a")</br>

v2</br>
General information about searching items using search fields with REST API v2: https://archief-qas.viaa.be/mediahaven-rest-api/v2/api-docs/index.html#mediahaven-rest-api-manual-search-for-records-search-on-data-within-specific-fields.</br>
GET call: https://archief-qas.viaa.be/mediahaven-rest-api/v2/records?q=%2B(dc_identifier_localidsScalaID:"{scala-id}")</br>
Example: https://archief-qas.viaa.be/mediahaven-rest-api/v2/records?q=%2B(dc_identifier_localidsScalaID:"uuid-fd82992d-169f-44ed-9139-6e1ad4f9e40a")</br>

General info about the REST API: https://developer.meemoo.be/docs/development/#rest-api.
  
</details>

##
<details><summary><b>Solr querying</b></summary>
  
URL: https://scala.meemoo.be/solr/#/.
  
Documentation: https://solr.apache.org/guide/7_7/index.html.
  
KEEP training Solr use cases and exercises: https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/RODA/Training%20Solr%20use%20cases.pdf.
  
KEEP training Solr answers: https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/RODA/Solr%20exercises%20answers.txt.

</details>
