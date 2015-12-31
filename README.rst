Patron
======

--------
Overview
--------

Patron is an access control service for OpenStack cloud. It controls the access to RESTful APIs
exposed by other OpenStack services based on policy enforcement. The goal is to make access controls
of other services easier and more powerful.

Patron is comprised of two parts: 
the ``patron service`` and a request filter called ``Access Endpoint Middleware (AEM)``:

* ``patron service`` stores the access control policies of other OpenStack services and provides access decisions based on those policies.
 
* ``AEM`` is to be installed on all other OpenStack services that needs access control. The requests to those services are first mediated by the patron service, who makes a decision (``YES`` or ``NO``) based on policy and returns the result back to AEM. If patron's answer is ``YES``, AEM permits this request, otherwise the request is going to be denied.

Patron provides RESTful APIs to users so that they can view and update their
access control policies to the cloud. Patron improves the original ``policy.json``
access control mechanism by allowing an individual user to have their own policy.
With the help of patron, the original access control hooks inside other services
can be removed.

Patron is designed to be capable of handling access control missions for many other
services. Currently supported services are: ``nova``, ``glance``, ``neutron``, ``cinder``, ``heat`` and
``ceilometer``. More service' supports will be added in the future.
