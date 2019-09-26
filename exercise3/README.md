## Exercise Description

In this exercise, we are going to learn how to expose our hello world VNF from the exercise 1, as a service.


### Mark VNF port as Ingress

Our HTTP server serves on port 5000. Therefore, mark it as ingress. 

At All-in-one UI open "OSM Web CLI".

Invoke the following to initiate Day 0 configuration parameters for the hello_world_vnfd VNF (whose index in the NSD is 1).

```bash
curl -X POST -d '{"service_ports": ["5000"]}' http://127.0.0.1:5002/conf/hello_world_instance_external/hello_world_vnfd/1
```



## Instantiate the network service

At All-in-one UI, select "Editor" then select NS Instances (left pane), select New NS (right pane) fill in the following fields

* Name:           select name: `hello_world_instance_external`. It is important for the name to match the one used for ingress port definition.
* Description:    give short description
* Nsd Id:         select `hello_world_nsd`
* Vim Account Id: select FaaS

Hit 'Create'

Wait for status to become 'running'



### Interact with the VNF

The VNF you just instantiated can now be externally accessed.

Your next step would be to retrieve its external port.

At All-in-one UI open "OSM Web CLI".

Invoke the following

```bash
curl 127.0.0.1:5002/osm/hello_world_instance_external | jq .vnfs[0].vim_info.service.service_ports.\"5000\"
```

Now, you can also access it from the local host or any other host connected to the VM. Replace `external_port` with the port printed in previous step

```bash
curl 127.0.0.1:<external_port>/hello
```

You should see output similar to this:

```
Hello World from my first FaaS VNF!
```

## What next

Next, we will enhance our application to receive day0 parameter and print it in the 'hello world' message

Continue to [4th exercise](../exercise4)
