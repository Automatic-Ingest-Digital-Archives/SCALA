# RODA Manual Ingestion Via HTTPS

## Summary

|Task||
|----|-----|
|Upload SIPs|Upload SIPs via the RODA website.</i></span></br>1. On the “Ingest” dropdown menu, click on “Transfer”.</br>2. On the transfer page, click on the three dots. Then select “Upload”.</br><img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Referenced%20Files/Pictures/Picture20.png"></br>3. Choose the SIPs you want to upload.</br>4. Click “Done”. Your SIPs will now be uploaded.</br><img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Referenced%20Files/Pictures/Picture21.png">|
|Select SIPs for processing|Go to the transfer page.</br>1. Select the SIPs to process into AIPs.</br>2. Click the three dots.</br>3. Click “Start new process”.</br><img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Referenced%20Files/Pictures/Picture22.png">|
|Select and execute the ingest workflow process|On the “New process” page:</br>1. Select “AIDA ingest workflow (X)".</br>2. Select “E-ARK SIP 2 (1.0).</br>3. Optionally, scroll down and select which plugins should be activated during the ingest workflow.</br>4. Click “Create”.</br><img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Referenced%20Files/Pictures/Picture23.png">|
|Monitor the status of the ingest workflow process|1. Go to the “Process” page.</br>2. Check the status of the ingest process.</br><img src="https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Referenced%20Files/Pictures/Picture24.png">|

## Detailed explanation

The following instructions are taken from the [AIDA Administrative Operations Manual](https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Referenced%20Files/MU221844%20-%20AIDA%20Administrative%20Operations%20Manual.pdf) by KEEPS.

### Manual Ingest

Content is usually ingested via an automatic drop folder mechanism, where new files are detected in the shared folder and ingested, but in cases where the default ingest parameters are not adequate or in case an ingest must be redone, a manual ingest procedure can be started.

To perform the manual ingestion in RODA through the interface, the first step is to click on the navigation bar on the ingestion menu, with the following options:

* Pre-ingest
* Transfer
* Process
* Assessment

To make an ingest you need to select or upload one or more SIP's in the system, so you need to click on the Transfer button in the menu described in above and shown in the figure:</br>
![image](https://user-images.githubusercontent.com/87436774/153420501-4eb5345f-a2b4-46b1-a1f5-e049af1be339.png)

This button sends you to the transfer page, as can be seen here:</br>
![image](https://user-images.githubusercontent.com/87436774/153420598-5c812251-42aa-4d01-9e00-3dd7b90de333.png)

In this page click on the upload button, to upload one or more SIP's, when the SIP's upload is done the page will be the same as shown:</br>
![image](https://user-images.githubusercontent.com/87436774/153420709-7d47a967-539b-45e2-aab7-48d7750dac11.png)

To start the ingest process in this page you need to select all the SIPs that you want to ingest and click on the three dots menu on the right side. This click open a menu with the following options:

* Rename
* Move
* Remove
* Start new process

To continue the ingest process after selecting all the SIP’s for the process, go to ”Start new process” in the menu described above. After clicking “Start new process”, the RODA will show a new page:</br>
![image](https://user-images.githubusercontent.com/87436774/153420960-2e9e5489-3b6d-47f9-a3c9-ee3c607f7135.png)

In this page will appear five options on the left side, being them:

* AIDA ingest workflow (1.0)
* Default ingest workflow (2.0)
* Default ingest workflow (1.0)
* Minimal ingest workflow (1.0)
* Minimal ingest workflow (2.0)

By default the __“AIDA ingest workflow (1.0)”__ is selected, this is the option with all necessary steps to ingest the AIP with AIDA specific requirements. On the right side of the screen you find a panel with options selected by default and fields to fill in like the __“Ingest finished email notification”__ this is the email address that RODA will send the notification of the ingest process. After concluding the configuration of ingest workflow, click on the __“create”__ button on the right side of the panel and the process starts.

This click sends you to the page with all job’s. In this page you can check the state of your job and see the job report by clicking on the row of your job.</br>
![image](https://user-images.githubusercontent.com/87436774/153421251-f32e3e28-dcf9-4982-9197-1bf22abb3568.png)

If the ingest process finished with success you can see the AIP or AIPs created in the catalogue page by clicking the __“Catalogue”__ button in the navigation bar.
