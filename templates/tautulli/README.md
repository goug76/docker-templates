# 🏡 Goug's HomeLab Docker Templates

Welcome to **Goug's HomeLab** — a growing collection of Docker Compose templates for apps I use or test in my HomeLab. These templates are built to help you get up and running quickly with no bloated configs or mysterious dependencies.

Each app folder includes:

* `docker-compose.yml` — core container setup
* `.env` — customizable environment variables
* `README.md` — you're reading it!
* Sample config files (if needed)

Explore more at [goug76/docker-templates](https://github.com/goug76/docker-templates).

---

## 📦 Tautulli

[Tautulli](https://tautulli.com/) is a monitoring and analytics tool for **Plex Media Server**. It tracks who’s watching what, when, and for how long. You’ll get rich playback stats, detailed history, customizable notifications, and a web UI to visualize everything.

Perfect for multi-user Plex setups and self-hosted streaming nerds.

---

## 🧰 Features

* Real-time monitoring of Plex streams
* Playback history, stats, and user tracking
* Email, Discord, Telegram notifications
* Graphs, charts, and dashboards galore
* Optional scripts for custom events/actions

---

## 🚀 Getting Started

### 🐳 Docker Compose

```yaml
---
services:
  tautulli:
    container_name: tautulli
    image: lscr.io/linuxserver/tautulli:latest
    read_only: true
    restart: unless-stopped
    ports:
      - 8181:8181
    environment:
      - PUID=${PUID}
      - PGID=${PGID}
      - TZ=${TZ}
    volumes:
      - $DOCKERDIR/tautulli/config:/config
    networks:
      - media
```

> Using `network_mode` set to `host` to avoid using ports

```yaml
---
services:
  tautulli:
    container_name: tautulli
    image: lscr.io/linuxserver/tautulli:latest
    restart: unless-stopped
    network_mode: host
    environment:
      - PUID=${PUID}
      - PGID=${PGID}
      - TZ=${TZ}
    volumes:
      - $DOCKERDIR/tautulli/config:/config
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

* `/config` holds your database, settings, and logs
* Tautulli connects to your Plex server using its IP or hostname and your Plex Token
* All setup is done via the web UI after first launch
* Alerts can be configured for playback start/stop, buffering, IP bans, etc.

---

## 🛠️ Tips & Customization

* Enable **Discord notifications** for new stream alerts or bandwidth abuse
* Use the **newsletter feature** to email recently added media
* Create **custom scripts** to auto-ban users, restart services, or post to APIs
* Combine with **Grafana** if you want to push Tautulli data into dashboards

---

## 🧯 Troubleshooting Notes

* 🚫 **Not seeing playback stats?** Check that the Plex token is valid and the IP is reachable
* 🔄 **Plex library not syncing?** Rescan manually under settings > Plex
* 📉 **No graphs/data showing?** Make sure you're logged in and that the Plex server is configured
* 🔒 **Access not protected?** Use a reverse proxy + Authentik for external lockdown

---

## 📚 More Info

* [Tautulli Official Site](https://tautulli.com/)
* [LinuxServer Image Docs](https://docs.linuxserver.io/images/docker-tautulli)
* [Setup Guide](https://github.com/Tautulli/Tautulli/wiki)
* [Authentik Configuration Doc](https://docs.goauthentik.io/integrations/services/tautulli/)

---

## 🧼 Cleanup

```bash
docker-compose down -v
```
