Description: TODO

## Pre-onboard your openwhisk action

### Create your action

```
wsk -i action create /guest/excercises/hello_world --kind python:2 hello_world.py
```

## Create VNF/NS packages

### Create skeleton descriptors

```bash
~/devops/descriptor-packages/tools/generate_descriptor_pkg.sh -c --nsd -t vnfd hello_world --image /guest/excercises/hello_world
```



### Copy example yaml files into skeleton

```
cp hello_world_vnfd.yaml hello_world_vnfd
cp hello_world_nsd.yaml hello_world_nsd
```



### Package the VNF/NS

The below commands create the packages to be onboarded to OSM

```bash
~/devops/descriptor-packages/tools/generate_descriptor_pkg.sh -a -t vnfd hello_world_vnfd
~/devops/descriptor-packages/tools/generate_descriptor_pkg.sh -a -t nsd hello_world_nsd
```

`hello_world_vnfd.tar.gz` and `hello_world_nsd.tar.gz` packages should be created in your current folder.



## Onboard the packages to OSM

At All-in-one UI, select Editor. Another tab is created with your OSM GUI.

* Select VNF Packages (left pane) and drag/drop the VNF package
* Select NS  Packages (left pane) and drag/drop the NS package



## Instantiate the network service

From OSM GUI select NS Instances (left pane), select New NS (right pane) fill in the following fields

* Name:           select a name (e.g. `hello_world_instance`) to give to your instance (TODO: review naming guidelines)
* Description:    give short description
* Nsd Id:         select your `hello_world` NS package
* Vim Account Id: select the VIM account. There should be one related to FaaS

At All-in-one UI, select Editor.



## Interact with the VNF

The VNF you just developed can only be accessed from whithin kubernetes cluster (e.g from inside of your minikube).

Your first step would be retrieve its ipaddrss from OSM. This can be achieve via simple curl command 

```bash
curl 127.0.0.1:5002/osm/hello_world_instance | jq .vnfs[0].ip_address 
```

Create a pod inside kubernetes and invoke `hello` endpoint of your first VNF

```bash
kubectl run curl-pod --image=radial/busyboxplus:curl -i --tty --rm

curl <ipaddress>:5000/hello
```

You see hello message. Congragulations !

Hit ^D to exit the container. It automatically deleted.

* Continue to 2nd excercise (TBD)

