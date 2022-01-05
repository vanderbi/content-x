
About EDI

Table of Contents


[TOC]



## Vision & Mission {#vision-&-mission}

The Environmental Data Initiative envisions a future of intensified and diverse scientific discovery fueled by data commons accessible to all.

We preserve environmental data for open and reproducible science, to promote synthesis across space and time, and to aid in the assessment of environmental change and its consequences.


## Project {#project}

The Environmental Data Initiative (EDI) provides key services and technical expertise to the scientific community that ensure environmental and ecological data are well curated and accessible for discovery and re-use well into the future. We assist researchers from field stations, individual laboratories, and research projects of all sizes to archive and publish their environmental data. EDI is committed to make data Findable, Accessible, Interoperable, and Reusable (FAIR).

We provide support, training, and resources to help archive and publish high-quality data and metadata. We operate a secure data repository and work closely with other leaders in information management, like the LTER Network Communications Office and DataONE, to promote data management best practices and stewardship. Our team consists of highly motivated and experienced data practitioners, software developers, and research scientists.

EDI is currently funded through grants from the National Science Foundation’s (NSF) Division of Biological Infrastructure to the University of New Mexico (Award #1931143) and the University of Wisconsin-Madison (Award #1931174): “Collaborative Research: Environmental Data Initiative: Sustaining the Legacy of Scientific Data”. Previous NSF funding was awarded through grants #1565103 and #1629233.


## Team {#team}

Corinna Gries is Principal Investigator of EDI and is based at the University of Wisconsin. Corinna leads the data curation, outreach and training activities of EDI and can be reached at cgries@wisc.edu.

Mark Servilla is Principal Investigator of EDI and is based at the University of New Mexico. Mark leads the development of the PASTA data repository software and can be reached at [mark.servilla@gmail.com](mailto:mark.servilla@gmail.com).

Robert B. Waide is an EDI co-PI and involved in project level outreach. He is based at the University of New Mexico and can be reached at [rbwaide@unm.edu](mailto:rbwaide@unm.edu).

Paul Hanson is an EDI co-PI and involved in project level outreach. He is based at the University of Wisconsin-Madison and can be reached at [pchanson@wisc.edu](mailto:pchanson@wisc.edu).

Margaret O’Brien assists in the design and development of efficient means to assure data submission by community members based on needs assessments and community science priorities. Margaret is based at the University of California at Santa Barbara and may be reached at [margaret.obrien@ucsb.edu](mailto:margaret.obrien@ucsb.edu).

Kristin Vanderbilt supports the Data Management as a Service activity. She is based at the University of New Mexico. Kristin can be reached at krvander@fiu.edu. 

James Brunt provides system administration and data management services in support of the EDI data repository. James is based at the University of New Mexico and may be reached at jbrunt@unm.edu.

Susanne Grossman-Clarke is EDI’s Training and Outreach Coordinator. She works through the University of Wisconsin-Madison and can be reached at [grossmanclar@wisc.edu](mailto:grossmanclar@wisc.edu).

Jon Ide is a software developer for EDI. He’s based in Madison, Wisconsin and can be reached at jride@wisc.edu.

Colin Smith is a part of EDI’s data curation team and works with data providers to clean, document, and submit their data to the EDI repository. He also works with the EDI community to develop data management software tools and helps run workshops and training events. Colin works through the University of Wisconsin-Madison. He can be reached at [colin.smith@wisc.edu](mailto:colin.smith@wisc.edu).

Kyle Zollo-Venecek is a part of EDI’s data curation team and works with data providers to clean, document, and submit their data to the EDI repository. Kyle works through the University of Wisconsin-Madison and can be reached at kylezollo@gmail.com.


## Repository Infrastructure

Development of the Provenance Aware Synthesis Tracking Architecture (PASTA) software began in 2009 by LTER information managers and software developers with the goal to serve as the LTER Network Information System data repository. A full production system was delivered to the LTER Network in January 2013 and quickly acquired a majority of LTER’s data products (> 5,900 as of January 2017). PASTA’s design was patterned on a Service Oriented Architecture to provide scalable data-repository functionality through a ReST-based application programmable interface (API), with primary operations to create, read, update, and delete (often termed CRUD) data packages to and from the repository. In addition, the PASTA development team delivered a browser-based web application for LTER called the Data Portal that gives users a human accessible interface to interact with PASTA. This was followed by an LTER Member Node (MN) in the DataONE federation, which exposes LTER data packages through DataONE’s search and catalog service.

By necessity, the original iteration of PASTA was LTER-centric. With the advent of EDI, aspects of the PASTA software that were idiomatic to LTER practices were generalized for broader use (or removed completely) into a revised software stack called PASTA+ (https://github.com/PASTAplus), which provides the underlying services for the EDI data repository. In simple terms, the EDI data repository is a “re-branding” of the LTER Network Information System data repository, including the full archive of LTER data packages, and uses the revised PASTA+ software stack. Because PASTA+ is backwards compatible with the previous PASTA API, the LTER Data Portal seamlessly interacts with the PASTA+ API. To promote broader inclusivity, EDI software developers released a generalized version of the LTER Data Portal in late 2016, which also interacts directly with the PASTA+ API. The EDI Data Portal can be used in lieu of the LTER Data Portal to access both LTER and non-LTER data packages. In March 2017, EDI released a new DataONE member node that exposes non-LTER data packages to the DataONE federation. Collectively, the infrastructure of EDI includes the EDI data repository, which uses the PASTA+ software stack, the EDI Data Portal, the EDI DataONE Member Node, and the LTER DataONE Member Node, in addition to a suite of software tools for information and data management (https://github.com/EDIorg). 


## Physical Management and Curation of Digital Products {#physical-management-and-curation-of-digital-products}

EDI employs industry standard protocols to ensure that all scientific data are well documented, secure, and persist for future use. 


### Standards for Data, Metadata, and Software

EDI’s data repository accepts data in any digital format. All science data curated by EDI is required to be described and documented with the Ecological Metadata Language (EML) standard (see: https://knb.ecoinformatics.org/tools/ eml). The data repository supports versions 2.1.0, 2.1.1, and 2.2.0 of EML. EML is a semantically rich science metadata standard that is actively supported as an open source project.

EDI-developed software products fall into two categories: the PASTA+ software stack for the data repository and software in support of general data management practices. All EDI software development follows principles utilized by open source projects, including frequent and incremental submittals of written code, documentation, and architectural diagrams to a recognized software repository. EDI uses two separate GitHub repositories for software management and control: one for PASTA+ software at [https://github.com/PASTAplus](https://github.com/PASTAplus) and another for data management support tools at [https://github.com/EDIorg](https://github.com/EDIorg).

The PASTA+ software is licensed under the Apache License, version 2.0 (AL2.0) (http://www.apache.org/licenses). AL2.0 is known as a “permissive” software license, which means that a user is free to download the software, to modify the software, and to use the software for any purpose without concern for royalties. AL2.0 is compatible with the GNU General Public License v3 “copyleft” software license. 

All other digital products (e.g., webinar recordings, informational documents) are licensed under Creative Commons CC0 1.0 “No Rights Reserved”.


### Risk Management {#risk-management}

Of utmost importance to EDI are the science data and metadata under our curatorial management. The repository's responsibility for science data and metadata begins at the moment of upload when a checksum is computed for all objects and stored as a measurement for comparison during random monitoring, which ensures long-term digital integrity. All objects are cataloged in our data package resource registry and written to physical storage. The science data and metadata are replicated daily to both a permanent mirrored storage device and to a removable storage device using a combination of copy and checksum verification. Once on the mirrored storage device, the aggregate “data package” is compressed as a single digital file and written to Amazon Glacier, a high-latency cloud storage service designed for long-term preservation. The removable storage is rotated offsite on a weekly basis. We view both the mirrored storage and removable storage as near-line backup systems for quick recovery of science data and metadata. Data packages stored at Amazon Glacier are considered only for large-scale catastrophic recovery; these data package files are sufficiently complete to fully recover our entire data repository or to allow transfer to another data repository system. Recovery scenario testing is performed on a monthly basis. Science metadata is also replicated to the DataONE Federation (see: https://www.dataone.org/) on an hourly basis.

Important operational information of the PASTA+ data repository environment and related services, such as compressed database dumps, log files and virtual machine images are regularly backed up.


### Security, Access, and Confidentiality {#security-access-and-confidentiality}

EDI implements physical security for access to all repository infrastructure. EDI technical staff limits privileged access to only certified personnel. System access logs and accounts are monitored for irregular or malicious activity and all systems operate firewall software that prohibits network intrusion from external sources.

Access to all science data and metadata through the PASTA+ software REST API is controlled through access rules that are declared in the corresponding EML metadata document. In principle, EDI recommends that open access be granted to read science data and metadata, but restricted access be enforced to revise or modify science data or metadata. PASTA+ software supports conditional logic such that rules may be set to allow or deny user access to science data or metadata. In the absence of access rules, PASTA+ defaults to denying access to science data and metadata for all users except for the single user who performed the original data and metadata contribution.

EDI requires users to register in a locally managed LDAP directory before they can contribute science data and metadata to the repository. With the exception of a valid electronic mail address, EDI does not store personal user information. All contributors are vetted and instructed on data and metadata standards before registration occurs. Session authentication is a precondition of upload access. Non-contributors may authenticate through external OAuth/OpenID Connect providers, but will not be allowed upload-access unless mapped to an EDI LDAP registration.  Access logs contain only the identification of users who have performed session authentication; all other users are recorded as “public”. No Internet address information is recorded in access logs, although the HTTP request agent value is stored to filter potential Internet robots and crawlers. EDI believes that science data and metadata that is collected through public means should be openly available and unfettered where possible.


### Reuse and Redistribution {#reuse-and-redistribution}

EDI advocates for open and unfettered access to science data and metadata, including data and metadata that reside in the EDI data repository. Science data and metadata contributors have the option to provide a reuse policy of their choice, which is declared within the “intellectual rights” section of the EML metadata document. If a contributor reuse policy does not exist in the EML metadata, EDI will apply a default policy that states data and metadata are to be released as “public domain” under Creative Commons CC0 1.0 “No Rights Reserved” license.

Science data and metadata, which are unfettered per access rules, can be downloaded individually and used in accordance with the stated reuse policy. Similarly, complete data packages can be accessed and downloaded as a single archive in a “zip” format, including a contents manifest. In the event that EDI ceases operations, all science data and metadata would be made available on portable storage for transfer to another repository; use of the embedded data package identifier and EML metadata would be possible with minimal effort. Updates to target URLs of Digital Object Identifiers (DOIs), managed through DataCite, would allow continued resolution to preferred landing pages. If a cessation scenario occurred, the target repository would be requested to support the access rules declared in all EML metadata documents.