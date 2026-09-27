# AXON SEC
Network threat detector — early beta

## What it does
Layer 3/4 network threat detection.
Designed for scan-heavy environments.

Detects well:
- RDP scanning (port 3389)
- VNC scanning (port 5910)
- Masscan/ZMap (SEW TCP flag)
- Mirai bots (port 23)
- SYN flood / port scanning

Does NOT detect:
- HTTP layer attacks (DoS Hulk, Slowloris)
- Application layer exploits
- Payload-based attacks

## Honest metrics
- Tested on own VPS (Hetzner):
  303 IPs blocked automatically
  in 24 hours of real traffic
- F1=83.5% on NSL-KDD dataset
- Not validated on enterprise networks yet

## Try it
Upload a CSV to https://axonsec.net
(free, no account needed)

## CSV format
src_ip,dst_port,bytes,flow_rate,duracion,paquetes,hora

## Status
Early beta. L3/L4 domain only.
Looking for feedback from sysadmins
with exposed servers.

## Contact
alberto@axonsec.net
