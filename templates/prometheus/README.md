# 🏡 Goug's HomeLab Docker Templates

Welcome to **Goug's HomeLab** — a growing collection of Docker Compose templates for apps I use or test in my HomeLab. These templates are built to help you get up and running quickly with no bloated configs or mysterious dependencies.

Each app folder includes:

* `docker-compose.yml` — core container setup
* `.env` — customizable environment variables
* `README.md` — you're reading it!
* Sample config files (if needed)

Explore more at [goug76/docker-templates](https://github.com/goug76/docker-templates).

---

## 📦 Prometheus

[Prometheus](https://prometheus.io/) is an open-source monitoring system and time series database built for high-performance metric collection. It’s the go-to backend for pulling in metrics from your containers, services, VMs, and IoT devices.

This setup supports **live config reloads**, **container metrics scraping**, and integrates with tools like Grafana, Alertmanager, and Blackbox Exporter.

---

## 🧰 Features

* Time-series metrics storage (TSDB)
* Pull-based metrics collection (scraping)
* Powerful PromQL query language
* Live reloading and admin API enabled
* Integrates with Node Exporter, cAdvisor, Blackbox, and more

---

## 🚀 Getting Started

### 🐳 Docker Compose

```yaml
---
services:
  prometheus:
    container_name: prometheus
    image: prom/prometheus
    user: "0"
    restart: unless-stopped
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
      - '--storage.tsdb.path=/prometheus' 
      - '--web.console.libraries=/etc/prometheus/console_libraries' 
      - '--web.console.templates=/etc/prometheus/consoles' 
      - '--web.enable-lifecycle'
      - '--web.enable-admin-api'
    ports:
      - 9091:9090
    environment:
      - TZ=$TZ
    volumes:
      - $DOCKERDIR/prometheus:/etc/prometheus
      - $DOCKERDIR/prometheus:/prometheus
    networks:
      - monitoring
```

> ⚠️ Be sure to copy and edit the `.env` file included in this directory.

---

## ⚙️ Environment Variables

| Variable | Description | Example |
|----|----|----|
| `DOCKERDIR` | Docker file Location | `/home/user/docker` |
| `TZ` | Your time zone | `America/New_York` |

---

## 🧪 Sample Configuration

Here’s a preloaded prometheus.yml:

```yaml
# my global config
# Reload Prometheus with: curl -X POST http://<host>:9091/-/reload

global:
  scrape_interval: 15s # Set how often metrics are scraped (default: 60s)

scrape_configs:
  # Self-scrape (Prometheus monitors itself)
  - job_name: "prometheus"
    static_configs:
      - targets: ["localhost:9090"]

  # Node Exporter (for system metrics)
  # - job_name: "node_exporter"
  #   static_configs:
  #     - targets: ["node-exporter:9100"]

  # cAdvisor (for container metrics)
  # - job_name: "cadvisor"
  #   static_configs:
  #     - targets: ["cadvisor:8080"]

  # Blackbox Exporter (ping/http/dns/etc.)
  # - job_name: "blackbox"
  #   metrics_path: /probe
  #   params:
  #     module: [http_2xx]
  #   static_configs:
  #     - targets:
  #         - https://example.com
  #   relabel_configs:
  #     - source_labels: [__address__]
  #       target_label: __param_target
  #     - source_labels: [__param_target]
  #       target_label: instance
  #     - target_label: __address__
  #       replacement: blackbox-exporter:9115

# TODO:
# - Add alerting rules under rule_files:
# - Enable remote_write if integrating with Grafana Cloud or Thanos
```

---

## 🛠️ Tips & Customization

* Use `--web.enable-lifecycle` to support `/-/reload` for config updates
* Hook up **Grafana** as a frontend for visual dashboards
* Mount external alerting rules or use Alertmanager for notifications
* Add `remote_write` to ship metrics to external storage (e.g., InfluxDB, Cortex)

---

## 🧯 Troubleshooting Notes

* 🧱 **"Target down"?** Ensure services are reachable on the right ports/IPs
* 🔄 **Reload failed?** Confirm config syntax with `promtool check config`
* 🧪 **Missing metrics?** Review `scrape_interval`, target labels, and exporter configs
* 🔒 **Securing UI?** Use Authentik proxy or serve behind VPN

---

## 📚 More Info

* [Prometheus Docs](https://prometheus.io/docs/)
* [PromQL Basics](https://prometheus.io/docs/prometheus/latest/querying/basics/)
* [Best Exporters List](https://prometheus.io/docs/instrumenting/exporters/)

---

## 🧼 Cleanup

```bash
docker-compose down -v
```
