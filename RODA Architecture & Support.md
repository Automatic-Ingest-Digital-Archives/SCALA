# RODA Architecture & Support

## Standalone vs cluster architecture

### Single-node RODA implementation

- This option includes a single VM with a RODA instance and a separated Solr instance with embedded Zookeeper.
- External availability monitoring if service is exposed on the Internet.
- Reactive maintenance service.
- Testing/acceptance environment for release acceptance and other testing activities.
- Same configurations as in pilot (metadata, plugins, integrations). No new developments included. No data migration (from pilot system) included.

Included items:

- Update pilot installation with RODA 5 and Solr 8.X1
- Setup new installation of the same single-node configuration as in pilot for testing/acceptance 
environment
- Setup new installation of the same single-node configuration as in pilot for production 
environment
- Review list of users and institutions
- Review integration with SFTP service for drop folder
- Configure system with new infrastructure settings (DNS, SSL, SMTP, etc.)

### 5-node cluster with RODA and monitoring system

- This option includes five (5) VMs setting up a Docker swarm cluster with a RODA instance, Solr ensemble with three (3) nodes and a three (3) replication-factor connected to a Zookeeper ensemble with three (3) nodes. Separated VM for internal Docker registry and a Prometheus+Grafana monitoring stack with curated set of metrics, dashboards and alarms. 
- Alarms sent via email, Slack and connected to KEEPS issue tracker, initiating maintenance and support service without  client’s intervention. External availability monitoring if service is exposed on the Internet.
- Pro-active maintenance service.
- Testing/acceptance environment for release acceptance and other testing activities.
- Same configurations as in pilot (metadata, plugins, integrations). No new developments included. No data migration (from pilot system) included.

Included items:

- New deploy configuration for swarm cluster with RODA 5 and Solr 8.X
- Setup new deployment installation for testing/acceptance environment
- Setup new deployment installation for production environment
- Review list of users and institutions
- Review integration with SFTP service for drop folder
- Configure system with new infrastructure settings (DNS, SSL, SMTP, etc.)
- Setup monitoring stack and connect to the service, setup alerts and notifications.

### Upscaling implications

The biggest change is from a standalone to a cluster architecture, then the effort on deployment, maintenance and system requirements are more or less linear, as we add more Solr instances.

This is true for capacity in terms of global amount of content and access throughput, but not on ingest, as I have explained before, we currently still need to control ingest and edition in a single-node, but we can vertically scale this single-node and have done so in some very large implementations.

Sales can provide with more clear numbers on how double the capacity would look like in terms of deployment and maintenance costs, but in terms of system requirements, we would probably need a couple more Solr nodes with the same characteristics as the other ones. This would of-course depend on how much descriptive metadata is available, small files vs large files, number of users, etc., and the decision to increase is normally based on the current used resources of an implementation, how much index space is available and how much time a query would take on average. The required infrastructure and cluster-size to double the capacity is very often smaller than a linear prediction as metadata ends up being very homogeneous and, unfortunately, records with rich descriptive metadata are not frequent. An analysis of our biggest and older implementation still shows a direct correlation between the number of files and the index size, only matched with the amount of preservation events which correlates with the number of records but is most of the time bigger than the actual descriptive metadata.

## Testing/acceptance environment

We would normally have a testing/acceptance environment in the same infrastructure of the production environment, with the most similar architecture (same number of VMs) but with lesser resources (less CPU, RAM, Storage). All services would be replicated in the testing/acceptance environment and the technology stack should be also in the same version (Operative System, supporting services like SMTP, docker, etc.).

Before an new release in the production system (where release [of the implementation project] is any considerable change in the system, being it software components updates for features, bug fixes or security fixes, or change in the configuration), the release would be first deployed in the testing/acceptance environment and after validation and intervention to the production system would be scheduled.

The testing/acceptance environment should be able to receive and maintain corpora to support the testing of features. Please note that a testing/acceptance environment with reduced resources is not able to test performance or capacity correctly, although some stress testing may be possible.

## Maintenance and support services

### Maintenance and support with remote assistance

- This service encompasses troubleshooting, support in the use of the software and changes to the system’s settings in order for it to cope with the modifications in its execution environment. This service also includes maintenance and support with remote assistance of the entire system installed for the contracted period of time. This service ensures a fast response to an unlimited number of incidences and support requests according to the stipulated level of service.
- The process of maintenance and support performed by KEEP SOLUTIONS is in accordance with the ISO 27001 standard – Information Security Management Systems.

Included items:

- Customer support service (i.e. helpdesk) for the clarification of questions regarding software usage and problems arising from software malfunction;
- Remote assistance for diagnosing and solving technical problems detected in the software or associated services;
- Correction of software configuration problems;
- Small changes to the design;
- Monitoring the availability of the modules exposed on the Internet and immediate notification of the maintenance teams for a quick reactivation of the services;
- Configuration of the software in order to adapt it to any changes made to its infrastructure, execution context or network;
- Access to minor versions of the software that are released during the maintenance and support service period;
- Upgrade to a major version of the software (3-year contracts only).

Duration:

- This service normally has a duration of 1 or 3 years after the system has been put into production, that is, after the completion of the installation and configuration service.

Exceptions:

- Failures in the monitoring system, messaging or telecommunication service provider that compromise the timely communication of the detected anomaly;
- Failures in the internal or external network of the customer and its components (e.g. firewalls, load distributors, etc.) that compromise the correct operation of the services, hardware failures, including the local and/or remote storage system, servers and their components, failures in the operating system that affect the correct operation of the application servers and all of the remaining types of failures whose reason or cause is undetermined;
- The negligent use of the equipment or software, misuse or use for a purpose other than the one intended;
- Damage resulting from inappropriate conditions of the place of use or that has been caused by components developed by third parties;
- Damage resulting from faulty electrical installation (incorrect voltage values), temperature or resulting from external causes (atmospheric discharges and other natural phenomena that influence the proper functioning of the equipment);
- Attempts to repair, update, or modify made by technicians that are unauthorized or unrecognized by KEEP SOLUTIONS;
- When there is an incorrect installation of the software or incorrect configuration changes or improper alterations in the operating system or network that affect the normal operation of the software and that were performed by others;
- When the problem in the equipment is a result of computer viruses, hacking, DoS or incompatibilities with software later installed.

### Maintenance and support hours package

- This service includes the maintenance and support with remote assistance of the whole system installed and user support, based on the hour consumption of a previously contracted package.
- The process of maintenance and support performed by KEEP SOLUTIONS is in accordance with the ISO 27001 standard – Information Security Management Systems.

Included items:

- Customer support service (i.e. helpdesk) for clarification of questions regarding usage and problems arising from software malfunction;
- Remote assistance for diagnosing and solving technical problems detected in the software or associated services;
- Correction of software configuration problems;
- Small changes to the design;
- Monitoring the modules exposed on the Internet for immediate notification of the maintenance teams about eventual service breaks;
- Configuration of the software in order to adapt it to any changes made to its infrastructure, execution context or network;
- Development and installation of new reports;
- Software updates.

Duration:

- The total duration of this service corresponds to the number of hours of the package contracted by the customer. KEEP SOLUTIONS offers packages of 40, 80 and 120 hours.
- The minimum taxation for an intervention reported by the customer is 1 hour.
- The hour package is valid for 1 year after the adjudication date.
