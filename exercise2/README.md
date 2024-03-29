## Exercise Description

In this exercise, we will learn how to package our application as black-box openwhisk action. We will manually dockerize our application so that it can be invoked as an openshik action.

As we can see, our app `hello_world.py` starts with `#!/usr/bin/env python`. This because the file is now being invoked as a generic process (i.e the file is being invoked as an executable) in contrast to a regular pythonic runtime as demonstrated in previous exercise. Moreover, our docker image derives from a special base one: `docker5gmedia/5gmedia-base`. This base image contains openwhisk artifacts needed by the image we build so that it can be invoked as an openwhisk action.


## Pre-onboard your openwhisk action

In below commands, replace `<your docker id>` with yours.


### Package your code as black-box action

At all-in-one UI open "Lean OW Web CLI".

Invoke these commands to build your black-box image

```
cd FaaS-VIM-Exercises/exercise2/
```

```bash
docker build --tag "<your docker id>/hello_world_blackbox" --force-rm=true .
docker login --username=<your docker id>
docker push <your docker id>/hello_world_blackbox
```


### Create your action

Create your action passing the docker image we just created

```
wsk -i action create /guest/exercises/hello_world_blackbox  --docker <your docker id>/hello_world_blackbox
```

## Create VNF/NS packages


### An automated way to generate VNFD skeleton

[VNFD generation tool](https://osm.etsi.org/wikipub/index.php/Creating_your_own_VNF_package)


Run skeleton creation tool

```bash
../tools/generate_descriptor_pkg.sh -c --nsd -t vnfd hello_world_blackbox --image /guest/exercises/hello_world_blackbox
```

You will notice two yaml descriptor files created under vnfd and nsd folders

`hello_world_blackbox_vnfd/hello_world_blackbox_vnfd.yaml` and `hello_world_blackbox_nsd/hello_world_blackbox_nsd.yaml`


At all-in-one UI open "Validator".

### Produce VNFD package

* Hit 'Reset'.
* Select OSM Schema.
* Select Type VNFD.
* Copy/paste the contents of `hello_world_blackbox_vnfd/hello_world_blackbox_vnfd.yaml`
* Hit 'Validate'. Fix any errors.
* Once validates successully hit 'Export to your computer'


### Produce NSD package

* Hit 'Reset'.
* Select OSM Schema.
* Select Type NSD.
* Copy/paste the contents of `hello_world_blackbox_nsd/hello_world_blackbox_nsd.yaml`
* Hit 'Validate'. Fix any errors.
* Once validates successully hit 'Export to your computer'



## Onboard the packages to OSM

At All-in-one UI, select "Editor".

* Select VNF Packages (left pane) and drag/drop the VNF package you created at previous step
* Select NS  Packages (left pane) and drag/drop the NS package you created at previous step



## Instantiate the network service

From OSM GUI select NS Instances (left pane), select New NS (right pane) fill in the following fields

* Name:           select a name (e.g. `hello_world_blackbox_instance`) to give to your instance (review [naming guidelines](../GUIDELINES.md))
* Description:    give short description
* Nsd Id:         select `hello_world_blackbox_nsd`
* Vim Account Id: select FaaS

Hit 'Create'

Wait for status to become 'running'



## Interact with the VNF

Follow same instructions as in exercise 1 [interact-with-the-vnf](../exercise1#interact-with-the-vnf) to send your blackbox VNF hello message.

```
curl 127.0.0.1:5002/osm/hello_world_blackbox_instance | jq .vnfs[0].ip_address
```

```
kubectl run curl-pod --image=radial/busyboxplus:curl -i --tty --rm

curl <ipaddress>:5000/hello
```

## What next

Next, we will learn how to attach the VNF an Ingress port so that it can be extrenally accessed.

Continue to [3rd exercise](../exercise3)
