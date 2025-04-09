# 🏡 Goug's HomeLab Docker Templates

Welcome to **Goug's HomeLab** — a growing collection of Docker Compose templates for apps I use or test in my HomeLab. These templates are built to help you get up and running quickly with no bloated configs or mysterious dependencies.

Each app folder includes:

* `docker-compose.yml` — core container setup
* `.env` — customizable environment variables
* `README.md` — you're reading it!
* Sample config files (if needed)

Explore more at [goug76/docker-templates](https://github.com/goug76/docker-templates).

---

## 📦 Portainer Agent

The **Portainer Agent** is a lightweight companion service for **Portainer** that enables it to manage remote Docker environments or provide **host-level container features** such as live stats, volume browsing, container logs, and more.

> ✅ If you want full host management capabilities or are managing multiple Docker hosts, the **agent is required**. You’ll typically run both `portainer` and `portainer_agent` on the same host.

---

## 🧰 Features

* Required for multi-node management in Portainer
* Enables live container logs, stats, and volume browsing
* Automatically detects and connects with Portainer UI
* Can be deployed on local and remote Docker hosts
* Secure communication with TLS (in Swarm setups)

---

## 🚀 Getting Started

### 🐳 Docker Compose

```yaml
---
services:
  # Portainer - WebUI for Containers
  portainer_agent:
    container_name: portainer_agent
    image: portainer/agent:latest
    security_opt:
      - no-new-privileges:true
    restart: unless-stopped
    ports:
      - 9001:9001
    environment:
      - TZ=$TZ
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro 
      - /var/lib/docker/volumes:/var/lib/docker/volumes:rslave
```

> ⚠️ Be sure to copy and edit the `.env` file included in this directory.

---

## ⚙️ Environment Variables

| Variable | Description | Example |
|----|----|----|
| `TZ` | Your time zone | `America/New_York` |

---

## 🧪 Sample Configuration

* Must be deployed on every Docker host you want Portainer to manage
* Will appear in Portainer as a "remote" endpoint once connected
* Mounts the Docker socket and volume paths for complete visibility
* Default port is `9001`, used by Portainer to communicate securely

---

## 🛠️ Tips & Customization

* If you're managing **only one** host and don't need volume browsing or live stats, the agent is optional
* You **must use the agent** for Swarm setups or remote endpoints
* Combine this with **portainer-ce** on the same device for full feature access
* Avoid exposing port `9001` to the public internet — it's meant for internal use only

---

## 🧯 Troubleshooting Notes

* 🧱 **Agent not showing in Portainer?** Make sure ports are open and the `9001` port is reachable
* 🔒 **Remote agent error?** Double-check Docker socket access and firewall rules
* 🚫 **"Agent unreachable" message?** Restart both Portainer and the agent to re-establish the connection

---

## 📚 More Info

* [Portainer Agent Docs](https://docs.portainer.io/start/install/server/docker/linux)
* [Official GitHub Repo](https://github.com/portainer/portainer)
* [Portainer Docker Image](https://hub.docker.com/r/portainer/agent)
* [Best Practices for Docker Socket Security](https://docs.docker.com/engine/security/)

---

## 🧼 Cleanup

```bash
docker-compose down -v
```
