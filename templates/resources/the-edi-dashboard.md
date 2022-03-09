# The EDI Dashboard

The EDI Dashboard gives users access to information and processes related to the functioning of the EDI Data Repository (a.k.a. PASTA). The dashboard provides useful tools for generating site- or package-specific reports, checking the status of data package evaluations and uploads, or for monitoring the health of EDI services and portals. Access is restricted to admin users for some dashboard features (noted in subheaders here and on the dashboard).

[TOC]

## Health

[Health at a Glance](https://dashboard.edirepository.org/dashboard/health/glance) displays the statuses for PASTA+ Infrastructure and corresponding EDI Data Portals (see [Repository Environments](repository-environments.md) for more on the differences), EDI and LTER Generic Member Nodes (used to expose data hosted on the EDI Data Repository to DataONE), and other related services from EDI.

## Reports

### No Public Access (admin)

Users with admin privileges can access the list of data packages with entities (data objects, metadata, or both) that are currently placed under embargo.


### Offline Data (admin)

Users with admin privileges can access the list of data packages with entities that are only available for offline distribution.


### DOI Report (admin)

Users with admin privileges can access the list of active and inactive data packages with DOIs that either fail to resolve or have no entry in PASTA.


### Package Tracker

The package tracker is a useful way to view data package overview information (title, data package identifier, DOI) and download information for specific resources within the data package. A time series plot for downloads by resource can also be generated. To use the package tracker, enter the full [data package identifier](the-data-package.md#data-package-identifier) for the data package of interest.

### Recent Uploads

These links provide access to a list and time series plot of data packages uploaded to the EDI Data Repository in the last 1, 7, or 30 day intervals.

### Upload Report

The upload report feature allows the user to access a list of packages uploaded to the EDI Data Repository during a specified interval and filtered on an LTER site (this feature will be expanded to all sites/projects in the future). The upload report is a table that consists of the data package id, DOI, title (optional), and upload date and time. 

### Site Report

The site report allows a user to view the entire list of data packages for an LTER site (this feature will be expanded to all sites/projects in the future). The site report is a table that consists of the data package id (latest revision), DOI, list of authors, title, date of publication, temporal coverage, keywords, and funding. The table can also be generated in “citation format” (data package id and citation).

## PASTA+

### Reservations

View the list of all active package identifier reservations, who holds the reservation, and when it was made. Reservations appear on this list until a data package is created using the identifier, or the reservation is deleted. 

### Working On

View the current status of data packages being processed across the three repository environments. This page may be useful when verifying that a data package evaluation or upload has successfully started or completed.

### Embargo Management (admin)

From this page, users with admin privileges are able to set or clear data package embargoes.


## User Management

This dropdown contains options for managing users. Without admin privileges, users have the ability to change or reset a password and update accounts for which they have the password. Users with admin privilege have the ability to create and delete users as well as view the list of all users.


## EDI Portals

The links underneath this dropdown bring users directly to the EDI Data Portal [environment](repository-environments.md) listed (Production, Staging, Development).
