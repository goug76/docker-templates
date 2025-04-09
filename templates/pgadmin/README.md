# 🏡 Goug's HomeLab Docker Templates

Welcome to **Goug's HomeLab** — a growing collection of Docker Compose templates for apps I use or test in my HomeLab. These templates are built to help you get up and running quickly with no bloated configs or mysterious dependencies.

Each app folder includes:

* `docker-compose.yml` — core container setup
* `.env` — customizable environment variables
* `README.md` — you're reading it!
* Sample config files (if needed)

Explore more at [goug76/docker-templates](https://github.com/goug76/docker-templates).


---

## 📦 pgAdmin

[pgAdmin](https://www.pgadmin.org/) is a popular web-based interface for managing PostgreSQL databases. It lets you browse tables, run queries, manage users, view logs, and more — all in a simple, polished UI. Ideal for devs and DBAs working with local or remote Postgres instances.

This container is pre-configured to support OpenID Connect (OIDC) login via **Authentik**, making it easy to manage secure access to your database tools.

---

## 🧰 Features

* Modern PostgreSQL GUI in your browser
* Secure authentication (internal + Authentik OIDC)
* Server group management for multiple Postgres instances
* Query tool, ERD diagrams, database metrics
* Role management, backups, data import/export

---

## 🚀 Getting Started

### 🐳 Docker Compose

```yaml
---
services:
  pgadmin:
    container_name: pgadmin
    image: dpage/pgadmin4
    restart: unless-stopped
    ports:
      - "8081:80"
    environment:
      PGADMIN_DEFAULT_EMAIL: '${EMAIL}'
      PGADMIN_DEFAULT_PASSWORD: '${POSTGRES_PASSWORD}'
      PGADMIN_CONFIG_AUTHENTICATION_SOURCES: '${PGADMIN_CONFIG_AUTHENTICATION_SOURCES}'
      PGADMIN_CONFIG_OAUTH2_AUTO_CREATE_USER: '${PGADMIN_CONFIG_OAUTH2_AUTO_CREATE_USER}'
      PGADMIN_CONFIG_OAUTH2_CONFIG: '${PGADMIN_CONFIG_OAUTH2_CONFIG}'
      TZ: '${TZ}'
    volumes: 
      - $DOCKERDIR/pgadmin:/var/lib/pgadmin
    networks:
      - database
```

> ⚠️ Be sure to copy and edit the `.env` file included in this directory.

> This application has a unique `.env` file

```bash

EMAIL=email@address.com
TZ="America/New_York"
DOCKERDIR="/path/to/docker/dir"
PGADMIN_DEFAULT_PASSWORD=<password>
PGADMIN_CONFIG_AUTHENTICATION_SOURCES="['oauth2', 'internal']"
PGADMIN_CONFIG_OAUTH2_AUTO_CREATE_USER=True
PGADMIN_CONFIG_OAUTH2_CONFIG="[{
    'OAUTH2_NAME' : 'authentik',
	'OAUTH2_DISPLAY_NAME' : '<display-name>',
	'OAUTH2_CLIENT_ID' : '<client-id>',
	'OAUTH2_CLIENT_SECRET' : '<client-secret>',
	'OAUTH2_TOKEN_URL' : 'https://authentik.company/application/o/token/',
	'OAUTH2_AUTHORIZATION_URL' : 'https://authentik.company/application/o/authorize/',
	'OAUTH2_API_BASE_URL' : 'https://authentik.company/',
	'OAUTH2_USERINFO_ENDPOINT' : 'https://authentik.company/application/o/userinfo/',
	'OAUTH2_SERVER_METADATA_URL' : 'https://authentik.company/application/o/<app-slug>/.well-known/openid-configuration',
	'OAUTH2_SCOPE' : 'openid email profile',
	'OAUTH2_ICON' : '<fontawesome-icon>',
	'OAUTH2_BUTTON_COLOR' : '#fd4b2d'
}]"
```

---

## ⚙️ Environment Variables

| Variable | Description | Example |
|----|----|----|
| `EMAIL` | Default admin email | `admin@example.com` |
| `POSTGRES_PASSWORD` | Password for Postgres | `supersecurepass` |
| `DOCKERDIR` | Docker file Location | `/home/user/docker` |
| `TZ` | Timezone | `America/New_York` |
| `PGADMIN_CONFIG_AUTHENTICATION_SOURCES` | Enabled auth types | `oauth2`, `internal` |
| `PGADMIN_CONFIG_OAUTH2_AUTO_CREATE_USER` | Auto-create users from OIDC | `True` |
| `PGADMIN_CONFIG_OAUTH2_CONFIG` | Python-style OIDC configuration block | `see .env file` |

---

## 🧪 Sample Configuration

* Fix file permissions with `sudo chown -R 5050:5050 $DOCKERDIR/pgadmin/`
* Credentials for your Postgres servers are added *after* logging in via the web UI
* Saved server connections persist under `/var/lib/pgadmin` volume
* Admin email + password are used for internal login fallback if needed

---

## 🛠️ Tips & Customization

* To **disable internal login**, remove `internal` from `PGADMIN_CONFIG_AUTHENTICATION_SOURCES`
* Add additional Postgres servers by clicking "Add New Server" in the UI
* Use `.pgpass` files or embedded credentials for automated access (advanced use)
* Customize the OIDC button with your own icon or color

---

## 🧯 Troubleshooting Notes

* 🧠 **OIDC login failing?** Check redirect URLs and ensure the app is registered properly in Authentik
* ❌ **Password rejected?** Be sure your `.env` doesn’t have quotes around values like `True`
* 🔐 **OAuth button not showing?** Confirm` PGADMIN_CONFIG_AUTHENTICATION_SOURCES` includes `'oauth2'`
* 📁 **Data not saving?** Check ownership of your `$DOCKERDIR/pgadmin` volume

---

## 📚 More Info

* [pgAdmin Website](https://www.pgadmin.org/)
* [Docker Image on DockerHub](https://hub.docker.com/r/dpage/pgadmin4)
* [Authentik Configuration Doc](https://docs.goauthentik.io/integrations/services/pgadmin/)

---

## 🧼 Cleanup

```bash
docker-compose down -v
```
