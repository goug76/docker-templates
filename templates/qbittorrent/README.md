# 🏡 Goug's HomeLab Docker Templates

Welcome to **Goug's HomeLab** — a growing collection of Docker Compose templates for apps I use or test in my HomeLab. These templates are built to help you get up and running quickly with no bloated configs or mysterious dependencies.

Each app folder includes:

* `docker-compose.yml` — core container setup
* `.env` — customizable environment variables
* `README.md` — you're reading it!
* Sample config files (if needed)

Explore more at [goug76/docker-templates](https://github.com/goug76/docker-templates).

---

## 📦 qBittorrent

[qBittorrent](https://www.qbittorrent.org/) is a free, open-source BitTorrent client with a slick web UI and native category/tag support — making it an ideal download client for automation setups like Sonarr, Radarr, Lidarr, and more.

This container setup is built with **PUID/PGID** support, web UI on port `8080`, and direct port mappings for torrenting.

---

## 🧰 Features

* Modern web UI (accessible via port `8080`)
* Supports labels, categories, and multiple torrents
* Works seamlessly with Sonarr/Radarr/Lidarr
* RSS feed support, IP filtering, and scheduler
* Lightweight and resource-friendly

---

## 🚀 Getting Started

### 🐳 Docker Compose

```yaml
---
services:
  qbittorrent:
    container_name: qbittorrent
    image: lscr.io/linuxserver/qbittorrent:latest
    restart: unless-stopped
    ports:
      - 8080:8080
      - 6882:6881
      - 6882:6881/udp
    environment:
      - PUID=${PUID}
      - PGID=${PGID}
      - TZ=${TZ}
      - WEBUI_PORT=8080
      - TORRENTING_PORT=6881
    volumes:
      - $DOCKERDIR/qbittorrent:/config
      - $DOWNLOADDIR:/downloads
    networks:
      - media
```

> ⚠️ Be sure to copy and edit the `.env` file included in this directory.

Using `network_mode` set to `host` to avoid using ports

```yaml
---
services:
  qbittorrent:
    container_name: qbittorrent
    image: lscr.io/linuxserver/qbittorrent:latest
    restart: unless-stopped
    network_mode: host
    environment:
      - PUID=${PUID}
      - PGID=${PGID}
      - TZ=${TZ}
      - WEBUI_PORT=8080
      - TORRENTING_PORT=6881
    volumes:
      - $DOCKERDIR/qbittorrent:/config
      - $DOWNLOADDIR:/downloads
```

---

## ⚙️ Environment Variables

| Variable | Description | Example |
|----|----|----|
| `PUID` | User ID for file ownership | `1000` |
| `PGID` | Group ID for file ownership | `1000` |
| `DOCKERDIR` | Docker file Location | `/home/user/docker` |
| `DOWNLOADDIR` | Download Location | `/mnt/downloads` |
| `TZ` | Timezone | `America/New_York` |
| `WEBUI_PORT` | Port for the qBittorrent web interface | `8080` |
| `TORRENTING_PORT` | Incoming port for torrents | `6881` |

---

## 🧪 Sample Configuration

* All config data is stored in `$DOCKERDIR/qbittorrent`
* Downloaded files go into `$DOWNLOADDIR`
* You can set different folders and categories inside the web UI for Sonarr/Radarr compatibility
* Don't forget to update download client settings inside \*arr apps with matching ports and credentials

---

## 🛠️ Tips & Customization

* Change UI credentials under **Web UI > Authentication**
* Limit speeds and seed ratios with the built-in scheduler
* Enable `IP filtering` to block known bad actors
* Adjust connection limits for seed-heavy libraries

---

## 🧯 Troubleshooting Notes

* 🔄 **Can't access UI?** Make sure port `8080` isn’t already in use
* 🚫 **Slow download speeds?** Check port forwarding, firewall rules, or ISP restrictions
* 🔁 **Arr apps not pushing?** Confirm client is added correctly in their download settings
* 🧱 **Settings not saving?** Confirm correct permissions on the `/config` volume

---

## 📚 More Info

* [qBittorrent Website](https://www.qbittorrent.org/)
* [LinuxServer.io Image Docs](https://docs.linuxserver.io/images/docker-qbittorrent)
* [Arr Wiki for qBittorrent Setup](https://wiki.servarr.com/download-clients/qbittorrent)

---

## 🧼 Cleanup

```bash
docker-compose down -v
```
