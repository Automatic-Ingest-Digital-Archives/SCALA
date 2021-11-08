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
|Create and add additional non-xml metadata [optional]|Create a folder called “_submissionDocumentation” in the root of the TS.</br><span title="E.g. file format identification files, file lists, etc."><i>Add additional non-xml metadata accompanying the content files</i></span>|

#### Extra <span title="With RODA-In, you can create basic SIPs for ingest into the SCALA repository. All Roda-In does is to create a descriptive metadata file with a METS-file, preserving fixity. You might want to do other steps before ingest. We give a short overview of these with the different options about the way with which you can achieve this. Bear in mind integrated pre-ingest tools like RMtool exist for more intensive pre-ingest operations."><i>data preparation tasks</i></span>

Here are optional but recommended tasks to execute before submitting a TS to RODA-In. Please execute your chosen tasks
in the order presented.

|Task|Win10|Mac/Linux|
|----|-----|---------|
|Unpack zipped files <span title="The SCALA digital repository does not unpack container files or zipped files, due to multiple possible issues. zip-files in the SIP will be zip-files in the AIP. If you want to unpack all ZIP-files you can do this before. However, be aware that this always requires some human control."><i>[optional]</i></span>|Open a terminal and run:</br><code>Expand-Archive -Path ".\*.zip"</code>,</br>where * is the name of the zip file.|Open a terminal and run:</br><code>unzip "*.zip" && ls -l</code>,</br>where * is the name of the zip file.|

|Task|Win10|
|----|-----|
|<span title="Trailing and leading whitespace in filenames causes RODA-In to crash in Windows."><i>Trim whitespace from filenames in Windows [optional]</i></span>|Manually trim whitespace from filenames.</br></br>OR run <a href="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Scripts/RemoveWhitespaceFromDirsAndFiles.txt">this bash script</a> in a <b>Mac/Linux environment</b> in the root folder of your TS, before continuing on Windows.|

A backup, or data backup is a copy of computer data taken and stored elsewhere so that it may be used to restore the original after a data loss event. These files may be automatically generated by your operating system. Normally, such files are of no value to your TS.

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
<details><summary><b>RODA-In installation & configuration</b></summary>

|Task||
|----|---------|
|Install & start RODA-In|Download RODA-In 2.3.1 <a href="https://github.com/keeps/roda-in/releases/tag/2.3.1">here</a> and install it.</br>Start RODA-In.<br><img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture5.png">|
|Configure RODA-In to use the SCALA metadata template|Open the configuration folder.</br><img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture6.png"></br><a href="https://drive.google.com/drive/folders/1PTWH4zf_BDFZ4FjzZVVD_6BreUhwFLZb?usp=sharing">Download</a> the “scala.xml.hbs” and “config.properties” files.<br>Add the file “scala.xml.hbs” to the folder “\roda-in\templates”.</br>Overwrite the config file in “\roda-in” with the “config.properties” file.</br><img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture7.png">|

</details>

###
<details><summary><b>RODA-In SIP creation</b></summary>

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
|Create SIP(s)|Click “Create SIP(s)”.</br><img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture16.png"></br>On the popup screen, select the following options:</br>1. Export all items - toggle this off if you only want to create a SIP from the currently selected IP. Toggle on if you want to create SIPs for all IPs in the IP (middle) panel. Toggle off by default.</br>2. Include hierarchy - toggle on to keep relationships between SIPs in their METS (e.g. siblings, parent-child). Toggle on by default.</br>3. Create inventory report - toggle on to make a list of all items contained per SIP. Toggle off by default.</br>4. Output directory - select where the SIP(s) will be saved.</br>5. SIP format - select E-ARK2.</br>6. SIP names - select Title + ID. This will render the SIP(s) easy to work with later on.</br>Newer versions of RODA-In also require you to add a submitter name and a submitter ID. Simply enter your name; if you don't have an ID from your organization, just enter your name again in the ID field.</br>Click “Start” to create the SIP(s).</br><img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture17.png">|

</details>

##
<details><summary><b>RODA account, FTP client and meemoo connection</b></summary>

|Task||
|----|-----|
|Request a RODA account|Ask your organization’s admin to create an account for you.|
|Log into RODA|Log into <a href="https://scala.meemoo.be/#login/welcome">RODA</a> using your username and password.|
	
Your organization's administrator can add you to the ingest-user account group. Then you should receive email confirmation for each finished ingest job.
	
The File Transfer Protocol (FTP) is a standard communication protocol used for the transfer of files between computers.
This is better suited to transfer large SIPs to RODA instead of using their website.

|Task|Win10|Mac/Linux|
|----|-----|---------|
|Download and install an FTP client|You can choose whichever client you wish. Here is one option:</br><a href="https://winscp.net/eng/download.php">Download WinSCP</a>.</br>Install WinSCP.|You can choose whichever client you wish. Here is one option:</br><a href="https://filezilla-project.org/download.php?platform=osx">Download FileZilla</a>.</br>Install FileZilla.|

|Task||
|----|-----|
|Connect to RODA on meemoo via FTP|Create a <a href="https://accounts-qas.meemoo.be/pwm/public/ForgottenPassword">meemoo user account</a>.</br>Open your FTP client.</br>Use settings:</br>* File protocol: SFTP</br>* Host name: scala-sftp.meemoo.be</br>* Port number: 22</br>* User name: [your meemoo username]</br>* Password: [your meemoo password]</br></br>Login and connect to the server.</br><img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture18.png">|

</details>

###
<details><summary><b>RODA AIP creation & assessment</b></summary>

|Task||
|----|-----|
|Upload SIPs|<b>Option 1 (preferred):</b> Upload SIPs via your FTP client.</br>Follow the guidelines in <a href="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Dropfolder%20-%20User%20guide.pdf">this user guide</a>.</br></br>Here is a short version:</br>1. Create a .ready file locally on your computer.</br>Call the file ".ready". You might have to use your FTP program or a terminal to create this special file. If you have issues creating this file, please contact jelle.kleevens@vai.be.</br><img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Screenshot_4.png"></br>2. Create a job folder for your SIPs on the server.</br>On the RODA/meemoo server side of your FTP program, navigate to the "incoming" folder. Then navigate to the folder of your institution/company (if there is no such folder, just remain in the "incoming" folder).</br>Create a new "job" folder. Give it any name you want. This folder will contain all SIPs to be uploaded in this job.</br><img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Screenshot_6.png"></br>Then navigate into this new job folder.</br><img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Screenshot_7.png"></br>3. Load your SIPs into the job folder.</br>Wait until all SIPs have loaded before going to the next step.</br><img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Screenshot_8.png"></br>4. Drag the .ready file into the job folder.</br><img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Screenshot_9.png"></br>After they are uploaded, access SIPs via the RODA website.</br></br><span title="There is a limit to the size of allowed information packages when choosing this option."><i><b>Option 2:</b> Upload SIPs via the RODA website.</i></span></br>1. On the “Ingest” dropdown menu, click on “Transfer”.</br>2. On the transfer page, click on the three dots. Then select “Upload”.</br><img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture20.png"></br>3. Choose the SIPs you want to upload.</br>4. Click “Done”. Your SIPs will now be uploaded.</br><img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture21.png">|
|Select SIPs for processing [only in case of option 2: Upload SIPs via the RODA website]|Go to the transfer page.</br>1. Select the SIPs to process into AIPs.</br>2. Click the three dots.</br>3. Click “Start new process”.</br><img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture22.png">|
|Select and execute the ingest workflow process [only in case of option 2: Upload SIPs via the RODA website]|On the “New process” page:</br>1. Select “AIDA ingest workflow (X)".</br>2. Select “E-ARK SIP 2 (1.0).</br>3. Optionally, scroll down and select which plugins should be activated during the ingest workflow.</br>4. Click “Create”.</br><img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture23.png">|
|Monitor the status of the ingest workflow process|1. Go to the “Process” page.</br>2. Check the status of the ingest process.</br><img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture24.png">|
|Edit the AIPs [optional]|Click on the process to consult the results. You can check the status of all the AIPs from the process.</br><img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture25.png"></br>1. Click “Created Packages”. You will now go to an AIP inspection page.</br><img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture26.png"></br>2. Inspect the description XML. Editing is possible.</br>3. Scroll down.</br>4. Inspect the representations. Editing is possible. Starting processes on file level is possible as well.</br><img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture27.png"></br><img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture28.png">|
|Start a new ingest process on the AIPs [optional]|Click “Start new process”.</br>Select plugins you wish to run in a new process on the AIPs.</br><img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/Picture29.png">|

|Task||
|----|-----|
|AIP assessment|![image](https://user-images.githubusercontent.com/87436774/138085894-e06e3476-a3d7-4d9a-8eea-e122262d366f.png)</br>Assessment is the process of determining whether records and other materials have permanent (archival) value. Assessment may be done at the collection, creator, series, file, or item level.|

</details>

###
<details><summary><b>RODA AIP storage</b></summary>
	
|Task||
|----|-----|
| Store AIP on meemoo | ![](https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/meemoo.png)|
| Check AIP synchronization status |![image](https://user-images.githubusercontent.com/87436774/138085154-5db47ed5-c4f0-4396-99d7-8d5a180b0225.png)|
| Prune AIP in RODA|Pruning an AIP includes removing PREMIS files and other technical metadata. This results in pruned AIPs having less information for reporting. Therefore, pruning should generally not be done.</br>![image](https://user-images.githubusercontent.com/87436774/138085338-43ad9e04-92d5-424b-90fc-f5ef338734ce.png)|
| Restore pruned AIP representations from meemoo to in RODA|![image](https://user-images.githubusercontent.com/87436774/138085445-8f54ec7f-75f2-4563-bd16-19c03fc360da.png)|
		
</details>

###
<details><summary><b>RODA AIP editing</b></summary>

|Task||
|----|-----|
| Start new process on IP | ![](https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/conversion%20plugin%201.png)|
| File conversion | ![](https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/conversion%20plugin%202.png)|
| Start new process on representation | ![](https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/representation%201.png)|
| Create new representation manually ||
| Create new representation automatically after running plugin | ![](https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/representation%202.png)</br>Deselect "Create dissemination".|
| Set status of representation | ![](https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/representation%203.png)</br> ![](https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Manual%20Ingest/Pictures/representation%204.png)|
	
</details>

###
<details><summary><b>RODA AIP searching</b></summary>

|Task||
|----|-----|
| Catalogue | ![image](https://user-images.githubusercontent.com/87436774/138086822-128b2adc-c401-483c-a3bc-7180655b9415.png)|
| Assessment tab | ![image](https://user-images.githubusercontent.com/87436774/138086883-73410974-fccd-4df9-8ff0-19dfb341c96f.png)|
| Search facets | ![image](https://user-images.githubusercontent.com/87436774/138086934-89630095-3e7c-4363-a1c9-801ed48cc13a.png)|
| Search field | ![image](https://user-images.githubusercontent.com/87436774/138086973-c0cb4230-cce4-493b-a074-efe077477438.png)|
| Advanced search field | ![image](https://user-images.githubusercontent.com/87436774/138087110-fea88151-0a69-4704-874c-e0607ceb4759.png)|
	
</details>

###
<details><summary><b>RODA AIP plugins</b></summary>
	
| Workflow| Details|
|---------|--------|
| AIP Virus check (ClamAV 0.103.3/26312/Mon Oct 4 09:03:30 2021)| Scans Information Package(s) for malicious software using the Antivirus application ClamAV. Clam AntiVirus (ClamAV) is a free and open-source, cross-platform antivirus software toolkit able to detect many types of malicious software, including viruses.If malicious software is detected a report will be generated and a PREMIS event will record this occurrence.Categories: validation, characterization |
| AIP batch export (1.0)| Exports selected AIP(s) to a ZIP file or folder on the server file system. To retrieve the results of the export action you must have access to the server file system.NOTE: This action can potentially generate a large amount of data. Make sure you select a destination folder that has enough storage space to accommodate the results of the export action.Categories: management |
| AIP corruption risk assessment (1.0)| Computes the fixity/checksum information of files inside an Archival Information Package (AIP) and verifies if this information differs from the information stored in the preservation metadata (i.e. PREMIS objects). If so, it creates a new risk called “File(s) corrupted due to hardware malfunction or human intervention“ and assigns the corrupted file to that risk in the Risk register.It also creates an incidence linked to the representation if a PREMIS file exists but the associated file does not. Within the repository, fixity checking is used to ensure that digital files have not been affected by data rot or other digital preservation dangers. By itself, fixity checking does not ensure the preservation of a digital file. Instead, it allows a repository to identify which corrupted files to replace with a clean copy from the producer or from a backup.Categories: risk management|
| Create E-ARK AIP manifest files (METS.xml) (1.0)| Plugin that generates E-ARK AIP manifest files ("METS.xml") from existing AIP information in the storage layer. This plugin only works with filesystem as the storage service.Categories: misc |
| Create E-ARK DIP manifest files (METS.xml) (1.0)| Plugin that generates E-ARK DIP manifest files ("METS.xml") from existing AIP information in the storage layer. This plugin only works with filesystem as the storage service.Categories: dissemination|
| File format identification (Siegfried) (1.9.1 w/ DROID_SignatureFile_V97) | Identifies the file format and version of data files included in Information Packages using the Siegfried tool (a signature-based file format identification tool that supports PRONOM identifiers and Mimetypes).The task updates PREMIS objects metadata in the Information Package to store the results of format identification. A PREMIS event is also recorded after the task is run.Categories: format identification, characterization |
| Fixity information computation (1.0)| Computes file fixity information (also known as checksum) for all data files within an AIP, representation or file and stores this information in PREMIS objects within the corresponding entity. This task uses SHA-256 as the default checksum algorithm, however, other algorithms can be configured in “roda-core.properties”.File fixity is the property of a digital file being fixed, or unchanged. “AIP corruption risk assessment” is the process of validating that a file has not changed or been altered from a previous state. In order to validate the fixity of an AIP or file, fixity information has to be generated beforehand.Categories: characterization|
| Image conversion (imagemagick) (6.9.11-60)| ImageMagick is a tool that can read and write images in a variety of formats (over 200) including PNG, JPEG, JPEG-2000, GIF, TIFF, DPX, EXR, WebP, Postscript, PDF, and SVG.ImageMagick can also be used to resize, flip, mirror, rotate, distort, shear and transform images, adjust image colours, apply various special effects, or draw text, lines, polygons, ellipses and Bézier curves (e.g. set Command arguments to “ -resample 90” to resize the image to 90 dpi).The results of conversion will be placed on a new representation under the same Archival Information Package (AIP) where the files were originally found. A PREMIS event is also recorded after the task is run.For a full list of supported formats, please visit http://www.imagemagick.org/script/formats.phpCategories: conversion, dissemination|
| Inventory report (1.0)| Creates a report in CSV format that includes a listing of all AIP and its inner files (data and metadata) which also includes some of their technical properties (e.g. sipId, aipId, representationId, filePath, SHA-256, MD5, SHA-1). The report will be stored in a folder on the server side as defined by the user. To obtain the report, one needs access to the storage layer of the repository server.This report may be used to validate the completeness and correctness of an ingest process.Categories: management|
| Metadata validation (1.0) | Checks if the descriptive metadata included in the Information Package is present, and if it is valid according to the XML Schemas installed in the repository. A validation report is generated indicating which Information Packages have valid and invalid metadata.Categories: validation, characterization|
| Move orphan(s) to a parent node (1.0) | Moves selected AIP(s) that are also orphans, i.e. AIPs whose direct ancestor in the catalogue hierarchy does not exist (except root level nodes) to a new parent node defined by the user.This task aims to fix problems that may occur when SIPs are ingested but not all the necessary items to construct the catalogue hierarchy have been received or properly ingested.Categories: management |
| Office documents conversion (unoconv) (7.0.4.2) | Converts office files using the “unoconv” (Universal Office Converter). The results of conversion will be placed on a new representation under the same Archival Information Package (AIP) where the files were originally found. A PREMIS event is also recorded after the task is run.“unoconv” is a tool that converts between any document format that OpenOffice understands. It uses OpenOffice's UNO bindings for non-interactive conversion of documents.Supported document formats include Open Document Format (odt), MS Word (doc), MS Office Open/MS OOXML (ooxml), Portable Document Format (pdf), HTML (html), XHTML (xhtml), RTF (rtf), Docbook (docbook), and more.The outcome of this task is the creation of a new OpenOffice (and thus unoconv) support various import and export formats. Not all formats that can be imported can be exported and vice versa. For a full list of supported formats, please visit - http://dag.wiee.rs/home-made/unoconv/Categories: conversion, dissemination |
| Prune AIP representations (1.0) | This plugin will remove all representations from the AIPCategories: Meemoo |
| Rebuild AIP index (1.0) | Clears the index and recreates it from actual physical data that exists on the storage. This task aims to fix inconsistencies between what is shown in the graphical user interface of the repository and what is actually kept at the storage layer. Such inconsistencies may occur for various reasons, e.g. index corruption, ungraceful shutdown of the repository, etc.Categories: reindex|
| Rebuild preservation AIP event index (1.0)| Clears the index and recreates it from actual physical data that exists on the storage. This task aims to fix inconsistencies between what is shown in the graphical user interface of the repository and what is actually kept at the storage layer. Such inconsistencies may occur for various reasons, e.g. index corruption, ungraceful shutdown of the repository, etc.Categories: reindex|
| Restore pruned representations from Meemoo (1.0)| Fetch the representations from Meemoo API and restores back to RODA. A PREMIS event is recorded after the task is run.Categories: Meemoo |
| Risk association (1.0)| Associates selected items to existing risks in the Risk registry (as risk incidences).This task is convenient when the preservation expert wants to associate a set of items (e.g. AIPs, representations or files) to a risk to be mitigated in the near future.As an example, if the designated community of the repository provides feedback that a given format under a certain collection is not being displayed properly on the graphical user interface of the repository, then the preservation expert may want to mark these files to be targeted by a preservation action (e.g. generate new representations for access purposes).Categories: risk management |
| Submit AIP to Meemoo (1.0)| AIP submission plugin for MEEMOO integrated serviceCategories: Meemoo|
| Verify user authorization (1.0) | Checks if the user has enough permissions to place the AIP under the desired node in the classification schemeCategories: validation |
	
</details>


##
<details><summary><b>View AIPs on meemoo</b></summary>

|Task||
|----|-----|
|Log into meemoo QAS|[Meemoo QAS site](https://archief-qas.viaa.be/).</br>Username and password are the same as for the meemoo FTP server login.|

</details>

##
<details><summary><b>Issues & questions</b></summary>

All issues can be reported in the <a href="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/issues">SCALA
    GitHub repository</a>. Please check if the same issue was already reported before creating a new issue.

Alternatively, you can contact jelle.kleevens@vai.be to report the issue or for any other questions.

</details>
