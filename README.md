# 🐳 Goug's HomeLab — Docker Compose Templates

**Purpose:**  
This repository serves as a reference library of working **Docker Compose files** for various services commonly used in home lab setups. These templates are intended for **copy-paste usage**, modification, and inspiration — not as a turnkey stack.

---

## 📁 About This Repo

Rather than one giant `docker-compose.yml` for everything, this repo contains **standalone examples**, each in its own folder, representing services I've tested or used in my home lab.

They’re written with:

- Simplicity in mind (no huge stack dependencies)
- Practicality (tested on systems like Raspberry Pi, Ubuntu, etc.)
- Clear separation so you can use only what you need

---

## 📦 Services Included

Here's a quick overview of what you’ll find:

| Service       | Description                                     |
|---------------|-------------------------------------------------|
| AdGuard Home  | DNS-based ad/tracker blocking                  |
| Grafana       | Dashboarding and visualization tool            |
| Plex          | Media server for local streaming               |
| Portainer     | Web UI to manage Docker                        |
| ...and more   | Explore each folder for more templates         |

Each folder contains a `docker-compose.yml`, an `.env`, `README.md` and sometimes sample config files.

---

## 🛠 How to Use

1. **Browse this repo** and find the service you're interested in
2. Open the folder (e.g., `grafana/`) and review the `docker-compose.yml`
3. Copy the file to your own system and **adjust paths, ports, and variables** to suit your setup
4. Deploy it with Docker:

   ```bash
   docker-compose up -d
   ```
   >These templates are not intended to be used all at once — treat them like ingredients in your own custom home lab recipe. 🧪

   ---

## 🔐 Secure Variables
Some services (like Grafana or Watchtower) may require credentials, API tokens, or secrets. Always do the following:

- Use .env files or Docker secrets
- Never hardcode passwords into compose files
- Adjust volume mounts for persistence (e.g., /config, /data)

---

## 🙋‍♂️ Why Use This?
Because not all Docker Compose examples on the internet are:

- Minimal and easy to understand
- Designed for home lab setups
- Updated or Raspberry Pi-friendly

This repo aims to provide tested, clean, and reusable examples that just make sense.

---

## 📜 License
MIT License — see LICENSE for details.
You're free to use, share, and adapt anything here.

---

## 👨‍🔧 Maintainer
Goug's HomeLab
https://github.com/goug76

---

>⚡ Pro Tip: Bookmark this repo or specific folders to quickly grab Compose files when building out new services.