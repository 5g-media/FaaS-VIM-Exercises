## Exercise Description

In this exercise are going to create two VNFs: ping and pong that communicate with each other.

## Pre-onboard your openwhisk action

### Create your action

We are going to create an openwhisk action out from our VNF source code. We create this action using runtime semantic (i.e. proviging runtime kind).

At all-in-one UI open "Lean OW Web CLI".

```
cd FaaS-VIM-Exercises/exercise5/
```

Invoke the following

```bash
wsk -i action create /guest/exercises/ping --kind python:2 ping.py
wsk -i action create /guest/exercises/pong --kind python:2 pong.py
```

## Create VNF/NS packages

At all-in-one UI open "Validator".

### Produce VNFD package

* Hit 'Reset'.
* Select OSM Schema.
* Select Type VNFD.
* Copy/paste the contents of `ping_vnfd.yaml`
* Hit 'Validate'. Fix any errors.
* Once validates successully hit 'Export to your computer'

Repeat the steps above for `pong_vnfd.yaml`

### Produce NSD package

* Hit 'Reset'.
* Select OSM Schema.
* Select Type NSD.
* Copy/paste the contents of `pingpong_nsd.yaml`
* Hit 'Validate'. Fix any errors.
* Once validates successully hit 'Export to your computer'



## Onboard the packages to OSM

At All-in-one UI, select "Editor".

* Select VNF Packages (left pane) and drag/drop ping pong VNF package you created at previous step
* Select NS  Packages (left pane) and drag/drop pingpong NS package you created at previous step


### Mark ping VNF port as Ingress


At All-in-one UI open "OSM Web CLI".

Invoke the following

```bash
curl -X POST -d '{"service_ports": ["5000"]}' http://127.0.0.1:5002/conf/pingpong_instance/ping_vnfd/1
```



## Instantiate the network service

At All-in-one UI, select "Editor" then select NS Instances (left pane), select New NS (right pane) fill in the following fields

* Name:           select name: `pingpong_instance`. It is important for the name to match the one used for ingress port definition.
* Description:    give short description
* Nsd Id:         select `pingpong_nsd`
* Vim Account Id: select FaaS

Hit 'Create'

Wait for status to become 'running'



### Interact with the VNF

Retrieve Ping VNF external port.

At All-in-one UI open "OSM Web CLI".


Invoke the following

```bash
curl 127.0.0.1:5002/osm/pingpong_instance | jq .vnfs[0].vim_info.service.service_ports.\"5000\"
```

Now, let's ping the VNF to send 10 messages to pong. Replace `external_port` with the port printed in previous step

```bash
curl 127.0.0.1:<external_port>/ping/10
```

We see similar message to this:

```

I don't know the target I should ping to :(

```

In the next step we will push day1 configuration with the ip addess of Pong VNF so that Ping can communicate with it.

### Define ping VNF with day1 parameter

At All-in-one UI open "OSM Web CLI".

Retrieve ipaddesss of pong VNF

```bash
curl 127.0.0.1:5002/osm/pingpong_instance | jq .vnfs[1].ip_address
```

Push day1 parameters. Replace `ip_address` with the ipaddress printed in previous step

```bash
curl -X POST -d '{"coe_action_params": {"action_params": {"target_ip": "<ip_address>"}}}' http://127.0.0.1:5002/osm/reconfigure/pingpong_instance/ping_vnfd.1
```

### Interact with the VNF again

Let's ping again the VNF to send 10 messages to pong. Replace `external_port` with the port printed in previous step

```bash
curl 127.0.0.1:<external_port>/ping/10
```

We should see it is working:

```

pongpongpongpongpongpongpongpongpongpong

```

## What next

Now, lets continue with real VNF examples such as vtranscoder that processes media frames.

Continue to [6th exercise](../exercise6)

But.. perhaps you want to familiarized with yourself with the `wskdeploy` tool. In that case, quickly jump to [5b exercise](../exercise5b)
