# Repository Tiers

There are three different tiers in the EDI Data Repository: production, staging, and development. Production is the primary tier where fully published data packages are securely and permanently hosted, staging is used for previewing data packages and testing workflows, and the development tier is used by EDI Repository developers to test new repository features.

 ![](../../static/images/repository-tier-earths.png)

Analogous to use of the EDI Data Repository tiers, a worldly deity would  (hopefully) test new features on development and staging Earths before releasing to production.


[TOC]



## Production {#production}

The production tier is where data packages are officially and securely published with a DOI and made permanently accessible for reuse. All features of the production tier are mature and stable. The production version of the EDI Data Portal is accessible at [portal.edirepository.org](http://portal.edirepository.org). 


## Staging {#staging}

The staging tier is where new features of the EDI Data Repository mature before release to production, and is used for creating a shareable proof of a data package during the [review process](https://docs.google.com/document/d/1aNInQhyCylgBuu0mucPSS92haTp3krjFMSracEwMkFs/edit?usp=sharing), and testing new workflow. The staging version of the EDI Data Portal can be accessed at [portal-s.edirepository.org](http://portal-s.edirepository.org). 

While the staging functions almost exactly as production, there are notable differences. The key differences are that packages published to the staging portal are not assigned a DOI and that Summary Pages in the staging portal have additional markup to alert users that they are viewing a test version of a package. Furthermore, EDI does not guarantee for data to be available here indefinitely.


## Development {#development}

The development tier is used for testing new and, possibly, unstable features of the EDI Data Repository that are not yet mature enough for release to staging. The development version of the EDI Data Portal can be accessed at [portal-d.edirepository.org](http://portal-d.edirepository.org). 

While there is rarely a reason for most users to operate in the development tier, it can be used to test data packages and workflows with the newest features that will eventually be released to production.
