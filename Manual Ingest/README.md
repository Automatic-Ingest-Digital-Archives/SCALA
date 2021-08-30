# SCALA ingest manual
> The SCALA way to create and store SIPs and AIPs

This manual provides step-by-step instructions for getting your archival data into an AIP.

We use the following definitions:

<table>
    <thead>
        <tr>
            <th>Definition</th>
            <th>Explanation</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>TS</td>
            <td><ul><li>Transfer Set.</li><li>Folder containing all archival materials that are to be converted to an AIP.</li></ul>          </td>
      </tr>
      <tr>
            <td>SIP</td>
            <td><ul><li>Submission Information Package.</li><li>An E-ARK conform set of files that is offered to the e-depot.</li><li>A content producer creates one SIP from one TS.</li></ul>          </td>
      </tr>
      <tr>
            <td>AIP</td>
            <td><ul><li>Archival Information Package.</li><li>An E-ARK conform structure that stores the files in the SIP in the e-depot.</li></ul>          </td>
      </tr>
      <tr>
            <td>RODA-In</td>
            <td><ul><li>SIP creation software by KEEP SOLUTIONS.</li></ul>          </td>
      </tr>
      <tr>
            <td>RODA</td>
            <td><ul><li>AIP (re)ingestion browser tool by KEEP SOLUTIONS.</li></ul>          </td>
      </tr>
      <tr>
            <td>meemoo</td>
            <td><ul><li>Long term archival storage provider.</li></ul>          </td>
      </tr>
    </tbody>
</table>

There are instructions for Win10 and Mac/Linux operating systems.

The manual is structured as follows:
  1. **Using a terminal** - for some tasks, basic knowledge about using a terminal is needed.
  2. **Testing best practices** - if you are using this manual for testing purposes, consider these best practices.
  3. **Archival data preparation** - tasks to execute before submitting a TS to RODA-In.
  4. **RODA-In SIP creation**
  5. **RODA AIP creation & storage**
  6. **Issues & questions** - what to do if you encounter issues or have questions.

## 1. Using a terminal

Some tasks are best performed by running a script in a terminal. A terminal is a program where you can write instructions for your computer to execute. Computers normally come with a terminal program installed by default. On Windows the program is “PowerShell” and on Mac/Linux it is usually “Bash”. A terminal looks something like this:

![Terminals](https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture1.png)

There are always two tasks involved when using a terminal for a SCALA ingest task. (1) Open the terminal in the root folder of your TS and (2) copy-paste the script in the terminal and press “Enter” to run it.

<table>
    <thead>
        <tr>
            <th>Task</th>
            <th>Win10</th>
            <th>Mac/Linux</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><ul><li>Open terminal at <i><span title="Depending on the script you wish to execute, Root Folder can be either the parent folder containing all of 1 TS. Or it can be the parent folder containing multiple TS' in a separate folder each.">root folder</span></i></li></ul></td>
            <td><b> Option 1 </b> </br> Navigate to the root folder in File Explorer. </br> Shift + right click the folder. </br> Click “Open PowerShell window here”. </br> <img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture2.png"></br></br> <b> Option 2 </b> </br> Open the Windows PowerShell app. </br> Navigate to the root folder in PowerShell.</td>
            <td><b> Option 1 </b> </br> Navigate to the root folder in Finder. </br> Right click the folder. </br> Click “Services > New Terminal at Folder”. </br> <img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture3.png"> </br></br> <b> Option 2 </b> </br> Open the Terminal app. </br> Navigate to the root folder in the Terminal.</td>
        </tr>
        <tr>
            <td><ul><li> Paste and run script </li></ul></td>
            <td>Copy the script you have to run. </br> Paste the script in PowerShell. </br> Click “Enter” to run the script.</td>
            <td>Copy the script you have to run. </br> Paste the script in Bash. </br> Click “Enter” to run the script.</td>
        </tr>
    </tbody>
</table>

Now, whenever you are requested to “Open a terminal and run ``` some script ```”, you can execute both tasks above.

## 2. Testing best practices

If you are using this manual for testing purposes, please consider these best practices.

<table>
    <thead>
        <tr>
            <th>Task</th>
            <th>Win10</th>
            <th>Mac/Linux</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><ul><li>Keep test materials on an external harddrive</li></ul></td>
            <td colspan=2>Get an external hard drive. </br> Move testing TS’ to the hard drive.</td>
        </tr>
        <tr>
            <td><ul><li>Install dedicated file management software to transfer files from your external hard drive to your computer</li></ul></td>
            <td>One option is to download and install Total Commander from <a href="https://www.ghisler.com/download.htm">this website</a>. </br></td>
            <td>One option is to download and install Double Commander from <a href="https://doublecmd.sourceforge.io/">this website</a>.</td>
        </tr>
    </tbody>
</table>

## 3. Archival data preparation

 ### a. Create your TS

<table>
    <thead>
        <tr>
            <th>Task</th>
            <th>Win10</th>
            <th>Mac/Linux</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><ul><li>Create your TS</li></ul></td>
            <td colspan=2>Create a working folder (with a unique id) with your essence or data that needs to be transformed in a SIP. The folder contains the original files and files already migrated before ingestion.</td>
        </tr>
        <tr>
            <td><ul><li>Create and add a descriptive metadata file to your TS [optional]</li></ul></td>
            <td colspan=2>Create a metadata XML-file which follows the instructions at Add descriptive metadata.</td>
      </tr>
      <tr>
        <td><ul><li>Create and add additional unstructured metadata [optional]</li></ul></td>
            <td colspan=2>Create a folder called “submissionDocumentation” in the root of the TS.</br> Add additional unstructured metadata accompanying the content files.
</td>
        </tr>
    </tbody>
</table>

### b.  Extra data preparation tasks

Here are optional but recommended tasks to execute before submitting a TS to RODA-In. Please execute your chosen tasks in the order presented.

#### i. Unpack zipped files [optional]

<table>
    <thead>
        <tr>
            <th>Task</th>
            <th>Win10</th>
            <th>Mac/Linux</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><ul><li>Unpack zipped files</li></ul></td>
          <td>Open a terminal and run:</br><code>Expand-Archive -Path ".\*.zip"</code>,</br>where * is the name of the zip file.</td>
            <td>Open a terminal and run:</br><code>unzip "*.zip" && ls -l</code>,</br>where * is the name of the zip file.</td>
        </tr>
    </tbody>
</table>

#### ii.  Remove backup files [optional]

<table>
    <thead>
        <tr>
            <th>Task</th>
            <th>Win10</th>
            <th>Mac/Linux</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><ul><li>Remove backup files</li></ul></td>
          <td colspan=2>Manually remove backup files.</td>
        </tr>
    </tbody>
</table>

#### iii. Create a filelist and filetree [recommended]

A filelist is a text file containing all folders and files in your TS. A filetree contains the same information in a more human readable form.

<img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture4.png">

If you are on Mac or Linux, you have to install the “tree” app. Windows has it installed by default.

<table>
    <thead>
        <tr>
            <th>Task</th>
            <th>Win10</th>
            <th>Mac/Linux</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><ul><li>Install the “tree” app</li></ul></td>
          <td></td>
          <td>Install on Mac</br>Open a terminal and run:</br><code>brew install tree</code></br></br>Install on Linux</br>Open a terminal and run:</br><code>sudo apt update && sudo apt-get install tree</td>
        </tr>
    </tbody>
</table>

You can create a filelist and filetree for the root folder you are in using option 1. Alternatively, if you want to create filelists and filetrees for many TS’ at once, please follow option 2.

<b>Option 1:</b> create a filelist and filetree for the current TS.

<table>
    <thead>
        <tr>
            <th>Task</th>
            <th>Win10</th>
            <th>Mac/Linux</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><ul><li>Create a filelist and filetree for the current TS</li></ul></td>
          <td>Open a terminal and run:</br></br><code>
$File = "tree.txt";
$Path = "./submissionDocumentation"
md -Force $Path | Out-Null
Get-ChildItem -Path .\ -Recurse -Force | Resolve-Path -Relative | sort | tee $Path\filelist.txt;
if (-not(Test-Path -Path $Path\$File -PathType Leaf)) {
	New-Item -Path $Path -Name $File -ItemType File
};
Tree /f | tee $Path\$File
  </code>
</td>
          <td>Open a terminal and run:</br></br><code>FILE="tree.txt" &&
DIR="./submissionDocumentation" &&
if [ ! -d "$DIR" ]; then
mkdir $DIR
fi &&
touch $DIR/$FILE &&
find | tee $DIR/filelist.txt &&
tree | tee $DIR/$FILE
</code>
</td>
        </tr>
    </tbody>
</table>

<b>Option 2:</b> create a filelist and filetree for a list of TS’ in the current root folder. Therefore, open a terminal in the root folder containing all your TS’ in separate folders.

<table>
    <thead>
        <tr>
            <th>Task</th>
            <th>Win10</th>
            <th>Mac/Linux</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><ul><li>Create a filelist and filetree for each TS in the current folder</li></ul></td>
          <td>Open a terminal and run:</br></br><code>
$File = "tree.txt";
Get-ChildItem |
where {$_.PsIsContainer} |
foreach {
$Path = "$_/submissionDocumentation";
md -Force $Path | Out-Null;
Get-ChildItem -Path $_ -Recurse | Resolve-Path -Relative | sort | tee $Path\filelist.txt;
if (-not(Test-Path -Path $Path\$File -PathType Leaf)) {
	New-Item -Path $Path -Name $File -ItemType File
};
Tree $_ /f | tee $Path\$File
}
  </code>
</td>
          <td>Open a terminal and run:</br></br><code>FILE="tree.txt" &&
find . -maxdepth 1 -type d  \( ! -name . \) -exec bash -c "cd '{}' && 
DIR="./submissionDocumentation" &&
if [ ! -d "$DIR" ]; then
mkdir $DIR
fi &&
touch $DIR/$FILE &&
find | tee $DIR/filelist.txt &&
tree | tee $DIR/$FILE
" \;
</code>
</td>
        </tr>
    </tbody>
</table>

#### iv.  Delete system files [recommended]

Make sure to only execute this step after Create a filelist and filetree [recommended].

<table>
    <thead>
        <tr>
            <th>Task</th>
            <th>Win10</th>
            <th>Mac/Linux</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><ul><li>Delete system files</li></ul></td>
          <td colspan=2>Manually delete system files.</td>
        </tr>
    </tbody>
</table>

## 4. RODA-In SIP creation

### a. RODA-In installation & configuration

<table>
    <thead>
        <tr>
            <th>Task</th>
            <th>Win10</th>
            <th>Mac/Linux</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><ul><li>Install & start RODA-In</li></ul></td>
          <td colspan=2>Follow the installation guide on https://rodain.roda-community.org/.</br>Start RODA-In.<br><img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture5.png">
</td>
        </tr>
        <tr>
            <td><ul><li>Configure RODA-In to use the SCALA metadata template</li></ul></td>
          <td colspan=2>Open the configuration folder.</br><img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture6.png"></br>Download the “scala.xml.hbs” and “config.properties” files from https://github.com/Automatic-Ingest-Digital-Archives/SCALA/tree/main/Roda-In.<br><ol><li>Add the file “scala.xml.hbs” to the folder “\roda-in\templates”.</li><li>Overwrite the config file in “\roda-in” with the “config.properties” file.</li><ol><img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture7.png">
</td>
        </tr>
    </tbody>
</table>

### b. Using RODA-In

<table>
    <thead>
        <tr>
            <th>Task</th>
            <th>Win10</th>
            <th>Mac/Linux</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><ul><li>Load your TS in RODA-In</li></ul></td>
          <td colspan=2>Choose the working folder in your file system. This will serve as the root of your project.<br><img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture8.png">
</td>
        </tr>
        <tr>
            <td><ul><li>Create a new classification scheme</li></ul></td>
          <td colspan=2>Click to create a new classification scheme.</br><img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture9.png">
</td>
        </tr>
	        <tr>
            <td><ul><li>Add the TS to the IP panel</li></ul></td>
          <td colspan=2>Select the root folder of your TS.</br>
Add this folder to the IP panel by clicking “Associate” or by dragging it to the IP panel.</br>
You can also choose to select and add folders/files individually.
</br><img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture10.png">
</td>
        </tr>
	        <tr>
            <td><ul><li>Select an association method</li></ul></td>
          <td colspan=2>Choose the association method “One information package for each selected files or folders”.</br>
Click on the button “Continue”. 
</br><img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture11.png">
</td>
        </tr>
	        <tr>
            <td><ul><li>Add descriptive metadata</li></ul></td>
	<td colspan=2><b>Option 1:</b> Create new metadata from a template.</br>
Select option 1.</br>
Select the descriptive metadata standard/type of your choice.</br>
Click “Continue”.</br></br>
<b>Option 2:</b> Load metadata from a single file.</br>
Select option 2.</br>
Select and add the descriptive metadata file.</br>
Select the descriptive metadata standard/type of your file.</br>
Click “Continue”.
</br><img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture12.png">
</td>
        </tr>
	 <tr>
            <td><ul><li>Edit descriptive metadata [optional]</li></ul></td>
          <td colspan=2>Make changes to the metadata file using the tool. 
</br><img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture13.png">
</td>
        </tr>
	 <tr>
            <td><ul><li>Add more representations of the data [optional]</li></ul></td>
          <td colspan=2>Click “Add representation”. 
</br><img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture14.png">
</td>
        </tr>
	 <tr>
            <td><ul><li>Add documentation [optional]</li></ul></td>
          <td colspan=2>Click on “Documentation”.</br>
Drop files or folders from your file explorer to add documentation.
</br><img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture15.png">
</td>
        </tr>
	 <tr>
            <td><ul><li>Create SIP(s)</li></ul></td>
          <td colspan=2>Click “Create SIP(s)”.
</br><img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture16.png"></br>
On the popup screen, select the following options:</br>
<ol><li>Export all items - toggle this off if you only want to create a SIP from the currently selected IP. Toggle on if you want to create SIPs for all IPs in the IP (middle) panel. Toggle off by default.</li>
<li>Include hierarchy - toggle on to keep relationships between SIPs in their METS (e.g. siblings, parent-child). Toggle on by default.</li>
<li>Create inventory report - toggle on to make a list of all items contained per SIP. Toggle off by default.</li>
	<li>Output directory - select where the SIP(s) will be saved.</li>
	<li>SIP format - select E-ARK2.</li>
	<li>SIP names - select Title + ID. This will render the SIP(s) easy to work with later on.</li>
	</ol>
Click “Start” to create the SIP(s).</br>
<img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture17.png">
</td>
        </tr>
    </tbody>
</table>

## 5. RODA AIP creation & storage

### a. RODA account

### b. Install an FTP client and connect to meemoo

### c. Using RODA

## 6. Issues & questions

All issues can be reported in the SCALA GitHub repository: https://github.com/Automatic-Ingest-Digital-Archives/SCALA/issues. Please check if the same issue was already reported before creating a new issue.

Alternatively, you can contact jelle.kleevens@vai.be to report the issue or for any other questions.
