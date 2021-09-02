###PS
<code>
Start-Transcript;
$delimiter = ";";
$csv = Get-Content "./20210901_metadata_CK.csv";
foreach ($line in ($csv | select -skip 1)){
$path = $line.Split($delimiter)[0];
$path;
py .\descriptionxmlgen.py $line.replace('"', "'") $delimiter > "./$path/description.xml"
};
Stop-Transcript;
</code>
