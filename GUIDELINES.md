# Guidelines for FaaS Network services and VNFs

### Naming conventions

* VNFD and NSD names should contain only alphanumeric and underscores (`_`)
* Network service should be instantiated under name containing only alphanumeric and underscores (`_`)
* Do not instantiate two network services with same name

### Short lived VNFs

* FaaS VNF PODs automatically terminated after 1 hour. Delete the network service
when done or before 1 hour elapse.

### Large runtime images

FaaS VNF (media) runtime images are large. When an action is being invoked for the first time, OpenWhisk invoker pulls them out from docker hub. Depending on the network conditions this can take a fairly amount of time and can cause timeouts for the action invocation. In oder to avoid this, pull your VNF docker images in advance, by invoking these commands from all of cluster nodes.

Replace IMAGE_NAME with your docker5gmedia repository images (e.g. docker5gmedia/action-vdetection, docker5gmedia/transcoder_2_8_4)

```
docker pull <IMAGE_NAME>
```
