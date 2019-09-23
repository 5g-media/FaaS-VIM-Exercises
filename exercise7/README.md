## Exercise Description

TODO.

[VLC](https://www.videolan.org/vlc/) should be installed on your laptop to watch the stream produced by the detection service.


In below commands, replace `<your docker id>` with yours.

### Package RTMP server as black-box action

At all-in-one UI open "Lean OW Web CLI".

Invoke these commands to build your black-box image

```
cd FaaS-VIM-Exercises/exercise7/
```

```bash
docker build --tag "<your docker id>/nginx_rtmp" --force-rm=true .
docker login --username=<your docker id>
docker push <your docker id>/nginx_rtmp
```


### Create your actions

Create your action passing the docker image we just created

```bash
wsk -i action create /guest/exercises/nginx_rtmp  --docker <your docker id>/nginx_rtmp
wsk -i action create /guest/exercises/vdetection --docker docker5gmedia/action-vdetection
```

Detection image is large. Depending on the network conditions this can take a fairly amount of time and can cause timeouts for the action invocation. To avoid this, pull the image in advance

```
docker pull docker5gmedia/action-vdetection
```


## Create VNF/NS packages


### An automated way to generate VNFD skeleton

At all-in-one UI open "Validator".


### Produce VNFD package

* Hit 'Reset'.
* Select OSM Schema.
* Select Type VNFD.
* Copy/paste the contents of `vdetection_vnfd.yaml`
* Hit 'Validate'. Fix any errors.
* Once validates successully hit 'Export to your computer'

Repreat above steps for `nginx_rtmp_vnfd.yaml`

### Produce NSD package

* Hit 'Reset'.
* Select OSM Schema.
* Select Type NSD.
* Copy/paste the contents of `vdetection_nsd.yaml`
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
curl -X POST -d '{"service_ports": ["3145"]}' http://127.0.0.1:5002/conf/vdetection_instance/vdetection_vnfd/1
curl -X POST -d '{"service_ports": ["1935", "8080"]}' http://127.0.0.1:5002/conf/vdetection_instance/nginx_rtmp_vnfd/2
```


## Instantiate the network service

At All-in-one UI, select "Editor" then select NS Instances (left pane), select New NS (right pane) fill in the following fields

* Name:           select name: `vdetection_instance`. It is important for the name to match the one used for ingress port definition.
* Description:    give short description
* Nsd Id:         select `vdetection_nsd`
* Vim Account Id: select FaaS

Hit 'Create'

Wait for status to become 'running'


### Configure vdetection VNF to start streaming

We are going to internact with the VNF by calling its `rest/detections/start` endpoint passing it the parameters. It will start streaming to the RTPM server we just started.

At All-in-one UI open "OSM Web CLI".

Retrieve the port and pass it to start command

```bash
PORT1=`curl 127.0.0.1:5002/osm/vdetection_instance | jq .vnfs[0].vim_info.service.service_ports.\"3145\"`
echo $PORT1
```

Ensure port retrieved (it can take few seconds, repeat above commands if needed)

Next, retrieve ipaddress of RTMP VNF

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
        "url": "rtmp://<All in one VM IP>:1935/detection/demo"
      }
    }
  }
}'
```

Ensure curl returns 200
```
"status":{"code":200,"msg":"ok"}
```

**Tip:** You can check whether vdetection publishes its results by pointing your browser to: `http://<VM IP>:<ingress port of 8080>/stat`. 
You should notice a `demo` link in `publishing` state with an increase of `In Bytes`. It may take several seconds for the stream to become ready (refresh browser until it apprears).

```bash
curl 127.0.0.1:5002/osm/vdetection_instance | jq .vnfs[1].vim_info.service.service_ports.\"8080\"
```


### Open VLC

At first you need the ingress port so that your VLC can play the stream of RTMP VNF.

At All-in-one UI open "OSM Web CLI".

```bash
curl 127.0.0.1:5002/osm/vdetection_instance | jq .vnfs[1].vim_info.service.service_ports.\"1935\"
```

From your laptop open VLC and point it to all-in-one VM (the ipaddress you received from the instructor)

VLC -> Media -> Open Network Stream...

Enter `rtmp://<all-in-one VM IP>:<ingress port of 1935>/detection/demo`
