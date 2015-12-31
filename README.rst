Patron
======

--------
Overview
--------

Patron is an access control service for OpenStack clouds. It contains two parts: 
the **patron** service and the request filter called **Access Endpoint Middleware (AEM)**.
AEM is to be installed on all other OpenStack services that needs access control 
(except keystone). The requests to those services are first mediated by the
patron service, patron make a decision (**YES** or **NO**) based on policy and return the decision
result to AEM. If patron's answer is **YES**, AEM permits this request to the service,
or the request is going to be denied.

Patron provides RESTful APIs to users so that they can view and update their
access control policies to the cloud. Patron improves the original policy.json
access control mechanism by allowing an individual user to have their own policy.

Patron is designed to be capable of handling access control missions for many other
services. Currently supported services are: **Nova**, **Glance**, **Neutron**, **Cinder**, **Heat** and
**Ceilometer**. More service' supports will be added in the future.
