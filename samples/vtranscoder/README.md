

```
wsk -i action create /guest/exercises/vtranscoder --docker docker5gmedia/transcoder_2_8_4
```

```bash
curl -X POST http://127.0.0.1:5002/conf/sky_balls/vtranscoder_vnfd/1 -H 'content-type: application/json' -d '{
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

```
curl 127.0.0.1:5002/osm/sky_balls | jq .vnfs[0].vim_info.service.service_ports
```

```
../../tools/simulator2 -a 0 -i 172.15.0.100  -r 30145 -s 30051 -c 32032 -f ~/_SpaceWars_Player1_Reconstruction_0.pay -n 500
```
