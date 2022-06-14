# RODA Architecture

## Standalone vs Cluster Architecture

The biggest change is from a standalone to a cluster architecture, then the effort on deployment, maintenance and system requirements are more or less linear, as we add more Solr instances.

This is true for capacity in terms of global amount of content and access throughput, but not on ingest, as I have explained before, we currently still need to control ingest and edition in a single-node, but we can vertically scale this single-node and have done so in some very large implementations.

Sales can provide with more clear numbers on how double the capacity would look like in terms of deployment and maintenance costs, but in terms of system requirements, we would probably need a couple more Solr nodes with the same characteristics as the other ones. This would of-course depend on how much descriptive metadata is available, small files vs large files, number of users, etc., and the decision to increase is normally based on the current used resources of an implementation, how much index space is available and how much time a query would take on average. The required infrastructure and cluster-size to double the capacity is very often smaller than a linear prediction as metadata ends up being very homogeneous and, unfortunately, records with rich descriptive metadata are not frequent. An analysis of our biggest and older implementation still shows a direct correlation between the number of files and the index size, only matched with the amount of preservation events which correlates with the number of records but is most of the time bigger than the actual descriptive metadata.
