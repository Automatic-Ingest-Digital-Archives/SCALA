# How to generate discription.xml files for all your SIPs

1. Prepare a correct XLSX (Excel) file
2. Download and install Python
3. Download Python script
4. Execute shell script

Each output description.xml file will look like [this example](https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/DescriptionXML/ExampleXmlOutput.xml).

## 1. Prepare a correct XLSX (Excel) file

Must contain the following headers:
`destinationDirectory	creation	archdeskLevel	unitTitle	scalaID	repositoryCode	localID	unitDate	corpName	creatorName	producerName	scopeContent	relatedMaterial	accessRestrict	processDate
`

| destinationDirectory | creation         | archdeskLevel | unitTitle                                                                                          | scalaID | repositoryCode | localID      | unitDate  | corpName | creatorName | producerName | scopeContent                                                                                                                                                                                                                                   | relatedMaterial | accessRestrict               | processDate |
|----------------------|------------------|---------------|----------------------------------------------------------------------------------------------------|---------|----------------|--------------|-----------|----------|-------------|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|------------------------------|-------------|
| 0099-CK_0167         | JelleKleevensVAI | Collection    | Aanbevelingsbrief van Bob van Reeth   voor Christian Kieckens betreffende een project te Nederland |         | BE/653717      | 0099-CK_0167 | 2010/..   | Vai      | Vai         | SCALA?       | Bevat 3 scans van een vraag van Cees Nagelkerke aan Bob van Reeth. |                 | Enkel raadpleegbaar door Vai | 23/09/2021  |
| 0099-CK_0168         | JelleKleevensVAI | Collection    | Foto's betreffende een appartement   te Diksmuide                                                  |         | BE/653717      | 0099-CK_0168 | 2005/2016 | Vai      | Vai         | SCALA?       | Bevat foto's allerlei betreffende een appartement in Diksmuide. |                 | Enkel raadpleegbaar door Vai | 23/09/2021  |

Please refer to this [example XLSX](https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/DescriptionXML/ExampleDescriptions.xlsx) when creating your file. The contents should make clear what is expected under each header.

Put the XLSX file in the **root folder** of your SIPs.

## 2. Download and install Python

https://www.python.org/downloads/

## 3. Download Python script

[Download here.](https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/DescriptionXML/DescriptionGenerator.py)

Put the python file in the **root folder** of your SIPs.

## 4. Execute shell script

Open a terminal in the root folder of your SIPs. Then execute the script below.

! Please note: in the script replace {{YOURFILE}} with the name of your XLSX file.

<b>PowerShell</b>

```powershell
py .\DescriptionGenerator.py .\{{YOURFILE}}.xlsx
```
