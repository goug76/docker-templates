# 🏡 Goug's HomeLab Docker Templates

Welcome to **Goug's HomeLab** — a growing collection of Docker Compose templates for apps I use or test in my HomeLab. These templates are built to help you get up and running quickly with no bloated configs or mysterious dependencies.

Each app folder includes:

* `docker-compose.yml` — core container setup
* `.env` — customizable environment variables
* `README.md` — you're reading it!
* Sample config files (if needed)

Explore more at [goug76/docker-templates](https://github.com/goug76/docker-templates).

---

## 📦 Proxmox VE Exporter

The [Prometheus PVE Exporter](https://github.com/prometheus-pve/prometheus-pve-exporter) collects system and virtual machine metrics from your **Proxmox VE** instance and makes them available to **Prometheus**. This is ideal for getting deep visibility into your Proxmox server, cluster health, node stats, and even per-VM metrics — all from Grafana dashboards.

---

## 🧰 Features

* Exposes metrics from Proxmox VMs, LXC containers, and nodes
* Compatible with Prometheus and Grafana
* Supports token-based authentication
* Optional SSL verification skip for local homelabs
* Lightweight and easy to deploy

---

## 🚀 Getting Started

### 🐳 Docker Compose

```yaml
---
services:
  pve-exporter:
    container_name: pve-exporter
    image: prompve/prometheus-pve-exporter
    restart: unless-stopped
    ports:
      - "9221:9221"
    volumes:
      - $DOCKERDIR/pve/pve.yml:/etc/prometheus/pve.yml
    networks: 
      - monitoring
```

> 🧠 Exporter will listen on http://<host>:9221/pve

---

## ⚙️ Config File: `pve.yml`

```yaml
default:
    user: <Proxmox User>
    token_name: "<Token ID from API Token>"
    token_value: "<Token from API Token>"
    # Optional: set to false to skip SSL/TLS verification
    verify_ssl: false
```

> 🔐 You must create an API Token in the Proxmox UI (Datacenter > Permissions > API Tokens)

---

## 🔧 Prometheus Integration

Add this job to your prometheus.yml to start scraping PVE metrics:

```yaml
# Prometheus PVE Exporter
- job_name: 'pve'
  static_configs:
    - targets:
        - 192.168.1.x  # IP of your Proxmox VE node
  metrics_path: /pve
  params:
    module: [default]
    cluster: ['1']
    node: ['1']
  relabel_configs:
    - source_labels: [__address__]
      target_label: __param_target
    - source_labels: [__param_target]
      target_label: instance
    - target_label: __address__
      replacement: 192.168.1.x:9221  # IP of PVE exporter container
```

> 📍 You'll need to match your actual IPs for both the Proxmox node and exporter.

---

## ⚙️ Environment Variables

| Variable | Description | Example |
|----|----|----|
| `DOCKERDIR` | Docker file Location | `/home/user/docker` |

---

## 🧪 Sample Configuration

* PVE API tokens must have permission to `/` with `PVEAuditor` role
* If you’re using self-signed certs, set `verify_ssl: false`
* The exporter calls `/api2/json/` endpoints from your Proxmox server every 15s by default (based on Prometheus scrape interval)

---

## 🛠️ Tips & Customization

* You can configure multiple Proxmox nodes in the `pve.yml` file by adding more entries under different module names
* Combine with [Grafana dashboards](https://grafana.com/grafana/dashboards?search=proxmox) for instant insights
* Use the `--log.level=debug` flag for troubleshooting startup or token errors

---

## 🧯 Troubleshooting Notes

* ❌ **401 Unauthorized?** Make sure your API token has proper ACL permissions
* 🧱 **No metrics showing?** Confirm Proxmox node IP and that the exporter is accessible on port `9221`
* 🔄 **Metrics not updating?** Check scrape interval and relabel configs in Prometheus
* 🔐 **SSL issues?** Set `verify_ssl: false` if using self-signed certs

---

## 📚 More Info

* [Exporter GitHub Repo](https://github.com/prometheus-pve/prometheus-pve-exporter)
* [Proxmox API Docs](https://pve.proxmox.com/pve-docs/api-viewer/)
* [Grafana Proxmox Dashboards](https://grafana.com/grafana/dashboards?search=proxmox)
* [Proxmox Token Setup Guide](https://pve.proxmox.com/wiki/User_Management#API_Tokens)

---

## 🧼 Cleanup

```bash
docker-compose down -v
```
