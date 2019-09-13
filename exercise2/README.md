
**Note:** Ensure you already followed [prerequisites](../prerequisites.md)

## Exercise Description

TODO

## Pre-onboard your openwhisk action

### Package your code as black-box action

At all-in-one UI open "Lean OW Web CLI" and invoke these commands to build your black-box action. Replace `<your dockerhub userid>` with yours.

```bash
docker build --tag "<your dockerhub userid>/hello_world_blackbox" --force-rm=true .
docker login --username=<your dockerhub userid>
docker push <your dockerhub userid>/hello_world_blackbox
```

### Create your action

Replace `<your dockerhub userid>` with yours

```
wsk -i action create /guest/exercises/hello_world_blackbox  --docker <your dockerhub userid>/hello_world_blackbox
```

## Create VNF/NS packages

At all-in-one UI open "Validator".

### Produce VNFD package

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
* Nsd Id:         select your `hello_world_blackbox` NS package
* Vim Account Id: select the VIM account. There should be one related to FaaS

Wait for the status to become "running".

At All-in-one UI, select Editor.



## Interact with the VNF

Check to see that the VNF is in running state.

At All-in-one UI open "OSM Web CLI" and invoke the following

```bash
curl 127.0.0.1:5002/osm/hello_world_blackbox_instance | jq . 
```

You can interact with your VNF as done in the previous exercise


## What next

Next, we will learn how to attach the VNF an Ingress port so that it can be extrenally accessed.

Continue to [3rd exercise](../exercise3)
