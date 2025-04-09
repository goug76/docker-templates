# 🏡 Goug's HomeLab Docker Templates

Welcome to **Goug's HomeLab** — a growing collection of Docker Compose templates for apps I use or test in my HomeLab. These templates are built to help you get up and running quickly with no bloated configs or mysterious dependencies.

Each app folder includes:

* `docker-compose.yml` — core container setup
* `.env` — customizable environment variables
* `README.md` — you're reading it!
* Sample config files (if needed)

Explore more at [goug76/docker-templates](https://github.com/goug76/docker-templates).

---

## 📦 PostgreSQL (Postgres)

[PostgreSQL](https://www.postgresql.org/) is a powerful, open-source object-relational database system that's trusted by developers, sysadmins, and large-scale apps worldwide. Whether you're storing app data, user credentials, or structured logs, it's a rock-solid backend choice.

This setup uses version `16` and includes health checks, secure permissions, and persistent storage.

---

## 🧰 Features

* Standards-compliant SQL engine
* ACID-compliant transactions
* Strong data integrity and reliability
* Excellent performance and scalability
* Works out of the box with apps like Outline, Authentik, pgAdmin, and more

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
      TZ: '${TZ}'
    networks:
      - database
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -h localhost -U $$POSTGRES_USER"]
      interval: 2s
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

---

## 🧪 Sample Configuration

* All data is persisted to `$DOCKERDIR/postgres`
* `POSTGRES_USER` and `POSTGRES_PASSWORD` define the default superuser
* First-time startup will initialize the DB volume and apply credentials
* Use `pgAdmin` or CLI tools to manage schemas, users, and permissions

---

## 🛠️ Tips & Customization

* For better performance, mount a dedicated SSD or use a Docker volume
* Add additional `POSTGRES_DB=myapp` to pre-create databases on boot
* Use `pg_isready` or `docker exec` for manual connection testing
* Avoid exposing `5432` publicly — pair with VPN or SSH tunnels for remote access

---

## 🧯 Troubleshooting Notes

* 🔄 **App can't connect?** Verify DB credentials and network settings
* ⏱️ **Startup slow?** Health checks may delay container readiness
* 📂 **Data not saving?** Check that the volume is mounted and writable
* 🔒 **Security hardening?** Use `pg_hba.conf` to restrict IP ranges if needed

---

## 📚 More Info

* [PostgreSQL Official Site](https://www.postgresql.org/)
* [Docker Image on DockerHub](https://hub.docker.com/_/postgres)
* [PostgreSQL Docs]()
* [pg_isready Utility](https://www.postgresql.org/docs/current/app-pg-isready.html)

---

## 🧼 Cleanup

```bash
docker-compose down -v
```
