# AXON SEC
Network threat detector — early beta

## What it detects
Tested on a real VPS (Hetzner):
- RDP scanning (port 3389)
- VNC scanning (port 5910)
- Masscan/ZMap (SEW flag)
- Mirai bots (port 23)

## Honest metrics
- F1=83.5% on NSL-KDD dataset
- F1=53% on external CICIDS2017 data
- False positive rate is high on external networks
- Works best on scan-heavy traffic

## Try it
Upload a CSV to https://axonsec.net
(free, no account needed)

## CSV format
src_ip,dst_port,bytes,flow_rate,duracion,paquetes,hora
185.220.101.5,3389,0,1.0,0.001,1,14

## Status
Early beta. Not production ready.
Looking for feedback on real networks.

## Contact
alberto@axonsec.net
