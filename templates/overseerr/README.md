# 🏡 Goug's HomeLab Docker Templates

Welcome to **Goug's HomeLab** — a growing collection of Docker Compose templates for apps I use or test in my HomeLab. These templates are built to help you get up and running quickly with no bloated configs or mysterious dependencies.

Each app folder includes:

* `docker-compose.yml` — core container setup
* `.env` — customizable environment variables
* `README.md` — you're reading it!
* Sample config files (if needed)

Explore more at [goug76/docker-templates](https://github.com/goug76/docker-templates).


---

## 📦 Overseerr

[Overseerr](https://overseerr.dev/) is a beautiful web app for managing media requests for your Plex server. It gives your users a self-service portal to request movies and TV shows, integrates with Radarr and Sonarr, and supports Discord, notifications, and more.

It's like running your own Netflix, with you as the librarian.


---

## 🧰 Features

* Web UI for Plex users to request content
* Full integration with Plex, Radarr, and Sonarr
* Discord, Telegram, Pushover, and email notifications
* Approvals, auto-downloads, and user role support
* Built-in admin dashboard and user activity logs


---

## 🚀 Getting Started

### 🐳 Docker Compose

```yaml
---
services:
  overseerr:
    container_name: overseerr
    image: lscr.io/linuxserver/overseerr:latest
    restart: unless-stopped
    ports:
      - 5055:5055
    environment:
      - PUID=${PUID}
      - PGID=${PGID}
      - TZ=${TZ}
    volumes:
      - $DOCKERDIR/overseerr/config:/config
    networks:
      - media
```

Using `network_mode` set to `host` to avoid using ports

```yaml
---
services:
  overseerr:
    container_name: overseerr
    image: lscr.io/linuxserver/overseerr:latest
    restart: unless-stopped
    network_mode: host
    environment:
      - PUID=${PUID}
      - PGID=${PGID}
      - TZ=${TZ}
    volumes:
      - $DOCKERDIR/overseerr/config:/config
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

* All app settings are stored in `/config` on host
* First-time setup is handled via the web UI
* Link your Plex server and set up your Radarr/Sonarr connection in Settings → Services


---

## 🛠️ Tips & Customization

* Enable automatic approval for trusted Plex users
* Link your Discord server to get notified on new requests
* Use the **discover** section to let users browse upcoming movies/shows
* Customize request restrictions by user role


---

## 🧯 Troubleshooting Notes

* 🚪 **Plex login not working?** Ensure Overseerr can reach `plex.tv` and you’re using a Plex admin account
* 🔒 **Want more security?** Proxy Overseerr through Authentik with strict access policies
* 🧱 **Container not saving settings?** Double-check volume mount path and permissions
* 🌐 **Can't connect to Sonarr/Radarr?** Verify container-to-container network resolution (e.g., use service names)


---

## 📚 More Info

* [Overseerr Docs](https://docs.overseerr.dev/)
* [GitHub Project](https://github.com/sct/overseerr)
* [LinuxServer Overseerr Docs](https://docs.linuxserver.io/images/docker-overseerr)


---

## 🧼 Cleanup

```bash
docker-compose down -v
```
