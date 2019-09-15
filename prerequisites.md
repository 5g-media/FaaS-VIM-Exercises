# Prerequisites

Please follow these prerequisites before doing the excercises.

### Docker regitry user

Some of the exercises involve in creating docker file images. Therefore you should sign up for an account at [docker hub](https://hub.docker.com/)

### Login to All in one UI

Log in with your chrome browser `http://<VM ip address>:8401/` with developer/developer credentials

### Create openwhisk package

During the exercises you will create various openwhisk actions. Therefore we will create dedicated package name where our actions created under.

At all in one UI open "Lean OW Web CLI" and invoke the following command

```
wsk -i package create exercises
```
