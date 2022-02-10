# DAV AIP Example

###
<details><summary><b>metsHdr</b></summary>
  
![image](https://user-images.githubusercontent.com/87436774/148406033-72d7dccc-d73e-4695-929a-041711722582.png)

- No E-ARK required agent "SUBMITTER" registered (ROLE="OTHER" OTHERROLE="SUBMITTER" TYPE="INDIVIDUAL").
  
</details>

##
<details><summary><b>dmdSec</b></summary>
      
![image](https://user-images.githubusercontent.com/87436774/148405992-e1f3e8f9-08fb-49da-9ea9-ce4bea4b539b.png)
      
- There is a dmdSec for each document or representation. There is a corresponding amdSec for each dmdSec, containing all PREMIS events for that file.
- What is a document or representation exactly?
      
![image](https://user-images.githubusercontent.com/87436774/148406199-d7e5ca85-8f8c-41d0-8b71-f06f11e018c8.png)
  
- Is UploadedBy the same as submitter information in E-ARK?

![image](https://user-images.githubusercontent.com/87436774/148406272-a79ca10d-645f-4647-a575-cef14fbe5ff3.png)
  
- What does 'IsPreservation' mean?

![image](https://user-images.githubusercontent.com/87436774/148406316-df946f8e-318b-426b-9dff-c2a6a07dbd0b.png)
  
- How can a filesize be zero?

![image](https://user-images.githubusercontent.com/87436774/148406394-9781c817-2a35-442a-a16b-a8fd01afd6a3.png)
  
- Is the 'Internal' section similar to meemoo mediahaven metadata?

![image](https://user-images.githubusercontent.com/87436774/148406476-75c3ff40-751e-4c13-9bd9-57881eb48440.png)
  
- IsParentOf is not registered in RODA METS.

![image](https://user-images.githubusercontent.com/87436774/148406534-6e0f1911-72bc-4618-8be3-bc97b60ba7a7.png)

![image](https://user-images.githubusercontent.com/87436774/148406633-a781b70d-d7be-4dca-a812-7a9bd7b453c6.png)
  
- Is the 'Dynamic' section for metadata inherited from the original archival management system?
  
</details>

##
<details><summary><b>amdSec</b></summary>
      
![image](https://user-images.githubusercontent.com/87436774/148407963-c3d0a671-804c-4ae7-af0b-76999efbc53f.png)
  
- There is an amdSec per dmdSec - so one per document or representation.
- They all seem to be PREMIS events. Are they exclusively PREMIS events?

![image](https://user-images.githubusercontent.com/87436774/148408459-738aad12-d597-4d22-9e25-0fc0a5c07cba.png)
  
</details>

##
<details><summary><b>fileSec</b></summary>
      
![image](https://user-images.githubusercontent.com/87436774/148409112-6d4fda16-c19c-4778-b5c7-c4dd2cb7334b.png)

Example of a mets:file element:
  
```xml
<mets:file CHECKSUM="05693677e43aaa69ab8351cb578caf2b" CHECKSUMTYPE="MD5" CREATED="2020-09-25T09:49:56Z" ID="FILEID-Representation-934074b39ef54b1bb74d57a8bff3c22e8eb4ce8109784c7481871b0aea475e4fa9056c457d0a4fc4b027d76cf2b8e3ff" MIMETYPE="application/vnd.openxmlformats-officedocument.presentationml.presentation" USE="Original"/>
```
 
</details>

##
<details><summary><b>structMap</b></summary>
      
![image](https://user-images.githubusercontent.com/87436774/148409636-efd1819a-2a1e-4ff6-b027-139e7c795ad9.png)

![image](https://user-images.githubusercontent.com/87436774/148410189-388cad91-315e-49ed-b67c-486298f9e7b4.png)

- Is the original folder structure represented in here?
- The structMap references all data and metadata files pertaining to each layer of the original folder structure --> right?
  
</details>
