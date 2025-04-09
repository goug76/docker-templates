# 🏡 Goug's HomeLab Docker Templates

Welcome to **Goug's HomeLab** — a growing collection of Docker Compose templates for apps I use or test in my HomeLab. These templates are built to help you get up and running quickly with no bloated configs or mysterious dependencies.

Each app folder includes:

* `docker-compose.yml` — core container setup
* `.env` — customizable environment variables
* `README.md` — you're reading it!
* Sample config files (if needed)

Explore more at [goug76/docker-templates](https://github.com/goug76/docker-templates).


---

## 📦 Cloudflare-DDNS

[cloudflare-ddns](https://github.com/timothyjmiller/cloudflare-ddns) is a lightweight Docker container that keeps your dynamic IP address in sync with Cloudflare DNS records. Perfect for homelabs behind residential ISPs or setups where you don’t have a static IP.

This app works by updating A/AAAA records on Cloudflare via their API, using either an API token or legacy API key.


---

## 🧰 Features

* Supports Cloudflare API token or API key authentication
* Keeps your DNS records updated with your current IP
* Supports both IPv4 (A) and IPv6 (AAAA) records
* Host networking for accurate public IP detection
* Configurable TTL and record purging behavior


---

## 🚀 Getting Started

### 🐳 Docker Compose

```yaml
---
services:
  cloudflare-ddns:
    container_name: cloudflare-ddns
    image: timothyjmiller/cloudflare-ddns:latest
    security_opt:
      - no-new-privileges:true
    restart: unless-stopped
    environment:
      - PUID=${PUID}
      - PGID=${PGID}
      - TZ=$TZ
    volumes:
      - $DOCKERDIR/cloudflare-ddns/config.json:/config.json
    network_mode: "host"
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

Here’s a sample config.json you can place at $DOCKERDIR/cloudflare-ddns/config.json:

```json
{
    "cloudflare": [
      {
        "authentication": {
          "api_token": "api_token_here",
          "api_key": {
            "api_key": "api_key_here",
            "account_email": "your_email_here"
          }
        },
        "zone_id": "your_zone_id_here",
        "subdomains": [
          {
            "name": "",
            "proxied": false
          },
          {
            "name": "remove_or_replace_with_your_subdomain",
            "proxied": false
          }
        ]
      }
    ],
    "a": true,
    "aaaa": true,
    "purgeUnknownRecords": false,
    "ttl": 300
  }
```
> 💡 Set proxied: true if you're using Cloudflare’s CDN and protection features.

---

## 🛠️ Tips & Customization

* For best results, use an **API token** scoped to just your DNS zone
* Use host networking to ensure the container sees your public IP correctly
* If running behind CG-NAT or double NAT, updates might fail — consider using an external IP lookup override
* You can run this alongside cron or a scheduler like watchtower if you want automatic container refreshes


---

## 🧯 Troubleshooting Notes

* 🧪 **IP not updating?** Check container logs — it’ll print the last known and current IP
* 🧱 **Permission denied?** Make sure PUID/PGID match your user and the volume is writable
* 🔐 **Invalid credentials?** Double-check your config.json for token format or account email
* 🕵️‍♂️ **Stuck at startup?** Confirm that your host's DNS and IP reachability is healthy


---

## 📚 More Info

* [cloudflare-ddns GitHub](https://github.com/timothyjmiller/cloudflare-ddns)
* [Cloudflare API Tokens](https://developers.cloudflare.com/api/tokens/create/)
* [Zone ID Lookup](https://dash.cloudflare.com/) (under your domain settings)


---

## 🧼 Cleanup

```bash
docker-compose down -v
```
