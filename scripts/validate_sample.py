import json
from jsonschema import Draft202012Validator
from pathlib import Path

root = Path(__file__).resolve().parents[1]
contracts = root / "contracts"
samples = root / "samples"

def validate_one(schema_file, sample_file, label):
    schema = json.loads((contracts / schema_file).read_text(encoding="utf-8"))
    data = json.loads((samples / sample_file).read_text(encoding="utf-8"))
    Draft202012Validator(schema).validate(data)
    print(f"✓ {label}: {sample_file} is valid")

def main():
    validate_one("telemetry.schema.json", "telemetry_ok.json", "telemetry")
    validate_one("status.schema.json", "status_ok.json", "status")
    validate_one("command.schema.json", "command_ok.json", "command")
    print("\nAll samples are valid ✅")

if __name__ == "__main__":
    main()
