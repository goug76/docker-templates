# 🏡 Goug's HomeLab Docker Templates

Welcome to **Goug's HomeLab** — a growing collection of Docker Compose templates for apps I use or test in my HomeLab. These templates are built to help you get up and running quickly with no bloated configs or mysterious dependencies.

Each app folder includes:

* `docker-compose.yml` — core container setup
* `.env` — customizable environment variables
* `README.md` — you're reading it!
* Sample config files (if needed)

Explore more at [goug76/docker-templates](https://github.com/goug76/docker-templates).


---

## 📦 Nginx Proxy Manager (NPM)

[Nginx Proxy Manager](https://nginxproxymanager.com/) is a simple, powerful web interface for managing Nginx reverse proxies with automatic SSL via Let’s Encrypt. It makes it incredibly easy to expose, secure, and route traffic to your self-hosted services.

No manual editing of `nginx.conf` required — just click, fill, and go.


---

## 🧰 Features

* Beautiful UI for managing proxies
* Built-in Let's Encrypt support with auto-renewal
* Wildcard, HTTP challenge, and DNS challenge support
* Access control, redirection, custom headers, and more
* Works great with Authentik, Heimdall, and Jellyfin


---

## 🚀 Getting Started

### 🐳 Docker Compose

```yaml
---
services:
  npm:
    container_name: npm
    image: 'jc21/nginx-proxy-manager:latest'
    restart: unless-stopped
    ports:
      - 80:80
      - 81:81
      - 443:443
    environment:
      - TZ=$TZ
    volumes:
      - $DOCKERDIR/npm/data:/data
      - $DOCKERDIR/npm/letsencrypt:/etc/letsencrypt
    networks:
      - networking
```

> ⚠️ Be sure to copy and edit the `.env` file included in this directory.


---

## ⚙️ Environment Variables

| Variable | Description | Example |
|----|----|----|
| `DOCKERDIR` | Docker file Location | `/home/user/docker` |
| `TZ` | Timezone | `America/New_York` |


---

## 🧪 Sample Configuration

* `/data` stores all NPM configs, UI settings, and logs
* `/etc/letsencrypt` holds SSL certs issued by Let's Encrypt
* First-time login:
  * **Default Email**: `admin@example.com`
  * **Default Password**: `changeme`

You’ll be prompted to update both upon first login at http://<host>:81.


---

## 🛠️ Tips & Customization

* Set up **wildcard domains** with DNS challenge for easy subdomain routing
* Use **access lists** to require basic auth on sensitive services
* Add custom headers or rewrite rules under **Advanced** tab per host
* Enable logging to `/data/logs` for debugging


---

## 🧯 Troubleshooting Notes

* 🔒 **SSL cert not issuing?** Confirm DNS is pointing to your public IP and ports 80/443 are accessible
* 📉 **Web UI down?** Check that port 81 isn't used by another service
* 🔁 **Proxy not forwarding?** Make sure internal service port is reachable from the NPM container
* 🔐 **Too many failed certs?** Let’s Encrypt has rate limits — wait or switch to DNS challenge


---

## 📚 More Info

* [Official NPM Website](https://nginxproxymanager.com/)
* [jc21/nginx-proxy-manager Docker Hub](https://hub.docker.com/r/jc21/nginx-proxy-manager/)
* [Let’s Encrypt Rate Limits](https://letsencrypt.org/docs/rate-limits/)


---

## 🧼 Cleanup

```bash
docker-compose down -v
```
