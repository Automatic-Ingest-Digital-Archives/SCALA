## Roda is a browser tool where you can upload SIPs and transform them to AIPs.

###
<details><summary><b>To use Roda</b></summary>
  
1. Go to https://roda-community.org/#welcome.
  
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
  

  
</details>

##
<details><summary><b>Metadata format configuration</b></summary>
  
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
<details><summary><b>Commercial plugins</b></summary>
  
Info and documentation [here](https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/RODA/RODA%20plugins.pdf).
  
</details>

##
<details><summary><b>Meemoo tape deletion</b></summary>
  
The current strategy is to archive all AIP versions on meemoo. These versions should be documented in the meemoo sidecar xml. RODA will always restore the latest version from meemoo. It is up to meemoo to develop a way to delete obsolete AIP versions later on.
  
</details>
