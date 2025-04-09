# 🏡 Goug's HomeLab Docker Templates

Welcome to **Goug's HomeLab** — a growing collection of Docker Compose templates for apps I use or test in my HomeLab. These templates are built to help you get up and running quickly with no bloated configs or mysterious dependencies.

Each app folder includes:

* `docker-compose.yml` — core container setup
* `.env` — customizable environment variables
* `README.md` — you're reading it!
* Sample config files (if needed)

Explore more at [goug76/docker-templates](https://github.com/goug76/docker-templates).

---

## 📦 Vaultwarden (Self-Hosted Bitwarden)

[Vaultwarden](https://github.com/dani-garcia/vaultwarden) is a lightweight, unofficial Bitwarden server implementation written in Rust. It's ideal for self-hosters who want to manage their own password vault with full Bitwarden client compatibility — apps, browser extensions, CLI, and all.

This setup includes PostgreSQL for database storage and optional push notifications support.

---

## 🧰 Features

* Fully compatible with Bitwarden clients (web, mobile, desktop, CLI)
* Self-contained server with minimal resource use
* Supports PostgreSQL, MySQL, or SQLite
* Optional admin UI, 2FA, Duo, email, and FIDO2 support
* Bitwarden Send, attachments, file sharing, and password health checks
* Optional push notification support for mobile apps

---

## 🚀 Getting Started

### 🐳 Docker Compose

```yaml
---
services:
  postgres:
    container_name: postgres
    image: postgres:16
    security_opt:
      - no-new-privileges:true
    restart: unless-stopped
    ports:
      - 5432:5432
    # set shared memory limit when using docker-compose
    shm_size: 128mb
    volumes: 
      - $DOCKERDIR/postgres:/var/lib/postgresql/data
    environment:
      POSTGRES_USER: '${USER}'
      POSTGRES_PASSWORD: '${POSTGRES_PASSWORD}'
      POSTGRES_DB: vaultwarden
      TZ: '${TZ}'
    networks:
      - database
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -h localhost -U $$POSTGRES_USER"]
      interval: 2s

  vaultwarden:
    container_name: vaultwarden
    image: vaultwarden/server:latest
    security_opt:
      - no-new-privileges:true
    restart: unless-stopped
    ports:
      - 83:80
    environment:
      - PUSH_ENABLED=true
      - PUSH_INSTALLATION_ID=${PUSH_INSTALLATION_ID}
      - PUSH_INSTALLATION_KEY=${PUSH_INSTALLATION_KEY}
      - DATABASE_URL=postgresql://${USER}:${POSTGRES_PASSWORD}@postgres/vaultwarden
      - ADMIN_TOKEN=${ADMIN_TOKEN}
      - TZ=$TZ
    volumes:
      - $DOCKERDIR/vaultwarden/:/data/
    networks:
      database:
    depends_on:
      postgres:
        condition: service_healthy
```

> ⚠️ Be sure to copy and edit the `.env` file included in this directory.

---

## ⚙️ Environment Variables

| Variable | Description | Example |
|----|----|----|
| `USER` | Postgres database user | `authentik` |
| `POSTGRES_PASSWORD` | Password for Postgres | `supersecurepass` |
| `DOCKERDIR` | Docker file Location | `/home/user/docker` |
| `TZ` | Timezone | `America/New_York` |
| `DATABASE_URL` | DB connection string (postgres://user:pass@...) | `postgresql://${username}:${password}@postgres/vaultwarden` |
| `ADMIN_TOKEN` | Token to access the admin panel | `openssl rand -base64 48` |

### 📲 Mobile Push Notification Variables

| Variable | Description | Example |
|----|----|----|
| `PUSH_ENABLED` | Enable push notifications (mobile login support) | `true` |
| `PUSH_INSTALLATION_ID` | From Bitwarden push gateway (opt-in) | `your_id_here` |
| `PUSH_INSTALLATION_KEY` | Push service key | `your_key_here` |

> To get the `PUSH_INSTALLATION_ID` and `PUSH_INSTALLATION_KEY` [visit here](https://bitwarden.com/host/)

---

## 🧪 Sample Configuration

* Data is stored in `$DOCKERDIR/vaultwarden`
* PostgreSQL is preferred over SQLite for performance and stability
* Admin panel is available at `/admin` when `ADMIN_TOKEN` is set
* Mobile push notifications require setup with Bitwarden’s official gateway

---

## 🛠️ Tips & Customization

* Disable registration with `SIGNUPS_ALLOWED=false`
* Enable 2FA or email integrations using SMTP env variables
* Backup `/data/` regularly — it includes your vault, configs, and keys
* Set `WEBSOCKET_ENABLED=true` to allow real-time sync in web vault (if reverse proxy supports it)

---

## 🧯 Troubleshooting Notes

* ❌ **Can't log in from mobile app?** Double-check your push keys or try disabling `PUSH_ENABLED`
* 🔐 **Admin page not working?** Ensure `ADMIN_TOKEN` is set and not empty
* 🔄 **Login loops?** May be due to missing TLS headers if behind a reverse proxy — ensure HTTPS is terminated properly
* ⚠️ **Database not found?** Check the formatting of your `DATABASE_URL` and make sure Postgres is healthy

---

## 📚 More Info

* [Vaultwarden GitHub](https://github.com/dani-garcia/vaultwarden)
* [PostgreSQL Connection Strings](https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING)
* [LinuxServer Image Docs](https://hub.docker.com/r/vaultwarden/server)
* [Bitwarden Push Setup](https://bitwarden.com/host/)

---

## 🧼 Cleanup

```bash
docker-compose down -v
```
