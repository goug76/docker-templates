# 🏡 Goug's HomeLab Docker Templates

Welcome to **Goug's HomeLab** — a growing collection of Docker Compose templates for apps I use or test in my HomeLab. These templates are built to help you get up and running quickly with no bloated configs or mysterious dependencies.

Each app folder includes:

* `docker-compose.yml` — core container setup
* `.env` — customizable environment variables
* `README.md` — you're reading it!
* Sample config files (if needed)

Explore more at [goug76/docker-templates](https://github.com/goug76/docker-templates).


---

## 📦 Deluge

[Deluge](https://deluge-torrent.org/) is a lightweight, full-featured BitTorrent client that runs headless in Docker with a web UI. It’s great for automated torrenting via Sonarr, Radarr, or manual downloads. The container is powered by [linuxserver.io](https://docs.linuxserver.io/images/docker-deluge), with all the homelab-friendly extras.


---

## 🧰 Features

* Simple web UI for managing torrents
* Supports labels, scheduling, and plugins
* Web, daemon, and console modes
* Optional Deluge thin client support via port `58846`
* PUID/PGID mapping for secure file permissions


---

## 🚀 Getting Started

### 🐳 Docker Compose

```yaml
---
services:
  deluge:
    container_name: deluge
    image: lscr.io/linuxserver/deluge:latest
    restart: unless-stopped
    ports:
      - 8112:8112
      - 6881:6881
      - 6881:6881/udp
      - 58846:58846 #optional
    environment:
      - PUID=${PUID}
      - PGID=${PGID}
      - TZ=${TZ}
      - DELUGE_LOGLEVEL=error #optional
    volumes:
      - $DOCKERDIR/deluge/config:/config
      - $DOWNLOADDIR:/downloads
    networks:
      - media
```

Using `network_mode` set to `host` to avoid using ports

```yaml
---
services:
  deluge:
    container_name: deluge
    image: lscr.io/linuxserver/deluge:latest
    restart: unless-stopped
    network_mode: host
    environment:
      - PUID=${PUID}
      - PGID=${PGID}
      - TZ=${TZ}
      - DELUGE_LOGLEVEL=error #optional
    volumes:
      - $DOCKERDIR/deluge/config:/config
      - $DOWNLOADDIR:/downloads
```

> ⚠️ Be sure to copy and edit the `.env` file included in this directory.


---

## ⚙️ Environment Variables

| Variable | Description | Example |
|----|----|----|
| `PUID` | User ID for file ownership | `1000` |
| `PGID` | Group ID for file ownership | `1000` |
| `DOCKERDIR` | Docker file Location | `/home/user/docker` |
| `DOWNLOADDIR` | Download Location | `/mnt/downloads` |
| `TZ` | Timezone | `America/New_York` |


---

## 🧪 Sample Configuration

* All configuration data is stored under /config and will be generated on first run.
* Web UI is available at `http://<host>:8112` — default password is `deluge`
* Download path is bound to `/downloads`, set by `$DOWNLOADDIR` in `.env`


---

## 🛠️ Tips & Customization

* Change the default web password after first login
* Enable plugins like Extractor and Label via the web UI
* Set up a VPN Proxy to secure your connections
* Use with Sonarr, Radarr, Lidarr, or Medusa for automated downloads


---

## 🧯 Troubleshooting Notes

* 🧪 **Can't access UI?** Check that port 8112 is open and no firewall is blocking it
* 🔐 **Can't change password?** Delete web.conf in /config to reset
* 🧱 **Files not saving?** Check volume permissions for $DOWNLOADDIR
* 🐌 **Slow speeds?** Forward ports 6881 TCP/UDP if behind a router with NAT


---

## 📚 More Info

* [Deluge Project](https://deluge-torrent.org/)
* [linuxserver/deluge Docs](https://docs.linuxserver.io/images/docker-deluge)
* [Authentik Proxy Guide](https://goauthentik.io/docs/providers/proxy/)


---

## 🧼 Cleanup

```bash
docker-compose down -v
```


