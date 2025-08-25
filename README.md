## Step 2 — Infrastructure (Docker dev-first)

This repo ships with a dev-first stack:
- **mosquitto** (MQTT broker with auth)
- **api** (FastAPI backend, to be implemented in Step 3)
- **web** (Next.js frontend, to be implemented in Step 4)

### Quick start

```bash
# 1. Copy env
cp .env.example .env

# 2. Build and run the stack
docker compose up -d --build

# 3. Check logs
docker compose logs -f mosquitto
