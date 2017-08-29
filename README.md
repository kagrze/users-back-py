users-back-py
===

A simple REST service written in Python that demonstrates [Flask](http://flask.pocoo.org/) and [SQLAlchemy](http://www.sqlalchemy.org/).

In order to play with it just type `./run.sh`, wait a while, and then open [http://localhost:8080](http://localhost:8080) in a web browser. Optionally you can test the service with [users-front](https://github.com/kagrze/users-front) client.

It is a level two REST service according to [Richardson Maturity Model](http://martinfowler.com/articles/richardsonMaturityModel.html)
with some [HATEOAS](https://en.wikipedia.org/wiki/HATEOAS) principles (multiple media types for the root resource; list of available resources for the root resource).

The same API is also implemented in Scala: [users-back](https://github.com/kagrze/users-back).
