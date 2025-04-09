# 🏡 Goug's HomeLab Docker Templates

Welcome to **Goug's HomeLab** — a growing collection of Docker Compose templates for apps I use or test in my HomeLab. These templates are built to help you get up and running quickly with no bloated configs or mysterious dependencies.

Each app folder includes:

* `docker-compose.yml` — core container setup
* `.env` — customizable environment variables
* `README.md` — you're reading it!
* Sample config files (if needed)

Explore more at [goug76/docker-templates](https://github.com/goug76/docker-templates).


---

## 📦 Glances

[Glances](https://nicolargo.github.io/glances/) is a real-time system monitoring tool that shows you CPU, memory, disk I/O, network usage, Docker stats, and more — all from a web interface or CLI. It’s perfect for getting a quick health check on your homelab machines or remote systems.

This setup uses the `-w` flag to enable web mode on port `61208`.


---

## 🧰 Features

* Web-based dashboard with real-time system metrics
* CPU, RAM, network, load, filesystem, and process info
* Docker container monitoring support
* Extendable with plugins and APIs
* Lightweight and runs nearly anywhere


---

## 🚀 Getting Started

### 🐳 Docker Compose

```yaml
---
services:
  glances:
    container_name: glances
    image: nicolargo/glances:latest-full
    restart: unless-stopped
    ports:
      - 61208:61208
    environment:
      - GLANCES_OPT=-w
      - PUID = ${PUID}
      - PGID = ${PGID}
      - TZ=$TZ
    pid: host
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro
```

> ⚠️ Be sure to copy and edit the `.env` file included in this directory.


---

## ⚙️ Environment Variables

| Variable | Description | Example |
|----|----|----|
| `GLANCES_OPT` | Launch flag for Glances | `-w` (web UI mode) |
| `PUID` | User ID for file ownership | `1000` |
| `PGID` | Group ID for file ownership | `1000` |
| `TZ` | Timezone | `America/New_York` |


---

## 🧪 Sample Configuration

No config file needed — everything is set via container args or environment variables.

This container uses:

* GLANCES_OPT=-w to launch in web server mode
* pid: host so it can access full system process info
* A mounted Docker socket to read container stats

Access the UI at http://<host>:61208


---

## 🛠️ Tips & Customization

* Add -p 61209:61209 and expose the REST API with -w --export-rest
* Enable Docker stats by ensuring /var/run/docker.sock is mounted (read-only is fine)
* Set up Glances on multiple machines and use **Glances Server/Client mode**
* Can be used with Prometheus or InfluxDB for advanced metrics


---

## 🧯 Troubleshooting Notes

* 🔒 **No auth by default** — use Authentik or Traefik ForwardAuth
* 🧱 **Missing data?** Confirm pid: host is enabled
* 🐳 **No container stats?** Make sure Docker socket is properly mounted
* 🧪 **Web UI not responding?** Confirm port 61208 is open and GLANCES_OPT=-w is set


---

## 📚 More Info

* [Official Glances Site](https://nicolargo.github.io/glances/)
* [Glances GitHub Repo](https://github.com/nicolargo/glances)
* [Web UI Setup Guide](https://glances.readthedocs.io/en/latest/config.html#web-server-mode)
* [Authentik Proxy Docs](https://goauthentik.io/docs/providers/proxy/)


---

## 🧼 Cleanup

```bash
docker-compose down -v
```
