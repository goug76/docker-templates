# 🏡 Goug's HomeLab Docker Templates

Welcome to **Goug's HomeLab** — a growing collection of Docker Compose templates for apps I use or test in my HomeLab. These templates are built to help you get up and running quickly with no bloated configs or mysterious dependencies.

Each app folder includes:

* `docker-compose.yml` — core container setup
* `.env` — customizable environment variables
* `README.md` — you're reading it!
* Sample config files (if needed)

Explore more at [goug76/docker-templates](https://github.com/goug76/docker-templates).

---

## 📦 Vikunja (Self-Hosted Task Manager)

[Vikunja](https://vikunja.io/) is a modern, lightweight, self-hosted task manager and project planner — think Todoist meets Trello, but FOSS. It’s a great option for personal use, team collaboration, or organizing your smart home and homelab tasks.

---

## 🧰 Features

* Tasks, lists, labels, and Kanban-style boards
* Due dates, priorities, repeating tasks, reminders
* Sharing and collaboration with team features
* Fast, simple web UI and full REST API
* Native desktop and mobile apps available

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
      POSTGRES_DB: vikunja
      TZ: '${TZ}'
    networks:
      - database
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -h localhost -U $$POSTGRES_USER"]
      interval: 2s

  vikunja:
    container_name: vikunja
    image: vikunja/vikunja
    restart: unless-stopped
    ports:
      - 3456:3456
    environment:
      VIKUNJA_SERVICE_PUBLICURL: ${VIKUNJA_SERVICE_PUBLICURL}
      VIKUNJA_DATABASE_HOST: postgres
      VIKUNJA_DATABASE_PASSWORD: ${POSTGRES_PASSWORD}
      VIKUNJA_DATABASE_TYPE: postgres 
      VIKUNJA_DATABASE_USER: ${USER}
      VIKUNJA_DATABASE_DATABASE: vikunja
      VIKUNJA_SERVICE_JWTSECRET: ${VIKUNJA_SERVICE_JWTSECRET}
      TZ: '${TZ}'
    volumes:
      - $DOCKERDIR/vikunja/files:/app/vikunja/files
      - $DOCKERDIR/vikunja/config.yml:/etc/vikunja/config.yml
    networks:
      - database
    depends_on:
      postgres:
        condition: service_healthy
```

> 🗂️ Access Vikunja at `http://<host>:3456`.

> ✨ First run allows user registration — you’ll create your first account and start building lists!

---

## ⚙️ Environment Variables

| Variable | Description | Example |
|----|----|----|
| `USER` | Postgres database user | `authentik` |
| `POSTGRES_PASSWORD` | Password for Postgres | `supersecurepass` |
| `DOCKERDIR` | Docker file Location | `/home/user/docker` |
| `TZ` | Timezone | `America/New_York` |
| `VIKUNJA_SERVICE_PUBLICURL` | Public base URL for the service | `https://tasks.domain.com` |
| `VIKUNJA_SERVICE_JWTSECRET` | Secret key for token generation | `generate_a_secure_string` |

> 🔐 Use a long, random value for `VIKUNJA_SERVICE_JWTSECRET`. You can generate one with `openssl rand -hex 32`.

---

## 🧪 Sample Configuration

* `/app/vikunja/files` stores uploaded attachments
* `/etc/vikunja/config.yml` can override all environment variables with a persistent config
* You can export/import tasks in `.json` format via the UI
* Set up scheduled tasks or repeating to-dos via task options

---

## 🛠️ Tips & Customization

* Enable **Kanban view** from list options for Trello-like flow
* Assign labels and due dates for productivity tracking
* Use **teams** to collaborate with family, roommates, or coworkers
* Backup `/files` and your DB regularly to preserve data

---

## 🧯 Troubleshooting Notes

* ❌ **UI won’t load?** Check that port `3456` is exposed and the public URL is correct
* 🔑 **Login issues?** Verify JWT secret hasn’t changed between restarts
* 🧾 **Database errors?** Ensure Postgres is healthy and all credentials match
* 🔐 **OAuth not working?** Double-check all Authentik URLs and scopes

---

## 📚 More Info

* [Vikunja Official Site](https://vikunja.io/)
* [Vikunja GitHub](https://github.com/go-vikunja/vikunja)
* [Config Reference](https://vikunja.io/docs/config-options/)
* [Authentik Configuration Guide](https://docs.goauthentik.io/integrations/services/vikunja/)

---

## 🧼 Cleanup

```bash
docker-compose down -vv
```
