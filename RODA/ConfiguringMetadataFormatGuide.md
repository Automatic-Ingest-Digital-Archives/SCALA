Note that, as you were the ones extending the RODA-in metadata fields, it makes sense to me that you take over the task of configuring your metadata format.
The documentation on how to do so is t:
https://scala.meemoo.be/#theme/Metadata_Formats.md

The off-the-shelf configurations for EAD 2002 are:
•	Validation schema: https://github.com/keeps/roda/blob/master/roda-core/roda-core/src/main/resources/config/schemas/ead_2002.xsd
•	Visualization stylesheet: https://github.com/keeps/roda/blob/master/roda-ui/roda-wui/src/main/resources/config/crosswalks/dissemination/html/ead_2002.xslt
•	Indexing stylesheet: https://github.com/keeps/roda/blob/master/roda-core/roda-core/src/main/resources/config/crosswalks/ingest/ead_2002.xslt
•	Editing template: https://github.com/keeps/roda/blob/master/roda-ui/roda-wui/src/main/resources/config/templates/ead_2002.xml.hbs
•	Destruction metadata pruning rules: https://github.com/keeps/roda/blob/master/roda-core/roda-core/src/main/resources/config/disposal/destruction/ead_2002.xslt
•	Translations (English, other files for other languages):
o	Title: https://github.com/keeps/roda/blob/98edeaa80218fc7fd7bdeda7c6d90ed2365c78bb/roda-ui/roda-wui/src/main/resources/config/i18n/ServerMessages.properties#L292
o	Fields: https://github.com/keeps/roda/blob/98edeaa80218fc7fd7bdeda7c6d90ed2365c78bb/roda-ui/roda-wui/src/main/resources/config/i18n/ServerMessages.properties#L303-L418
•	Settings:
o	Adding metadata schema: https://github.com/keeps/roda/blob/b302d503400decce9fc6c632e3b03b2b135f2949/roda-ui/roda-wui/src/main/resources/config/roda-wui.properties#L242

I also forgot to point out that the search configuration, to define advanced search fields and fields of the search results, are defined at:
•	Advanced search fields: https://github.com/keeps/roda/blob/master/roda-ui/roda-wui/src/main/resources/config/roda-wui.properties#L261-L354
•	Search and catalogue searching results configuration: https://github.com/keeps/roda/blob/master/roda-ui/roda-wui/src/main/resources/config/roda-wui.properties#L910-L1048
•	Facets: https://github.com/keeps/roda/blob/master/roda-ui/roda-wui/src/main/resources/config/roda-wui.properties#L1585-L1650
Other configurations available for other lists that present AIPs either than the Search and Catalogue pages.
