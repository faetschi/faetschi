from datetime import datetime, timezone
from bs4 import BeautifulSoup

# === 1. Age calculation ===
birthdate = datetime(2001, 12, 30, tzinfo=timezone.utc)
now = datetime.now(timezone.utc)

years = now.year - birthdate.year
months = now.month - birthdate.month
days = now.day - birthdate.day
if days < 0:
    months -= 1
    days += 30
if months < 0:
    years -= 1
    months += 12

age_str = f"{years} years, {months} months, {days} days"

# === 2. Visual alignment using character count ===
# The ideal line length, based on your working screenshot
TARGET_LINE_LEN = 59  # Total characters across the whole line

label = "Uptime:"
space_after_label = " "
gap = " "  # Space between dots and age string

fixed_part_len = len(label + ":" + space_after_label + gap + age_str)
dots_len = TARGET_LINE_LEN - fixed_part_len
dots = "." * max(dots_len, 0)

# === 3. Update SVG ===
with open("profile.svg", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "xml")

dots_tag = soup.find("tspan", {"id": "age_data_dots"})
if dots_tag:
    dots_tag.string = f" {dots} "

age_tag = soup.find("tspan", {"id": "age_data"})
if age_tag:
    age_tag.string = age_str

with open("profile.svg", "w", encoding="utf-8") as f:
    f.write(str(soup))

print("SVG updated!")
