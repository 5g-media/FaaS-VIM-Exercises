# Prerequisites

Ensure you perform these steps before doing the excercises.

Log into your development VM

### Clone devops tool

```
cd ~
git clone https://osm.etsi.org/gerrit/osm/devpos
cd devops
git checkout tags/v5.0.5
```

### Create openwhisk package

```
wsk -i package create excercises
```

