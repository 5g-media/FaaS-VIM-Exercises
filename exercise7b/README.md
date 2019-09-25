## Exercise Description

This time we are going to package RTMP server as openwhisk action so that we have two FaaS VNFs: vdetection and RTMP service talking with each other.


### Package RTMP server as black-box action

At all-in-one UI open "Lean OW Web CLI".

Invoke these commands to build your black-box image

```
cd FaaS-VIM-Exercises/exercise7b/
```

```bash
docker build --tag "<your docker id>/nginx_rtmp" --force-rm=true .
docker login --username=<your docker id>
docker push <your docker id>/nginx_rtmp
```

### Create the action

Create your action passing the docker image you just created

```bash
wsk -i action create /guest/exercises/nginx_rtmp  --docker <your docker id>/nginx_rtmp
```

## Create VNF/NS packages


### An automated way to generate VNFD skeleton

[VNFD generation tool](https://osm.etsi.org/wikipub/index.php/Creating_your_own_VNF_package)


Run skeleton creation tool


```bash
../tools/generate_descriptor_pkg.sh -c -t vnfd nginx_rtmp --image /guest/exercises/nginx_rtmp
```

You will notice yaml descriptor file under

`nginx_rtmp_vnfd/nginx_rtmp_vnfd.yaml`


At all-in-one UI open "Validator".


### Produce VNFD package

* Hit 'Reset'.
* Select OSM Schema.
* Select Type VNFD.
* Copy/paste the contents of `nginx_rtmp_vnfd/nginx_rtmp_vnfd.yaml`
* Hit 'Validate'. Fix any errors.
* Once validates successully hit 'Export to your computer'

### Produce NSD package

* Hit 'Reset'.
* Select OSM Schema.
* Select Type NSD.
* Copy/paste the contents of `vdetection_rtmp_nsd.yaml`
* Hit 'Validate'. Fix any errors.
* Once validates successully hit 'Export to your computer'


## Onboard the packages to OSM

At All-in-one UI, select "Editor".

* Select VNF Packages (left pane) and drag/drop the VNF package you created at previous step
* Select NS  Packages (left pane) and drag/drop the NS package you created at previous step


### Mark VNF ports as Ingress

At All-in-one UI open "OSM Web CLI".


Invoke the following

```bash
curl -X POST -d '{"service_ports": ["3145"]}' http://127.0.0.1:5002/conf/vdetection_rtmp_instance/vdetection_vnfd/1
curl -X POST -d '{"service_ports": ["1935", "8080"]}' http://127.0.0.1:5002/conf/vdetection_rtmp_instance/nginx_rtmp_vnfd/2
```

## Instantiate the network service

At All-in-one UI, select "Editor" then select NS Instances (left pane), select New NS (right pane) fill in the following fields

* Name:           select name: `vdetection_rtmp_instance`. It is important for the name to match the one used for ingress port definition.
* Description:    give short description
* Nsd Id:         select `vdetection_rtmp_nsd`
* Vim Account Id: select FaaS

Hit 'Create'

Wait for status to become 'running'


### Configure vdetection VNF to start streaming

We are going to internact with the VNF by calling its `rest/detections/start` endpoint passing it the parameters. It will start streaming to the RTPM server we just started.

At All-in-one UI open "OSM Web CLI".

Retrieve ingress port of vdetetion.

```bash
PORT1=`curl 127.0.0.1:5002/osm/vdetection_instance | jq .vnfs[0].vim_info.service.service_ports.\"3145\"`
echo $PORT1
```

Ensure port retrieved (it can take few seconds, repeat above commands if needed)

Next, retrieve ipaddress and ingress port of RTMP VNF. You will need to pass it to VLC

```bash
curl 127.0.0.1:5002/osm/vdetection_instance | jq .vnfs[1].ip_address
```

```bash
curl -H  "Content-Type: application/json" -X POST http://127.0.0.1:$PORT1/rest/detections/start -d '{
  "config": {
    "input": {
      "source": {
        "url": "assets/video/TBBT01.mp4"
      }
    },
    "output": {
      "settings": {
        "image": {
          "type": "jpg"
        }
      },
      "serve": {
        "frmt": "flv",
        "url": "rtmp://<vnfs[1].ip_address>:1935/detection/demo"
      }
    }
  }
}'
```

Ensure curl returns 200



### Open VLC

At first you need the ingress port so that your VLC player in your laptop can play the stream of RTMP VNF.

At All-in-one UI open "OSM Web CLI".

```bash
curl 127.0.0.1:5002/osm/vdetection_instance | jq .vnfs[1].vim_info.service.service_ports.\"1935\"
```

From your laptop open VLC and point it to all-in-one VM (the ipaddress you received from the instructor)

VLC -> Media -> Open Network Stream...

Enter `rtmp://<all-in-one VM IP>:<ingress port of 1935>/detection/demo`


