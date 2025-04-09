# 🏡 Goug's HomeLab Docker Templates

Welcome to **Goug's HomeLab** — a growing collection of Docker Compose templates for apps I use or test in my HomeLab. These templates are built to help you get up and running quickly with no bloated configs or mysterious dependencies.

Each app folder includes:

* `docker-compose.yml` — core container setup
* `.env` — customizable environment variables
* `README.md` — you're reading it!
* Sample config files (if needed)

Explore more at [goug76/docker-templates](https://github.com/goug76/docker-templates).


---

## 📦 Lidarr

[Lidarr](https://lidarr.audio/) is a music collection manager that automates the process of finding, downloading, organizing, and updating your music library. It works similarly to Sonarr and Radarr, but is built specifically for managing artists and albums using metadata from sources like MusicBrainz.


---

## 🧰 Features

* Automatically monitor and download new albums by tracked artists
* Integration with popular download clients (NZB and torrent)
* Post-processing and renaming
* Metadata fetching from MusicBrainz and other sources
* Works well with Jellyfin, Plex, or any local music player


---

## 🚀 Getting Started

### 🐳 Docker Compose

```yaml
---
services:
  lidarr:
    container_name: lidarr
    image: lscr.io/linuxserver/lidarr:latest
    restart: unless-stopped
    ports:
      - 8686:8686
    environment:
      - PUID=${PUID}
      - PGID=${PGID}
      - TZ=${TZ}
    volumes:
      - $DOCKERDIR/appdata/lidarr/config:/config
      - $MEDIADIR:/multimedia
      - $DOWNLOADDIR:/downloads
    networks:
      - media
```

Using `network_mode` set to `host` to avoid using ports

```yaml
---
services:
  lidarr:
    container_name: lidarr
    image: lscr.io/linuxserver/lidarr:latest
    restart: unless-stopped
    network_mode: host
    environment:
      - PUID=${PUID}
      - PGID=${PGID}
      - TZ=${TZ}
    volumes:
      - $DOCKERDIR/lidarr/config:/config
      - $MEDIADIR:/multimedia
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
| `MEDIADIR` | Media Location | `/mnt/media` |
| `DOWNLOADDIR` | Download Location | `/mnt/downloads` |
| `TZ` | Timezone | `America/New_York` |


---

## 🧪 Sample Configuration

* `/config` stores Lidarr's database, settings, and logs
* `/downloads` is the location where your download client places new files
* `/multimedia` should point to your organized music library
* Post-processing is handled through Lidarr’s UI under Settings > Media Management


---

## 🛠️ Tips & Customization

* Connect Lidarr with **qBittorrent**, **Deluge**, or **NZBGet** for downloads
* Use **Folder Rename** options to organize by artist/album
* Add indexers via Jackett or Prowlarr for better search results
* Schedule library rescans to keep metadata fresh and synced


---

## 🧯 Troubleshooting Notes

* 🔄 **Metadata not updating?** Force a rescan from the Artist menu
* 📁 **Files not moving?** Double-check permissions and path mappings
* 🚫 **App not starting?** Make sure config volume is writable by the container user
* 🌐 **Can't connect to download client?** Check hostnames and port mappings


---

## 📚 More Info

* [Lidarr Project Site](https://lidarr.audio/)
* [LinuxServer.io Image Docs](https://docs.linuxserver.io/images/docker-lidarr)
* [Authentik Configuration Doc](https://docs.goauthentik.io/integrations/services/sonarr/) (for Sonarr but same process)
* [Prowlarr (for indexers)](https://github.com/Prowlarr/Prowlarr)


---

## 🧼 Cleanup

```bash
docker-compose down -v
```
