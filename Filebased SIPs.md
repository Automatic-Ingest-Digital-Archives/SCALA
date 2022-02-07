## How to create filebased SIPs using Python

Use the scripts to do the following:

* Create Transfer Set dir in outputDir. This dir will contain a flattened version of the original Transfer Set.
* Prepare variables + make new folder in tsOutputDir.
* Copy file in targetDir. Optionally delete rootDir.
* Make description xml and put in xmlOutputDir.

### Scripts

https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Referenced%20Files/main.py

https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Referenced%20Files/validateXml.py

https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Referenced%20Files/xmlgen_file.py

https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Referenced%20Files/xmlgen_parent.py

### Instructions for PowerShell

1. Locate a Root Directory containing all the Transfer Sets.
2. Download the pythons scripts and save them in the same directory.
3. Open a PowerShell terminal.
4. Run the following script. Replace the placeholders with appropriate values.

<code>
$rootDir = {{INSERT PATH TO ROOT DIR}}
$outputDir = {{INSERT PATH TO OUTPUT DIR}}
$xmlOutputDir = {{INSERT PATH TO XMLOUTPUT DIR}}
$deleteOriginal = $false
$script = {{INSERT PATH TO MAIN SCRIPT}}

python $script $rootDir $outputDir $xmlOutputDir $deleteOriginal
</code>

### Making changes to descriptive metadata xmls

Use this script and adjust as needed.

https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Referenced%20Files/EditXml.py
