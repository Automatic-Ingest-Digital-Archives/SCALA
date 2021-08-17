# SCALA ingest manual

## Basic ingest with Roda-in
For Roda-in installation and configuration, see --> link naar pagina met Roda-in

Basic ingest with Roda-in implies the following steps:
1. Prepare your essence or data in a folder
2. Load folders in Roda-in using option (één of twee, ik weet het niet meer zo goed)
3. Add descriptive metadata
4. Add - if applicable - documentation

Bear in mind that Roda-in deletes empty folders without a log. If you need to find a work around for this, see other pre-ingest steps under.

### Prepare folders
@Jelle: Verder uitwerken
### Load folders in Roda-in
@Jelle: Verder uitwerken (voorlopig uitgaan van creatie bulkSIP)
### Add descriptive metadata
@Jelle: Verder uitwerken (voorlopig wel nog block hier op hoe ons definitief descriptive metadataschema eruit gaat zien)
### Add documentation
@Jelle: Verder uitwerken

## Advanced ingest with Roda-in
There are several options that allow you to produce SIPs in bulk more efficiently
1. Add metadata from a file

### Add metadata from a file
@Jelle: Verder uitwerken. Focus op de vijf à zes essentiële metadata. Voorlopig wel nog block

## Other pre-ingest steps
With Roda-in, you can create basic SIPs for ingest into the SCALA repository. All Roda does is to create a descriptive metadata file with a METS-file, preserving the checksums. You might want to do other steps before ingest. We give a short overview of these with the different options about the way with which you can achieve this. Bear in mind integrated pre-ingest tools like RMtool exist for more intensive pre-ingest operations.

### Create a filelist for each SIP -- recommended
It's always handy to create a filelist about all the files in a SIP or in an archive. You can use this as an authoritative list of all the material received + as an inventory for researchers. This step is also recommended because Roda-in deletes without a log all empty folders.

You should be able to restore the original filestructure based on the filelist. Make sure the filelist lists files, folders and eventually symbolic links (hyperlinks to files stored elsewhere)

**Manuals**
* Create filelist using Windows Powershell: --> verder uitwerken in nieuw markdown-file. Twee gedeeltes: een filelist maken voor één folder + een filelist maken voor meerdere folders.
* Create filelist using Linux Terminal: --> verder uitwerken in nieuw markdown-file
* Create filelist using Treesize: --> verder uitwerken in nieuwe markdown-file
* Create filelist using Python os.module --> Verder uitwerken in nieuwe markdown-file. Data bij Wim

Andere partners kunnen andere methodes toevoegen.

You can also create a filelist of the whole archive and include this in the documentation folder.

### Delete system files -- recommended
The SCALA digital repository contains a delete systemfiles function. However, including system files in your SIP includes a heavier METS-file. It is recommended to delete these before adding them in Roda-in.
Only do this after creation of a filelist.

* Delete system files with shell script --> Amsab verder uitwerken.

Andere partners kunnen andere methodes toevoegen

### Unpack zipped files -- optional
The SCALA digital repository does not unpack container files or zipped files, due to multiple possible issues. zip-files in the SIP will be zip-files in the AIP. If you want to unpack all ZIP-files you can do this before. However, be aware that this always requires some human control.

* Unpack zipped files using powershell script
* Unpack zipped files using Linux terminal

Andere partners kunnen andere methodes toevoegen.
