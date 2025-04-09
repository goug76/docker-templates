# 🏡 Goug's HomeLab Docker Templates

Welcome to **Goug's HomeLab** — a growing collection of Docker Compose templates for apps I use or test in my HomeLab. These templates are built to help you get up and running quickly with no bloated configs or mysterious dependencies.

Each app folder includes:

* `docker-compose.yml` — core container setup
* `.env` — customizable environment variables
* `README.md` — you're reading it!
* Sample config files (if needed)

Explore more at [goug76/docker-templates](https://github.com/goug76/docker-templates).

---

## 📦 Semaphore (Ansible GUI)

[Semaphore](https://github.com/ansible-semaphore/semaphore) is a modern, open-source web UI for managing and executing **Ansible playbooks**. It gives you role-based access control, task history, scheduling, secrets management, and a clean UI for managing inventory and jobs — all powered by your existing Ansible skills.

---

## 🧰 Features

* Web-based GUI for executing Ansible playbooks
* Role-based permissions for users and teams
* Store inventories, environments, secrets, and templates
* Real-time logs and job status dashboards
* PostgreSQL backend for full persistence

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

  semaphore:
    container_name: semaphore
    image: semaphoreui/semaphore:latest
    restart: unless-stopped
    ports:
      - 3001:3000
    environment:
      SEMAPHORE_DB_USER: ${USER}
      SEMAPHORE_DB_PASS: '${SEMAPHORE_DB_PASS}'
      SEMAPHORE_DB_HOST: postgres # for postgres, change to: postgres
      SEMAPHORE_DB_PORT: 5432 # change to 5432 for postgres
      SEMAPHORE_DB_DIALECT: postgres # for postgres, change to: postgres
      SEMAPHORE_DB: semaphore
      SEMAPHORE_PLAYBOOK_PATH: /tmp/semaphore/
      SEMAPHORE_ADMIN_PASSWORD: '${SEMAPHORE_ADMIN_PASSWORD}'
      SEMAPHORE_ADMIN_NAME: Administrator
      SEMAPHORE_ADMIN_EMAIL: ${ADMIN_EMAIL}
      SEMAPHORE_ADMIN: ${SEMAPHORE_USER}
      SEMAPHORE_ACCESS_KEY_ENCRYPTION: '${SEMAPHORE_ACCESS_KEY_ENCRYPTION}'
      ANSIBLE_HOST_KEY_CHECKING: false
      TZ: ${TZ}
    volumes: 
      - $DOCKERDIR/semaphore:/etc/semaphore
    depends_on:
      postgres:
        condition: service_healthy
    networks:
      - database
```

> ⚠️ Be sure to copy and edit the `.env` file included in this directory.

---

## ⚙️ Environment Variables

| Variable | Description | Example |
|----|----|----|
| `USER` | Postgres database user | `semaphore` |
| `SEMAPHORE_DB_PASS` | Password for Postgres | `supersecurepass` |
| `DOCKERDIR` | Docker file Location | `/home/user/docker` |
| `SEMAPHORE_DB` | Name of the Semaphore DB | `semaphore` |
| `SEMAPHORE_USER` | Admin username for web login | `admin` |
| `SEMAPHORE_ADMIN_PASSWORD` | Admin web UI password | `yourpassword` |
| `SEMAPHORE_ADMIN_EMAIL` | Admin email address | `admin@example.com` |
| `SEMAPHORE_ACCESS_KEY_ENCRYPTION` | Key used to encrypt stored secrets | `base64secretkey` |
| `TZ` | Timezone | `America/New_York` |

> 🔐 Use `openssl rand -base64 32` to generate a strong value for SEMAPHORE_ACCESS_KEY_ENCRYPTION.

---

## 🧪 Sample Configuration

* Database is hosted via the `postgres` container
* Semaphore persists config and playbooks under `$DOCKERDIR/semaphore`
* Playbooks are run from `/tmp/semaphore/` (mounted inside the container)
* Use the web UI to add inventories, secrets, environments, and templates

---

## 🛠️ Tips & Customization

* Schedule playbook runs or trigger manually via the UI
* Store sensitive SSH/private keys using secrets
* Separate environments for dev, staging, and prod
* Use labels/tags to organize your jobs and projects

---

## 🧯 Troubleshooting Notes

* 🔄 **Container won’t start?** Ensure Postgres is healthy and available on the same network
* 🔑 **Secrets not decrypting?** Check that `SEMAPHORE_ACCESS_KEY_ENCRYPTION` hasn’t changed
* 📥 **Playbooks not showing?** Verify that they exist inside `/tmp/semaphore/` or upload them via the UI
* 🔐 **UI exposed publicly?** Protect it with Authentik or a firewall

---

## 📚 More Info

* [Semaphore GitHub](https://github.com/ansible-semaphore/semaphore)
* [Official Docs](https://docs.semaphoreui.com/)
* [PostgreSQL Docs](https://www.postgresql.org/docs/)
* [Authentik Configuation Doc](https://docs.goauthentik.io/integrations/services/semaphore/)

---

## 🧼 Cleanup

```bash
docker-compose down -v
```
