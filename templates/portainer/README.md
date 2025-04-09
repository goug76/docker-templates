# 🏡 Goug's HomeLab Docker Templates

Welcome to **Goug's HomeLab** — a growing collection of Docker Compose templates for apps I use or test in my HomeLab. These templates are built to help you get up and running quickly with no bloated configs or mysterious dependencies.

Each app folder includes:

* `docker-compose.yml` — core container setup
* `.env` — customizable environment variables
* `README.md` — you're reading it!
* Sample config files (if needed)

Explore more at [goug76/docker-templates](https://github.com/goug76/docker-templates).

---

## 📦 Portainer

[Portainer](https://www.portainer.io/) is a lightweight, web-based Docker management UI that lets you monitor containers, manage volumes, view logs, and deploy stacks without needing to touch the CLI. It’s ideal for homelab environments, production clusters, and everything in between.

---

## 🧰 Features

* Web UI to manage Docker containers, images, networks, and volumes
* Role-based access control (RBAC)
* Supports standalone, Swarm, and Kubernetes environments
* Visual stack deployments and real-time container stats
* Easy container logs and console access

---

## 🚀 Getting Started

### 🐳 Docker Compose

```yaml
---
services:
  # Portainer - WebUI for Containers
  portainer:
    container_name: portainer
    image: portainer/portainer-ce:latest
    restart: unless-stopped
    ports:
      - 9443:9443
    environment:
      - TZ=$TZ
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro
      - $DOCKERDIR/portainer/data:/data
    networks:
      - networking
```

> ⚠️ Be sure to copy and edit the `.env` file included in this directory.

---

## ⚙️ Environment Variables

| Variable | Description | Example |
|----|----|----|
| `DOCKERDIR` | Docker file Location | `/home/user/docker` |
| `TZ` | Your time zone | `America/New_York` |

---

## 🧪 Sample Configuration

* The first time you access Portainer, you’ll be prompted to create an admin account.
* Your Docker environment will be auto-detected via the mounted `/var/run/docker.sock` socket.
* All settings and user data are stored under `$DOCKERDIR/portainer/data`.

---

## 🛠️ Tips & Customization

* Create endpoint groups for organizing multiple Docker environments
* Add templates for rapid deployment of apps
* Use the “Stacks” section to manage Docker Compose YAMLs directly
* Customize access via users and teams (with built-in RBAC)

---

## 🧯 Troubleshooting Notes

* 🔐 **Login screen still shows without SSO?** Authentik proxy only protects access to the page, not Portainer’s internal auth
* 🔄 **Portainer not updating?** Use `latest` tag or specify a version for stability
* ❌ **Can't see containers?** Ensure `/var/run/docker.sock` is mounted and readable
* 📦 **Data loss after restart?** Make sure the `/data` volume is persistent

---

## 📚 More Info

* [Portainer Official Site](https://www.portainer.io/)
* [Portainer Docker Image](https://hub.docker.com/r/portainer/portainer-ce)
* [Authentik Configuration Doc](https://docs.goauthentik.io/integrations/services/portainer/)
* [Docker Socket Security](https://docs.docker.com/engine/security/)

---

## 🧼 Cleanup

```bash
docker-compose down -v
```
