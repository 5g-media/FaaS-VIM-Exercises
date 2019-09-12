**Note:** Ensure you already followed [prerequisites](../prerequisites.md)


## Exercise Description

We are going to externally expose your `hello_world` VNF so that it can be externally accessed.

We will mark its local port 5000 to be accessed from the outside.


### Mark VNF port as Ingress

At All-in-one UI open "OSM Web CLI" and invoke the following

```bash
curl -X POST -d '{"service_ports": ["5000"]}' http://127.0.0.1:5002/conf/hello_world_instance/helloworld_vnfd/1
```


### Instantiate the network service

Instantiate again your network service under `hello_world_instance` name. You can follow [this step](../exercise1/README.md#instantiate-the-network-service) in exercise 1.


### Interact with the VNF

The VNF you just instantiated can now be externally accessed.

Your next step would be to retrieve its external port.

At All-in-one UI open "OSM Web CLI" and invoke the following

```bash
curl 127.0.0.1:5001/osm/hello_world_instance | jq .vnfs[0].vim_info.service.service_ports.\"5000\"
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

Continue to [4nd exercise](../exercise4)
