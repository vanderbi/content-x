# Publishing a Data Package

Publishing a [data package](https://docs.google.com/document/d/10lbSR34T_Q6qaZoT6ZqxQoUcBRLy34LUokSFeqhtrXw/edit#heading=h.brmxkomw8tom) in the EDI Data Repository can be done manually via the EDI Data Portal, or programmatically using the EDIutils R package or the REST API. Across these three methods, the same general pattern is always followed: login, reserve a data package identifier, evaluate the data package, and publish the data package.

![](../../static/images/publish.png)

>We recommend creating a test version of a data package for review before publishing the final version. For more on this topic see [here](https://docs.google.com/document/d/1LTsh1HpZNtFFbhRy8H1S4J3No80JgtC5aTpPYzTOtJM/edit?usp=sharing).

>Uploading a data package to the EDI Data Repository requires an [EDI account](https://docs.google.com/document/d/1NRhNJX9GfYZ_-JtG4nv9jBYARdTdV3kiZSRXzwwwNnc/edit#heading=h.8n3xfdqgg3qr). Other methods of authentication (e.g. Google, ORCID, GitHub) do not allow upload. Most data authors don't upload directly to the EDI Repository but rather publish via the EDI Curation Team.


[TOC]



## EDI Data Portal {#edi-data-portal}

The process of publishing via the [EDI Data Portal](https://portal.edirepository.org/nis/home.jsp) is covered in detail in [this video](https://www.youtube.com/watch?v=F_twNhGb42k) and is outlined below:


### Login {#login}

From the Data Portal, click the **Login** button and enter EDI account credentials.




### Reserving a data package identifier {#reserving-a-data-package-identifier}

Access the **Data Package Identifier Reservations** button in the **TOOLS** dropdown menu. Click the **Reserve Next Available Identifier(s)** button to create the reservation.



Add the reserved identifier to the EML metadata document of the data package to be published. Identifiers can be added in the **Data Package ID** tab of [ezEML](https://docs.google.com/document/d/12sdLhID6SwaKAjU1aT5PAXA-9q1zaq31eNBmPRvYBC0/edit#heading=h.ren642sx8n1f) or provided as the argument to the `package.id` parameter of the `make_eml()` function in [EMLassemblyline](https://docs.google.com/document/d/12sdLhID6SwaKAjU1aT5PAXA-9q1zaq31eNBmPRvYBC0/edit#heading=h.alm45es0k04q).


### Evaluating the data package {#evaluating-the-data-package}

Navigate to the **Evaluate/Upload Data Packages** page. 





1. **Choose File** - Browse and select the EML file to be evaluated
2. Unless every data object in the EML file is associated with [direct download links](https://docs.google.com/document/d/1DC403Wd6PfssjPXl-ToRNlC97xcr6kVoTWoFE4R2_bk/edit#heading=h.92gv8b4z5ors), select the checkbox next to **Manually upload data…** to allow manual upload.

    

3. From the manual uploads page, choose the files to upload for the data package and click the **Evaluate** button.

    


>Be aware that the length of the evaluation process increases with the size of the data being evaluated. Once the process has begun, the browser window can be closed without interrupting the evaluation. Use the EDI Dashboard [PASTA is Working On](https://dashboard.edirepository.org/dashboard/pasta/render_working_on) feature to see when evaluation has completed. The [evaluation report summary](https://docs.google.com/document/d/111fsC4AR1K1jrwlASDDRCu8T7FvPPs3nilT2zCGTLEw/edit#heading=h.vdql88f0cw57) and [full report](https://docs.google.com/document/d/111fsC4AR1K1jrwlASDDRCu8T7FvPPs3nilT2zCGTLEw/edit#heading=h.10e4qgi4bsdc) can be viewed from the **View Evaluate/Upload Results** page.

Read about [interpreting the report summary](https://docs.google.com/document/d/111fsC4AR1K1jrwlASDDRCu8T7FvPPs3nilT2zCGTLEw/edit#heading=h.fr9cs2icxodm) and [interpreting the full report](https://docs.google.com/document/d/111fsC4AR1K1jrwlASDDRCu8T7FvPPs3nilT2zCGTLEw/edit#heading=h.k3pbq74vz7kp).


### Publishing the data package {#publishing-the-data-package}

Navigate to the **Evaluate/Upload Data Packages** 



1. **Choose File** - Browse and select the EML file to be uploaded.
2. Unless every data object in the EML file is associated with [direct download links](https://docs.google.com/document/d/1DC403Wd6PfssjPXl-ToRNlC97xcr6kVoTWoFE4R2_bk/edit#heading=h.92gv8b4z5ors), select the checkbox next to **Manually upload data…** to allow manual upload.





3. Confirm that upload to the EDI Data Repository.





4. Select files for manual upload and click the **Upload** button.
5. At the **Evaluate/Upload Results** page, if the upload was successful, the data package identifier will be linked to the newly published data package [summary page](https://docs.google.com/document/d/1fYIJAKFaA4lPyqo6Rz0ZSEUKKiNMLF5UZCxlyUfhxwM/edit#heading=h.9ggm7vr49sl).

    


>Be aware that the length of the upload process increases with the size of the data being published. Once the process has begun, the browser window can be closed without interrupting the evaluation. Use the EDI Dashboard [PASTA is Working On](https://dashboard.edirepository.org/dashboard/pasta/render_working_on) feature to see when evaluation has completed. The [evaluation report summary](https://docs.google.com/document/d/111fsC4AR1K1jrwlASDDRCu8T7FvPPs3nilT2zCGTLEw/edit#heading=h.vdql88f0cw57), [full report](https://docs.google.com/document/d/111fsC4AR1K1jrwlASDDRCu8T7FvPPs3nilT2zCGTLEw/edit#heading=h.10e4qgi4bsdc), and link to the published package can be viewed from the **View Evaluate/Upload Results** page.


## EDIutils {#ediutils}

Publishing with the [EDIutils](https://ediorg.github.io/EDIutils/index.html) R package allows each step of the process to be executed from an R environment. For a language-agnostic solution, see the [REST API](https://pastaplus-core.readthedocs.io/en/latest/doc_tree/about.html) documentation for [reserve a data package identifier](https://pastaplus-core.readthedocs.io/en/latest/doc_tree/pasta_api/data_package_manager_api.html#create-reservation), [evaluate a data package](https://pastaplus-core.readthedocs.io/en/latest/doc_tree/pasta_api/data_package_manager_api.html#evaluate-data-package), and [publish a data package](https://pastaplus-core.readthedocs.io/en/latest/doc_tree/pasta_api/data_package_manager_api.html#create-data-package).

>To publish with EDIutils all data objects must be associated with [direct download links](https://docs.google.com/document/d/1DC403Wd6PfssjPXl-ToRNlC97xcr6kVoTWoFE4R2_bk/edit?usp=sharing).


### Login {#login}

Use the `[login()](https://ediorg.github.io/EDIutils/reference/login.html)` function with EDI account credentials.


### Reserving a data package identifier {#reserving-a-data-package-identifier}

Use the `[create_reservation()](https://ediorg.github.io/EDIutils/reference/create_reservation.html)`** **function to reserve the next available identifier in the specified scope and repository tier.


### Evaluating the data package {#evaluating-the-data-package}

Use the `[evaluate_data_package()](https://ediorg.github.io/EDIutils/reference/evaluate_data_package.html)`** **function to begin the evaluation process. See [evaluating a data package](https://docs.google.com/document/d/111fsC4AR1K1jrwlASDDRCu8T7FvPPs3nilT2zCGTLEw/edit#heading=h.c54is1drrrdw) for details.


### Publishing the data package {#publishing-the-data-package}

Use the `[create_data_package()](https://ediorg.github.io/EDIutils/reference/create_data_package.html)`** **function to publish the data package in the EDI Data Repository.

This function returns a "transaction identifier" which can be passed to [check_status_create](https://ediorg.github.io/EDIutils/reference/check_status_create.html) to determine the status of the publication.
