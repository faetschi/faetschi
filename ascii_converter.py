from PIL import Image

# ASCII character set from darkest to lightest
ASCII_CHARS = "@%#*+=-:. "

# Resize the image
def resize_image(image, new_width=40, new_height=30):
    return image.resize((new_width, new_height))

# Convert image to grayscale
def grayify(image):
    return image.convert("L")

# Map grayscale pixels to ASCII characters with contrast adjustment
def pixels_to_ascii(image):
    pixels = image.getdata()
    gamma = 1.6  # Higher = more contrast
    def contrast_map(pixel):
        norm = pixel / 255
        adjusted = norm ** gamma
        index = int(adjusted * (len(ASCII_CHARS) - 1))
        return ASCII_CHARS[index]
    return "".join(contrast_map(p) for p in pixels)

# Full conversion: image path → list of ASCII lines
def image_to_ascii(path):
    image = Image.open(path)
    image = resize_image(image)
    image = grayify(image)
    ascii_str = pixels_to_ascii(image)
    lines = [ascii_str[i:i+40] for i in range(0, 40 * 30, 40)]
    return lines

# --- MAIN EXECUTION ---

image_path = r"C:\Users\Admin\Documents\Downloads\asciitest.jpg" # change image path
ascii_lines = image_to_ascii(image_path)

# Ensure 30 lines
while len(ascii_lines) < 30:
    ascii_lines.append(" " * 40)

# Find the index of the first non-blank line
start_index = next((i for i, line in enumerate(ascii_lines) if line.strip()), 0)

# Output SVG <tspan> lines with dynamic Y starting at y=30 for the first visible line
for i, line in enumerate(ascii_lines[start_index:], start=0):
    y = 30 + i * 20
    print(f'<tspan x="15" y="{y}">{line.ljust(40)}</tspan>')
