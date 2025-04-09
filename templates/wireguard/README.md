# 🏡 Goug's HomeLab Docker Templates

Welcome to **Goug's HomeLab** — a growing collection of Docker Compose templates for apps I use or test in my HomeLab. These templates are built to help you get up and running quickly with no bloated configs or mysterious dependencies.

Each app folder includes:

* `docker-compose.yml` — core container setup
* `.env` — customizable environment variables
* `README.md` — you're reading it!
* Sample config files (if needed)

Explore more at [goug76/docker-templates](https://github.com/goug76/docker-templates).

---

## 📦 WireGuard (wg-easy)

[wg-easy](https://github.com/wg-easy/wg-easy) is a user-friendly web interface for managing a **WireGuard VPN server**. It lets you create and manage clients with one-click QR codes and config file downloads — all without touching the command line.

It’s lightweight, fast, and incredibly easy to use. Perfect for exposing your homelab securely from anywhere.

---

## 🧰 Features

* One-click WireGuard client creation
* Web UI for viewing connection stats and exporting configs
* Mobile-friendly with built-in QR code support
* Minimal configuration — just set your public IP or domain
* Tracks per-client bandwidth usage and allows revocation

---

## 🚀 Getting Started

### 🐳 Docker Compose

```yaml
---
services:
  wg-easy:
    container_name: wg-easy
    image: ghcr.io/wg-easy/wg-easy:latest
    restart: unless-stopped
    ports:
      - "51820:51820/udp"
      - "51821:51821/tcp"
    cap_add:
      - NET_ADMIN
      - SYS_MODULE
    sysctls:
      - net.ipv4.ip_forward=1
      - net.ipv4.conf.all.src_valid_mark=1
    environment:
      - LANG=en
      - WG_HOST=${WG_HOST}
      - PASSWORD_HASH=${WG_PWD}
      - WG_DEFAULT_DNS= 
      - UI_TRAFFIC_STATS=true 
      - UI_CHART_TYPE=1 
      - $DOCKERDIR/wireguard:/etc/wireguard
    networks:
      - networking
```

> 🌐 Web UI available at `http://<host>:51821` 
>
> 🔐 VPN clients connect using port `51820/udp`

---

## ⚙️ Environment Variables

| Variable | Description | Example |
|----|----|----|
| `DOCKERDIR` | Docker file Location | `/home/user/docker` |
| `TZ` | Timezone | `America/New_York` |
| `WG_HOST` | Public IP or domain for the VPN | `vpn.mydomain.com` |
| `PASSWORD_HASH` | Hashed password for web UI login | `$argon2id$v=19$...` |
| `WG_DEFAULT_DNS` | DNS client will use inside the VPN | `10.0.0.1 (e.g., AdGuard)` |
| `UI_TRAFFIC_STATS` | Enables RX/TX per-client stats in UI | `true` |
| `UI_CHART_TYPE` | Chart style: 0=none, 1=line, 2=area, 3=bar | `1` |

> 🔐 Use htpasswd or bcrypt/argon2 generators to create secure hashes for PASSWORD_HASH. 
>
> 🌐 Having AdGuard and WirdGuard on the same Docker network allows you to use the AdGuard Docker IP for `WG_DEFAULT_DNS`

---

## 🧪 Sample Configuration

* Client config files are stored and managed under `/etc/wireguard`
* Clients can be scanned with a mobile device or downloaded directly
* Web UI password is required unless disabled (not recommended)
* Reverse proxy should terminate TLS for public-facing UI

---

## 🛠️ Tips & Customization

* Use `WG_DEFAULT_DNS` to route client DNS through Pi-hole or AdGuard
* Consider enabling only the UI port publicly, and restrict VPN port to trusted IPs
* Use `iptables` or UFW to allow only authenticated VPN traffic if adding extra security layers

---

## 🧯 Troubleshooting Notes

* 🌐 **Can’t access UI?** Check port `51821` and password hash
* 📱 **Client won’t connect?** Double-check public IP in `WG_HOST` and UDP port forwarding
* 🔐 **Web UI exposed?** Protect with reverse proxy and Authentik or VPN-only access
* 🧱 **"Permission denied"?** Ensure Docker has `NET_ADMIN` and `SYS_MODULE` capabilities

---

## 📚 More Info

* [wg-easy GitHub](https://github.com/wg-easy/wg-easy)
* [WireGuard Docs](https://www.wireguard.com/)
* [Generate Argon2 Hash](https://argon2.online/)

---

## 🧼 Cleanup

```bash
docker-compose down -v
```
