# 🏡 Goug's HomeLab Docker Templates

Welcome to **Goug's HomeLab** — a growing collection of Docker Compose templates for apps I use or test in my HomeLab. These templates are built to help you get up and running quickly with no bloated configs or mysterious dependencies.

Each app folder includes:

* `docker-compose.yml` — core container setup
* `.env` — customizable environment variables
* `README.md` — you're reading it!
* Sample config files (if needed)

Explore more at [goug76/docker-templates](https://github.com/goug76/docker-templates).


---

## 📦 Outline Wiki

[Outline](https://www.getoutline.com/) is a powerful, self-hosted knowledge base and team wiki built with markdown at its core. It's fast, clean, and ideal for organizing technical documentation, SOPs, personal notes, and more — with a beautiful UI and support for collaborative editing.

This setup uses Postgres and Redis and is prepped for SSO via OpenID Connect (OIDC) using Authentik or any compatible IdP.


---

## 🧰 Features

* Markdown-based content with live editor
* Nested collections and tags for easy organization
* Powerful full-text search
* Built-in role-based access controls
* SSO/OIDC login support (e.g., with Authentik)
* File uploads with local or external storage


---

## 🚀 Getting Started

### 🐳 Docker Compose

```yaml
networks:
  database:
    name: database
    driver: bridge

services:
  redis:
    container_name: redis
    image: docker.io/library/redis:alpine
    command: redis-server /redis.conf --save 60 1 --loglevel warning
    restart: unless-stopped
    ports:
      - "6379:6379"
    volumes:
      - $DOCKERDIR/redis/redis.conf:/redis.conf
      - $DOCKERDIR/redis:/data
    networks:
      - database
    healthcheck:
      test: ["CMD-SHELL", "redis-cli ping | grep PONG"]
      start_period: 20s
      interval: 30s
      retries: 5
      timeout: 3s

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
      TZ: '${TZ}'
    networks:
      - database
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -h localhost -U $$POSTGRES_USER"]
      interval: 2s

  outline:
    container_name: outline
    image: docker.getoutline.com/outlinewiki/outline:latest
    restart: unless-stopped
    user: "0"
    ports:
      - "3000:3000"
    environment:
      PGSSLMODE: disable
      SECRET_KEY: ${SECRET_KEY}
      UTILS_SECRET: ${UTILS_SECRET}
      DATABASE_URL: postgres://${USER}:${POSTGRES_PASSWORD}@postgres:5432/outline
      REDIS_URL: redis://redis:6379
      URL: ${URL}
      PORT: ${PORT}
      FILE_STORAGE: local
      FILE_STORAGE_LOCAL_ROOT_DIR: /var/lib/outline/data
      FILE_STORAGE_UPLOAD_MAX_SIZE: 26214400
      OIDC_CLIENT_ID: ${OIDC_CLIENT_ID}
      OIDC_CLIENT_SECRET: ${OIDC_CLIENT_SECRET}
      OIDC_AUTH_URI: ${OIDC_AUTH_URI}
      OIDC_TOKEN_URI: ${OIDC_TOKEN_URI}
      OIDC_USERINFO_URI: ${OIDC_USERINFO_URI}
      OIDC_LOGOUT_URI: ${OIDC_LOGOUT_URI}
      OIDC_USERNAME_CLAIM: ${OIDC_USERNAME_CLAIM}
      OIDC_DISPLAY_NAME: ${OIDC_DISPLAY_NAME}
      OIDC_SCOPES: ${OIDC_SCOPES}
      SMTP_HOST=: ${SMTP_HOST}
      SMTP_PORT: ${SMTP_PORT}
      SMTP_USERNAME: ${SMTP_USERNAME}
      SMTP_PASSWORD: ${SMTP_PASSWORD}
      SMTP_FROM_EMAIL: ${SMTP_FROM_EMAIL}
      SMTP_REPLY_EMAIL: ${SMTP_REPLY_EMAIL}
      SMTP_TLS_CIPHERS: ${SMTP_TLS_CIPHERS}
      SMTP_SECURE: ${SMTP_SECURE}
      TZ: $TZ
    volumes:
      - $DOCKERDIR/outline:/var/lib/outline/data
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy
    networks:
      - database
```

> ⚠️ Be sure to copy and edit the `.env` file included in this directory.


---

## ⚙️ Environment Variables

### ✅ Common Environment Variables for Outline

| Variable | Description | Example |
|----|----|----|
| `USER` | Postgres database user | `outline` |
| `POSTGRES_PASSWORD` | Password for Postgres | `supersecurepass` |
| `DOCKERDIR` | Docker file Location | `/home/user/docker` |
| `TZ` | Timezone | `America/New_York` |
| `SECRET_KEY` | Application secret key (must be unique and long) | `openssl rand -hex 32` |
| `UTILS_SECRET` | Another internal crypto key (same as above) | `openssl rand -hex 32` |
| `URL` | Publicly accessible URL of the Outline instance | `https://wiki.domain.com` |
| `PORT` | Port Outline will bind to inside container | `3000` |
| `FILE_STORAGE` | File storage provider | `local` |
| `FILE_STORAGE_LOCAL_ROOT_DIR` | Folder where uploads are saved when using local FS | `/var/lib/outline/data` |
| `FILE_STORAGE_UPLOAD_MAX_SIZE` | Upload size limit in bytes | `26214400` (25MB) |

### 🔐 OpenID Connect (OIDC) / Authentik Integration

| Variable | Description | Example |
|----|----|----|
| `OIDC_CLIENT_ID` | Client ID from Authentik OAuth2 Provider | `outline-client` |
| `OIDC_CLIENT_SECRET` | Client Secret from Authentik | `supersecretclientkey` |
| `OIDC_AUTH_URI` | Authentik authorize endpoint | `https://auth.domain.com/application/o/authorize/` |
| `OIDC_TOKEN_URI` | Authentik token endpoint | `https://auth.domain.com/application/o/token/` |
| `OIDC_USERINFO_URI` | Authentik userinfo endpoint | `https://auth.domain.com/application/o/userinfo/` |
| `OIDC_LOGOUT_URI` | Redirect URI on logout | `https://auth.domain.com/application/o/end-session/` |
| `OIDC_USERNAME_CLAIM` | Field from userinfo to use as Outline username | `preferred_username` |
| `OIDC_DISPLAY_NAME` | Display name for login button in Outline | `Authentik` |
| `OIDC_SCOPES` | OIDC scopes to request | `openid profile email` |

### 📧 SMTP / Email Settings

| Variable | Description | Example |
|----|----|----|
| `SMTP_HOST` | SMTP server address | `smtp.mailgun.org` |
| `SMTP_PORT` | SMTP server port | `587` |
| `SMTP_USERNAME` | SMTP username or sender address | `no-reply@domain.com` |
| `SMTP_PASSWORD` | SMTP account password | `emailpassword` |
| `SMTP_FROM_EMAIL` | Default sender email address | `wiki@domain.com` |
| `SMTP_REPLY_EMAIL` | Reply-to email address | `support@domain.com` |
| `SMTP_TLS_CIPHERS` | Optional TLS ciphers (usually leave blank) | (blank or `TLS_AES_256_GCM_SHA384` etc.) |
| `SMTP_SECURE` | Whether to use SSL (`true`) or startTLS (`false`) | `false` |

### 🧪 Optional Debugging or Advanced Settings (if applicable)

| Variable | Description | Example |
|----|----|----|
| `PGSSLMODE` | SSL mode for Postgres connection | `disable` |
| `LOG_LEVEL` | Adjust app verbosity | `info`, `debug`, `error` |


---

## 🧪 Sample Configuration

* Markdown documents are stored in Postgres (not on disk)
* Files uploaded (like images) are stored in `/var/lib/outline/data`
* You can switch to S3/MinIO storage by setting `FILE_STORAGE=s3` and adding the relevant env vars


---

## 🛠️ Tips & Customization

* Add logo and branding in Settings > Appearance
* Use Collections for departments or categories
* Grant edit/view/create permissions per group
* Set `FILE_STORAGE_UPLOAD_MAX_SIZE` if uploading large media files
* Integrate with Slack or Webhooks for notifications


---

## 🧯 Troubleshooting Notes

* ⚠️ **Auth loop?** Double-check `OIDC_*` values and callback URLs
* 🧱 **App crashes?** Ensure `SECRET_KEY` and `UTILS_SECRET` are set and not empty
* 🔍 **Search isn’t working?** Try clearing cache or restarting Redis
* 📧 **No email notifications?** Confirm SMTP settings and firewall rules


---

## 📚 More Info

* [Outline Official Site](https://www.getoutline.com/)
* [GitHub Repo](https://github.com/outline/outline)
* [Environment Variables Guide](https://wiki.generaloutline.com/s/environment-variables)
* [Authentik Configuration Doc](https://docs.goauthentik.io/integrations/services/outline/)


---

## 🧼 Cleanup

```bash
docker-compose down -v
```


