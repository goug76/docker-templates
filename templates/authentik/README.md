# 🏡 Goug's HomeLab Docker Templates

Welcome to **Goug's HomeLab** — a growing collection of Docker Compose templates for apps I use or test in my HomeLab. These templates are built to help you get up and running quickly with no bloated configs or mysterious dependencies.

Each app folder includes:

* `docker-compose.yml` — core container setup
* `.env` — customizable environment variables
* `README.md` — you're reading it!
* Sample config files (if needed)

Explore more at [goug76/docker-templates](https://github.com/goug76/docker-templates).


---

## 📦 Authentik

[Authentik](https://goauthentik.io) is an open-source Identity Provider built for modern infrastructure. It supports SSO, OIDC, SAML, LDAP, and reverse proxy authentication — making it an excellent choice for homelab environments looking to centralize authentication and authorization securely.


---

## 🧰 Features

* Single Sign-On support (OIDC, SAML, LDAP)
* Reverse proxy authentication
* Per-app policies and access control
* Web UI for admin and users
* Email notifications and flows (reset, invite, verify)
* Runs well in Docker with PostgreSQL and Redis


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

  server:
    container_name: authentik-server
    image: ghcr.io/goauthentik/server
    restart: unless-stopped
    command: server
    environment:
      AUTHENTIK_REDIS__HOST: redis
      AUTHENTIK_POSTGRESQL__HOST: postgres
      AUTHENTIK_POSTGRESQL__USER: ${USER}
      AUTHENTIK_POSTGRESQL__NAME: authentik
      AUTHENTIK_POSTGRESQL__PASSWORD: ${POSTGRES_PASSWORD}
      AUTHENTIK_ERROR_REPORTING__ENABLED: true
      AUTHENTIK_SECRET_KEY: ${AUTHENTIK_SECRET_KEY}
      AUTHENTIK_EMAIL__HOST: ${AUTHENTIK_EMAIL__HOST}
      AUTHENTIK_EMAIL__PORT: ${AUTHENTIK_EMAIL__PORT}
      AUTHENTIK_EMAIL__USERNAME: ${AUTHENTIK_EMAIL__USERNAME}
      AUTHENTIK_EMAIL__PASSWORD: ${AUTHENTIK_EMAIL__PASSWORD}
      AUTHENTIK_EMAIL__USE_TLS: ${AUTHENTIK_EMAIL__USE_TLS}
      AUTHENTIK_EMAIL__USE_SSL: ${AUTHENTIK_EMAIL__USE_SSL}
      AUTHENTIK_EMAIL__TIMEOUT: ${AUTHENTIK_EMAIL__TIMEOUT}
      AUTHENTIK_EMAIL__FROM: ${AUTHENTIK_EMAIL__FROM}
    volumes:
      - $DOCKERDIR/authentik/media:/media
      - $DOCKERDIR/authentik/custom-templates:/templates
    ports:
      - "9000:9000"
      - "8443:9443"
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy
    networks:
      - database
      
  worker:
    container_name: authentik-worker
    image: ghcr.io/goauthentik/server
    restart: unless-stopped
    command: worker
    environment:
      AUTHENTIK_REDIS__HOST: redis
      AUTHENTIK_POSTGRESQL__HOST: postgres
      AUTHENTIK_POSTGRESQL__USER: ${USER}
      AUTHENTIK_POSTGRESQL__NAME: authentik
      AUTHENTIK_POSTGRESQL__PASSWORD: ${POSTGRES_PASSWORD}
      AUTHENTIK_ERROR_REPORTING__ENABLED: true
      AUTHENTIK_SECRET_KEY: ${AUTHENTIK_SECRET_KEY}
      AUTHENTIK_EMAIL__HOST: ${AUTHENTIK_EMAIL__HOST}
      AUTHENTIK_EMAIL__PORT: ${AUTHENTIK_EMAIL__PORT}
      AUTHENTIK_EMAIL__USERNAME: ${AUTHENTIK_EMAIL__USERNAME}
      AUTHENTIK_EMAIL__PASSWORD: ${AUTHENTIK_EMAIL__PASSWORD}
      AUTHENTIK_EMAIL__USE_TLS: ${AUTHENTIK_EMAIL__USE_TLS}
      AUTHENTIK_EMAIL__USE_SSL: ${AUTHENTIK_EMAIL__USE_SSL}
      AUTHENTIK_EMAIL__TIMEOUT: ${AUTHENTIK_EMAIL__TIMEOUT}
      AUTHENTIK_EMAIL__FROM: ${AUTHENTIK_EMAIL__FROM}
    user: root
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - $DOCKERDIR/authentik/media:/media
      - $DOCKERDIR/authentik/certs:/certs
      - $DOCKERDIR/authentik/custom-templates:/templates
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

| Variable | Description | Example |
|----|----|----|
| `USER` | Postgres database user | `authentik` |
| `POSTGRES_PASSWORD` | Password for Postgres | `supersecurepass` |
| `DOCKERDIR` | Docker file Location | `/home/user/docker` |
| `AUTHENTIK_SECRET_KEY` | Django secret key (use a long random string) | \`openssl rand 60 |
| `AUTHENTIK_EMAIL__HOST` | SMTP host | `smtp.mailserver.com` |
| `AUTHENTIK_EMAIL__PORT` | SMTP port | `587` |
| `AUTHENTIK_EMAIL__USERNAME	` | SMTP username | `user@example.com` |
| `AUTHENTIK_EMAIL__PASSWORD` | SMTP password | `emailpass` |
| `AUTHENTIK_EMAIL__USE_TLS` | Enable TLS | `true` |
| `AUTHENTIK_EMAIL__USE_SSL` | Enable SSL (if not using TLS) | `false` |
| `AUTHENTIK_EMAIL__TIMEOUT` | SMTP timeout in seconds | `10` |
| `AUTHENTIK_EMAIL__FROM` | "From" address for system emails | `noreply@example.com` |
| `TZ` | Timezone | `America/New_York` |


---

## 🧪 Sample Configuration

* Where config files go, how to use them, etc.
* Tips for pre-seeding configs or backup/restore


---

## 🛠️ Tips & Customization

* Performance tuning
* DNS tweaks, security hardening, etc.


---

## 🧯 Troubleshooting Notes

* Common issues and fixes
* Log file locations or container-specific quirks


---

## 📚 More Info

* [Authentik Docs](https://goauthentik.io/docs/)
* [Proxy Provider Guide](https://goauthentik.io/docs/providers/proxy/)
* [OIDC Setup](https://goauthentik.io/docs/providers/oidc/)
* [SAML Setup](https://goauthentik.io/docs/providers/saml/)


---

## 🧼 Cleanup

```bash
docker-compose down -v
```


