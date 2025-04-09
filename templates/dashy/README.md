# 🏡 Goug's HomeLab Docker Templates

Welcome to **Goug's HomeLab** — a growing collection of Docker Compose templates for apps I use or test in my HomeLab. These templates are built to help you get up and running quickly with no bloated configs or mysterious dependencies.

Each app folder includes:

* `docker-compose.yml` — core container setup
* `.env` — customizable environment variables
* `README.md` — you're reading it!
* Sample config files (if needed)

Explore more at [goug76/docker-templates](https://github.com/goug76/docker-templates).


---

## 📦 Dashy

[Dashy](https://github.com/Lissy93/dashy) is a highly customizable self-hosted dashboard that helps you organize and access all your homelab services from a single place. It’s open-source, has a sleek UI, and supports YAML-based configuration for total control over layout and content.


---

## 🧰 Features

* Gorgeous and responsive interface out of the box
* Fully YAML-configurable UI
* Supports custom icons, themes, and link groups
* Live status indicators and health checks
* Easy to extend with custom HTML, widgets, and shortcuts


---

## 🚀 Getting Started

### 🐳 Docker Compose

```yaml
---
services:
  dashy:
    container_name: dashy
    image: lissy93/dashy:latest
    restart: unless-stopped
    ports:
      - 80:8080
    environment:
      - TZ=$TZ
    volumes:
      - $DOCKERDIR/dashy/conf.yml:/app/user-data/conf.yml
      - $DOCKERDIR/dashy/icons:/app/public/item-icons/icons
    networks:
      - default
```

> ⚠️ Be sure to copy and edit the `.env` file included in this directory.


---

## ⚙️ Environment Variables

| Variable | Description | Example |
|----|----|----|
| `DOCKERDIR` | Docker file Location | `/home/user/docker` |
| `TZ` | Timezone | `America/New_York` |


---

## 🧪 Sample Configuration

Here’s a sample conf.yml to get started:

```yaml
# Page meta info, like heading, footer text and nav links
pageInfo:
  title: Dashy
  description: Welcome to your new dashboard!
  navLinks:
    - title: GitHub
      path: https://github.com/Lissy93/dashy
    - title: Documentation
      path: https://dashy.to/docs

appConfig:
  theme: colorful

sections:
  - name: Getting Started
    icon: fas fa-rocket
    items:
      - title: Dashy Live
        description: Development & project links
        icon: https://i.ibb.co/qWWpD0v/astro-dab-128.png
        url: https://live.dashy.to/
        target: newtab
      - title: GitHub
        description: Source Code, Issues and PRs
        url: https://github.com/lissy93/dashy
        icon: favicon
      - title: Docs
        description: Usage Documentation
        url: https://dashy.to/docs
        icon: far fa-book
      - title: Showcase
        description: Community dashboards
        url: https://github.com/Lissy93/dashy/blob/master/docs/showcase.md
        icon: far fa-grin-hearts
      - title: Config Guide
        description: Full list of configuration options
        url: https://github.com/Lissy93/dashy/blob/master/docs/configuring.md
        icon: fas fa-wrench
      - title: Support
        description: Help, bug reports, contact
        url: https://github.com/Lissy93/dashy/blob/master/.github/SUPPORT.md
        icon: far fa-hands-helping
```


---

## 🛠️ Tips & Customization

* Use your own icons/ folder to store personalized icons for each app
* Health checks can be enabled per app using the statusCheck option in YAML
* You can load custom HTML, embed widgets, or group apps into nested sections
* Dashy has a built-in config editor at /edit when not locked


---

## 🧯 Troubleshooting Notes

* 🧪 **Blank screen?** Likely due to malformed YAML — validate it online
* 🔒 **No Auth?** Use Authentik or secure the port behind a reverse proxy
* 🧹 **Lost settings?** Ensure you're mounting the correct conf.yml volume
* 🌐 **DNS or URL issues?** Check for typos in url: fields in your items


---

## 📚 More Info

* [Dashy GitHub](https://github.com/Lissy93/dashy)
* [Full Config Docs](https://dashy.to/docs)
* [Showcase Gallery](https://github.com/Lissy93/dashy/blob/master/docs/showcase.md)
* [Themes & UI Customization](https://github.com/Lissy93/dashy/blob/master/docs/theming.md)


---

## 🧼 Cleanup

```bash
docker-compose down -v
```
