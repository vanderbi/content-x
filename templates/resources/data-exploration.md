# Data Exploration

At the beginning of any data reuse or synthesis project, it is important to quickly gain a thorough understanding of the type and scope of data under consideration. Additionally, it is a good practice to scan data for issues before publishing.

While data package page features such as the [Data Entities](https://docs.google.com/document/d/1fYIJAKFaA4lPyqo6Rz0ZSEUKKiNMLF5UZCxlyUfhxwM/edit#heading=h.a8wxh1c77yym) section in the detailed metadata pages provide concise explanations of the attributes in a table, summary and visualization tools can provide a quick and easy interactive view into the actual data values. EDI offers three options for data exploration: Data eXplorer, Data Import Scripts, and datapie.


[TOC]



## Data eXplorer (DeX) {#data-explorer-dex}

The EDI Data Explorer (DeX) is a web browser application offering summary information, subsetting, and plotting features for data packages containing tabular data files. DeX is a great tool for making a preliminary assessment about fitness for use. Click the **Data Explorer** link next to a data object from the **Resources** section of a data package summary page (currently only available in the [staging tier](https://docs.google.com/document/d/1LTsh1HpZNtFFbhRy8H1S4J3No80JgtC5aTpPYzTOtJM/edit#heading=h.jrdj8ing72sc) of the Data Portal).



Alternatively, open a table from a data package in DeX by providing the Data Entity URL (currently limited to tabular data) at [dex.edirepository.org.](http://dex.edirepository.org) 


### Profile {#profile}

The Profile tab provides data table overview information, a sample of the first and last rows in the table, and summary information for every variable in the table.


#### Overview {#overview}

A breakdown of dataset statistics (size, missing value and duplicate row counts, etc.) and variable types (number of datetime, numerical, unique, and other variable types). This section also includes notes for individual variables and information about the profile report.


#### Sample {#sample}

This section displays the first and last ten rows of the data table, a row index, and column names.


#### Variables {#variables}

For every variable in the table, this section displays a miniature summary page complete with counts of missing and duplicate rows, minimum and maximum values, and a frequency plot for the variable.


### Subset {#subset}

The Subset tab allows users to filter and download data by a query, time period, row index, category, or by simply selecting the columns of interest with checkboxes.


#### Query {#query}

Users can type a query to filter data. The query syntax is based on the Python Pandas' query method.

Rows can be filtered by values in character columns using the `==` and `!=` operators:



Rows can also be filtered by values in numeric columns using the `>`, `&lt;`, `>=`, `&lt;=`, `!=` and `==` operators. Use backticks to select columns that have spaces or special characters in their name:



Rows can be filtered using comparisons between different columns. Multiple logical queries can be combined with the `&` and `|` symbols to create advanced logical queries:



Individual rows can be selected by their index using square brackets:



Rows where the values from two columns are equal (or not equal) may also be filtered by comparing the two columns: `col_1 == col_2` or `col_1 != col_2`



Rows where the values from one column are present (or not present) anywhere in another column may be filtered by using the "in" (or "not in") operator with the two columns: `col_1 in col_2` or `col_1 not in col_2`



For details, refer to the Pandas' [general guide to querying data](https://pandas.pydata.org/docs/user_guide/indexing.html#the-query-method) and the [pandas.DataFrame.query](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html) API documentation specifically. 


#### Time Period {#time-period}

Users can filter by time period by selecting a Date column and entering a start and end date.


#### Row Index {#row-index}

Users can filter by entering the start and end row index.


#### Category {#category}

For tables with categorical data columns declared in the EML, users can filter by specific categories within a given column.


### Plot {#plot}

The Plot tab allows users to create scatter plots for the table by selecting an independent and one or more dependent variables.


### EML {#eml}

This tab takes you back to the Detailed Metadata page for the data package.


## Data Import Scripts {#data-import-scripts}

[Data import scripts](https://docs.google.com/document/d/11dI1N_KeOkkmvwmamlVnEX8DDOrlSr6BpMwHAI28IT4/edit#heading=h.rz9p6ko82ldl), available in the **[Code Generation](https://docs.google.com/document/d/1fYIJAKFaA4lPyqo6Rz0ZSEUKKiNMLF5UZCxlyUfhxwM/edit#heading=h.3sp2i4secucf)** section of the data package summary page, read data directly from the EDI Data Repository into common programming language workspaces. This service provides full control over data manipulation and statistical exploration.


## datapie {#datapie}

The Data Package Interface for Evaluation ([datapie](https://imcr-hackathon.github.io/datapie/)) R Package lets users explore data packages that are available through the DataONE Network via an R Shiny application. This project is under development.
