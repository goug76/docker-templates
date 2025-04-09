# 🏡 Goug's HomeLab Docker Templates

Welcome to **Goug's HomeLab** — a growing collection of Docker Compose templates for apps I use or test in my HomeLab. These templates are built to help you get up and running quickly with no bloated configs or mysterious dependencies.

Each app folder includes:

* `docker-compose.yml` — core container setup
* `.env` — customizable environment variables
* `README.md` — you're reading it!
* Sample config files (if needed)

Explore more at [goug76/docker-templates](https://github.com/goug76/docker-templates).

---

## 📦 Redis

[Redis](https://redis.io/) is an ultra-fast, in-memory key-value store used as a database, cache, and message broker. It's commonly used for session storage, pub/sub systems, and background queues.

In this homelab setup, Redis is used as a dependency for several apps including **Authentik**, **Outline**, and potentially others in your monitoring or automation stack.

---

## 🧰 Features

* Lightning-fast key-value storage
* Pub/Sub and stream support
* TTL-based caching for session data
* Supports basic persistence with snapshots
* Used as a backend by many modern web apps

---

## 🚀 Getting Started

### 🐳 Docker Compose

```yaml
---
services:
  redis:
    container_name: redis
    image: docker.io/library/redis:alpine
    command: redis-server /redis.conf --save 60 1 --loglevel warning
    restart: unless-stopped
    ports:
      - "6379:6379"
    volumes:
      - $DOCKERDIR/redis:/data
    networks:
      - database
    healthcheck:
      test: ["CMD-SHELL", "redis-cli ping | grep PONG"]
      start_period: 20s
      interval: 30s
      retries: 5
      timeout: 3s
```

> ⚠️ Be sure to copy and edit the `.env` file included in this directory.

---

## ⚙️ Configuration Notes

- `--save 60 1`: Snapshot the DB every 60 seconds if at least 1 key changed.
- `--loglevel warning`: Limits log verbosity to important events only.
- No password or TLS is enabled in this lightweight config — secure it behind internal networks/firewalls.

If you need password protection:

```bash
redis-server /redis.conf --requirepass your_secure_password
```

## ⚙️ Environment Variables

| Variable | Description | Example |
|----|----|----|
| `DOCKERDIR` | Docker file Location | `/home/user/docker` |

---

## 🧪 Sample Configuration

* Data is stored in $DOCKERDIR/redis (as dump.rdb)
* Make sure other containers in the same Docker network use redis:6379 in their env configs
* You can use redis-cli from another container or install it locally to test:

```bash
docker exec -it redis redis-cli ping
# Should return: PONG
```

---

## 🛠️ Tips & Customization

* Use `redis:alpine` for small footprint or `redis:latest` for more built-in tooling
* If you need clustering or replication, use Redis Sentinel or Redis Stack (advanced)
* Secure with password + TLS if exposing beyond Docker (use `requirepass` and `tls-port`)

---

## 🧯 Troubleshooting Notes

* ⚠️ **App can't connect?** Confirm that Redis is reachable from the app's container and on the same network
* 🔁 **Redis data not persisting?** Check volume mount path and write permissions
* 🔒 **Need security?** Redis by default allows unauthenticated access — only expose internally or add a password
* 🚫 **High CPU usage?** Review client behavior — some apps retry aggressively on failure

---

## 📚 More Info

* [Redis Official Site](https://redis.io/)
* [Docker Redis Docs](https://hub.docker.com/_/redis)
* [Redis CLI Commands](https://redis.io/commands/)
* [RedisInsight GUI](https://www.redis.com/redis-enterprise/redis-insight/)

---

## 🧼 Cleanup

```bash
docker-compose down -v
```
