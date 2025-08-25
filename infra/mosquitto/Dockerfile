FROM eclipse-mosquitto:2.0

# Copy config into the standard path
COPY mosquitto.conf /mosquitto/config/mosquitto.conf

# Create a dev password file inside the image (local dev only)
RUN mosquitto_passwd -c -b /mosquitto/config/passwd dev devpass

# Data & log as volumes
VOLUME ["/mosquitto/data", "/mosquitto/log"]

EXPOSE 1883
