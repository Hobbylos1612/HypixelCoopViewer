import pendulum

# Example timestamp in milliseconds
timestamp_ms = 1747584612526

# Convert milliseconds to seconds for pendulum
dt = pendulum.from_timestamp(timestamp_ms / 1000, tz="Europe/Berlin")

print(dt)            # Full datetime
print(dt.to_datetime_string())  # Pretty format: 'YYYY-MM-DD HH:MM:SS'
