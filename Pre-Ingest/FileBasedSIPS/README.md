## How to create filebased SIPs using Python

Use the scripts to do the following:

* Create Transfer Set dir in outputDir. This dir will contain a flattened version of the original Transfer Set.
* Prepare variables + make new folder in tsOutputDir.
* Copy file in targetDir. Optionally delete rootDir.
* Make description xml and put in xmlOutputDir.

### Instructions for Linux

1. Locate a Root Directory containing all the Transfer Sets.
2. Download the three pythons scripts and save them in the Root Directory.
3. Open a terminal (bash) in the Root Directory.
4. Run the following one-line script. Replace the placeholders with appropriate values. <code>for D in */; do $(echo $D) $(python3 main.py $(realpath $D) "{{OutputDirectory}}" "{{DescriptiveMetadataOutputDirectory}}" "{{DeleteFilesAfterCopying?TRUE/FALSE}}"); done</code>
