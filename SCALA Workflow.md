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
| How | Download an FTP client and connect to the server. Upload SIPs and mark them as 'ready for ingestion by RODA'.</br>![image](https://user-images.githubusercontent.com/87436774/161511035-c9e7fcfd-4818-4dc0-8e1a-b33666880092.png)|
| Where | Any FTP client you can find online should work, such as WinSCP. Contact a server administration at meemoo to get the required connection details for the server. |
| Video example | Coming soon! |

### 2.2. Transform SIPs into AIPs using the AIDA ingest workflow in RODA

|  |  |
|--|--|
| What | Transform uploaded SIPs into AIPs in RODA. |
| How | Automatically! SIPs on the SFTP server are picked up and go through an AIDA ingest workflow where several plugins do checks and transformations on the SIP. This results in an E-ARK2 AIP if no issues were found. |
| Where | The ingest process can be tracked on the [RODA process tab](https://scala.meemoo.be/#ingest/process). |
| Video example | Coming soon! |

#### AIDA ingest workflow steps

RODA executes the following plugins in order during the AIDA ingest workflow.

1. **E-ARK SIP2 to AIP** - Checks if the IP is correct according to E-ARK validators.
1. **Remove unwanted files** - A blacklist is maintained with useless file formats that are automatically extracted from the SIP. This blacklist can be expanded if necessary.
1. **Antivirus** - Scans information package(s) for malicious content using the antivirus application ClamAV. If malicious software is detected, a report is generated and a PREMIS event records this action.
1. **Descriptive metadata validation** - Checks that descriptive metadata exists in the information package and that it is valid according to the XML Schemas (XSD) installed in the repository. A validation report is generated indicating which information packets have valid and invalid metadata.
1. **Fixity information computation**
1. **File format identification (Siegfried)**
1. **Verify user authorization**
1. **Generate meemoo descriptive metadata**
1. **Auto accept IP**

#### 2.2.2. Consult AIW progress and results

|  |  |
|--|--|
| What |  |
| How |  |
| Where |  |
| Video example | Coming soon! |

### 3. Edit and assess AIPs in RODA

## 3.1. AIP to MAM

|  |  |
|--|--|
| What |  |
| How |  |
| Where |  |
| Video example | Coming soon! |

### 3.2. Submit AIPs from RODA to MAM for permanent storage

|  |  |
|--|--|
| What |  |
| How |  |
| Where |  |
| Video example | Coming soon! |

### 3.3. Retrieve AIPs from MAM to RODA for editing

|  |  |
|--|--|
| What |  |
| How |  |
| Where |  |
| Video example | Coming soon! |
