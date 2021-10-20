# SCALA IP ingest manual

###
<details><summary><b>Introduction</b></summary>

This manual provides step-by-step instructions for getting your archival data into an AIP.
	
|Definition||
|----|----|
|TS|Transfer Set.</br>Folder containing all archival materials that are to be converted to an AIP.|
|SIP|Submission Information Package.</br>An E-ARK conform set of files that is offered to the e-depot.</br>A content producer creates one SIP from one TS.|
|AIP|Archival Information Package.</br>An E-ARK conform structure that stores the files in the SIP in the e-depot.|
|RODA-In|SIP creation software by KEEP SOLUTIONS.|
|RODA|AIP (re)ingestion browser tool by KEEP SOLUTIONS.|
|meemoo|Long term archival storage provider.|

There are instructions for Win10, Mac and Linux operating systems.

Text written in <span title="I have some extra information"><i>italic</i></span> has some extra information if you hover
over it.

</details>

##
<details><summary><b>Using a terminal</b></summary>

Some tasks are best performed by running a script in a terminal. A terminal is a program where you can write
instructions for your computer to execute. Computers normally come with a terminal program installed by default. On
Windows the program is “PowerShell” and on Mac/Linux it is usually “Bash”. A terminal looks something like this:

<img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture1.png">

There are always two tasks involved when using a terminal for a SCALA ingest task. (1) Open the terminal in the root
folder of your TS and (2) copy-paste the script in the terminal and press “Enter” to run it.

|Task|Win10|Mac/Linux|
|----|-----|---------|
|Open terminal at <i><span title="Depending on the script you wish to execute, Root Folder can be either the parent folder containing all of 1 TS. Or it can be the parent folder containing multiple TS' in a separate folder each.">root folder</span></i>|Navigate to the root folder in File Explorer. </br> Shift + right click the folder. </br> Click “Open PowerShell window here”. </br> <img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture2.png"></br></br>OR open the Windows PowerShell app. </br> Navigate to the root folder in PowerShell.|Navigate to the root folder in Finder. </br> Right click the folder. </br> Click “Services > New Terminal at Folder”. </br> <img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture3.png"></br></br>OR open the Terminal app. </br> Navigate to the root folder in theTerminal.|
|Paste and run script|Copy the script you have to run. </br> Paste the script in PowerShell. </br> Click “Enter” to run the script.|Copy the script you have to run. </br> Paste the script in Bash. </br> Click “Enter” to run the script.|

Now, whenever you are requested to “Open a terminal and run ``` some script ```”, you can execute both tasks above.

</details>

##
<details><summary><b>Testing best practices</b></summary>

If you are using this manual for testing purposes, please consider these best practices.
	
|Task||
|----|-----|
|Keep test materials on an external harddrive|Get an external hard drive. </br> Move testing TS’ to the hard drive.|

|Task|Win10|Mac/Linux|
|----|-----|---------|
|<span title="These tools are preferred over the default file transfer tools of Win10 and Mac. They are fast and give clear error messages."><i>Install dedicated file management software to transfer files from your external hard drive to your computer</i></span>|One option is to download and install <a href="https://www.ghisler.com/download.htm">Total Commander</a>.|One option is to download and install <a href="https://doublecmd.sourceforge.io/">Double Commander</a>.|

|Task||
|----|-----|
|Show hidden files and file extensions|In your file management and browsing software, check the boxes to view all files and extensions.</br><img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Screenshot_2.png"></br><img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Screenshot_3.png">|

</details>

##
<details><summary><b>Archival data preparation</b></summary>

#### Create your TS

|Task||
|----|-----|
|Create your TS|Create a working folder (with a unique id) with your essence or data that needs to be transformed in a SIP. The folder contains the original files and files already migrated before ingestion.|
|Create and add a descriptive metadata file to your TS [optional]|Create a metadata XML-file which follows the instructions at Add descriptive metadata.|
|Create and add additional unstructured metadata [optional]|Create a folder called “_submissionDocumentation” in the root of the TS.</br><span title="E.g. file format identification files, file lists, etc."><i>Add additional unstructured metadata accompanying the content files</i></span>|

#### Extra <span title="With RODA-In, you can create basic SIPs for ingest into the SCALA repository. All Roda-In does is to create a descriptive metadata file with a METS-file, preserving fixity. You might want to do other steps before ingest. We give a short overview of these with the different options about the way with which you can achieve this. Bear in mind integrated pre-ingest tools like RMtool exist for more intensive pre-ingest operations."><i>data preparation tasks</i></span>

Here are optional but recommended tasks to execute before submitting a TS to RODA-In. Please execute your chosen tasks
in the order presented.

|Task|Win10|Mac/Linux|
|----|-----|---------|
|Unpack zipped files <span title="The SCALA digital repository does not unpack container files or zipped files, due to multiple possible issues. zip-files in the SIP will be zip-files in the AIP. If you want to unpack all ZIP-files you can do this before. However, be aware that this always requires some human control."><i>[optional]</i></span>|Open a terminal and run:</br><code>Expand-Archive -Path ".\*.zip"</code>,</br>where * is the name of the zip file.|Open a terminal and run:</br><code>unzip "*.zip" && ls -l</code>,</br>where * is the name of the zip file.|

|Task|Win10|
|----|-----|
|Trim whitespace from filenames in Windows [optional]|<span title="Trailing and leading whitespace in filenames causes RODA-In to crash in Windows. Might be automated at some point."><i>Manually trim whitespace from filenames.</i></span>|

|Task||
|----|-----|
|Remove backup files [optional]|<span title="Might be automated at some point."><i>Manually remove backup files.</i></span>|

A filelist is a text file containing all folders and files in your TS. A filetree contains the same information in a
more human readable form.

<img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture4.png">

If you are on Mac or Linux, you have to install the “tree” app. Windows has it installed by default.

|Task|Mac/Linux|
|----|---------|
|Install the “tree” app|Install on Mac</br>Open a terminal and run:</br><code>brew install tree</code></br></br>Install on Linux</br>Open a terminal and run:</br><code>sudo apt update && sudo apt-get install tree|

<span title="We may add more options for creating filelists/filetrees at a later stage: Create filelist using Treesize; Create filelist using Python os.module; + filelist / treetool in Bitcurator. Partners can add their own preferred methods. You can also create a filelist of the whole archive and include this in the documentation folder."><i>You can create a filelist and filetree for the root folder you are in using option 1. Alternatively, if you want to create filelists and filetrees for many TS’ at once, please follow option 2.</i></span>
	
|Task|Win10|Mac/Linux|
|----|-----|---------|
|Option 1: create a filelist and filetree for the current TS <span title="It's always handy to create a filelist about all the files in a SIP or in an archive. You can use this as an authoritative list of all the material received + as an inventory for researchers. This step is also recommended because Roda-in deletes without a log all empty folders. You should be able to restore the original file structure based on the filelist. Make sure the filelist lists files, folders and eventually symbolic links (hyperlinks to files stored elsewhere)."><i>[recommended]</i></span>|Open a terminal and run <a href="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Scripts/create_filetree_filelist_powershell_option1.ps1">this script.</a>|On Linux, open a terminal and run <a href="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Scripts/create_filetree_filelist_linux_bash_option1.txt">this script.</a></br></br>On Mac, open a terminal and run <a href="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Scripts/create_filetree_filelist_mac_bash_option1.txt">this script.</a>|
|Option 2: create a filelist and filetree for each TS in the current root folder <span title="It's always handy to create a filelist about all the files in a SIP or in an archive. You can use this as an authoritative list of all the material received + as an inventory for researchers. This step is also recommended because Roda-in deletes without a log all empty folders. You should be able to restore the original file structure based on the filelist. Make sure the filelist lists files, folders and eventually symbolic links (hyperlinks to files stored elsewhere)."><i>[recommended]</i></span>|Open a terminal and run <a href="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Scripts/create_filetree_filelist_powershell_option2.ps1">this script.</a>|On Linux, open a terminal and run <a href="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Scripts/create_filetree_filelist_linux_bash_option2.txt">this script.</a></br></br>On Mac, open a terminal and run <a href="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Scripts/create_filetree_filelist_mac_bash_option2.txt">this script.</a>|

|Task||
|----|---------|
|Delete system files <span title="The SCALA digital repository contains a delete system files function. However, including system files in your SIP includes a heavier METS-file. It is recommended to delete these before adding them in RODA-In."><i>[recommended]</i></span>|Make sure to only execute this step after Create a filelist and filetree [recommended].</br>Manually delete system files.|

</details>

##
<details><summary><b>RODA-In SIP creation</b></summary>

#### RODA-In installation & configuration

|Task||
|----|---------|
|Install & start RODA-In|Follow the <a href="https://rodain.roda-community.org/">installation guide</a>.</br>Start RODA-In.<br><img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture5.png">|
|Configure RODA-In to use the SCALA metadata template|Open the configuration folder.</br><img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture6.png"></br><a href="https://drive.google.com/drive/folders/1PTWH4zf_BDFZ4FjzZVVD_6BreUhwFLZb?usp=sharing">Download</a> the “scala.xml.hbs” and “config.properties” files.<br>Add the file “scala.xml.hbs” to the folder “\roda-in\templates”.</br>Overwrite the config file in “\roda-in” with the “config.properties” file.</br><img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture7.png">|

#### Using RODA-In

|Task||
|----|---------|
|<span title="Bear in mind that Roda-in deletes empty folders without a log. If you need a work around for this issue, see other pre-ingest steps “Create a filelist and filetree for each SIP”."><i>Load your TS in RODA-In</i></span>|Choose the working folder in your file system. This will serve as the root of your project.<br><img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture8.png">|
|Create a new classification scheme|Click to create a new classification scheme.</br><img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture9.png">|
|Add the TS to the IP panel|Select the root folder of your TS.</br>Add this folder to the IP panel by clicking “Associate” or by dragging it to the IP panel.</br>You can also choose to select and add folders/files individually.</br><img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture10.png">|
|<span title="This will determine how (S)IPs will be associated with eachother (e.g. are two IPs siblings or parent-child)."><i>Select an association method</i></span>|Choose the association method <span title="We may explore other SIP/AIP association methods in the future."><i>“One information package for each selected files or folders”</i></span>.</br>Click on the button “Continue”.</br><img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture11.png">|
|Add descriptive metadata|Option 1: Create new metadata from a template.</br>Select option 1.</br>Select the descriptive metadata standard/type of your choice.</br>Click “Continue”.</br></br>Option 2: Load metadata from a single file.</br>Select option 2.</br>Select and add the descriptive metadata file.</br>Select the descriptive metadata standard/type of your file.</br>Click “Continue”.</br><img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture12.png">|
|Edit descriptive metadata [optional]|Make changes to the metadata file using the tool.</br><img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture13.png">|
|Add more representations of the data [optional]|Click “Add representation”.</br><img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture14.png">|
|Add documentation [optional]|Click on “Documentation”.</br>Drop files or folders from your file explorer to add documentation.</br><img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture15.png">|
|Create SIP(s)|Click “Create SIP(s)”.</br><img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture16.png"></br>On the popup screen, select the following options:</br>Export all items - toggle this off if you only want to create a SIP from the currently selected IP. Toggle on if you want to create SIPs for all IPs in the IP (middle) panel. Toggle off by default.</br>Include hierarchy - toggle on to keep relationships between SIPs in their METS (e.g. siblings, parent-child). Toggle on by default.</br>Create inventory report - toggle on to make a list of all items contained per SIP. Toggle off by default.</br>Output directory - select where the SIP(s) will be saved.</br>SIP format - select E-ARK2.</br>SIP names - select Title + ID. This will render the SIP(s) easy to work with later on.</br>Newer versions of RODA-In also require you to add a submitter name and a submitter ID. Simply enter your name; if you don't have an ID from your organization, just enter your name again in the ID field.</br>Click “Start” to create the SIP(s).</br><img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture17.png">|

</details>

##
<details><summary><b>RODA AIP creation</b></summary>

### a. RODA account

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
            <td>
                <ul>
                    <li>Request a RODA account</li>
                </ul>
            </td>
            <td colspan=2>Ask your organization’s admin to create an account for you.</td>
        </tr>
        <tr>
            <td>
                <ul>
                    <li>Log into RODA</li>
                </ul>
            </td>
            <td colspan=2>Log into <a href="https://scala.meemoo.be/#login/welcome">RODA</a> using your username and
                password.</td>
        </tr>
    </tbody>
</table>

### b. Install an FTP client and connect to meemoo

The File Transfer Protocol (FTP) is a standard communication protocol used for the transfer of files between computers.
This is better suited to transfer large SIPs to RODA instead of using their website.

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
            <td>
                <ul>
                    <li>Download and install an FTP client</li>
                </ul>
            </td>
            <td>You can choose whichever client you wish. Here is one option:</br>
                <a href="https://winscp.net/eng/download.php">Download WinSCP</a>.</br>
                Install WinSCP.
            </td>
            <td>You can choose whichever client you wish. Here is one option:</br>
                <a href="https://filezilla-project.org/download.php?platform=osx">Download FileZilla</a>.</br>
                Install FileZilla.
            </td>
        </tr>
        <tr>
            <td>
                <ul>
                    <li>Connect to RODA on meemoo via FTP</li>
                </ul>
            </td>
            <td colspan=2>Create a <a href="https://accounts-qas.meemoo.be/pwm/public/ForgottenPassword">meemoo user
                    account</a>.</br>
                Open your FTP client.</br>
                Use settings:
                <ul>
                    <li>File protocol: SFTP</li>
                    <li>Host name: scala-sftp.meemoo.be</li>
                    <li>Port number: 22</li>
                    <li>User name: [your meemoo username]</li>
                    <li>Password: [your meemoo password]</li>
                </ul>
                Login and connect to the server.</br>
                <img
                    src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture18.png">
            </td>
        </tr>
    </tbody>
</table>

### c. Using RODA

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
            <td>
                <ul>
                    <li>Upload SIPs</li>
                </ul>
            </td>
            <td colspan=2><b>Option 1 (preferred):</b> Upload SIPs via your FTP client.</br>
                Follow the guidelines in <a
                    href="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Dropfolder%20-%20User%20guide.pdf">this
                    user guide</a>.</br></br>Here is a short version:</br>
1. Create a .ready file locally on your computer.</br>
Call the file ".ready". You might have to use your FTP program or a terminal to create this special file. If you have issues creating this file, please contact jelle.kleevens@vai.be.</br>
<img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Screenshot_4.png"></br>
2. Create a job folder for your SIPs on the server.</br>
On the RODA/meemoo server side of your FTP program, navigate to the "incoming" folder. Then navigate to the folder of your institution/company (if there is no such folder, just remain in the "incoming" folder).</br>
Create a new "job" folder. Give it any name you want. This folder will contain all SIPs to be uploaded in this job.</br>
<img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Screenshot_6.png"></br>
Then navigate into this new job folder.</br>
<img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Screenshot_7.png"></br>
3. Load your SIPs into the job folder.</br>
Wait until all SIPs have loaded before going to the next step.</br>
<img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Screenshot_8.png"></br>
4. Drag the .ready file into the job folder.</br>
<img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Screenshot_9.png"></br>
                After they are uploaded, access SIPs via the RODA website.</br></br>
                <span title="There is a limit to the size of allowed information packages when choosing this option."><i><b>Option 2:</b> Upload SIPs via the RODA website.</i></span>
                <ol>
                    <li>On the “Ingest” dropdown menu, click on “Transfer”.</li>
                    <li>On the transfer page, click on the three dots. Then select “Upload”.</br>
                        <img
                            src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture20.png">
                    </li>
                    <li>Choose the SIPs you want to upload.</li>
                    <li>Click “Done”. Your SIPs will now be uploaded.</br>
                        <img
                            src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture21.png">
                    </li>
                </ol>
            </td>
        </tr>
        <tr>
            <td>
                <ul>
                    <li>Select SIPs for processing [only in case of option 2: Upload SIPs via the RODA website]</li>
                </ul>
            </td>
            <td colspan=2>Go to the transfer page.
                <ol>
                    <li>Select the SIPs to process into AIPs.</li>
                    <li>Click the three dots.</li>
                    <li>Click “Start new process”.</li>
                </ol>
                <img
                    src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture22.png">
            </td>
        </tr>
        <tr>
            <td>
                <ul>
                    <li>Select and execute the ingest workflow process [only in case of option 2: Upload SIPs via the
                        RODA website]</li>
                </ul>
            </td>
            <td colspan=2>On the “New process” page:
                <ol>
                    <li>Select “Default ingest workflow (2.0).</li>
                    <li>Select “E-ARK SIP 2 (1.0).</li>
                    <li>Optionally, scroll down and select which plugins should be activated during the ingest workflow.
                    </li>
                    <li>Click “Create”.</li>
                </ol>
                <img
                    src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture23.png">
            </td>
        </tr>
        <tr>
            <td>
                <ul>
                    <li>Monitor the status of the ingest workflow process</li>
                </ul>
            </td>
            <td colspan=2>
                <ol>
                    <li>Go to the “Process” page.</li>
                    <li>Check the status of the ingest process.</li>
                </ol>
                <img
                    src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture24.png">
            </td>
        </tr>
        <tr>
            <td>
                <ul>
                    <li>Edit the AIPs [optional]</li>
                </ul>
            </td>
            <td colspan=2>
                <ol>
                    <li>Click on the process to consult the results. You can check the status of all the AIPs from the
                        process.</br>
                        <img
                            src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture25.png">
                    </li>
                    <li>Click “Created Packages”. You will now go to an AIP inspection page.</br>
                        <img
                            src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture26.png">
                    </li>
                    <li>Inspect the description XML. Editing is possible.</li>
                    <li>Scroll down.</li>
                    <li>Inspect the representations. Editing is possible. Starting processes on file level is possible
                        as well.</br>
                        <img
                            src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture27.png"></br>
                        <img
                            src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture28.png">
                    </li>
                </ol>
            </td>
        </tr>
        <tr>
            <td>
                <ul>
                    <li>Start a new ingest process on the AIPs [optional]</li>
                </ul>
            </td>
            <td colspan=2>Click “Start new process”.</br>
                Select plugins you wish to run in a new process on the AIPs.</br>
                <img
                    src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture29.png">
            </td>
        </tr>
        <tr>
            <td>
                <ul>
                    <li><span title="To be added"><i>Assess the AIP and send to meemoo storage</i></span></li>
                </ul>
            </td>
            <td colspan=2>
            </td>
        </tr>
    </tbody>
</table>

### d. RODA catalogue

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
            <td>
                <ul>
                    <li>Consult RODA catalogue [optional]</li>
                </ul>
            </td>
            <td colspan=2>The catalogue is the inventory of all items or records found in the repository. This includes
                AIPs.</br>
                <img
                    src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture30.png">
            </td>
        </tr>
    </tbody>
</table>

|  |  |
| ----------- | ----------- |
| AIP assessment | ![image](https://user-images.githubusercontent.com/87436774/138085894-e06e3476-a3d7-4d9a-8eea-e122262d366f.png)</br>Assessment is the process of determining whether records and other materials have permanent (archival) value. Assessment may be done at the collection, creator, series, file, or item level.|

</details>

###
<details><summary><b>RODA AIP storage</b></summary>
	
|  |  |
| ----------- | ----------- |
| Store AIP on meemoo | ![](https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/meemoo.png)|
| Check AIP synchronization status |![image](https://user-images.githubusercontent.com/87436774/138085154-5db47ed5-c4f0-4396-99d7-8d5a180b0225.png)|
| Prune AIP in RODA|![image](https://user-images.githubusercontent.com/87436774/138085338-43ad9e04-92d5-424b-90fc-f5ef338734ce.png)|
| Restore pruned AIP representations from meemoo to in RODA|![image](https://user-images.githubusercontent.com/87436774/138085445-8f54ec7f-75f2-4563-bd16-19c03fc360da.png)|
		
</details>

###
<details><summary><b>RODA AIP editing</b></summary>

|  |  |
| ----------- | ----------- |
| Start new process on IP | ![](https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/conversion%20plugin%201.png)|
| File conversion | ![](https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/conversion%20plugin%202.png)|
| Start new process on representation | ![](https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/representation%201.png)|
| Create new representation manually ||
| Create new representation automatically after running plugin | ![](https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/representation%202.png)</br>Deselect "Create dissemination".|
| Set status of representation | ![](https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/representation%203.png)</br> ![](https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/representation%204.png)|
	
</details>

###
<details><summary><b>RODA AIP searching</b></summary>

|  |  |
| ----------- | ----------- |
| Catalogue | ![image](https://user-images.githubusercontent.com/87436774/138086822-128b2adc-c401-483c-a3bc-7180655b9415.png)|
| Assessment tab | ![image](https://user-images.githubusercontent.com/87436774/138086883-73410974-fccd-4df9-8ff0-19dfb341c96f.png)|
| Search facets | ![image](https://user-images.githubusercontent.com/87436774/138086934-89630095-3e7c-4363-a1c9-801ed48cc13a.png)|
| Search field | ![image](https://user-images.githubusercontent.com/87436774/138086973-c0cb4230-cce4-493b-a074-efe077477438.png)|
| Advanced search field | ![image](https://user-images.githubusercontent.com/87436774/138087110-fea88151-0a69-4704-874c-e0607ceb4759.png)|
	
</details>

##
<details><summary><b>Issues & questions</b></summary>

All issues can be reported in the <a href="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/issues">SCALA
    GitHub repository</a>. Please check if the same issue was already reported before creating a new issue.

Alternatively, you can contact jelle.kleevens@vai.be to report the issue or for any other questions.

</details>
