# mom3api
Mom3 - Django Experiment to investigate how a REST API can be added

This requires the following steps:

- create and setup a django project
- copy the Mom3 database with ``mysqldbcopy``
- generate the Django ``models.py`` with ``inspectdb``
- clean up the conversion mess (following the instruction that automatically added to ``models.py``)
- wire the model to the Django Rest Framework to create the REST API
- ``migrate`` the database to Django (existing tables remain unchanged, but django specific tables are added).

This is what you get when you setup the ``urls``, ``models``, ``views`` and ``serializers``. A hyperlinked navigable REST API:

<p align="center">
  <img src="https://github.com/vermaas/mom3api/blob/master/docs/mom3_django_screenshot1.png"/>
</p>

- Adding pagination and filtering to improve performance and usability

<p align="center">
  <img src="https://github.com/vermaas/mom3api/blob/master/docs/mom3_django_screenshot3.png"/>
</p>

- Connecting MoM3 to the migrated database. (change jdbc configuration in Tomcat's ``context.xml``) 

Now changes made in either MoM, the Django Admin interface, or the REST API, are reflected everywhere.

<p align="center">
  <img src="https://github.com/vermaas/mom3api/blob/master/docs/mom3_django_screenshot4.png"/>
</p>

<p align="center">
  <img src="https://github.com/vermaas/mom3api/blob/master/docs/mom3_django_screenshot5.png"/>
</p>

Aladin
------
This screenshot shows how a frontend archive application (ALTA) can connect the Beams from the MoM REST API to Aladin VO to show all observed fields.

<p align="center">
  <img src="https://github.com/vermaas/mom3api/blob/master/docs/alta_mom_api.jpg"/>
</p>

----
## usage

Example: retrieve a dataproduct by its name:
http://localhost:8000/mom3api/dataproducts/?name=L770733_SAP000_B017_P000_bf.tar

```json
        {
            "id": 28215535,
            "name": "L770733_SAP000_B017_P000_bf.tar",
            "indexid": 17,
            "timestamp": "2020-03-04T14:16:52Z",
            "type": "LOFAR_PULSAR",
            "released": 0,
            "exported": 0,
            "fileformat": "PULP",
            "archived": 0,
            "pipelined": 0,
            "topology": null,
            "status": null,
            "placeholder": 0,
            "status_code": 0,
            "message": null,
            "mom2objectid": "http://localhost:8000/mom3api/mom2objects/983655/"
        }

```
Which could be used to get the proper SIP like this:
https://lofar.astron.nl/mom3/interface/importXML2.do?command=GETSIP&id=28215535