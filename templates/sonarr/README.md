# 🏡 Goug's HomeLab Docker Templates

Welcome to **Goug's HomeLab** — a growing collection of Docker Compose templates for apps I use or test in my HomeLab. These templates are built to help you get up and running quickly with no bloated configs or mysterious dependencies.

Each app folder includes:

* `docker-compose.yml` — core container setup
* `.env` — customizable environment variables
* `README.md` — you're reading it!
* Sample config files (if needed)

Explore more at [goug76/docker-templates](https://github.com/goug76/docker-templates).

---

## 📦 Sonarr

[Sonarr](https://sonarr.tv/) is a PVR (Personal Video Recorder) for **TV shows**. It monitors your favorite series, downloads new episodes from your configured indexers, and manages the files — renaming, sorting, and keeping your library fresh.

It works beautifully alongside **Prowlarr**, **qBittorrent**, **Radarr**, and **Jellyfin** or **Plex**.

---

## 🧰 Features

* Auto-search and auto-download of TV episodes
* Multiple quality profiles with preferred words and tags
* Full season and backlog search
* Integration with torrent and Usenet clients
* Metadata and artwork fetching for Plex/Jellyfin
* Manual or automatic importing

---

## 🚀 Getting Started

### 🐳 Docker Compose

```yaml
---
services:
  sonarr:
    container_name: sonarr
    image: lscr.io/linuxserver/sonarr:latest
    restart: unless-stopped
    ports:
      - 8989:8989 # Sonarr
    environment:
      - PUID=${PUID}
      - PGID=${PGID}
      - TZ=${TZ}
    volumes:
      - $DOCKERDIR/sonarr/data:/config
      - $MEDIADIR:/multimedia
      - $DOWNLOADDIR:/downloads
    networks:
      - media
```

> Using `network_mode` set to `host` to avoid using ports

```yaml
---
services:
  radarr:
    container_name: radarr
    image: lscr.io/linuxserver/radarr:latest
    restart: unless-stopped
    network_mode: host
    environment:
      - PUID=${PUID}
      - PGID=${PGID}
      - TZ=${TZ}
    volumes:
      - $DOCKERDIR/radarr/data:/config
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

* `/config` holds Sonarr’s settings and DB
* `/multimedia` should point to your organized TV show library
* `/downloads` is the path your torrent/NZB client uses for completed downloads
* Use the UI to connect download clients, Prowlarr, and define quality profiles

---

## 🛠️ Tips & Customization

* Add custom **tags** to control download behavior (e.g. preferred formats)
* Set up **Import Lists** (formerly RSS) for auto-adding upcoming shows
* Enable **Episode Title Renaming** for clean filenames
* Use **health checks** to alert for missing root folders or failed imports

---

## 🧯 Troubleshooting Notes

* ⚠️ **Nothing downloading?** Check indexers (via Prowlarr) and download client integration
* 🔁 **Files not importing?** Double-check folder paths, permissions, and category mappings
* 📦 **Missing artwork or metadata?** Re-scan the series folder and refresh metadata
* 🔒 **Reverse proxy issues?** Validate forwarded headers and port accessibility

---

## 📚 More Info

* [Sonarr Official Site](https://sonarr.tv/)
* [LinuxServer Docs](https://docs.linuxserver.io/images/docker-sonarr)
* [Arr Stack Wiki](https://wiki.servarr.com/)
* [Authentik Configuration Doc](https://docs.goauthentik.io/integrations/services/sonarr/) (for Sonarr but same process)
* [Prowlarr (for indexers)](https://github.com/Prowlarr/Prowlarr)

---

## 🧼 Cleanup

```bash
docker-compose down -v
```
