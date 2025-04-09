# 🏡 Goug's HomeLab Docker Templates

Welcome to **Goug's HomeLab** — a growing collection of Docker Compose templates for apps I use or test in my HomeLab. These templates are built to help you get up and running quickly with no bloated configs or mysterious dependencies.

Each app folder includes:

* `docker-compose.yml` — core container setup
* `.env` — customizable environment variables
* `README.md` — you're reading it!
* Sample config files (if needed)

Explore more at [goug76/docker-templates](https://github.com/goug76/docker-templates).


---

## 📦 Jellyfin

[Jellyfin](https://jellyfin.org/) is a free and open-source media server, perfect for organizing and streaming your personal collection of movies, shows, music, and more. It’s a full-featured Plex alternative with no subscriptions, no tracking, and no restrictions.

This containerized setup uses **host networking** for maximum compatibility with DLNA devices and native discovery apps.


---

## 🧰 Features

* Streams movies, TV, music, and photos to virtually any device
* Native apps for iOS, Android, Fire TV, Roku, and more
* DLNA, Chromecast, and hardware transcoding support
* User accounts, watch history, and parental controls
* Beautiful, fast web interface


---

## 🚀 Getting Started

### 🐳 Docker Compose

```yaml
---
services:
  jellyfin:
    container_name: jellyfin
    image: lscr.io/linuxserver/jellyfin:latest
    restart: unless-stopped
    network_mode: host
    environment:
      - PUID=${PUID}
      - PGID=${PGID}
      - TZ=${TZ}
      - JELLYFIN_PublishedServerUrl=http://192.168.1.66 #optional
    volumes:
      - $DOCKERDIR/jellyfin:/config
      - $MEDIADIR:/multimedia
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
| `TZ` | Timezone | `America/New_York` |
| `JELLYFIN_PublishedServerUrl` | Public IP or hostname for external clients | `http://192.168.1.66` |


---

## 🧪 Sample Configuration

* Configuration and metadata is stored in `$DOCKERDIR/jellyfin:/config`
* Media libraries should be mounted to `/multimedia` (or `/media`, your choice)
* The first launch runs a setup wizard via browser at `http://<host>:8096`


---

## 🛠️ Tips & Customization

* Mount GPU devices and configure for **hardware transcoding** if needed
* Use Jellyfin's **Scheduled Tasks** to refresh metadata and images
* Sync subtitles automatically or link to external subtitle folders
* Use [Jellyseerr](https://github.com/Fallenbagel/jellyseerr) for request management


---

## 🧯 Troubleshooting Notes

* 🧪 **Can't reach the web UI?** Try accessing on port `8096` or check `JELLYFIN_PublishedServerUrl`
* 🎞 **Buffering or slow playback?** Consider enabling transcoding and reviewing system load
* 🔒 **Users can't log in?** Verify Jellyfin internal permissions and group roles
* 🌐 **Network discovery not working?** Must use `network_mode: host` for DLNA, etc.


---

## 📚 More Info

* [Jellyfin Official Site](https://jellyfin.org/)
* [LinuxServer Jellyfin Docs](https://docs.linuxserver.io/images/docker-jellyfin)
* [Jellyfin GitHub](https://github.com/jellyfin/jellyfin)
* [Hardware Transcoding Guide](https://jellyfin.org/docs/general/administration/hardware-acceleration/)
* [Authentik Configuration Doc](https://docs.goauthentik.io/integrations/services/jellyfin/)


---

## 🧼 Cleanup

```bash
docker-compose down -v
```
