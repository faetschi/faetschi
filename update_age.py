import re
from datetime import datetime, timezone

# Your birthdate
birthdate = datetime(2001, 12, 30, tzinfo=timezone.utc)
now = datetime.now(timezone.utc)

# Calculate age
years = now.year - birthdate.year
months = now.month - birthdate.month
days = now.day - birthdate.day
if days < 0:
    months -= 1
    days += 30  # rough approx.
if months < 0:
    years -= 1
    months += 12

age_str = f"{years} years, {months} months, {days} days"

# Calculate dynamic dots to keep visual balance
target_total_width = 62  # baseline from your example
uptime_label_length = len("Uptime:")  # 7
spacing = 2  # spaces around dots
dots_needed = target_total_width - uptime_label_length - spacing - len(age_str)
dots = "." * max(dots_needed, 0)

# Load SVG
file_path = "profile.svg"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace age
content = re.sub(
    r'(<tspan class="value" id="age_data">)(.*?)(</tspan>)',
    rf'\1{age_str}\3',
    content
)

# Replace dots
content = re.sub(
    r'(<tspan class="cc" id="age_data_dots">)(.*?)(</tspan>)',
    rf'\1 {dots} \3',
    content
)

# Save updated SVG
with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
