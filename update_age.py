from datetime import datetime, timezone
from bs4 import BeautifulSoup

# Age calculation
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

# Visual balance
target_width = 62
label_len = len("Uptime:")
padding = 2
dots_len = target_width - label_len - padding - len(age_str)
dots = "." * max(dots_len, 0)

# Read and parse SVG
with open("profile.svg", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "xml")

# Replace dots
dots_tag = soup.find("tspan", {"id": "age_data_dots"})
if dots_tag:
    dots_tag.string = f" {dots} "

# Replace age
age_tag = soup.find("tspan", {"id": "age_data"})
if age_tag:
    age_tag.string = age_str

# Write back SVG
with open("profile.svg", "w", encoding="utf-8") as f:
    f.write(str(soup))
