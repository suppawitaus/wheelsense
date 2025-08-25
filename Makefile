SHELL := /bin/sh

up:
\tdocker compose up -d --build

down:
\tdocker compose down -v

logs:
\tdocker compose logs -f --tail=150

mqtt-shell:
\tdocker exec -it wheelsense_mosquitto sh
