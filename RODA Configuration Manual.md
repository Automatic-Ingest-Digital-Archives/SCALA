# RODA Configuration Manual

###
<details><summary><b>Institution registration</b></summary>
  
These instructions are taken from the [AIDA Administrative Operations Manual](https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Referenced%20Files/MU221844%20-%20AIDA%20Administrative%20Operations%20Manual.pdf) by KEEPS.

To add an institution, the following items of information are required:

* Organization’s name;
* OR identifier;
* At least one email to receive notifications;
* The path of the SFTP share drop folder engine, provided by the server manager.

For each new institution it is necessary to create a group, a user for the ingestion and a new “fonds” intellectual entity in RODA.

__Step 1:__ Create the group:

1. On RODA go to Administration menu and click on “Users and Groups”
2. On “Users and Groups” page, find the kebab menu next to the search button and then click "Add group"
3. Add a group with the organization name and add the permissions that are in
[RODA user types](https://docs.google.com/spreadsheets/d/1nuXN6n75VVjwyudz0MI9uPqnwJ0N0YbuLT9r8xwMQvU/edit#gid=0)
  
__Step 2:__ Create the ingest user:
  
1. On RODA go to Administration menu and click on “Users and Groups”;
2. On “Users and Groups” page, find the kebab menu next to the search button and then click "Add user";
3. Add a user with the following parameters:
    * User name : ingest-<OR_ID>
    * Full name: INGEST_<Organization_name>
    * Email: ingest_<Organization_name>@scala.meemoo.be
    * Groups: ingest

__Step 3:__ Create a new “fonds” intellectual entity
  
1. On RODA go to Catalogue page;
2. Find the kebab menu next to the search button and then click “Create intellectual entity”;
3. Add a new intellectual entity with the following parameters:
    * Type: Dublin Core
    * Metadata, Title: <Organization_name>
    * Metadata, Type: Fonds
  
__Step 4:__ After creating the “fonds” intellectual entity, it is necessary to associate the group and the ingestion user to that fonds:
  
1. On RODA go to Catalogue page and find the new “fonds” intellectual entity;
2. Select the entity, find the kebab menu next to the search button and then click
“Permissions”;
3. Click on “ADD PERMISSION” action;
4. Search for the group created for this institution and click on “SELECT” button;
5. Do the same step above for the ingest user;
6. For assigned groups permission select only the “READ” option;
7. For assigned users permission select only the “Create” option for ingest user;
8. Click on the “APPLY TO HIERARCHY” action.
  
> __It is highly recommended that the following actions be done by a specialist in implementations with containers in a linux environment!__
  
__Step 5:__ For the configuration of the dropfolder mechanism, a file on the server must be modified and the service must be restarted for the actions to take effect.
  
1. Find the docker-compose.yml file on: </br>__/roda/data/git/roda-aida/01-code/deploys/production__
2. Increment the env ```RODA_DROP_FOLDERS_QTY``` and add the following environment vars to roda service:
```
RODA_MONITOR_DROP_USER_N=<INGEST_USER_NAME>
RODA_MONITOR_DROP_PASSWORD_N=<INGEST_USER_PASS>
RODA_DROP_FOLDER_N=/roda/data/sftp/<OR_ID>/incoming/
RODA_DROP_INGEST_PLUGIN_N=org.roda.core.plugins.external.aida.AIDAIngestPlugin
'RODA_DROP_INGEST_PLUGIN_PARAMETERS_N={
"parameter.parent_id":"<FOUND_ID>",
"parameter.sip_to_aip_class":"org.roda.core.plugins.plugins.ingest.EARKSIP2ToAIPPlugin",
"parameter.or_identifier":"<OR_ID>",
"parameter.email_notification":"<email>",
"parameter.can_be_auto_submitted":"false",
"parameter.do_auto_accept":"false",
"parameter.do_aip_prune": "false"
}'
```
Where N is the number following the last configured institution

  3. Restart the service so the new configuration take effect </br>__docker-compose up -d__
  
</details>
  
###
<details><summary><b>Metadata format configuration</b></summary>

RODA supports any descriptive metadata format (i.e. Descriptive Information as stated in the OAIS) as long as it represented by an XML file. If you have a descriptive metadata format that is not based on XML (e.g. CSV, JSON, MARC21, etc.), you will have to convert it to XML before you can use in RODA. Several tools exist on the Web that allow you to convert most data formats into XML.

Once you have your metadata in XML you are ready to package it into a Submission Information Package (SIP) and ingest it on the repository. Alternatively, you may want to create a metadata file directly on the repository by using the functionality provided by the Catalogue. When the metadata format is new to RODA, the repository will do its best to support without the need to do any reconfiguration of system.
  
[Main documentation](https://scala.meemoo.be/#theme/Metadata_Formats.md).
  
The off-the-shelf configurations for EAD 2002 are:
  
* Validation schema: https://github.com/keeps/roda/blob/master/roda-core/roda-core/src/main/resources/config/schemas/ead_2002.xsd
* Visualization stylesheet: https://github.com/keeps/roda/blob/master/roda-ui/roda-wui/src/main/resources/config/crosswalks/dissemination/html/ead_2002.xslt
* Indexing stylesheet: https://github.com/keeps/roda/blob/master/roda-core/roda-core/src/main/resources/config/crosswalks/ingest/ead_2002.xslt
* Editing template: https://github.com/keeps/roda/blob/master/roda-ui/roda-wui/src/main/resources/config/templates/ead_2002.xml.hbs
* Destruction metadata pruning rules: https://github.com/keeps/roda/blob/master/roda-core/roda-core/src/main/resources/config/disposal/destruction/ead_2002.xslt
* Translations (English, other files for other languages) - Title: https://github.com/keeps/roda/blob/98edeaa80218fc7fd7bdeda7c6d90ed2365c78bb/roda-ui/roda-wui/src/main/resources/config/i18n/ServerMessages.properties#L292
* Translations (English, other files for other languages) - Fields: https://github.com/keeps/roda/blob/98edeaa80218fc7fd7bdeda7c6d90ed2365c78bb/roda-ui/roda-wui/src/main/resources/config/i18n/ServerMessages.properties#L303-L418
* Settings - adding metadata schema: https://github.com/keeps/roda/blob/b302d503400decce9fc6c632e3b03b2b135f2949/roda-ui/roda-wui/src/main/resources/config/roda-wui.properties#L242
 
The specific setting of level and title in the search results, pertains to the "level" and "title" indexed fields, defined at:
  
* Level: https://github.com/keeps/roda/blob/master/roda-core/roda-core/src/main/resources/config/crosswalks/ingest/ead_2002.xslt#L343-L356
* Title: https://github.com/keeps/roda/blob/master/roda-core/roda-core/src/main/resources/config/crosswalks/ingest/ead_2002.xslt#L15-L19

To define advanced search fields and fields of the search results:

* Advanced search fields: https://github.com/keeps/roda/blob/master/roda-ui/roda-wui/src/main/resources/config/roda-wui.properties#L261-L354
* Search and catalogue searching results configuration: https://github.com/keeps/roda/blob/master/roda-ui/roda-wui/src/main/resources/config/roda-wui.properties#L910-L1048
* Facets: https://github.com/keeps/roda/blob/master/roda-ui/roda-wui/src/main/resources/config/roda-wui.properties#L1585-L1650

Other configurations available for other lists that present AIPs either than the Search and Catalogue pages.
  
</details>

###
<details><summary><b>User permissions</b></summary>

#### Top level repository permissions

| Permission | Detail |
|------------|--------|
| Create | Permission to submit or create a new archival package under this one. |
| Read | Permission to search or access this archival package. |
| Update | Permission to change this archival package or any of its sub-components. |
| Delete | Permission to delete this archival package or any of its sub-components. |
| Grant | Permission to change the permissions of this archival package. |
  
#### Lower level IP permissions

| Permission |
|------------|
| Retrieve intellectual entities (AIPs) |
| List and search intellectual entities (AIPs) |
| Accept or reject intellectual entities in assessment |
| Create top intellectual entities |
| Create intellectual entities |
| Update intellectual entities |
| Delete intellectual entities |
| List and search representations and computer files |
| Retrieve representations and computer files |
| Create representations and computer files |
| Update representations and computer files |
| Delete representations and computer files |
| List and retrieve descriptive metadata |
| Create descriptive metadata |
| Update descriptive metadata |
| Delete descriptive metadata |
| List and retrieve preservation metadata |
| Create preservation metadata |
| Delete preservation metadata |
| List and retrieve files in transfer |
| Create files and transfer |
| Update files and transfer |
| Delete files and transfer |
| List and view processes (ingest and action) |
| Manage processes (ingest and action) |
| List and view users and groups |
| Manage users and groups |
| List and view notifications |
| Manage notifications |
| List and view log entries |
| Delete log entries |
| List and view preservation risks |
| Manage preservation risks |
| List and view representation information |
| Manage representation information |
| Read and query about the permissions of other users |
| List and view disposal rule information |
| Manage disposal rule information |
| List and view disposal schedule information |
| Manage disposal schedule information |
| Associate or disassociate disposal schedule from intellectual entities (AIPs) |
| List and view disposal hold information |
| Manage disposal hold information |
| Apply or lift disposal hold from intellectual entities (AIPs) |
| List and view disposal confirmation information |
| Manage disposal confirmation information |
| Destroy intellectual entities (AIPs) according to the disposal confirmation |
| Restore destroyed intellectual entities (AIPs) according to the disposal confirmation |
| Permanently delete destroyed intellectual entities (AIPs) according to the disposal confirmation |
  
</details>

