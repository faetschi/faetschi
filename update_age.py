import re
from datetime import datetime, timezone

# Use timezone-aware datetimes
birthdate = datetime(2001, 12, 30, tzinfo=timezone.utc)
now = datetime.now(timezone.utc)

# Calculate age
years = now.year - birthdate.year
months = now.month - birthdate.month
days = now.day - birthdate.day
if days < 0:
    months -= 1
    days += 30  # rough approximation
if months < 0:
    years -= 1
    months += 12

age_str = f"{years} years, {months} months, {days} days"

# Visual layout control
target_width = 62  # total "ideal" characters: Uptime: + dots + age
label_len = len("Uptime:")
padding = 2  # spaces before and after dots
dots_len = target_width - label_len - padding - len(age_str)
dots = "." * max(dots_len, 0)

print(f"Calculated age: {age_str}")
print(f"Using {len(dots)} dots: '{dots}'")

# Load SVG
file_path = "profile.svg"
with open(file_path, "r", encoding="utf-8") as f:
    svg_content = f.read()

# Update age string safely
svg_content = re.sub(
    r'(<tspan class="value" id="age_data">)(.*?)(</tspan>)',
    r'\1' + age_str + r'\3',
    svg_content
)

# Update dot string safely
svg_content = re.sub(
    r'(<tspan class="cc" id="age_data_dots">)(.*?)(</tspan>)',
    r'\1 ' + dots + r' \3',
    svg_content
)

# Save changes
with open(file_path, "w", encoding="utf-8") as f:
    f.write(svg_content)
