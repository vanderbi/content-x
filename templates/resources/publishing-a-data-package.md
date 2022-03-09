# Publishing a Data Package

Publishing a [data package](the-data-package.md) in the EDI Data Repository can be done manually via the EDI Data Portal, or programmatically using the EDIutils R package or the REST API. Across these three methods, the same general pattern is always followed: login, reserve a data package identifier, evaluate the data package, and publish the data package.

![](../../static/images/publish.png)

>We recommend [creating a test version](repository-environments.md) of a data package for review before publishing the final version.

>Uploading a data package to the EDI Data Repository requires an [EDI account](information-manager-quickstart.md#sign-up-for-an-edi-account). Other methods of authentication (e.g. Google, ORCID, GitHub) do not allow upload. Most data authors don't upload directly to the EDI Repository but rather publish via the EDI Curation Team.

[TOC]

## EDI Data Portal

The process of publishing via the [EDI Data Portal](https://portal.edirepository.org/nis/home.jsp) is covered in detail in [this video](https://www.youtube.com/watch?v=F_twNhGb42k) and is outlined below:

### Login

From the Data Portal, click the **Login** button and enter EDI account credentials.

![](../../static/images/login-portal.png)

### Reserving a data package identifier

Access the **Data Package Identifier Reservations** button in the **TOOLS** dropdown menu. Click the **Reserve Next Available Identifier(s)** button to create the reservation.

![](../../static/images/reserve-package-id-portal.png)

Add the reserved identifier to the EML metadata document of the data package to be published. Identifiers can be added in the **Data Package ID** tab of [ezEML](https://ezeml.edirepository.org/eml/) or provided as the argument to the `package.id` parameter of the [`make_eml()`](https://ediorg.github.io/EMLassemblyline/reference/make_eml.html) function in EMLassemblyline.


### Evaluating the data package

Navigate to the **Evaluate/Upload Data Packages** page: 

![](../../static/images/eval-upload-dropdown-portal.png)

1. **Choose File** - Browse and select the EML file to be evaluated
2. Unless every data object in the EML file is associated with [static data links](uploading-with-static-data-links.md), select the checkbox next to **Manually upload data…** to allow manual upload.

![](../../static/images/evaluate-manual-upload.png)    

3. From the manual uploads page, choose the files to upload for the data package and click the **Evaluate** button.

![](../../static/images/evaluate-manual-upload-page.png)

>Be aware that the length of the evaluation process increases with the size of the data being evaluated. Once the process has begun, the browser window can be closed without interrupting the evaluation. Use the EDI Dashboard [PASTA is Working On](https://dashboard.edirepository.org/dashboard/pasta/render_working_on) feature to see when evaluation has completed. The [evaluation report](evaluating-a-data-package.md#interpreting-the-evaluation-report) can be viewed from the **View Evaluate/Upload Results** page.

### Publishing the data package

Navigate to the **Evaluate/Upload Data Packages** 

1. **Choose File** - Browse and select the EML file to be uploaded.
2. Unless every data object in the EML file is associated with [static data links](uploading-with-static-data-links.md), select the checkbox next to **Manually upload data…** to allow manual upload.

![](../../static/images/upload-manual-upload.png)

3. Confirm that upload to the EDI Data Repository.

![](../../static/images/confirm-upload.png)

4. Select files for manual upload and click the **Upload** button.
5. At the **Evaluate/Upload Results** page, if the upload was successful, the data package identifier will be linked to the newly published data package [landing page](data-package-pages.md).

![](../../static/images/successful-upload.png)    

>Be aware that the length of the evaluation process increases with the size of the data being evaluated. Once the process has begun, the browser window can be closed without interrupting the evaluation. Use the EDI Dashboard [PASTA is Working On](https://dashboard.edirepository.org/dashboard/pasta/render_working_on) feature to see when evaluation has completed. The [evaluation report](evaluating-a-data-package.md#interpreting-the-evaluation-report) can be viewed from the **View Evaluate/Upload Results** page.

## EDIutils

Publishing with the [EDIutils](https://ediorg.github.io/EDIutils/index.html) R package allows each step of the process to be executed from an R environment. For a language-agnostic solution, see the REST API documentation for [Create Reservation](https://pastaplus-core.readthedocs.io/en/latest/doc_tree/pasta_api/data_package_manager_api.html#create-reservation), [Evaluate Data Package](https://pastaplus-core.readthedocs.io/en/latest/doc_tree/pasta_api/data_package_manager_api.html#evaluate-data-package), and [Create Data Package](https://pastaplus-core.readthedocs.io/en/latest/doc_tree/pasta_api/data_package_manager_api.html#create-data-package).

>To publish with EDIutils all data objects must be associated with [static data links](uploading-with-static-data-links.md).

### Login

Use the [`login()`](https://ediorg.github.io/EDIutils/reference/login.html) function with EDI account credentials.


### Reserving a data package identifier

Use the [`create_reservation()`](https://ediorg.github.io/EDIutils/reference/create_reservation.html) function to reserve the next available identifier in the specified scope and repository environment.


### Evaluating the data package

Use the [`evaluate_data_package()`](https://ediorg.github.io/EDIutils/reference/evaluate_data_package.html) function to begin the evaluation process. See [evaluating a data package](evaluating-a-data-package.md#evaluating-the-data-package) for details.


### Publishing the data package

Use the [`create_data_package()`](https://ediorg.github.io/EDIutils/reference/create_data_package.html) function to publish the data package in the EDI Data Repository.

This function returns a "transaction identifier" which can be passed to [`check_status_create()`](https://ediorg.github.io/EDIutils/reference/check_status_create.html) to determine the status of the publication.