# How to generate discription.xml files for all your SIPs

1. Prepare a correct csv file
2. Download and install Python
3. Download Python script
4. Execute shell script

## 1. Prepare a correct csv file

Must contain the following headers in that exact order:
container_id;reference_code;title;start_year;end_year;top_archive_value;content_remarks

- container_id: This must be the exact name of the SIP folder for which you create this description.xml.
- reference_code
- title
- start_year
- end_year
- top_archive_value
- content_remarks

Put the csv file in the root folder of your SIPs.

## 2. Download and install Python

https://www.python.org/downloads/

## 3. Download Python script

https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/VAi/descriptionxmlgen.py

Put the python file in the root folder of your SIPs.

## 4. Execute shell script

Open a terminal in the root folder of your SIPs. Then execute the script below.

! Please note:

- In the script replace {{INSERT FILE NAME HERE}} with the name of your csv file.
- Depending on your OS language settings, your csv file may be delimited with commas or with semicolons. Please adjust the $delimiter variable in the script accordingly. For Belgium, the delimiter is normally ";".

<b>PowerShell</b>

<code>
Start-Transcript;
$delimiter = ";";
$csv = Get-Content "./{{INSERT FILE NAME HERE}}.csv";
foreach ($line in ($csv | select -skip 1)){
$path = $line.Split($delimiter)[0];
$path;
py .\descriptionxmlgen.py $line.replace('"', "'") $delimiter > "./$path/description.xml"
};
Stop-Transcript;
</code>

<b>Bash</b>

<code>
To be added
</code>
