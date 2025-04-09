# 🏡 Goug's HomeLab Docker Templates

Welcome to **Goug's HomeLab** — a growing collection of Docker Compose templates for apps I use or test in my HomeLab. These templates are built to help you get up and running quickly with no bloated configs or mysterious dependencies.

Each app folder includes:

* `docker-compose.yml` — core container setup
* `.env` — customizable environment variables
* `README.md` — you're reading it!
* Sample config files (if needed)

Explore more at [goug76/docker-templates](https://github.com/goug76/docker-templates).

---

## 📦 Radarr

[Radarr](https://radarr.video/) is an independent fork of Sonarr built to manage your **movie collection**. It automatically finds, downloads, renames, and organizes movies from your favorite indexers — all in a clean web UI with deep customization.

If you’ve got Plex or Jellyfin running, this is your automated backend to keep your movie shelves full.

---

## 🧰 Features

* Automatic movie discovery and downloading
* Integrates with Prowlarr, qBittorrent, Deluge, NZBGet, etc.
* Custom quality profiles, tags, and filters
* Metadata support for Plex and Jellyfin
* Post-processing with rename/move/cleanup rules

---

## 🚀 Getting Started

### 🐳 Docker Compose

```yaml
---
services:
  radarr:
    container_name: radarr
    image: lscr.io/linuxserver/radarr:latest
    restart: unless-stopped
    ports:
      - 7878:7878 # Radarr
    environment:
      - PUID=${PUID}
      - PGID=${PGID}
      - TZ=${TZ}
    volumes:
      - $DOCKERDIR/radarr/data:/config
      - $MEDIADIR:/multimedia
      - $DOWNLOADDIR:/downloads
    networks:
      - media
```

> ⚠️ Be sure to copy and edit the `.env` file included in this directory.

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

* Radarr config and database are stored in `$DOCKERDIR/radarr/data`
* `/multimedia` should point to your main movie library
* `/downloads` should be where your download client places files (for importing)
* Add your download client and indexers under Settings → Download Clients & Indexers

---

## 🛠️ Tips & Customization

* Create **custom quality profiles** to filter 4K, HDR, etc.
* Use **tags and restrictions** to split by resolution, language, or release type
* Use with Tautulli to track viewing data across requests
* Sync with Plex or Jellyfin for metadata refreshes after post-processing

---

## 🧯 Troubleshooting Notes

* 🚫 **No files importing?** Check download client paths and completed download settings
* 🔄 **Nothing downloading?** Confirm indexers and client connectivity
* 📁 **Permissions error?** Ensure Radarr user can access both `/downloads` and `/multimedia`
* 🔒 **SSO not working?** Make sure your reverse proxy is forwarding the correct headers

---

## 📚 More Info

* [Radarr Official Site](https://radarr.video/)
* [LinuxServer Image Docs](https://docs.linuxserver.io/images/docker-radarr)
* [Arr Stack Setup Guide](https://wiki.servarr.com/)
* [Authentik Configuration Doc](https://docs.goauthentik.io/integrations/services/sonarr/) (for Sonarr but same process)
* [Prowlarr (for indexers)](https://github.com/Prowlarr/Prowlarr)

---

## 🧼 Cleanup

```bash
docker-compose down -v
```
