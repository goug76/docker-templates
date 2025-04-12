# 🏡 Goug's HomeLab Docker Templates

Welcome to **Goug's HomeLab** — a growing collection of Docker Compose templates for apps I use or test in my HomeLab. These templates are built to help you get up and running quickly with no bloated configs or mysterious dependencies.

Each app folder includes:

* `docker-compose.yml` — core container setup
* `.env` — customizable environment variables
* `README.md` — you're reading it!
* Sample config files (if needed)

Explore more at [goug76/docker-templates](https://github.com/goug76/docker-templates).

---

## 📦 Code-server

**Code-server** lets you run VS Code in your browser, turning your homelab into a full-featured development environment. It's perfect for remote coding, quick edits, or managing projects without needing a local IDE.

---

## 🧰 Features

* Browser-based VS Code interface
* Persistent workspace and settings
* Support for extensions and themes
* Secure access with optional password protection

---

## 🚀 Getting Started

### 🐳 Docker Compose

```yaml
---
services:
  code-server:
    container_name: code-server
    image: lscr.io/linuxserver/code-server:latest
    restart: unless-stopped
    ports:
      - 8443:8443
    environment:
      - PUID=${PUID}
      - PGID=${PGID}
      - TZ=${TZ}
      - SUDO_PASSWORD_HASH=${SUDO_PASSWORD_HASH} 
      - DEFAULT_WORKSPACE=/config/workspace 
    volumes:
      - $DOCKERDIR/code-server/config:/config
```

> ⚠️ Be sure to copy and edit the `.env` file included in this directory.

---

## ⚙️ Environment Variables

| Variable | Description | Example |
|----|----|----|
| `PUID` | User ID for file ownership | `1000` |
| `PGID` | Group ID for file ownership | `1000` |
| `TZ` | Timezone | `America/New_York` |
| `DOCKERDIR` | Docker file Location | `/home/user/docker` |
| `SUDO_PASSWORD_HASH` | Hashed password for sudo access | `$y$j9T$...` |
| `DEFAULT_WORKSPACE` | Default directory opened in VS Code | `/config/workspace` |

---

## 🧪 Sample Configuration

* * All user data, settings, and extensions are stored in `/config`
  * Customize your workspace by adding files inside the `workspace` folder
  * For pre-seeding: add `.vscode/settings.json` or extensions to `/config`

---

## 🛠️ Tips & Customization

* * Use Nginx Proxy Manager with SSL and Auth for secure public access
  * Mount project folders directly into `/config/workspace` for easy access
  * Enable extension sync by logging in with your GitHub or Microsoft account

---

## 🧯 Troubleshooting Notes

* * If the UI doesn't load, check container logs with `docker logs code-server`
  * Reset the password by regenerating `SUDO_PASSWORD_HASH` and restarting
  * Permissions issues? Ensure your `PUID`/`PGID` match your local user

---

## 📚 More Info

* * [Official Docs](https://coder.com/docs)
  * [Code-server GitHub](https://github.com/coder/code-server)
  * [LinuxServer Code-Server Doc](https://docs.linuxserver.io/images/docker-code-server/)

---

## 🧼 Cleanup

```bash
docker-compose down -v
```
