# 🏡 Goug's HomeLab Docker Templates

Welcome to **Goug's HomeLab** — a growing collection of Docker Compose templates for apps I use or test in my HomeLab. These templates are built to help you get up and running quickly with no bloated configs or mysterious dependencies.

Each app folder includes:

* `docker-compose.yml` — core container setup
* `.env` — customizable environment variables
* `README.md` — you're reading it!
* Sample config files (if needed)

Explore more at [goug76/docker-templates](https://github.com/goug76/docker-templates).

---

## 📦 Prowlarr

[Prowlarr](https://wiki.servarr.com/prowlarr) is a modern indexer manager and proxy built for the *arr* ecosystem. It centralizes your Usenet and torrent indexers into a single UI and integrates seamlessly with Sonarr, Radarr, Lidarr, and others — handling all your indexer headaches in one place.

---

## 🧰 Features

* Manages torrent and Usenet indexers across multiple \*arr apps
* Built-in proxy for privacy and control
* Supports hundreds of indexers via Jackett-compatible APIs
* Unified interface for configuring indexer limits, caps, and categories
* Native integration with Sonarr, Radarr, Lidarr, Readarr, and more

---

## 🚀 Getting Started

### 🐳 Docker Compose

```yaml
---
services:
  prowlarr:
    container_name: prowlarr
    image: lscr.io/linuxserver/prowlarr:latest
    restart: unless-stopped
    ports:
      - 9696:9696 # Prowlarr
    environment:
      - PUID=${PUID}
      - PGID=${PGID}
      - TZ=${TZ}
    volumes:
      - $DOCKERDIR/prowlarr/data:/config
    networks:
      - media
```

Using `network_mode` set to `host` to avoid using ports

```yaml
---
services:
  prowlarr:
    container_name: prowlarr
    image: lscr.io/linuxserver/prowlarr:latest
    restart: unless-stopped
    network_mode: host
    environment:
      - PUID=${PUID}
      - PGID=${PGID}
      - TZ=${TZ}
    volumes:
      - $DOCKERDIR/prowlarr/data:/config
```

> ⚠️ Be sure to copy and edit the `.env` file included in this directory.

---

## ⚙️ Environment Variables

| Variable | Description | Example |
|----|----|----|
| `PUID` | User ID for file ownership | `1000` |
| `PGID` | Group ID for file ownership | `1000` |
| `DOCKERDIR` | Docker file Location | `/home/user/docker` |
| `TZ` | Timezone | `America/New_York` |

---

## 🧪 Sample Configuration

* Config is stored in `/config`, mapped to `$DOCKERDIR/prowlarr/data`
* First run will walk you through indexer setup
* After connecting your \*arr apps, you can push indexers to them automatically

---

## 🛠️ Tips & Customization

* Use tags to organize indexers by content type
* Prowlarr supports **rate limiting**, **indexer rotation**, and **caps** — use these for stability
* You can enable logs and debugging under Settings → General
* Run it alongside your other \*arr stack in a shared `media` network

---

## 🧯 Troubleshooting Notes

* 🔒 **Login screen vulnerable?** Use Authentik or basic auth to protect access
* 🧱 **Can't connect to indexers?** Check category mappings and API keys
* 🔄 **Indexers not syncing with Sonarr/Radarr?** Use the "Test" button, then re-push indexers
* 🚫 **Prowlarr won't start?** Check for leftover database locks in `/config`

---

## 📚 More Info

* [Prowlarr Wiki](https://wiki.servarr.com/prowlarr)
* [GitHub Repo](https://github.com/Prowlarr/Prowlarr)
* [LinuxServer Image Docs](https://docs.linuxserver.io/images/docker-prowlarr)
* [Authentik Configuration Doc](https://docs.goauthentik.io/integrations/services/sonarr/) (for Sonarr but same process)

---

## 🧼 Cleanup

```bash
docker-compose down -v
```
