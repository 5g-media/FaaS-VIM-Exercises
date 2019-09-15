**Note:** Ensure you already followed [prerequisites](../prerequisites.md)


## Exercise Description

In this exercise, we will learn how to modify our hello world application to handle parameters.



### Update your action

We are going to update our action we created in exercise 1, with the updated code.

At all-in-one UI open "Lean OW Web CLI" invoke the following command

```
wsk -i action update /guest/exercises/hello_world  hello_world.py
```



### Define day0 parameter

At All-in-one UI open "OSM Web CLI".

Invoke the following

```bash
curl -X POST -d '{"service_ports": ["5000"], "action_params": {"name": "Avi"}}' http://127.0.0.1:5002/conf/hello_world_instance_day0/helloworld_vnfd/1
```



### Instantiate the network service

At All-in-one UI, select "Editor" then select NS Instances (left pane), select New NS (right pane) fill in the following fields

* Name:           select name: `hello_world_instance_day0`. It is important for the name to match the one used for day0 parameter definition.
* Description:    give short description
* Nsd Id:         select `hello_world_nsd`
* Vim Account Id: select FaaS

Hit 'Create'

Wait for status to become 'running'



### Interact with the VNF

Your next step would be to retrieve its external port.

At All-in-one UI open "OSM Web CLI".

Invoke the following

```bash
curl 127.0.0.1:5002/osm/hello_world_instance_day0 | jq .vnfs[0].vim_info.service.service_ports.\"5000\"
```

Now, issue the curl below replacing `external_port` with the port printed in previous step

```bash
curl 127.0.0.1:<external_port>/hello
```

You should see output similar to this:

```
Hello, Avi from my first FaaS VNF!
```

## What next

Next, we will create 2 VNFs that communicate with each other.

Continue to [5th exercise](../exercise5)
