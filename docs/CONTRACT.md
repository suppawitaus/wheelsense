# Wheelsense Data Contract (v1)

## Topics (MQTT)
- Telemetry (QoS 1, **not retained**):  
  `wheelsense/<deviceId>/telemetry/<sensorKind>`
- Status (QoS 1, **retained**):  
  `wheelsense/<deviceId>/status`
- Commands (QoS 1, not retained):  
  `wheelsense/<deviceId>/cmd/<action>`
- (Later) HA Discovery (QoS 1, **retained**):  
  `homeassistant/<platform>/<uniqueId>/config`

`deviceId`: lowercase, `[a-z0-9_-]{3,32}` (e.g., `lr-bme280-01`)  
`sensorKind`: e.g., `bme280`, `co2`, `pir`  
`action`: e.g., `relay_set`, `interval_set`

## Common fields
- `schema`: string, version, e.g. `"1.0"`
- `ts`: integer, Unix seconds UTC
- Units: embedded in keys (e.g., `temp_c`, `hum_pct`, `press_hpa`)

## QoS / Retain
- Telemetry: QoS 1, retain = false
- Status: QoS 1, retain = true
- Commands: QoS 1, retain = false
- HA Discovery: QoS 1, retain = true

## Payloads

### Telemetry
```json
{
  "schema": "1.0",
  "ts": 1724563200,
  "sensor": "bme280",
  "values": { "temp_c": 28.3, "hum_pct": 61.2, "press_hpa": 1006.5 },
  "meta": { "rssi_dbm": -58 }
}
