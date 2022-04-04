# SCALA Workflow

Here you can find a description of the steps involved in the SCALA workflow. Following these steps allows you to transfer archival data into SIPs, then into AIPs and finally have them stored on disk for permanent storage.

## 1. Archival data to SIP

### 1.1. Extract archival data from your archive management system

|  |  |
|--|--|
| What | Get your archival data and export it to your computer. |
| How | Arrange your digital born files into comprehensive units of archival data (such as series/files/items/...). For each such unit, we will later on create a SIP. You can go as granular as you wish, and there can be parent-child relations between SIPs. Each unit of archival data must be exported into its own separate folder on your computer. |
| Where | Your archival data is probably in your company's archive management system. |
| Video example | Coming soon! |

### 1.2. Extract descriptive metadata from your archive management system

|  |  |
|--|--|
| What | Prepare descriptive metadata for each SIP. |
| Why | Descriptive metadata will help make sure you can look up and retrieve the content of your SIPs in later stages. The more details given, the better. Examples of descriptive metadata fields are title, creator, producer, scope & content, release date, ... |
| How | From you archive management system, export descriptive metadata into an XML file per SIP. There are international standards with naming and structuring definitions for the fields in these XMLs. EAD 2002 and Dublin Core are famous examples you can adhere to. Otherwise simple key-value pairs work as well.</br></br> If there is no descriptive metadata available in your archive management system, you will have to type it yourself into an XML file per SIP (which can be a painful process). Or maybe there is an AI solution out there which can inspect your archival data and extract the metadata for you! |
| Where | Ideally you can export this data as an XML per SIP from your archive management system. Otherwise you will have to create the XMLs yourself. |
| Video example | Coming soon! |

### 1.3. Create SIPs using RODA-In

|  |  |
|--|--|
| What | Create E-ARK2 SIPs by combining archival data and their respective descriptive metadata in structured way. |
| How | RODA-In is our recommended SIP creation tool. Use it to select your data folders and automatically match descriptive metadata. Then you can make representation edits and add extra documentation if needed. Lastly generate E-ARK2 structured SIPS, with METS file and representations.</br>![image](https://user-images.githubusercontent.com/87436774/161509331-adc80ea2-8ad4-48a5-a5b1-8633440db885.png) |
| Where | You can download the latest RODA-In version [here](https://rodain.roda-community.org/). |
| Video example | Coming soon! |

## 2. SIP to AIP

### 2.1. Upload SIPs to a dedicated SFTP server

|  |  |
|--|--|
| What | Upload SIPs to a dedicated SFTP server using an FTP client. |
| Why | Once uploaded to the server, the RODA tool can automatically start ingesting the SIPs and transform them into AIPs. |
| How | Download an FTP client and connect to the server. Upload SIPs and mark them as 'ready for ingestion by RODA'. |
| Where | Any FTP client you can find online should work, such as WinSCP. Contact a server administration at meemoo to get the required connection details for the server. |
| Video example | Coming soon! |

### 2.2. Transform SIPs into AIPs using the AIDA ingest workflow in RODA

|  |  |
|--|--|
| What | Transform uploaded SIPs into AIPs in RODA. |
| How | Automatically! SIPs on the SFTP server are picked up and go through an AIDA ingest workflow where several plugins do checks and transformations on the SIP. This results in an E-ARK2 AIP if no issues were found. |
| Where | The ingest process can be tracked on the [RODA process tab](https://scala.meemoo.be/#ingest/process). You will need to request RODA login credentials with your organization. |
| Video example | Coming soon! |

#### AIDA ingest workflow steps

RODA executes the following plugins in order during the AIDA ingest workflow.

1. **E-ARK SIP2 to AIP** - Checks if the IP is correct according to E-ARK validators.</br>![image](https://user-images.githubusercontent.com/87436774/161522613-06bb421d-d153-4736-93ec-f08dac8ae681.png)
1. **Remove unwanted files** - A [blacklist](https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/Referenced%20Files/FileName%26ExtensionBlacklist.md) is maintained with useless file formats that are automatically extracted from the SIP. This blacklist can be expanded if necessary.</br>![image](https://user-images.githubusercontent.com/87436774/161522802-49434bd2-946b-4887-b9b6-eda50f859928.png)
1. **Antivirus** - Scans information package(s) for malicious content using the antivirus application ClamAV. If malicious software is detected, a report is generated and a PREMIS event records this action.</br>![image](https://user-images.githubusercontent.com/87436774/161522881-e4b2f078-8f55-47ef-b9d5-f2ef1bd4fad1.png)
1. **Descriptive metadata validation** - Checks that descriptive metadata exists in the information package and that it is valid according to the XML Schemas (XSD) installed in the repository. A validation report is generated indicating which information packets have valid and invalid metadata.</br>![image](https://user-images.githubusercontent.com/87436774/161522958-5627d9a8-f388-425a-ae31-efcae7083dc1.png)
1. **Fixity information computation** - Calculates the file fixity information (also known as checksum) for all data files within an AIP, representation, or file and stores this information in PREMIS objects.</br>![image](https://user-images.githubusercontent.com/87436774/161523009-76ce0ff3-badc-4645-a924-5b8cca22bd86.png)
1. **File format identification (Siegfried)** - Identifies the file format and version of data files contained in information packages using the Siegfried tool. Like DROID, Siegfried identifies files based on digital file signatures stored in the PRONOM database. The job updates the PREMIS object metadata in the information package to store the format identification results. A PREMIS event is logged after the task is executed. [Siegfried configuration information](https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/RODA%20Administrative%20Manual.md#siegfried-configuration).</br>![image](https://user-images.githubusercontent.com/87436774/161523072-26c363b2-6c09-4ef2-a121-36e8e9888245.png)
1. **Verify user authorization** - Checks whether the user has sufficient rights to ingest AIPs for the organization.</br>![image](https://user-images.githubusercontent.com/87436774/161523140-c1e88207-45fb-4933-a861-4355cd42f3e1.png)
1. **Generate meemoo descriptive metadata** - Create a [meemoo.xml](https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/RODA%20Administrative%20Manual.md#meemoo-descriptive-metadata) file with descriptive metadata detailing the synchronization status with meemoo MAM.</br>![image](https://user-images.githubusercontent.com/87436774/161523222-0dfe1ad4-5cfa-428a-91fb-6fc801355ac5.png)

### 2.3. Edit AIPs in RODA

|  |  |
|--|--|
| What | Edit AIPs in RODA and mark them for long-term storage. |
| How | In the RODA catalogue you will have be able to find and inspect all your AIPs.</br>![image](https://user-images.githubusercontent.com/87436774/161526406-50cc9282-2dd2-4d55-858f-17bd21cc13f1.png)</br>You can update the content of data representations or descriptive metadata, or run new [process plugins](https://github.com/Automatic-Ingest-Digital-Archives/SCALA/blob/main/RODA%20Administrative%20Manual.md#plugins) on your AIPs.</br>![image](https://user-images.githubusercontent.com/87436774/161526722-e5c505f7-fe98-4e93-b6ea-a22f9e8e1579.png)</br>These actions result in PREMIS events which are added to the AIPs.</br>![image](https://user-images.githubusercontent.com/87436774/161526543-17ff48c8-a4ac-4797-bfc7-883a56346f8e.png)</br>When you are done, you can mark your AIPs for long-term storage. |
| Where | All this can be done in the [RODA Catalogue](https://scala.meemoo.be/#browse) of your organization. You can use it to search, select and edit AIPs. |
| Video example | Coming soon! |

## 3. AIP to MAM

### 3.1. Submit AIPs from RODA to MAM for permanent storage

|  |  |
|--|--|
| What | Select AIPs to be stored long-term on the meemoo MAM. |
| How | Select all AIPs you wish to store. Then start the 'Submit  AIP to meemoo' plugin.</br>![image](https://user-images.githubusercontent.com/87436774/161527535-8937e2d4-a670-4301-9d84-3446b23cf24c.png)</br>The AIPs will then be submitted to the meemoo MAM. You can follow the progress of this job in RODA. Each AIP will have meemoo metadata present in RODA. This metadata details the synchronization status with MAM.</br>![image](https://user-images.githubusercontent.com/87436774/161529320-7a4fc8f1-8287-48d2-97eb-277a1557fc1c.png)</br>After the AIPs have been safely stored on the MAM, you can choose to remove the data representations in RODA. This way, you keep working memory available in RODA for new processes. The metadata will remain in RODA however, allowing you to keep using its search engine for looking up AIPs. The process of removing data representations is called pruning, and it can be reversed by restoring data from MAM to RODA using 'unpruning'.</br> ![image](https://user-images.githubusercontent.com/87436774/161530342-2ee7a0fd-5c20-4e1c-8293-dbfc1afd35ca.png)</br>![image](https://user-images.githubusercontent.com/87436774/161530432-434658ad-0253-421f-9f60-0155c1e597b0.png)|
| Where | All this can be done in the [RODA Catalogue](https://scala.meemoo.be/#browse) of your organization. Simply select the AIPs you want to submit to MAM, prune or unprune. Then execute the desired plugin. |
| Video example | Coming soon! |

### 3.2. Retrieve AIPs from MAM to RODA for updating

|  |  |
|--|--|
| What | Retrieve AIP representation data from MAM to RODA and make updates to it. |
| How | Select the 'restore pruned representations from meemoo' process and execute it on AIPs to restore their data representations. You can then further edit the data or run other plugins on it. |
| Where | All this can be done in the [RODA Catalogue](https://scala.meemoo.be/#browse) of your organization. Select the AIPs you want to retrieve data representations from and then execute the 'restore pruned representations from meemoo' plugin. |
| Video example | Coming soon! |

### 3.3. Inspect AIPs in MAM

|  |  |
|--|--|
| What | Confirm that your AIPs are stored in the MAM. |
| How | Log into the MAM site and search for your AIPs using the search bar.</br>![image](https://user-images.githubusercontent.com/87436774/161540816-12af1423-d06b-46e9-af96-b7e09e55cfbe.png) |
| Where | You can log into the MAM [here](https://archief-qas.viaa.be/index.php/search?fa%5B%5D=dtag%3A%22root%3Eorganisation_name%3Eapa%22&q%5B%5D=&csid=61765d6e97c24&view=list&limit=&sort=&per_page=0&sd=&ed=). Request user credentials via your meemoo contact. |
| Video example | Coming soon! |
