# Data Package Pages

A [data package summary page](https://portal.edirepository.org/nis/mapbrowse?scope=edi&identifier=1) (or dataset landing page) and [full metadata page](https://portal.edirepository.org/nis/metadataviewer?packageid=edi.1.1) are generated from the metadata within a data package and deliver the first impression of a data package scope and coverage to data users who are browsing on the EDI Data Portal. They can be discovered by resolving the Digital Object Identifier (DOI) of a data package, or through the Data Portal search feature. 


[TOC]



## Summary Page {#summary-page}

The summary page displays overview information for a data package and it can be discovered through its DOI and other links. 


### Title {#title}

The title of the data package.


### Creators {#creators}

A list of the data package creators and their affiliations.


### Publication Date {#publication-date}

The date that the data package was published.


### Citation {#citation}

The suggested citation for the data package and a button to copy it. Learn more about [citing data](https://docs.google.com/document/d/1YluETdZJozxSf0mGrsHf__Xd8lnUuxxlcJO_OG7tovE/edit).


### Abstract {#abstract}

The abstract for the data package.


### Spatial Coverage {#spatial-coverage}

An embedded map displaying the geographic location as provided in the EML metadata. The coverage may be one or more bounding boxes, point coordinates, or a mix of both. 


### Package ID {#package-id}

The package identifier of the data package. Learn more about [package identifiers](https://docs.google.com/document/d/10lbSR34T_Q6qaZoT6ZqxQoUcBRLy34LUokSFeqhtrXw/edit#heading=h.ocgev1cci1ph).

If multiple revisions of a [data package](https://docs.google.com/document/d/10lbSR34T_Q6qaZoT6ZqxQoUcBRLy34LUokSFeqhtrXw/edit#heading=h.a1enbjthfrbm) exist, this section will include links to traverse the revisions (previous revision, next revision) as well as a link to view all revisions.


### Resources {#resources}

A list of all files associated with the data package, including the [EML file](https://docs.google.com/document/d/12sdLhID6SwaKAjU1aT5PAXA-9q1zaq31eNBmPRvYBC0/edit#heading=h.xxho7vmcnti), an [Evaluation Report](https://docs.google.com/document/d/111fsC4AR1K1jrwlASDDRCu8T7FvPPs3nilT2zCGTLEw/edit#heading=h.k3pbq74vz7kp), and data entities. 


#### View Full Metadata {#view-full-metadata}

A link to the [Full Metadata Page](#full-metadata-page).


#### View Data Package Report {#view-data-package-report}

A link to the Evaluation Report for the data package. Learn more about [Evaluation Reports](https://docs.google.com/document/d/111fsC4AR1K1jrwlASDDRCu8T7FvPPs3nilT2zCGTLEw/edit#heading=h.k3pbq74vz7kp).


#### Download Data {#download-data}

A list of data entities in the data package. This section lists the entity name, file name, size, and number of downloads. The filename is linked to a direct download of the entity.


#### Download Zip Archive {#download-zip-archive}

This button downloads a zip file containing the data package metadata (as text and an EML document), the Evaluation Report (an XML file), a package manifest (text), and all of the data entities.


### Intellectual Rights {#intellectual-rights}

The license associated with the data package describing any restrictions on use. Learn more about [licensing data](https://docs.google.com/document/d/1F52hJFFapPHGwwIv5TWFS6VV1lyMKDw2tN6tCgUfSjY/edit).


### Digital Object Identifier {#digital-object-identifier}

The data package Digital Object Identifier (DOI). Learn more about [data package DOIs](https://docs.google.com/document/d/10lbSR34T_Q6qaZoT6ZqxQoUcBRLy34LUokSFeqhtrXw/edit#heading=h.khknpxdegdc9).


### PASTA Identifier {#pasta-identifier}

The data package PASTA Identifier. Learn more about the PASTA Identifier.


### Code Generation {#code-generation}

Links to generate scripts which can be run directly from local analysis software (R, Python, MATLAB, and more). These scripts enable a quick interactive view into a dataset and provide a basis for analytical workflows.

Code generation functionality is demonstrated in [this video](https://youtu.be/B50L1AKXcT8).


### Provenance {#provenance}

This section displays provenance information related to the data package, including any packages that are derivations of the data package, or any data package that serve as a source to it.



Additionally, the section contains a link to generate [provenance metadata](https://docs.google.com/document/d/1ytbqK72auywo0CX23TBG1L4rv7FmwedA0YIX8EBvB_Q/edit) for use in derived data packages.


### Journal Citations {#journal-citations}

This section displays journal citations that have been added to the data package. Learn more about [adding journal citations to data packages](https://docs.google.com/document/d/1C2YmVe96Nkfj4I4MucGJHlSqas4T1aATnnV5mIBpgFY/edit). 




## Full Metadata Page {#full-metadata-page}

The Full Metadata page provides a more in-depth description of the data package. Access the Full Metadata Page from the links at the top of the Summary page and in the Resources section.


### General Information {#general-information}

The General Information section contains information that should help a data user understand the scope and coverage of the data package.


#### Data Package {#data-package}

This section displays overview information about the data package, including its title, abstract, package identifier, DOI, and publication date.


#### For More Information {#for-more-information}

This section displays the DOI as a resolvable link. This link redirects to the Summary Page.


#### Time Period {#time-period}

This section displays the temporal coverage information of the data package. 


#### People and Organizations {#people-and-organizations}

This section displays the names, affiliations and positions of the Creators, Contacts, and Associated Parties of a data package.


#### Data Entities {#data-entities}

This section displays the name and description of the data entities of the data package.


### Detailed Metadata {#detailed-metadata}

The Detailed Metadata section contains organized representations of almost all of the elements from the EML metadata. Use the Show and Hide details buttons to expand or compact every subsection in the Detailed Metadata. Individual sections can be expanded or compacted using the **+/- **buttons next to the section headers.




#### Data Entities {#data-entities}

The Data Entities section provides a comprehensive breakdown of each data entity (tables, spatial data, or other entities) formed from the information provided in the EML metadata. In general, the subsections underneath Data Entities focus on overview information (name, type, and description; number of rows and columns for tables), physical structure (size, MD5 checksum, data format), and provide a direct download link for the entity.

For **Data Tables** in particular, there is an additional subsection, **Table Column Descriptions, **that provides name, definition, data type, and more, for each individual column within the table. For columns containing numeric values, the unit and range of the column is listed. For columns containing categorical information, each code and its explanation are featured. Due to the depth of information presented in the Table Column Descriptions sections, data users can generally gather all the information necessary to determine a data package's fitness for their particular purpose without ever downloading a table.


#### Data Package Usage Rights {#data-package-usage-rights}

The license associated with the data package. Learn more about [licensing data](https://docs.google.com/document/d/1F52hJFFapPHGwwIv5TWFS6VV1lyMKDw2tN6tCgUfSjY/edit).


#### Keywords {#keywords}

This section displays the keywords, organized by their source thesaurus.


#### Methods and Protocols {#methods-and-protocols}

The methods as outlined in the data package metadata.


#### People and Organizations {#people-and-organizations}

A detailed view of all Publishers, Creators, Contacts, and Associated Parties with all of their provided information.


#### Temporal, Geographic and Taxonomic Coverage {#temporal-geographic-and-taxonomic-coverage}

The temporal, geographic, and taxonomic coverage information of a data package. These are three properties of a research dataset that are particularly useful for dataset discovery.


#### Project {#project}

The funding and project information associated with this dataset, including the Principal Investigators on the grants 


#### Maintenance {#maintenance}

This section describes whether the data package creators plan to update the package with new data or if the research is completed. This section will also display any history of revisions as documented during a [data package update](https://docs.google.com/document/d/1OfT_XMpTbRhJNSMWMC7wcsNm71m2KOYEibEgW15rUew/edit#heading=h.wccq4ft4e732).


### Other Metadata {#other-metadata}


#### Additional Metadata {#additional-metadata}

This section displays any information from the additionalMetadata element of the EML metadata. Notably, any custom units will be displayed in this section.
