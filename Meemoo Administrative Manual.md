# Meemoo Administrative Manual

## View AIPs on meemoo

|Task||
|----|-----|
|Log into meemoo QAS|[Meemoo QAS site](https://archief-qas.viaa.be/).</br>Username and password are the same as for the meemoo FTP server login.|

## Archiving on meemoo
  
Meemoo keeps its own version of documentation for the project on https://meemoo.atlassian.net/wiki/spaces/SRP/overview?homepageId=3171909795.
  
The current strategy is to archive all AIP versions on meemoo. The AIP version is decided by RODA and is also sent with the AIP metadata sidecar xml to meemoo. RODA will always restore the latest version from meemoo. Obsolete versions are not deleted; it is up to meemoo to develop a way to delete obsolete AIP versions later on.

When archiving to meemoo, a sidecar xml is generated and passed to meemoo for cross platform linking of the IP. Example sidecar xml generated when archiving AIP on meemoo:
  
```xml
AIP successfully preserved in MEEMOO
The following representations were removed from the AIP: 
rep1

sidecar:
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<VIAA>
    <aip_version>1</aip_version>
    <md5>BB096878ED1F765088A85D23C587B482</md5>
    <dc_contributors/>
    <dcterms_created>2021-11-22T14:41:46Z</dcterms_created>
    <dc_creators/>
    <dc_identifier_localid>a7cb55ff-f8de-47ea-9a9f-6d14705d3b97</dc_identifier_localid>
    <dc_identifier_localids>
        <ScalaID>uuid-16c59bcd-b0c7-492f-9c18-89e83ba48604</ScalaID>
    </dc_identifier_localids>
    <CP_id>OR-jq0st8z</CP_id>
    <dc_titles/>
</VIAA>
```
  
Example of metadata in meemoo Mediahaven. It contains information from the sidecar xml, as well as more meemoo added metadata:
  
```json
{
	"mediaObjectId": "20b725eda374408cb149ef3f7725f8c7e05d11a6d42c4e24816c7b8ff3fcc94e",
	"fragmentId": "20b725eda374408cb149ef3f7725f8c7e05d11a6d42c4e24816c7b8ff3fcc94e7926bd8f40884530867f17606f7d29d1",
	"externalId": "qs348gfs3v",
	"title": "qs348gfs3v",
	"description": "",
	"date": "2021:11:22 15:42:09",
	"previewImagePath": "https://mheuropehot.blob.core.windows.net/mediahaven-saas-browse-main/no-preview.png",
	"thumbnailImagePath": "https://mheuropehot.blob.core.windows.net/mediahaven-saas-browse-main/no-preview.png",
	"videoPath": "",
	"originalFileName": "qs348gfs3v.zip",
	"width": 0,
	"height": 0,
	"keywords": [],
	"type": "Document",
	"authors": [],
	"lastModifiedDate": "2021-11-22T14:42:23Z",
	"archiveDate": "2021-11-22T14:42:20Z",
	"exportable": true,
	"editable": true,
	"deletable": false,
	"isPublic": false,
	"ingestSpaceId": "",
	"isInIngestSpace": false,
	"status": "FINISHED",
	"browseStatus": "no_browse",
	"originalStatus": "completed",
	"archiveStatus": "on_disk",
	"workflow": "borndigital",
	"mdProperties": [
		{
			"value": [
				{
					"value": "uuid-16c59bcd-b0c7-492f-9c18-89e83ba48604",
					"attribute": "ScalaID",
					"dottedKey": null
				}
			],
			"attribute": "dc_identifier_localids",
			"dottedKey": null
		},
		{
			"value": "2021-11-22T14:41:46Z",
			"attribute": "dcterms_created",
			"dottedKey": null
		},
		{
			"subKey": "multiselect",
			"value": [
				{
					"value": "VIAA-ONDERWIJS",
					"attribute": "multiselect",
					"dottedKey": null
				},
				{
					"value": "VIAA-ONDERZOEK",
					"attribute": "multiselect",
					"dottedKey": null
				},
				{
					"value": "VIAA-INTRA_CP-CONTENT",
					"attribute": "multiselect",
					"dottedKey": null
				},
				{
					"value": "VIAA-INTRA_CP-METADATA-ALL",
					"attribute": "multiselect",
					"dottedKey": null
				},
				{
					"value": "VIAA-PUBLIEK-METADATA-LTD",
					"attribute": "multiselect",
					"dottedKey": null
				}
			],
			"attribute": "dc_rights_licenses",
			"dottedKey": null
		},
		{
			"value": "a7cb55ff-f8de-47ea-9a9f-6d14705d3b97.zip",
			"attribute": "dc_source",
			"dottedKey": null
		},
		{
			"value": "qs348gfs3v",
			"attribute": "PID",
			"dottedKey": null
		},
		{
			"value": "1",
			"attribute": "aip_version",
			"dottedKey": null
		},
		{
			"value": "apa",
			"attribute": "CP",
			"dottedKey": null
		},
		{
			"value": "2021:11:22 15:42:09",
			"attribute": "CreationDate",
			"dottedKey": null
		},
		{
			"value": "OR-jq0st8z",
			"attribute": "CP_id",
			"dottedKey": null
		},
		{
			"value": "a7cb55ff-f8de-47ea-9a9f-6d14705d3b97",
			"attribute": "dc_identifier_localid",
			"dottedKey": null
		},
		{
			"value": "© apa",
			"attribute": "RightsOwner",
			"dottedKey": null
		},
		{
			"value": "BB096878ED1F765088A85D23C587B482",
			"attribute": "md5_viaa",
			"dottedKey": null
		},
		{
			"value": "borndigital",
			"attribute": "sp_name",
			"dottedKey": null
		}
	],
	"relations": {}
}
```
  


## Meemoo AIP querying
  
Querying the meemoo API for AIPs is based on the key dc_identifier_localidsScalaID. There are two versions of the API (v1 and v2). Make sure you are logged into the meemoo qas.
  
v1</br>
General information about searching items using search fields with REST API v1: https://archief-qas.viaa.be/mediahaven-rest-api/#mediahaven-rest-api-manual-search-for-media-objects-search-on-data-within-specific-fields.</br>
GET call: https://archief-qas.viaa.be/mediahaven-rest-api/resources/media/?q=%2B(dc_identifier_localidsScalaID:"{scala-id}")</br>
Example: https://archief-qas.viaa.be/mediahaven-rest-api/resources/media/?q=%2B(dc_identifier_localidsScalaID:"uuid-fd82992d-169f-44ed-9139-6e1ad4f9e40a")</br>

v2</br>
General information about searching items using search fields with REST API v2: https://archief-qas.viaa.be/mediahaven-rest-api/v2/api-docs/index.html#mediahaven-rest-api-manual-search-for-records-search-on-data-within-specific-fields.</br>
GET call: https://archief-qas.viaa.be/mediahaven-rest-api/v2/records?q=%2B(dc_identifier_localidsScalaID:"{scala-id}")</br>
Example: https://archief-qas.viaa.be/mediahaven-rest-api/v2/records?q=%2B(dc_identifier_localidsScalaID:"uuid-fd82992d-169f-44ed-9139-6e1ad4f9e40a")</br>

General info about the REST API: https://developer.meemoo.be/docs/development/#rest-api.
  


## MAM access rights information
  
Accessibility is defined in the following boolean fields. The default settings are:

```json
"exportable": true,
"editable": true,
"deletable": false,
"isPublic": false
```
	
Additionally, the AIPs fall under meemoo’s licensing framework. These are stored in the mdProperties’ dc_rights_licenses field. The default settings are:

```json
{
	"subKey": "multiselect",
	"value": [
		{
			"value": "VIAA-ONDERWIJS",
			"attribute": "multiselect",
			"dottedKey": null
		},
		{
			"value": "VIAA-ONDERZOEK",
			"attribute": "multiselect",
			"dottedKey": null
		},
		{
			"value": "VIAA-INTRA_CP-CONTENT",
			"attribute": "multiselect",
			"dottedKey": null
		},
		{
			"value": "VIAA-INTRA_CP-METADATA-ALL",
			"attribute": "multiselect",
			"dottedKey": null
		},
		{
			"value": "VIAA-PUBLIEK-METADATA-LTD",
			"attribute": "multiselect",
			"dottedKey": null
		}
	],
	"attribute": "dc_rights_licenses",
	"dottedKey": null
}
```

However, all settings in meemoo should be implementations of the original Access Rights Information stored in the partner’s Archive Management Systems. In case of an exit-scenario, the meemoo MAM access metadata SHOULD NOT be essential.

AIDA will probably always opt for keeping access rights information outside the AIP-package, since this information is prone to change and since it is not essential for safeguarding the AIP’s authenticity, integrity, useability and findability.

If however integration of Access Rights Information would be necessary within the AIP-package, this can be done by using PREMIS rights information or by adding a descriptive metadata file containing the access rights information. It is up to each partner to foresee a mapping from its conventions to the general AIDA convention. However, this general AIDA convention will  only be established when necessary. Therefore, it is highly recommended that an AIDA partner uses established practices in the archival world, like PREMIS rights, EAD or RiC-CM.
