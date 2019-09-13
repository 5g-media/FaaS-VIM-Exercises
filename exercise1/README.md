**Note:** Ensure you already followed [prerequisites](../prerequisites.md)

## Exercise Description

TODO

## Pre-onboard your openwhisk action

### Create your action

We are going to create an openwhisk action out from our VNF source code. We create this action using runtime semantic (i.e. proviging runtime kind).

In the next exercise we will learn how to achieve the same by using the black-box semantic action.

At all-in-one UI open "Lean OW Web CLI" invoke the following command

```
wsk -i action create /guest/exercises/hello_world --kind python:2 hello_world.py
```

## Create VNF/NS packages

At all-in-one UI open "Validator".

### Produce VNFD package

* Select OSM Schema.
* Select Type VNFD.
* Copy/paste the contents of `hello_world_vnfd.yaml`
* Hit 'Validate'. Fix any errors.
* Once validates successully hit 'Export to your computer'


### Produce NSD package

* Hit 'Reset'.
* Select OSM Schema.
* Select Type NSD.
* Copy/paste the contents of `hello_world_nsd.yaml`
* Hit 'Validate'. Fix any errors.
* Once validates successully hit 'Export to your computer'



## Onboard the packages to OSM

At All-in-one UI, select "Editor".

* Select VNF Packages (left pane) and drag/drop the VNF package you created at previous step
* Select NS  Packages (left pane) and drag/drop the NS package you created at previous step



## Instantiate the network service

From OSM GUI select NS Instances (left pane), select New NS (right pane) fill in the following fields

* Name:           select a name (e.g. `hello_world_instance`) to give to your instance (review [naming guidelines](../GUIDELINES.md))
* Description:    give short description
* Nsd Id:         select your `hello_world` NS package
* Vim Account Id: select the VIM account. There should be one related to FaaS

At All-in-one UI, select Editor.



## Interact with the VNF

The VNF you just developed can only be accessed from whithin kubernetes cluster (e.g from inside of your minikube).

Your first step would be to retrieve your VNF ipaddress. This can be achieved via simple OSM curl command.

At All-in-one UI open "OSM Web CLI" and invoke the following

```bash
curl 127.0.0.1:5002/osm/hello_world_instance | jq .vnfs[0].ip_address 
```

Create a pod inside kubernetes and invoke `hello` endpoint of your first VNF. Issue curl with the ipaddress retrieved above.

```bash
kubectl run curl-pod --image=radial/busyboxplus:curl -i --tty --rm

curl <ipaddress>:5000/hello
```

You see hello message. Congragulations !

Hit ^D to exit the container. It automatically deleted.


## What next

Next, we will develop the same VNF this time creating is as a black-box openwhisk action.

Continue to [2nd excercise](../exercise2)
