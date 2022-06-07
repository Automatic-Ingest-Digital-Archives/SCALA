# How to generate discription.xml files for all your SIPs

1. Prepare a correct XLSX (Excel) file
2. Download and install Python
3. Download Python script
4. Execute shell script

Each output description.xml file will look like [this example](https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/DescriptionXML/ExampleXmlOutput.xml).

## 1. Prepare a correct XLSX (Excel) file

Must contain the following headers:
`destinationDirectory	creation	archdeskLevel	unitTitle	repositoryCode	localID	unitDate	corpName	creatorName	producerName	scopeContent	relatedMaterial	accessRestrict	processDate
`

Example XLSX file:

| destinationDirectory | creation         | archdeskLevel | unitTitle                                                                                           | repositoryCode | localID      | unitDate  | corpName | creatorName | producerName | scopeContent                                                                                                                                                                                                                                   | relatedMaterial | accessRestrict               | processDate |
|----------------------|------------------|---------------|----------------------------------------------------------------------------------------------------|----------------|--------------|-----------|----------|-------------|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|------------------------------|-------------|
| 0099-CK_0167         | JelleKleevensVAI | Collection    | Aanbevelingsbrief van Bob van Reeth   voor Christian Kieckens betreffende een project te Nederland | BE/653717      | 0099-CK_0167 | 2010/..   | Vai      | Vai         | SCALA?       | Bevat 3 scans van een vraag van Cees Nagelkerke aan Bob van Reeth. |                 | Enkel raadpleegbaar door Vai | 23/09/2021  |
| 0099-CK_0168         | JelleKleevensVAI | Collection    | Foto's betreffende een appartement   te Diksmuide                                                  | BE/653717      | 0099-CK_0168 | 2005/2016 | Vai      | Vai         | SCALA?       | Bevat foto's allerlei betreffende een appartement in Diksmuide. |                 | Enkel raadpleegbaar door Vai | 23/09/2021  |

Put the XLSX file in the **root folder** of your SIPs.

These headers correspond to the following EAD and meemoo descriptive metadata:
<details>
  <summary>Click to expand</summary>

| XLSX header          |       RODA-IN interface      |                RODA-IN SCALA EAD                |            MEEMOO SIDECAR            |
|----------------------|:----------------------------:|:-----------------------------------------------:|:------------------------------------:|
| destinationDirectory |                              |                                                 |                                      |
| creation             |                              |                                                 |                                      |
| scalaUUID            | scala UUID                   | ead/archdesc/did/unitid@label="scalaId"         | /viaa/dc_identifier_localids/scalaId |
| localID              | local ID                     | ead/archdesc/did/unitid@label="localId"         | /viaa/dc_identifier_localid          |
| archdeskLevel        | type                         | ead/archdesc@level="collection"                 |                                      |
| unitTitle            | title                        | ead/archdesc/did/unittitle                      | /viaa/dc_title                       |
| unitDate             | date(s)                      | ead/archdesc/did/unitdate                       |                                      |
| creatorName          | archive creator(s)           | ead/archdesc/did/origination@label="creator"    | /viaa/dc_creators/Archiefvormer      |
| producerName         | producer                     | ead/archdesc/did/origination@label="producer"   | /viaa/dc_publishers/publisher        |
| repositoryCode       | repository ID                | ead/archdesc/did/unitid @label="repositorycode" |                                      |
| corpName             | repository name              | ead/archdesc/did/repository/corpname            | /viaa/CP                             |
|     scopeContent     | scope / content              | ead/archdesc/did/scopecontent                   | /viaa/dc_description                 |
| accessRestrict       | conditions governing access  | ead/archdesc/did/accessrestrict                 | /viaa/dc_rights_comment              |
| relatedMaterial      | related units of description | ead/archdesc/did/relatedmaterial                | /viaa/dc_titles/archief              |
| processDate          | date of creation             | ead/archdesc/procesinfo                         |                                      |

</details>

## 2. Download and install Python

https://www.python.org/downloads/

## 3. Download Python script and requirements

[Download the Python script here.](https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Referenced%20Files/DescriptionXML/DescriptionGenerator.py)

[And the required dependencies here.](https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Referenced%20Files/DescriptionXML/requirements.txt)

Put both in the **root folder** of your SIPs.

## 4. Execute shell script

Open a terminal in the root folder of your SIPs. Then copy, paste and execute the script below.

! Please note: in the script replace {{YOURFILE}} with the name of your XLSX file.

<b>PowerShell</b>

```powershell
py -m pip install --upgrade pip
pip install -r requirements.txt
py .\DescriptionGenerator.py .\{{YOURFILE}}.xlsx
```
