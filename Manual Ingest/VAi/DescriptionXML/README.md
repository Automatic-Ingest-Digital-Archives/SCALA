# How to generate discription.xml files for all your SIPs

1. Prepare a correct XLSX (Excel) file
2. Download and install Python
3. Download Python script
4. Execute shell script

## 1. Prepare a correct XLSX (Excel) file

Must contain the following headers:
`destinationDirectory	creation	archdeskLevel	unitTitle	scalaID	repositoryCode	localID	unitDate	corpName	creatorName	producerName	scopeContent	relatedMaterial	accessRestrict	processDate
`

Please refer to this [example XLSX](https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/VAi/DescriptionXML/ExampleDescriptions.xlsx) when creating your file. The contents should make clear what is expected under each header.

Put the XLSX file in the **root folder** of your SIPs.

## 2. Download and install Python

https://www.python.org/downloads/

## 3. Download Python script

[Download here.](https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/VAi/DescriptionXML/DescriptionGenerator.py)

Put the python file in the **root folder** of your SIPs.

## 4. Execute shell script

Open a terminal in the root folder of your SIPs. Then execute the script below.

! Please note: in the script replace {{YOURFILE}} with the name of your XLSX file.

<b>PowerShell</b>

```powershell
py .\DescriptionGenerator.py .\{{YOURFILE}}.xlsx
```
