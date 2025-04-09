# 🏡 Goug's HomeLab Docker Templates

Welcome to **Goug's HomeLab** — a growing collection of Docker Compose templates for apps I use or test in my HomeLab. These templates are built to help you get up and running quickly with no bloated configs or mysterious dependencies.

Each app folder includes:

* `docker-compose.yml` — core container setup
* `.env` — customizable environment variables
* `README.md` — you're reading it!
* Sample config files (if needed)

Explore more at [goug76/docker-templates](https://github.com/goug76/docker-templates).


---

## 📦 Grafana

[Grafana](https://grafana.com/) is a popular open-source platform for monitoring, observability, and dashboards. It supports a wide range of data sources like Prometheus, InfluxDB, Loki, MySQL, PostgreSQL, and more — all in a slick UI that’s built for customization and sharing.

This setup includes built-in OAuth support using **Authentik**, role-based access control, and optional automatic login.


---

## 🧰 Features

* Intuitive, responsive dashboard builder
* Supports over 50+ data sources
* Built-in alerting, graphing, and panels
* User, team, and role-based access
* OAuth2 login support (here: via Authentik)


---

## 🚀 Getting Started

### 🐳 Docker Compose

```yaml
---
services:
  grafana:
    container_name: grafana
    image: grafana/grafana
    user: "1000"
    restart: unless-stopped
    ports:
     - '3030:3000'
    environment:
      GF_SECURITY_ADMIN_USER: admin
      GF_SECURITY_ADMIN_PASSWORD: changeme
      GF_AUTH_GENERIC_OAUTH_ENABLED: "true"
      GF_AUTH_GENERIC_OAUTH_NAME: "authentik"
      GF_AUTH_GENERIC_OAUTH_CLIENT_ID: ${GF_AUTH_GENERIC_OAUTH_CLIENT_ID}
      GF_AUTH_GENERIC_OAUTH_CLIENT_SECRET: ${GF_AUTH_GENERIC_OAUTH_CLIENT_SECRET}
      GF_AUTH_GENERIC_OAUTH_SCOPES: "openid profile email"
      GF_AUTH_GENERIC_OAUTH_AUTH_URL: ${GF_AUTH_GENERIC_OAUTH_AUTH_URL}
      GF_AUTH_GENERIC_OAUTH_TOKEN_URL: ${GF_AUTH_GENERIC_OAUTH_TOKEN_URL}
      GF_AUTH_GENERIC_OAUTH_API_URL: ${GF_AUTH_GENERIC_OAUTH_API_URL}
      GF_AUTH_GENERIC_OAUTH_ROLE_ATTRIBUTE_PATH: "contains(groups, 'Grafana Admins') && 'Admin' || contains(groups, 'Grafana Editors') && 'Editor' || 'Viewer'"
      GF_SERVER_ROOT_URL: ${GF_SERVER_ROOT_URL}
      # Optionally enable auto-login (bypasses Grafana login screen)
      GF_AUTH_OAUTH_AUTO_LOGIN: "false"
      GF_SECURITY_ALLOW_EMBEDDING: "true"
      TZ: $TZ
    volumes:
      - $DOCKERDIR/grafana/datasources:/etc/grafana/provisioning/datasources
      - $DOCKERDIR/grafana:/var/lib/grafana
      - $DOCKERDIR/grafana/config/custom.ini:/etc/grafana/grafana.ini
    networks:
      - monitoring
```

> ⚠️ Be sure to copy and edit the `.env` file included in this directory.


---

## ⚙️ Environment Variables

| Variable | Description | Example |
|----|----|----|
| `DOCKERDIR` | Docker file Location | `/home/user/docker` |
| `TZ` | Timezone | `America/New_York` |
| `GF_SECURITY_ADMIN_USER` | Default admin username | `admin` |
| `GF_SECURITY_ADMIN_PASSWORD` | Admin password | `changeme` |
| `GF_AUTH_GENERIC_OAUTH_CLIENT_ID` | OAuth client ID from Authentik | `grafana-client-id` |
| `GF_AUTH_GENERIC_OAUTH_CLIENT_SECRET` | OAuth secret | `grafana-client-secret` |
| `GF_AUTH_GENERIC_OAUTH_AUTH_URL` | Authentik OAuth authorization endpoint | `https://auth.example.com/application/o/authorize/` |
| `GF_AUTH_GENERIC_OAUTH_TOKEN_URL` | OAuth token endpoint | `https://auth.example.com/application/o/token/` |
| `GF_AUTH_GENERIC_OAUTH_API_URL` | User info endpoint | `https://auth.example.com/application/o/userinfo/` |
| `GF_SERVER_ROOT_URL` | Public URL of Grafana | `https://grafana.domain.com` |
| `GF_AUTH_OAUTH_AUTO_LOGIN` | Skip Grafana login page | `"true"` or `"false"` |


---

## 🧪 Sample Configuration

* Pre-provision data sources by adding .yaml files in /provisioning/datasources
* Customize the look and feel using grafana.ini or custom plugins
* All dashboard and user data is stored in /var/lib/grafana


---

## 🛠️ Tips & Customization

* Use GF_AUTH_DISABLE_LOGIN_FORM=true to disable local logins entirely
* Mount dashboards to /var/lib/grafana/dashboards for version-controlled visuals
* If you use Loki, Tempo, or Prometheus — Grafana has built-in visualizers for each
* Add GF_SMTP_ variables to enable email alerts


---

## 🧯 Troubleshooting Notes

* 🧪 **OAuth not working?** Confirm redirect URI, token URLs, and client credentials
* 🔐 **Login page keeps appearing?** Set GF_AUTH_OAUTH_AUTO_LOGIN=true
* 📉 **No dashboards?** Provision default boards via /provisioning/dashboards
* 🧱 **Plugin errors?** Some plugins require persistence or browser reload


---

## 📚 More Info

* [Grafana Docs](https://grafana.com/docs/)
* [OAuth Setup for Grafana](https://grafana.com/docs/grafana/latest/setup-grafana/configure-security/configure-authentication/generic-oauth/)
* [Authentik Configuration Doc](https://docs.goauthentik.io/integrations/services/grafana/)


---

## 🧼 Cleanup

```bash
docker-compose down -v
```
