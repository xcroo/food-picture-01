#!/usr/bin/env python3
"""food-picture-01 entry: put the bundled food photograph in the output folder.

The photograph is a top-down shot of a bowl of Indonesian fried noodles,
fresh off the wok and still giving off steam. On top sit a fried egg with a
soft yolk, slices of red chilli, lime wedges, chopped spring onion and a
sprinkle of crisp shallots; a pair of chopsticks lies on the dark slate
beside the bowl. Warm tones, generous garnish, clearly the hero of the frame.

This script does no image work at all. It simply carries the finished picture
that ships next to it into the directory the harness expects
(MAKEFUN_OUTPUT_DIR, falling back to /output). Because it is a plain copy,
every run yields the identical file: a 1024x683 PNG, well inside the 1 MiB
limit.
"""

import os
from pathlib import Path


def main() -> None:
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    target.write_bytes(source.read_bytes())
    # Sanity check: the copy must be the same size as the bundled image,
    # otherwise something went wrong mid-write and we fail loudly.
    if target.stat().st_size != source.stat().st_size:
        raise RuntimeError("copied entry.png does not match the bundled image")
    print(f"Wrote {target} ({target.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
