# SCALA ingest manual
> The SCALA way to create and store SIPs and AIPs

This manual provides step-by-step instructions for getting your archival data into an AIP.

We use the following definitions:

| Definition | Explanation |
| :-- | :-- |
|TS|<ul><li>Transfer Set.</li><li>Folder containing all archival materials that are to be converted to an AIP.</li></ul>|
|SIP|<ul><li>Submission Information Package.</li><li>An E-ARK conform set of files that is offered to the e-depot.</li><li>A content producer creates one SIP from one TS.</li></ul>|
|AIP|<ul><li>Archival Information Package.</li><li>An E-ARK conform structure that stores the files in the SIP in the e-depot.</li></ul>|
|RODA-In|<ul><li>SIP creation software by KEEP SOLUTIONS.</li></ul>|
|RODA|<ul><li>AIP (re)ingestion browser tool by KEEP SOLUTIONS.</li></ul>|
|meemoo|<ul><li>Long term archival storage provider.</li></ul>|

There are instructions for Win10 and Mac/Linux operating systems.

The manual is structured as follows:
  1. **Using a terminal** - for some tasks, basic knowledge about using a terminal is needed.
  2. **Testing best practices** - if you are using this manual for testing purposes, consider these best practices.
  3. **Archival data preparation** - tasks to execute before submitting a TS to RODA-In.
  4. **RODA-In SIP creation**
  5. **RODA AIP creation & storage**
  6. **Issues & questions** - what to do if you encounter issues or have questions.

## Using a terminal

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

## Testing best practices

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

## Archival data preparation

### Create your TS

### Extra data preparation tasks

#### Unpack zipped files [optional]
#### Remove backup files [optional]
#### Create a filelist and filetree [recommended]
#### Delete system files [recommended]

## RODA-In SIP creation

## RODA AIP creation & storage

## Issues & questions
