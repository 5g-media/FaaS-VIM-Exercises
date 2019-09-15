
**Note:** Ensure you already followed [prerequisites](../prerequisites.md)

## Exercise Description

In this exercise, we will learn how to package our application as black-box openwhisk action. We will go over the steps of dockerizing it and the base docker image it derives from.


## Pre-onboard your openwhisk action

In below commands, replace `<your docker id>` with yours.


### Package your code as black-box action

At all-in-one UI open "Lean OW Web CLI".

Invoke these commands to build your black-box image

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

At all-in-one UI open "Validator".

### Produce VNFD package

* Hit 'Reset'.
* Select OSM Schema.
* Select Type VNFD.
* Copy/paste the contents of `hello_world_vnfd_blackbox.yaml`
* Hit 'Validate'. Fix any errors.
* Once validates successully hit 'Export to your computer'


### Produce NSD package

* Hit 'Reset'.
* Select OSM Schema.
* Select Type NSD.
* Copy/paste the contents of `hello_world_nsd_blackbox.yaml`
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
* Nsd Id:         select `helloworld_nsd_blackbox`
* Vim Account Id: select FaaS

Hit 'Create'

Wait for status to become 'running'



## Interact with the VNF

Follow same instructions as in exercise 1 [interact-with-the-vnf](../exercise1#interact-with-the-vnf) to send your blackbox VNF hello message.



## What next

Next, we will learn how to attach the VNF an Ingress port so that it can be extrenally accessed.

Continue to [3rd exercise](../exercise3)
