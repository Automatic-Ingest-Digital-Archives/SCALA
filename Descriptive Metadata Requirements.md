# Descriptive Metadata Requirements

Descriptive metadata must follow the EAD2002 structure. 

Furthermore, there are several fields required. If these required fields are missing from EAD, the AIP can not be submitted to meemoo. Note that these fields are case sensitive!

__Required fields for submitting to meemoo are:__

- ead/archdesc/did/repository/corpname
- ead/archdesc/did/unittitle
- ead/archdesc/did/scopecontent/p
- ead/archdesc/did/unitid@label='localId'
- ead/archdesc/did/origination@label='creator'/name
- ead/archdesc/did/origination@label='producer'/name

__Optional fields are:__

- ead/archdesc/did/accessrestrict/p

Example of a correct xml:

```xml
<?xml version='1.0' encoding='UTF-8'?>
<ns0:ead xmlns:ns0="urn:isbn:1-931666-22-9" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="urn:isbn:1-931666-22-9 http://www.loc.gov/ead/ead.xsd">
	<ns0:eadheader>
		<ns0:eadid/>
		<ns0:filedesc>
			<ns0:titlestmt>
				<ns0:titleproper/>
			</ns0:titlestmt>
		</ns0:filedesc>
		<ns0:profiledesc>
			<ns0:creation>JelleKleevensVAI</ns0:creation>
		</ns0:profiledesc>
	</ns0:eadheader>
	<ns0:archdesc level="file">
		<ns0:did>
			<ns0:unittitle>Aanbevelingsbrieven van Christian Kieckens voor studenten, stagiairs en medewerkers</ns0:unittitle>
			<ns0:unitid repositorycode="BE-653717" label="localId">0099-CK_0220</ns0:unitid>
			<ns0:unitdate>../..</ns0:unitdate>
			<ns0:repository>
				<ns0:corpname>Vai</ns0:corpname>
			</ns0:repository>
			<ns0:origination label="creator">
				<ns0:name>Vai</ns0:name>
			</ns0:origination>
			<ns0:origination label="producer">
				<ns0:name>SCALA</ns0:name>
			</ns0:origination>
		</ns0:did>
		<ns0:scopecontent>
			<ns0:p>Aanbevelingsbrieven</ns0:p>
			<ns0:p/>
		</ns0:scopecontent>
		<ns0:relatedmaterial>
			<ns0:p/>
		</ns0:relatedmaterial>
		<ns0:accessrestrict>
			<ns0:p>Enkel raadpleegbaar door Vai</ns0:p>
		</ns0:accessrestrict>
		<ns0:processinfo>
			<ns0:p>
				<ns0:date>2021-09-23</ns0:date>
			</ns0:p>
		</ns0:processinfo>
		<ns0:dsc type="combined"/>
	</ns0:archdesc>
</ns0:ead>
```
