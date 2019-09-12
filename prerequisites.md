# Prerequisites

Please follow these prerequisites before doing the excercises.

### Login to All in one UI

Log in with your chrome browser `http://<VM ip address>:8401/` 

Log into your development VM

### Clone devops tool

```
cd ~
git clone https://osm.etsi.org/gerrit/osm/devpos
cd devops
git checkout tags/v5.0.5
```

### Create openwhisk package

At all in one UI open "Lean OW Web CLI" and invoke the following command

```
wsk -i package create excercises
```
