from datetime import datetime

# Replace with your birthdate
birthdate = datetime(2001, 12, 30)
now = datetime.utcnow()

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

# File to update
file_path = "profile_card_expanded_ascii.svg"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the {{AGE}} placeholder
content = content.replace("{{AGE}}", age_str)

# Write updated SVG
with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
