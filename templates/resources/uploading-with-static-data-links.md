# Uploading with Static Data Links

A static URL resolving to a data file can be inserted into the physical/distribution element of an EML file and serve as a data source when uploading to the EDI Data Repository. This can be useful for bypassing the 500 MB size limit of manual uploads on the EDI Data Portal, for facilitating workflow automation, and for handling files that may be too large to transfer directly to a data curator.

[Box Cloud Storage](https://www.box.com/) is an example service that allows for generating links that do not offer any redirects and are static, two requirements of links that are used to upload to the EDI Data Portal.

![](../../static/images/download-links.png)


[TOC]



## Using Box Cloud Storage {#using-box-cloud-storage}

Files stored on a Box Cloud Storage application can be directly downloaded via a static URL. 

>A paid/premium Box account is required for generating direct download links or receiving files through a file request.


### Creating a Box File Request {#creating-a-box-file-request}

A File Request link allows anyone (with or without a Box account) to submit files to a directory in a Box account. They offer a good solution for collecting prohibitively large data from submitters that require static links. To create a request:



1. Navigate to the directory (from within the Box web application while logged into a premium account) where data files should be submitted.
2. Click the **File Request** button on the right side of the screen which will open a pop-up.





3. On the pop-up screen, set the link to enabled. This selection should be reflected on the first **File Request** button pressed.

    

4. Copy the shareable link from the pop-up screen and try it in a web browser. This link should lead to a page that looks like the one below.

    

5. Share this link with a data submitter. They will not need to have a Box account to submit data to this directory.


### Creating a static download link {#creating-a-static-download-link}

A static download link will function as a data source for the EDI Data Repository. To create a static download link:



1. Navigate to the directory that contains the data file for which to create a link. Click on the link icon which will open a pop-up window.

    

2. DO NOT use the Share Link from this window for direct download. Instead, click on the **Link Settings** button which will open another pop-up window.

    

3. In the shared link settings, at the bottom of the page, find and copy the direct link URL. 


## Adding download links to EML files {#adding-download-links-to-eml-files}

Direct download links of any type, and static links generated from a Box account, can be inserted into an EML document to facilitate upload to the EDI Data Repository.


### ezEML {#ezeml}

To insert a download link via [ezEML](https://docs.google.com/document/d/12sdLhID6SwaKAjU1aT5PAXA-9q1zaq31eNBmPRvYBC0/edit#heading=h.ren642sx8n1f):



1. Navigate to the **Data Tables** tab and click the **Edit** button next to the data table.





2. Paste the link into the **Online Distribution URL **textbox. Remember to click **Save and Continue** before moving on.



The data table will now be associated with the provided download link. Submit to EDI via **Send to EDI** or download the XML document with the **Download EML File** button.

>This method can be replicated in the **Other Entities **tab as well. 


### EMLassemblyline {#emlassemblyline}

To insert a download link via [EMLassembylline](https://docs.google.com/document/d/12sdLhID6SwaKAjU1aT5PAXA-9q1zaq31eNBmPRvYBC0/edit#heading=h.alm45es0k04q):



1. Supply the link as a character string to the `data.table.url`** **or `other.entity.url`** **arguments in the `[make_eml()](https://ediorg.github.io/EMLassemblyline/reference/make_eml.html)` function. To add multiple links, supply links as a vector of character strings.

    

2. Run `make_eml()` to associate the tables with the provided links and return an EML file.




### Manually editing XML {#manually-editing-xml}

To insert download links manually:



1. Open the XML file in a text editor. Within the &lt;dataTable> (or &lt;otherEntity>, &lt;spatialRaster>, or &lt;spatialVector>) element, add &lt;distribution>,** **&lt;online>, and** **&lt;url>** **elements to the &lt;physical> element.





2. Ensure that the elements are properly nested, and that the function attribute is set to **"**download". 


## Uploading to EDI {#uploading-to-edi}

>If creating a data package with ezEML, the easiest way to upload to the EDI Repository is by using the **Send to EDI** tab.

>If you've manually added download links to an EML file or have created a data package with EMLassemblyline, and don't have an EDI User Account, you can submit the EML document by emailing the EDI Curation Team and requesting that they upload it on your behalf. Make sure that every data file in the data package has a direct download link associated with it. There is no need to attach the data files in the email since the download links are listed.

If publishing a data package via the EDI Data Portal note:



1. In order to skip manual upload, all objects must have links (all or nothing).
2. Remember to **_NOT_ **check the "Manually upload data" checkbox.
3. If some of the objects in the data package package are already in the EDI Repository, remember to check the **Allow PASTA+ to skip …** checkbox.


