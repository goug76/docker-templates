# 🏡 Goug's HomeLab Docker Templates

Welcome to **Goug's HomeLab** — a growing collection of Docker Compose templates for apps I use or test in my HomeLab. These templates are built to help you get up and running quickly with no bloated configs or mysterious dependencies.

Each app folder includes:

* `docker-compose.yml` — core container setup
* `.env` — customizable environment variables
* `README.md` — you're reading it!
* Sample config files (if needed)

Explore more at [goug76/docker-templates](https://github.com/goug76/docker-templates).


---

## 📦 Step-CA (Smallstep Certificate Authority)

[Step-CA](https://smallstep.com/docs/step-ca/) is a small but powerful local Certificate Authority (CA) server that makes it easy to create and manage TLS certificates for your internal services, devices, and containers — without using a third-party provider.

It's perfect for securing your homelab with trusted certs that *you* control.

---

## 🧰 Features

* Issue TLS and SSH certificates from your own root or intermediate CA
* Automated renewal using ACME and `step` client
* OAuth or password-based authentication for certificate requests
* Built-in web interface (optional) and ACME-compatible APIs
* Works with Kubernetes, Docker, IoT, and traditional servers

---

## 🛠️ Initial Setup (Required Before Running Docker)

You **must initialize the CA** before launching the container for the first time. These steps set up your root CA, intermediate keys, config, and admin credentials.

### 1. Create a working directory

```bash
mkdir -p docker/step
cd docker/step
```

### 2. Initialize the Certificate Authority

Run this interactively on your host system:

```bash
docker run --rm -it \
  -v $PWD:/home/step \
  smallstep/step-ca \
  step ca init \
    --name "Goug Homelab CA" \
    --dns "step-ca.local" \
    --address ":8443" \
    --provisioner "admin@domain.com"
```

> 🧪 Replace the CA name, DNS, and email with your preferred values.

This will create:

* `/home/step/config/ca.json` — Step-CA configuration
* `/home/step/secrets/` — Encrypted CA keys
* `/home/step/certs/` — Public certs

### 3. (Optional) Trust the root CA locally

To install the root CA cert:

```bash
sudo cp $PWD/certs/root_ca.crt /usr/local/share/ca-certificates/goug-ca.crt
sudo update-ca-certificates
```

## 🚀 Getting Started

### 🐳 Docker Compose

```yaml
---
services:
  step-ca:
    container_name: step-ca
    image: smallstep/step-ca
    restart: unless-stopped
    ports:
      - 8443:8443
    environment:
      - TZ=$TZ
    volumes:
      - $DOCKERDIR/step:/home/step
    extra_hosts:
      - '[url]:127.0.0.1'
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

Create Certificate

```bash
step ca certificate your.domain.com your.domain.com.crt your.domain.com.key
```

---

## 🧯 Troubleshooting Notes

* 🔐 **Can’t request certs?** Make sure the provisioner you’re using (OIDC/password/token) is defined in `ca.json`
* 🔄 **Container restarts?** Confirm you initialized the CA before running the container
* 📁 **Missing certs or config?** Double-check volume mapping and folder permissions
* 🌐 **Access fails?** Make sure your DNS is pointing correctly and CA cert is trusted

---

## 📚 More Info

* [Step-CA Docs](https://smallstep.com/docs/step-ca/)
* [GitHub Repo](https://github.com/smallstep/certificates)

---

## 🧼 Cleanup

```bash
docker-compose down -v
```
