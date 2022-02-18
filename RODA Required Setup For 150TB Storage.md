# RODA Required Setup For 150TB Storage

### _Question: Which components are currently running on the server?_

You currently have the following components:

-	Docker 20.10.5
-	Docker compose 1.25.0
-	RODA 4.2.0
-	Apache Solr 7.7.3
-	Traefik 2.0.7

Besides that you also have an SFTP server that was installed and is managed by Herwig. RODA component includes other sub-components, like Siegfried, ClamAV, and tools installed by the plugins.

### _Question: What RODA setup would allow us to archive and work with ~130TB of data?_

If the 130TB are composed of very large files, and therefore there are few files, you'd be able to cope with the current setup given that you upgrade de amount of storage (currently you have 3TB available).

In terms of number of files, you are currently with a single indexing node with 89GB of SSD and 16GB of RAM dedicated to index (out of the available 32GB). This would be able to cope with a maximum of 5 million files/records, depending on the metadata of the record and file and their characteristics (heterogeneity). You could further improve your single indexing node up to 32GB of dedicated RAM and 500GB of SSD, and this would stretch it to a maximum of 10-50 million files/records. 

Currently, you have about 31k files occupying around 500GB, for 130TB you would have around 8 million files, for which the current setup would be able to manage if you could upgrade the RAM and the indexing SSD storage a bit.

> So, generally, for supporting 130TB I would recommend upgrading storage to 150 TB, indexing SSD to 500GB to 1TB, and double the available VM RAM (from 32GB to 64GB) so you could upgrade SOLR to 32 GB of dedicated RAM.

 ### _Question: Should everything be put on one system? How many cores are required per system? Seeing as the indexer possibly requires a lot of computing power._

Using a single system would use resources more efficiently, as every institution would share resources. This is off-course a double-edged sword, as the behaviour of one institution can affect the resources available for another, and you would not be able to easily reserve resources or set quotes for resources.

The cores per system better correlate with the ingest throughput (and preservation actions throughput), as ingest and other jobs will be parallelized into a thread pool with the number of threads equal to the number of available CPUs.

> So, you should increase CPUs if you want to increase job parallelization.
 
### _Question: Is the 150TB storage needed for disk storage, or for the tape storage. Should there be any buffer space on the disk? If so, how much?_

> That all depends on the behaviour of your institutions, how much time their content takes to ingest, if the content is submitted sparsely or all at once, if ingest assessment is enabled, if they use the restore from meemoo function frequently and/or with a lot of content, if meemoo availability is better than what was observed during the pilot.

With 150TB on disk would allow to have all content (130TB) available in RODA at any point. If you limit the users to have their content in meemoo (tapes) but cannot restore it in RODA due to lack of disk space, then this would need to be managed with them.

Generally, I think there is a gap because it is hard for an institution to know how many resources they have and what operations they can do. How much disk space are they using in RODA and in MEEMOO, how much can they use and what would be the result of a restore from meemoo operation on a certain set of AIPs.

Also, you were referring to tape space, but we could only test meemoo submission and restore using meemoo "on disk", so how would the system behave with submit and restore from tapes is unknown.
