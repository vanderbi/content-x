# Accessing Data

[Data packages](https://docs.google.com/document/d/10lbSR34T_Q6qaZoT6ZqxQoUcBRLy34LUokSFeqhtrXw/edit?usp=sharing) and their contents can be accessed through the EDI Data Portal and the REST API. These options support scientific workflows driven by manual human effort and automated machine routines.

![](../../static/images/access.png)


[TOC]



## Data Portal {#data-portal}


### Point and click {#point-and-click}

Single data objects or the entire data package can be downloaded through the EDI Data Portal as files:



1. From a data package [summary page](https://docs.google.com/document/d/1fYIJAKFaA4lPyqo6Rz0ZSEUKKiNMLF5UZCxlyUfhxwM/edit#heading=h.moggqkctxdnf) on the EDI Data Portal, navigate to the **Resources** section:

    

2. Download individual resources by clicking the links under **Download Data**.
3. Use the **Download Zip Archive **button to download the entire data package.


### Data import scripts {#data-import-scripts}

Data import scripts, available on the data package summary page, read data directly from the EDI Data Repository into common programming language workspaces. This option supports reproducible research by accessing the data directly and reducing the possibility of errors propagating through local files.



1. Navigate to the **Code Generation** section of a data package summary page. 
2. Select the language of interest (R, Python, MATLAB, etc).
3. Download the script that is generated as a file, or copy and paste the text into the language's development environment (e.g. RStudio).


## EDIutils {#ediutils}

Data can be read directly from the EDI Data Repository into the R environment. This option serves a similar use case as the data import scripts but provides full access to the REST API, which is useful when constructing automated workflows.



1. Download individual resources from a data package using the `[read_data_entity()](https://ediorg.github.io/EDIutils/reference/read_data_entity.html)` function.
2. Download an entire data package as a zip archive using the `[create_data_package_archive()](https://ediorg.github.io/EDIutils/reference/create_data_package_archive.html)` and `[read_data_package_archive()](https://ediorg.github.io/EDIutils/reference/read_data_package_archive.html)` functions.
3. Download the metadata of a data package using the `[read_metadata()](https://ediorg.github.io/EDIutils/reference/read_metadata.html)` function.

See the [Search and Access Data](https://ediorg.github.io/EDIutils/articles/search_and_access.html) vignette for an example of searching and accessing data using EDIutils.

For a language-agnostic solution, see the [REST API](https://pastaplus-core.readthedocs.io/en/latest/doc_tree/about.html) documentation for [Read Data Entity](https://pastaplus-core.readthedocs.io/en/latest/doc_tree/pasta_api/data_package_manager_api.html#read-data-entity), [Create Data Package Archive](https://pastaplus-core.readthedocs.io/en/latest/doc_tree/pasta_api/data_package_manager_api.html#create-data-package-archive), [Read Data Package Archive](https://pastaplus-core.readthedocs.io/en/latest/doc_tree/pasta_api/data_package_manager_api.html#read-data-package-archive-1), and [Read Metadata](https://pastaplus-core.readthedocs.io/en/latest/doc_tree/pasta_api/data_package_manager_api.html#read-metadata).


## Accessing embargoed data {#accessing-embargoed-data}

Embargoed data can be accessed by users who are authorized according to the &lt;access>** **element of the EML file. Users should reach out directly to the contact listed on the data package for access to embargoed data. If the contact is unresponsive, notify the EDI Data Curation Team for assistance.
