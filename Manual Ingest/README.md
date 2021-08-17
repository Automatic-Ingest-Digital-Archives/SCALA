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


### Delete system files -- recommended

### Unpack zipped files -- optional
