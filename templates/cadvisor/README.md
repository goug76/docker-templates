# 🏡 Goug's HomeLab Docker Templates

Welcome to **Goug's HomeLab** — a growing collection of Docker Compose templates for apps I use or test in my HomeLab. These templates are built to help you get up and running quickly with no bloated configs or mysterious dependencies.

Each app folder includes:

* `docker-compose.yml` — core container setup
* `.env` — customizable environment variables
* `README.md` — you're reading it!
* Sample config files (if needed)

Explore more at [goug76/docker-templates](https://github.com/goug76/docker-templates).


---

## 📦 cAdvisor

[cAdvisor](https://github.com/google/cadvisor) (short for **Container Advisor**) is a lightweight container monitoring tool developed by Google. It provides resource usage and performance stats for Docker containers running on your host — all through a simple web UI.

While it doesn’t offer persistent storage or dashboards like Prometheus/Grafana, it’s incredibly useful for real-time, low-overhead container visibility.


---

## 🧰 Features

* Realtime CPU, memory, network, and filesystem metrics per container
* Simple browser-based UI — no setup required
* Automatically detects all running containers
* Works great alongside Prometheus as a metrics source


---

## 🚀 Getting Started

### 🐳 Docker Compose

```yaml
---
services: 
  cadvisor: 
    container_name: cadvisor 
    image: gcr.io/cadvisor/cadvisor:latest 
    restart: unless-stopped 
    ports: 
      - 8080:8080 
    volumes: 
      - /:/rootfs:ro 
      - /var/run:/var/run:ro 
      - /sys:/sys:ro 
      - /var/lib/docker/:/var/lib/docker:ro
    networks: 
      - monitoring
```

> ⚠️ Be sure to copy and edit the `.env` file included in this directory.


---

## 🧪 Sample Configuration

* No sample config file is needed.

---

## 🛠️ Tips & Customization

* Mount read-only volumes to avoid permission issues
* Use in tandem with **Prometheus** to export metrics over `/metrics`


---

## 🧯 Troubleshooting Notes

* Common issues and fixes
* Log file locations or container-specific quirks


---

## 📚 More Info

* [cAdvisor GitHub](https://github.com/google/cadvisor)
* [Prometheus + cAdvisor](https://prometheus.io/docs/guides/cadvisor/)


---

## 🧼 Cleanup

```bash
docker-compose down -v
```
