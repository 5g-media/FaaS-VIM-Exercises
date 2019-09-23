## Exercise Description

TODO.

[VLC](https://www.videolan.org/vlc/) should be installed on your laptop to watch the stream produced by the detection service.

### Create your action

Create the action passing vdetection's docker image

At all-in-one UI open "Lean OW Web CLI".

```
cd FaaS-VIM-Exercises/exercise7/
```

```
wsk -i action create /guest/exercises/vdetection --docker docker5gmedia/action-vdetection
```

Detection image is large. Depending on the network conditions this can take a fairly amount of time and can cause timeouts for the action invocation. To avoid this, pull the image in advance

```
docker pull docker5gmedia/action-vdetection
```


## Create VNF/NS packages


### An automated way to generate VNFD skeleton

[VNFD generation tool](https://osm.etsi.org/wikipub/index.php/Creating_your_own_VNF_package)


Run skeleton creation tool


```bash
../tools/generate_descriptor_pkg.sh -c --nsd -t vnfd vdetection --image /guest/exercises/vdetection
```

You will notice two yaml descriptor files were created under vnfd and nsd folders

`vdetection_vnfd/vdetection_vnfd.yaml` and `vdetection_nsd/vdetection_nsd.yaml`

At all-in-one UI open "Validator".


### Produce VNFD package

* Hit 'Reset'.
* Select OSM Schema.
* Select Type VNFD.
* Copy/paste the contents of `vdetection_vnfd/vdetection_vnfd.yaml`
* Hit 'Validate'. Fix any errors.
* Once validates successully hit 'Export to your computer'


### Produce NSD package

* Hit 'Reset'.
* Select OSM Schema.
* Select Type NSD.
* Copy/paste the contents of `vdetection_nsd/vdetection_nsd.yaml`
* Hit 'Validate'. Fix any errors.
* Once validates successully hit 'Export to your computer'


## Onboard the packages to OSM

At All-in-one UI, select "Editor".

* Select VNF Packages (left pane) and drag/drop the VNF package you created at previous step
* Select NS  Packages (left pane) and drag/drop the NS package you created at previous step



### Mark VNF port as Ingress

At All-in-one UI open "OSM Web CLI".


Invoke the following

```bash
curl -X POST -d '{"service_ports": ["3145"]}' http://127.0.0.1:5002/conf/vdetection_instance/vdetection_vnfd/1
```


## Instantiate the network service

At All-in-one UI, select "Editor" then select NS Instances (left pane), select New NS (right pane) fill in the following fields

* Name:           select name: `vdetection_instance`. It is important for the name to match the one used for ingress port definition.
* Description:    give short description
* Nsd Id:         select `vdetection_nsd`
* Vim Account Id: select FaaS

Hit 'Create'

Wait for status to become 'running'


## RTMP Server

Before continuing with vdetection configuration, we need to start an RTMP server for the VNF to stream to

```bash
docker run -p 1935:1935 -p 8080:8080 -e RTMP_STREAM_NAMES=detection -d jasonrivers/nginx-rtmp
```



### Configure vdetection VNF to start streaming

We are going to internact with the VNF by calling its `rest/detections/start` endpoint passing it the parameters. It will start streaming to the RTPM server we just started.

At All-in-one UI open "OSM Web CLI".

Retrieve the port and pass it to start command

```bash
PORT1=`curl 127.0.0.1:5002/osm/vdetection_instance | jq .vnfs[0].vim_info.service.service_ports.\"3145\"`
```

Ensure port retrieved (it can take few seconds, repeat above commands if needed)

```
echo $PORT1
```

Invoke the following **replacing `all-in-one VM IP` with the VM IP address** you got from the instructor

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
        "url": "rtmp://<all-in-one VM IP>:1935/detection/demo"
      }
    }
  }
}'
```

Ensure curl returns 200
```
"status":{"code":200,"msg":"ok"}
```

**Tip:** You can check whether vdetection publishes its results by pointing your browser to: `http://<VM IP>:8080/stat`. 
You should notice a `demo` link in `publishing` state with an increase of `In Bytes`. It may take several seconds for the stream to become ready (refresh browser until it apprears).

### Open VLC

From your laptop open VLC and point it to the below url **replacing `all-in-one VM IP` with the VM IP address** you got from the instructor

VLC -> Media -> Open Network Stream...

Enter `rtmp://<all-in-one VM IP>:1935/detection/demo`

