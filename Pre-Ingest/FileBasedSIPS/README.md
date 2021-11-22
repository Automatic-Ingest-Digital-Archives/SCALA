## Instructions for Linux

1. Locate a Root Directory containing all the Transfer Sets.
2. Download the three pythons scripts and save them in the Root Directory.
3. Open a terminal (bash) in the Root Directory.
4. Run the following one-line script. Replace the placeholders with appropriate values. <code>for D in */; do $(echo $D) $(python3 main.py $(realpath $D) "{{OutputDirectory}}" "{{DescriptiveMetadataOutputDirectory}}" "{{DeleteFilesAfterCopying?TRUE/FALSE}}"); done</code>
