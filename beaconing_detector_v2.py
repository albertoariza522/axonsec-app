from collections import defaultdict, deque
from datetime import datetime, timedelta
import numpy as np

class BeaconingDetector:
    def __init__(self, min_muestras=10, cv_threshold=0.15,
                 iat_min=0.1, iat_max=3600.0, expiry_segundos=600.0):
        self.min_muestras = min_muestras
        self.cv_threshold = cv_threshold
        self.iat_min = iat_min
        self.iat_max = iat_max
        self.expiry_segundos = expiry_segundos
        self.iat_history = defaultdict(lambda: deque(maxlen=50))
        self.last_seen = {}
        self.beacons = {}
        self._iat_aceptados = defaultdict(int)
        self._iat_filtrados = defaultdict(int)

    def _expirar_beacons(self, ahora):
        expiradas = [ip for ip, d in self.beacons.items()
                     if (ahora - d["ultima_actividad"]).total_seconds() > self.expiry_segundos]
        for ip in expiradas:
            del self.beacons[ip]

    def analizar(self, ip, timestamp):
        self._expirar_beacons(timestamp)
        if ip in self.last_seen:
            delta = (timestamp - self.last_seen[ip]).total_seconds()
            if delta < 0:
                return {"ip": ip, "estado": "OUT_OF_ORDER", "cv": None, "muestras": len(self.iat_history[ip])}
            if delta == 0:
                return {"ip": ip, "estado": "DUPLICATE", "cv": None, "muestras": len(self.iat_history[ip])}
            if self.iat_min < delta < self.iat_max:
                self.iat_history[ip].append(delta)
                self._iat_aceptados[ip] += 1
            else:
                self._iat_filtrados[ip] += 1
        self.last_seen[ip] = timestamp
        iats = list(self.iat_history[ip])
        n = len(iats)
        if n < self.min_muestras:
            return {"ip": ip, "estado": "OBSERVANDO", "cv": 1.0, "muestras": n,
                    "iat_aceptados": self._iat_aceptados[ip], "iat_filtrados": self._iat_filtrados[ip]}
        media = np.mean(iats)
        cv = np.std(iats) / max(media, 0.001)
        es_beacon = cv < self.cv_threshold
        if es_beacon:
            self.beacons[ip] = {"periodo_seg": round(media, 2), "cv": round(cv, 4), "ultima_actividad": timestamp}
        elif ip in self.beacons:
            del self.beacons[ip]
        return {"ip": ip, "estado": "BEACON" if es_beacon else "NORMAL",
                "periodo_seg": round(media, 2), "cv": round(cv, 4), "muestras": n,
                "iat_aceptados": self._iat_aceptados[ip], "iat_filtrados": self._iat_filtrados[ip]}

    def get_beacons(self): return dict(self.beacons)
    def get_stats_filtrado(self, ip):
        total = self._iat_aceptados[ip] + self._iat_filtrados[ip]
        return {"ip": ip, "aceptados": self._iat_aceptados[ip], "filtrados": self._iat_filtrados[ip],
                "ratio_aceptados": round(self._iat_aceptados[ip] / total, 3) if total else 0.0}

    def reset_ip(self, ip):
        self.iat_history.pop(ip, None)
        self.last_seen.pop(ip, None)
        self.beacons.pop(ip, None)
        self._iat_aceptados.pop(ip, None)
        self._iat_filtrados.pop(ip, None)
