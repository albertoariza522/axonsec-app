# AXON SEC v4.0
Network Detection & Response — ultraligero

## Qué es
Motor de detección perimetral L3/L4
con análisis comportamental temporal.

NDR ultraligero que funciona en un VPS
de 3.29€/mes con capacidades equivalentes
a soluciones empresariales de miles de euros.

## Qué detecta

### L3/L4 — verificado en producción:
- RDP scanning (puerto 3389)
- VNC scanning (puerto 5910)
- Masscan/ZMap (SEW TCP flag)
- Mirai botnets (puerto 23)
- SYN flood coordinado

### Análisis comportamental temporal:
- Beaconing C2 — malware comunicando
- Slow Scan APT — reconocimiento sigiloso
- Clasificación BOTNET/APT/SCANNER/HUMANO
- Autenticación inteligente (HUMANO vs BOT)

## Lo que NO detecta
- Ataques HTTP/L7 (use un WAF)
- SQL injection, XSS (use un WAF)
- Contenido de paquetes cifrados

## Métricas reales — servidor Hetzner
- 1.077.232 paquetes analizados
- 15.258 IPs bloqueadas y clasificadas
- 43 rutas de ataque mapeadas
- 1 Beacon C2 real detectado
- 16 Slow Scans APT reales

## Pruébalo
App web: https://axonsec.net (gratis)
Docs: github.com/albertoariza522/axonsec-app

## Busco
Sysadmins con servidores expuestos
para validación externa real.
Contacto: alberto@axonsec.net
