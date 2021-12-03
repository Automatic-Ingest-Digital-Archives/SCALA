## Roda is a browser tool where you can upload SIPs and transform them to AIPs.

### To use Roda
1. Go to https://roda-community.org/#welcome.

### Siegfried configuration
We normally use the Siegfried REST API, as the command bootstrap time per file is huge. We do an /identify/%s?base64=true&format=json and will keep the original Siegfried information under the representation other metadata. From it, we take the mime type, pronom, and format name and version if of the most prominent match. We currently don't use the basis, warning or other matches to record them in PREMIS.

Example:
```
{
"filename": "/roda/data/storage/aip/3b6aeb0d-4c01-4c9b-a4fe-7541660dc8d5/representations/5c75eb81-84e4-498a-93a2-4551c25f6a3b/data/DILCISBOARD_E-ARK_AIP_1_0.pdf",
"filesize": 2547324,
"modified": "2021-09-14T03:20:22Z",
"errors": "",
"matches": [
{
"ns": "pronom",
"id": "fmt/95",
"format": "Acrobat PDF/A - Portable Document Format",
"version": "1a",
"mime": "application/pdf",
"basis": "extension match pdf; byte match at [[0 8] [2461063 44] [2461112 69]]",
"warning": ""
}
]
}
```


### Unoconv configuration

