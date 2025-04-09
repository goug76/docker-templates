# 🏡 Goug's HomeLab Docker Templates

Welcome to **Goug's HomeLab** — a growing collection of Docker Compose templates for apps I use or test in my HomeLab. These templates are built to help you get up and running quickly with no bloated configs or mysterious dependencies.

Each app folder includes:

* `docker-compose.yml` — core container setup
* `.env` — customizable environment variables
* `README.md` — you're reading it!
* Sample config files (if needed)

Explore more at [goug76/docker-templates](https://github.com/goug76/docker-templates).

---

## 📦 Plex Media Server

[Plex](https://www.plex.tv/) is a powerful and user-friendly media server that organizes and streams your personal collection of movies, TV, music, photos, and more. With apps for nearly every platform, it's the ultimate media companion.

This setup uses `host` networking for local discovery and hardware acceleration support, which is strongly recommended for best performance.

---

## 🧰 Features

* Organize and stream your entire media library
* DLNA support, local discovery, and remote access
* Transcoding and direct play options
* Metadata fetching, trailers, subtitles, and more
* Clients available for Roku, Android, iOS, Fire TV, and Web

---

## 🚀 Getting Started

### 🐳 Docker Compose

```yaml
---
services:
  plex:
    container_name: plex
    image: lscr.io/linuxserver/plex:latest
    restart: unless-stopped
    network_mode: host
    environment:
      - PUID=${PUID}
      - PGID=${PGID}
      - TZ=${TZ}
      - VERSION=docker
    volumes:
      - $DOCKERDIR/plex:/config
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

---

## 🧪 Sample Configuration

* `/config` contains the entire Plex database and settings
* `/multimedia` is your mounted media library — organize however you prefer
* First-time setup runs through the Plex web wizard at `http://<host>:32400/web`

---

## 🛠️ Tips & Customization

* Enable **hardware transcoding** (Intel QuickSync or NVIDIA) via additional `devices:` section
* Use **Tautulli** for analytics and playback tracking
* Customize your libraries with posters, themes, and agents
* Enable remote access in settings (be cautious with NAT/firewall config)

---

## 🧯 Troubleshooting Notes

* 🌍 **Remote access not working?** Manually forward port 32400 or use Plex Relay
* 🔄 **Library not scanning?** Confirm folder permissions and path mappings
* ❗ **Playback errors?** Check transcoder temp path and system resources
* 🧠 **Container updates breaking things?** Back up your `/config` folder first

---

## 📚 More Info

* [Plex.tv](https://www.plex.tv/)
* [LinuxServer Plex Docs](https://docs.linuxserver.io/images/docker-plex)
* [Tautulli (for analytics)](https://tautulli.com/)
* [Plex Hardware Transcoding Setup](https://support.plex.tv/articles/115002178853)

---

## 🧼 Cleanup

```bash
docker-compose down -v
```
