# Tracking Data Package Use

Metrics of activity surrounding a data package are commonly used when publicizing a data publication or reporting to funders.


[TOC]



## EDI Package Tracker {#edi-package-tracker}

[The Package Tracker](https://dashboard.edirepository.org/dashboard/reports/package_tracker), a feature of the [EDI Dashboard](https://dashboard.edirepository.org/dashboard/health/glance), is a convenient tool for viewing the resources and downloads of a given data package. For more on the EDI Dashboard see [here](https://docs.google.com/document/d/1WaL8ys9GsuPS_69o0TQeI6B6qMnLJMHVxU8V6RGqiWI/edit).


## Data package summary page {#data-package-summary-page}

Each data package [summary page](https://docs.google.com/document/d/1fYIJAKFaA4lPyqo6Rz0ZSEUKKiNMLF5UZCxlyUfhxwM/edit#heading=h.moggqkctxdnf) provides activity information in multiple places. The [Resources](https://docs.google.com/document/d/1fYIJAKFaA4lPyqo6Rz0ZSEUKKiNMLF5UZCxlyUfhxwM/edit#heading=h.1wijcfxy5kjg) section has the number of views the metadata has received, and the number of downloads for each resource. The [Provenance](https://docs.google.com/document/d/1fYIJAKFaA4lPyqo6Rz0ZSEUKKiNMLF5UZCxlyUfhxwM/edit#heading=h.iyws6aqvagy) and [Journal Citations](https://docs.google.com/document/d/1fYIJAKFaA4lPyqo6Rz0ZSEUKKiNMLF5UZCxlyUfhxwM/edit#heading=h.7n5j059sbpmb) sections, as well as the DataCite Badge at the bottom of the summary page, all provide information on where a data package has been used or cited.


## EDIutils {#ediutils}

Using the functions provided by the [EDIutils](https://ediorg.github.io/EDIutils/) R Package, it is possible to easily retrieve download and citation metrics for a data package. These processes have been detailed in [Retrieve Download Metrics](https://ediorg.github.io/EDIutils/articles/retrieve_downloads.html) and [Retrieve Citation Metrics](https://ediorg.github.io/EDIutils/articles/retrieve_citations.html) vignettes that accompany the package.

For a language agnostic solution follow a similar process using the [REST API](https://pastaplus-core.readthedocs.io/en/latest/doc_tree/about.html) documentation.
