# Updating a Data Package

Perform a data package update whenever data or metadata need to be changed or added to a published [data package](https://docs.google.com/document/d/10lbSR34T_Q6qaZoT6ZqxQoUcBRLy34LUokSFeqhtrXw/edit?usp=sharing). Updates may be performed routinely or sporadically and will result in a new "revision". A revision of a data package has the same identifier, but receives a new [version number](https://docs.google.com/document/d/10lbSR34T_Q6qaZoT6ZqxQoUcBRLy34LUokSFeqhtrXw/edit#heading=h.a1enbjthfrbm) and is assigned a new [DOI](https://docs.google.com/document/d/10lbSR34T_Q6qaZoT6ZqxQoUcBRLy34LUokSFeqhtrXw/edit#heading=h.khknpxdegdc9). All revisions of a data package are linked in the EDI Data Repository. Users who end up on the landing page of an older revision will be notified that a newer version is available.

![](../../static/images/data-package-versioning.png)

>Note to Information Managers: Be aware of the EML &lt;access> element. Only credentials already specified in an existing version of a data package can be used to publish an update (i.e. to publish edi.10.2, credentials must be specified in edi.10.1). If you are unable to publish a revision for this reason, contact the EDI Curation Team.


[TOC]



## Metadata to include {#metadata-to-include}

It is important to communicate changes and significance in the metadata of an updated data package so users can understand what has changed and why. This information is included in the [maintenance](https://ediorg.github.io/data-package-best-practices/EMLmetadata/maintenance.html) section of EML metadata. Guidance on adding this information is provided below.


## Editing data and metadata {#editing-data-and-metadata}


### ezEML {#ezeml}

Edit data and metadata using [ezEML](https://docs.google.com/document/d/12sdLhID6SwaKAjU1aT5PAXA-9q1zaq31eNBmPRvYBC0/edit#heading=h.ren642sx8n1f):



1. Open the EML document for the original data package. If this doesn't exist, request it by sending the EDI Curation Team an email with a link to the original data package in the EDI Repository.
2. Describe the changes in the new revision. From the **Maintenance** tab, add a new paragraph to the **Description** text.

    

3. Submit to EDI - Click **Send to EDI** and add a note mentioning that this is an update to an existing data package (e.g. "This submission is a revision to package edi.101.1"). 

    

4. The EDI curation team will receive the submission and iterate through the [review process](https://docs.google.com/document/d/1aNInQhyCylgBuu0mucPSS92haTp3krjFMSracEwMkFs/edit?usp=sharing) before the update is published.

>EML created with ezEML can be downloaded directly and published to the EDI Repository. If opting to publish your own updates, remember to enter an incremented version number in the **Data Package ID **tab of ezEML.


### EMLassemblyline {#emlassemblyline}

Edit data and metadata using [EMLassemblyline](https://docs.google.com/document/d/12sdLhID6SwaKAjU1aT5PAXA-9q1zaq31eNBmPRvYBC0/edit#heading=h.alm45es0k04q):



1. Get the metadata templates and `[make_eml()](https://ediorg.github.io/EMLassemblyline/reference/make_eml.html)` function call for the original data package. If these don't exist, use the `[eml2eal()](https://ediorg.github.io/EMLassemblyline/reference/eml2eal.html)` and `[eml2eal_losses()](https://ediorg.github.io/EMLassemblyline/reference/eml2eal_losses.html)` functions to create them.
2. Update the metadata templates and `make_eml()` function arguments to reflect the changes. Describe the changes made between revisions using the `maintenance.description`** **parameter of `make_eml()`. 
3. Increment the data package version number in the `package.id` parameter of `make_eml()`.
4. Run `make_eml()`.


## Publishing edited data and metadata {#publishing-edited-data-and-metadata}


### EDI Data Portal {#edi-data-portal}

An updated data package can be uploaded via the EDI Data Portal similarly to a [new data package](https://docs.google.com/document/d/1xk0LepVW6giT4UJBYIo-o2sddcdKqq_16aHBkoL0jks/edit#heading=h.brmxkomw8tom), but with one key difference:

Use the **Allow PASTA+ to skip…** option if any of the data files are unchanged between versions. This allows the EDI Data Repository (a.k.a. PASTA) to forgo reuploading replicate data and can save time and repository space. _Caution: take care to ensure that the metadata-documented checksum values of each data file are accurate and up to date._

For more information on this option, watch [this video](https://youtu.be/AS6-m17I6pk).


### EDIutils {#ediutils}

An updated data package can be uploaded via the [EDIutils](https://ediorg.github.io/EDIutils/) R package using the `[update_data_package()](https://ediorg.github.io/EDIutils/reference/update_data_package.html)` function. For updating with this function, all data files must be web-hosted and be associated with [direct download links](https://docs.google.com/document/d/1DC403Wd6PfssjPXl-ToRNlC97xcr6kVoTWoFE4R2_bk/edit#heading=h.92gv8b4z5ors). When using this function, the `useChecksum` option can be selected.

Set the `useChecksum` argument to TRUE if any of the data objects are unchanged between versions. This allows the EDI Data Repository (a.k.a. PASTA) to forgo reuploading replicate data and can save time and repository space. _Caution: take care to ensure that metadata-documented checksum values are accurate and up to date._

For a language-agnostic solution, see the [REST API](https://pastaplus-core.readthedocs.io/en/latest/doc_tree/about.html) documentation for [updating a data package](https://pastaplus-core.readthedocs.io/en/latest/doc_tree/pasta_api/data_package_manager_api.html#update-data-package).


## Submit via email {#submit-via-email}

Submit desired changes or the new and/or updated data along with the updated EML file to the EDI Curation Team via email. Make sure to mention the data package identifier that is being updated. The EDI Curation Team will create a proof for review before the update is published.
