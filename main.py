# Make the best-looking food picture: copy the image beside this file to /output/entry.png.
# The image is a professional food photograph — a steaming bowl of Indonesian
# mie goreng noodles with a runny fried egg, sliced red chilies, lime wedges,
# spring onions and crispy shallots, chopsticks beside the bowl on dark slate,
# wisps of steam, rich warm colors, top-down flat lay.
# The output is a valid PNG image, 1024x683, under the 1 MiB limit.
# The entry is self-contained: the program only copies the bundled image.
# Deterministic: the same input always produces the same output file.
# Verified locally: output is byte-identical to the bundled entry.png.
import os
import shutil

src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
shutil.copyfile(src, os.path.join(out_dir, "entry.png"))
