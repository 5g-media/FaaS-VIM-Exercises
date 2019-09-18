**Note:** Ensure you already followed [prerequisites](../prerequisites.md)

## Exercise Description

We will start with a simple hello world FaaS VNF that implements an HTTP server that serves `hello` endpoint. We will learn how to 'wrap' it as an OpenWhisk action, and create a Virtual Network Function (VNF) out of it, onboard it as a Network Service (NS) in the 5G-MEDIA platform, and instantiate it. We will go through all the steps starting from the VNF development to validation to onboarding and execution. 

## Pre-onboard your openwhisk action

### Create your action

We are going to create an openwhisk action out of our source code. We create this action using a standard runtime environment via specifying  a correct runtime "kind".

(In Exercise 2 we will learn how to achieve the same via a "black-box" action (i.e., using a Docker container without using the source code directly).


## In the all-in-one UI open "Lean OW Web CLI".

Invoke the following command

```
wsk -i action create /guest/exercises/hello_world --kind python:2 hello_world.py
```

## Create VNF/NS packages

## At all-in-one UI open "Validator".


### Produce VNFD package

* From the drop down menu select "OSM Schema";
* From the drop down menu select descriptor type "VNFD";
* Copy/paste the contents of `hello_world_vnfd.yaml`;
* Hit 'Validate'. Fix any errors;
* Once validated successully hit 'Export to your computer'


### Produce NSD package

* Hit 'Reset'.
* Select OSM Schema.
* Select Type NSD.
* Copy/paste the contents of `hello_world_nsd.yaml`
* Hit 'Validate'. Fix any errors.
* Once validated successully hit 'Export to your computer'


### An automated way to generate VNFD skeleton

[VNFD generation tool](https://osm.etsi.org/wikipub/index.php/Creating_your_own_VNF_package)

At all-in-one UI open "Lean OW Web CLI".

```
cd FaaS-VIM-Exercises/exercise1/
```

Run skeleton creation tool

```bash
../tools/generate_descriptor_pkg.sh -c --nsd -t vnfd hello_world --image /guest/exercises/hello_world
```

You will notice two yaml descriptor files were created under vnfd and nsd folders

`hello_world_vnfd/hello_world_vnfd.yaml` and `hello_world_nsd/hello_world_nsd.yaml`

Pass these to validator to create the packages



## Onboard the packages to OSM

At All-in-one UI, select "Editor".

* Select VNF Packages (left pane) and drag/drop the VNF package you created at previous step
* Select NS  Packages (left pane) and drag/drop the NS package you created at previous step



## Instantiate the network service

At All-in-one UI, select "Editor" then select NS Instances (left pane), select New NS (right pane) fill in the following fields

* Name:           select a name (e.g. `hello_world_instance`) to give to your instance (review [naming guidelines](../GUIDELINES.md))
* Description:    give short description
* Nsd Id:         select `hello_world_nsd`
* Vim Account Id: select FaaS

Hit 'Create'

Wait for status to become 'running'



## Interact with the VNF

The VNF you just developed can only be accessed from whithin kubernetes cluster (e.g from inside of your minikube).

Your first step would be to retrieve your VNF ipaddress. This can be achieved via simple OSM curl command.

At All-in-one UI open "OSM Web CLI" and invoke the following

```bash
curl 127.0.0.1:5002/osm/hello_world_instance | jq .vnfs[0].ip_address 
```

Create a pod inside kubernetes and invoke `hello` endpoint of your first VNF. Issue curl replacing `ipaddress` with the one printed above.

```bash
kubectl run curl-pod --image=radial/busyboxplus:curl -i --tty --rm

curl <ipaddress>:5000/hello
```

You should see hello message. Congragulations !

Hit ^D to exit the container.


## What next

Next, we will develop the same VNF this time creating it as a black-box openwhisk action.

Continue to [2nd excercise](../exercise2)
