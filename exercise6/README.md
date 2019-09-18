## Exercise Description

In this exercise we are going to delploy a real vtranscoder. We will send it media frames and watch its various metrics in SDK monitoring dashboard.

### Create your action

Create the action passing transcoder's docker image

At all-in-one UI open "Lean OW Web CLI".

```
cd FaaS-VIM-Exercises/exercise6/
```

```
wsk -i action create /guest/exercises/vtranscoder --docker docker5gmedia/transcoder_2_8_4
```

## Create VNF/NS packages


### An automated way to generate VNFD skeleton

[VNFD generation tool](https://osm.etsi.org/wikipub/index.php/Creating_your_own_VNF_package)


Run skeleton creation tool


```bash
../tools/generate_descriptor_pkg.sh -c --nsd -t vnfd vtranscoder --image /guest/exercises/vtranscoder
```

You will notice two yaml descriptor files were created under vnfd and nsd folders

`vtranscoder_vnfd/vtranscoder_vnfd.yaml` and `vtranscoder_nsd/vtranscoder_nsd.yaml`


At all-in-one UI open "Validator".

### Produce VNFD package

* Hit 'Reset'.
* Select OSM Schema.
* Select Type VNFD.
* Copy/paste the contents of `vtranscoder_vnfd/vtranscoder_vnfd.yaml`
* Hit 'Validate'. Fix any errors.
* Once validates successully hit 'Export to your computer'


### Produce NSD package

* Hit 'Reset'.
* Select OSM Schema.
* Select Type NSD.
* Copy/paste the contents of `vtranscoder_nsd/vtranscoder_nsd.yaml`
* Hit 'Validate'. Fix any errors.
* Once validates successully hit 'Export to your computer'


## Onboard the packages to OSM

At All-in-one UI, select "Editor".

* Select VNF Packages (left pane) and drag/drop the VNF package you created at previous step
* Select NS  Packages (left pane) and drag/drop the NS package you created at previous step



### Mark vTrancoder port and set day0 parameters

In order to send the vtranscoder frames, we need to open its ports and start it with predefined parameters.

At All-in-one UI open "OSM Web CLI".


Invoke the following

```bash
curl -X POST http://127.0.0.1:5002/conf/vtranscoder_instance/vtranscoder_vnfd/1 -d '{
  "action_params": {
    "gpu_node":"0",
    "send_broker_ip":"10.10.10.10",
    "send_broker_port":"9092",
    "metrics_broker_ip":"10.10.10.10",
    "metrics_broker_port":"9092"
  },
  "service_ports": [
    "18090",
    "18091",
    "18092"
  ]
}'
```

## Instantiate the network service

At All-in-one UI, select "Editor" then select NS Instances (left pane), select New NS (right pane) fill in the following fields

* Name:           select name: `vtranscoder_instance`. It is important for the name to match the one used for ingress port definition.
* Description:    give short description
* Nsd Id:         select `vtranscoder_nsd`
* Vim Account Id: select FaaS

Hit 'Create'

Wait for status to become 'running'


### Interact with the VNF

The VNF you just instantiated can now be externally accessed.

Your next step would be to retrieve its ports.

At All-in-one UI open "OSM Web CLI".

Invoke the following

```bash
PORT1=`curl 127.0.0.1:5002/osm/vtranscoder_instance | jq .vnfs[0].vim_info.service.service_ports.\"18090\"`
PORT2=`curl 127.0.0.1:5002/osm/vtranscoder_instance | jq .vnfs[0].vim_info.service.service_ports.\"18091\"`
PORT3=`curl 127.0.0.1:5002/osm/vtranscoder_instance | jq .vnfs[0].vim_info.service.service_ports.\"18092\"`
```

Ensure ports retrieved (it can take few seconds, repeat above commands if needed)

```bash
echo $PORT1
echo $PORT2
echo $PORT3
```

## Stream media frames (using simulation tool)


At all-in-one UI open "Lean OW Web CLI".

```
cd FaaS-VIM-Exercises/exercise6/
```


```bash
../tools/simulator2 -a 0 -i 127.0.0.1 -r $PORT1 -s $PORT2 -c $PORT3 -f ~/_SpaceWars_Player1_Reconstruction_0.pay -n 500
```

You should see similar output

```
TRANSCODING SIMULATION START
Number of frames in pay file: 500
OUTGOING CONNECTION ESTABLISHED (0 ms to connect)
INGOING CONNECTION ESTABLISHED (1 ms to connect)
STREAMED FRAME: 1 --> 335 KB
STREAMED FRAME: 2 --> 335 KB
...
```

### View monitor dashboard


During the streaming you should notice an increase in network metrics as well as cpu and memory.

At all-in-one UI open "Service monitoring"

Select SDK dashboard
  
