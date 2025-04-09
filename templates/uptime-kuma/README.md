# 🏡 Goug's HomeLab Docker Templates

Welcome to **Goug's HomeLab** — a growing collection of Docker Compose templates for apps I use or test in my HomeLab. These templates are built to help you get up and running quickly with no bloated configs or mysterious dependencies.

Each app folder includes:

* `docker-compose.yml` — core container setup
* `.env` — customizable environment variables
* `README.md` — you're reading it!
* Sample config files (if needed)

Explore more at [goug76/docker-templates](https://github.com/goug76/docker-templates).

---

## 📦 Uptime-Kuma

[Uptime-Kuma](https://github.com/louislam/uptime-kuma) is a fancy, self-hosted monitoring tool that helps you keep tabs on your services, apps, websites, and endpoints — all wrapped in a modern, slick UI with notifications, public status pages, and graph-based history.

It's like a self-hosted UptimeRobot, but better — and totally yours.

---

## 🧰 Features

* HTTP, TCP, ICMP (ping), DNS, and Docker health checks
* Public and private status pages
* Built-in notification support: Discord, Slack, Telegram, Gotify, SMTP, etc.
* Fast, mobile-friendly UI with dark mode
* Easy backup and restore

---

## 🚀 Getting Started

### 🐳 Docker Compose

```yaml
---
services:
  uptime-kuma:
    container_name: uptime-kuma
    image: louislam/uptime-kuma:latest
    restart: always
    environment:
      - NODE_EXTRA_CA_CERTS=/etc/ssl/certs/ca-certificates.crt
      - TZ=${TZ}
    ports:
      - 3002:3001
    volumes:
      - $DOCKERDIR/uptime-kuma:/app/data
      - /var/run/docker.sock:/var/run/docker.sock
      - /etc/ssl/certs/ca-certificates.crt:/etc/ssl/certs/ca-certificates.crt
    networks:
      - monitoring
```

> ⚠️ Be sure to copy and edit the `.env` file included in this directory.

---

## ⚙️ Environment Variables

| Variable | Description | Example |
|----|----|----|
| `NODE_EXTRA_CA_CERTS` | Trust additional SSL certs (optional) | `/etc/ssl/certs/ca-certificates.crt` |
| `DOCKERDIR` | Docker file Location | `/home/user/docker` |
| `TZ` | Timezone | `America/New_York` |

---

## 🧪 Sample Configuration

* All data (users, config, logs) is stored under `/app/data`
* Exposes on port `3002` (host) → `3001` (container)
* The container uses Docker socket and certificate volume for optional integration
* Supports **backup/restore** directly from the web UI

---

## 🛠️ Tips & Customization

* Use notification integrations for alerting (Discord, Telegram, etc.)
* Create a **public status page** for team visibility
* Group monitors into **tags** or **categories**
* Use Docker-based health checks to monitor local containers directly

---

## 🧯 Troubleshooting Notes

* 🔐 **Auth not working?** Remember, Authentik only protects access via proxy — Uptime-Kuma manages its own logins
* ❌ **Monitor failing?** Check DNS, firewall, or uptime-kuma’s timeout settings
* 🧱 **Broken certs?** Ensure the `ca-certificates.crt` is mounted and readable
* 🔄 **Container crash loops?** Try resetting the config by clearing `/app/data`

---

## 📚 More Info

* [GitHub Repo](https://github.com/louislam/uptime-kuma)
* [Docker Image](https://hub.docker.com/r/louislam/uptime-kuma)
* [Official Wiki](https://github.com/louislam/uptime-kuma/wiki)
* [Authentik Configuration Doc](https://docs.goauthentik.io/integrations/services/uptime-kuma/)

---

## 🧼 Cleanup

```bash
docker-compose down -v
```
