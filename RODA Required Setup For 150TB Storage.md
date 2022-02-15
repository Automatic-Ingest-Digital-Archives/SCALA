# RODA Required Setup For 150TB Storage

_Question: What RODA setup would allow us to archive and work with ~130TB of data?_

If the 130TB are composed of very large files, and therefore there are few files, you'd be able to cope with the current setup given that you upgrade de amount of storage (currently you have 3TB available).

In terms of number of files, you are currently with a single indexing node with 89GB of SSD and 16GB of RAM dedicated to index (out of the available 32GB). This would be able to cope with a maximum of 5 million files/records, depending on the metadata of the record and file and their characteristics (heterogeneity). You could further improve your single indexing node up to 32GB of dedicated RAM and 500GB of SSD, and this would stretch it to a maximum of 10-50 million files/records. 

Currently, you have about 31k files occupying around 500GB, for 130TB you would have around 8 million files, for which the current setup would be able to manage if you could upgrade the RAM and the indexing SSD storage a bit.

> So, generally, for supporting 130TB I would recommend upgrading storage to 150 TB, indexing SSD to 500GB to 1TB, and double the available VM RAM (from 32GB to 64GB) so you could upgrade SOLR to 32 GB of dedicated RAM.
