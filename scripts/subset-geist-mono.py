# /// script
# requires-python = ">=3.11"
# dependencies = ["fonttools==4.68.0", "brotli==1.2.1"]
# ///

# Regenerates src/fonts/GeistMonoVariable-{latin,rest}.woff2,
# src/fonts/InterVariable-keys.woff2, src/fonts/geist-mono.css and
# src/fonts/LICENSE-GeistMono.txt.
#
# Run it with uv, which installs the two dependencies above (fontTools reads and
# subsets the font, brotli writes woff2):
#
#   uv run scripts/subset-geist-mono.py [geist-font-v1.9.2.zip] [Inter-4.1.zip]
#
# Without arguments it downloads both releases and checks their SHA-256. The
# woff2 files differ byte for byte between runs (fontTools stamps head.modified),
# so regenerate only when the subsets or the release change.

import hashlib
import io
import sys
import textwrap
import urllib.request
import zipfile
from pathlib import Path

from fontTools import subset
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

RELEASE_URL = (
    "https://github.com/vercel/geist-font/releases/download/v1.9.2/geist-font-v1.9.2.zip"
)
RELEASE_SHA256 = "15f066d58dcb99fb10014a49913009fdaf41e464cfb8851a44b44e593c95d3d8"
SOURCE = "geist-font/GeistMono/webfonts/GeistMono[wght].woff2"
LICENSE = "geist-font/OFL.txt"

INTER_RELEASE_URL = "https://github.com/rsms/inter/releases/download/v4.1/Inter-4.1.zip"
INTER_RELEASE_SHA256 = "9883fdd4a49d4fb66bd8177ba6625ef9a64aa45899767dde3d36aa425756b11e"
INTER_SOURCE = "web/InterVariable.woff2"
OUT_DIR = Path(__file__).resolve().parent.parent / "src/fonts"
NAME = "GeistMonoVariable"

# The same latin range as scripts/subset-inter.py, so both fonts split alike.
CORE_RANGES = (
    "U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,"
    "U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,"
    "U+FEFF,U+FFFD,U+03A9,U+03BC,U+2190-21FF,U+2264-2265,U+221E,U+2248,"
    "U+2260,U+2318,U+2713,U+2717,U+23CE"
)

# Key symbols that Geist Mono 1.9.2 lacks: control, command, option and escape.
# Without them a shortcut such as "⌘ ⇧ P" draws ⌘ in the platform fallback font
# and ⇧ in Geist Mono. A third 'Geist Mono' face draws these few from Inter, so
# every key symbol comes from a font the package ships.
KEY_RANGES = "U+2303,U+2318,U+2325,U+238B"


def parse_ranges(ranges: str) -> set[int]:
    codepoints = set()
    for part in ranges.split(","):
        start, _, end = part.strip().removeprefix("U+").partition("-")
        codepoints.update(range(int(start, 16), int(end or start, 16) + 1))
    return codepoints


def format_ranges(codepoints: set[int], others: set[int]) -> str:
    """Collapses codepoints into ranges, bridging short gaps that hold none of `others`.

    A long bridge would make text in scripts Geist Mono lacks, such as CJK or
    emoji, download a file with nothing for it.
    """
    ranges = []
    for cp in sorted(codepoints):
        gap = range(ranges[-1][1] + 1, cp) if ranges else None
        if gap is not None and len(gap) <= 32 and not any(c in others for c in gap):
            ranges[-1][1] = cp
        else:
            ranges.append([cp, cp])
    return ", ".join(
        f"U+{a:04X}" if a == b else f"U+{a:04X}-{b:04X}" for a, b in ranges
    )


def read_release(path: str | None, url: str, sha256: str, name: str) -> zipfile.ZipFile:
    data = Path(path).read_bytes() if path else urllib.request.urlopen(url).read()
    if hashlib.sha256(data).hexdigest() != sha256:
        sys.exit(f"{name} release does not match its SHA-256")
    return zipfile.ZipFile(io.BytesIO(data))


def write_subset(font: TTFont, codepoints: set[int], path: Path) -> None:
    options = subset.Options()
    options.layout_features = ["*"]
    options.name_IDs = ["*"]
    options.name_languages = ["*"]
    options.notdef_outline = True
    options.hinting = False
    subsetter = subset.Subsetter(options=options)
    subsetter.populate(unicodes=codepoints)
    subsetter.subset(font)
    font.flavor = "woff2"
    font.save(path)


def face(filename: str, unicode_range: str) -> str:
    """Formats one face. `unicode_range` starts with a space or a line break."""
    return (
        "@font-face {\n"
        "\tfont-family: 'Geist Mono';\n"
        "\tfont-style: normal;\n"
        "\tfont-weight: 100 900;\n"
        "\tfont-display: swap;\n"
        f"\tsrc: url('./{filename}') format('woff2');\n"
        f"\tunicode-range:{unicode_range}\n"
        "}\n"
    )


def write_keys(release: zipfile.ZipFile, available: set[int]) -> str:
    """Writes the Inter subset of the key symbols Geist Mono lacks, returns its face."""
    keys = parse_ranges(KEY_RANGES)
    if keys & available:
        sys.exit("Geist Mono now has some of KEY_RANGES; drop them from the list")
    pinned = io.BytesIO()
    # Pinned like scripts/subset-inter.py, so the symbols match the Inter text faces.
    source = TTFont(io.BytesIO(release.read(INTER_SOURCE)))
    instancer.instantiateVariableFont(source, {"opsz": 14}).save(pinned)
    pinned.seek(0)
    font = TTFont(pinned)
    if not keys <= set(font.getBestCmap()):
        sys.exit("Inter lacks some of KEY_RANGES")
    filename = "InterVariable-keys.woff2"
    write_subset(font, keys, OUT_DIR / filename)
    # Listed one by one: a bridged range would send unrelated symbols to this file.
    return face(filename, " " + ", ".join(f"U+{cp:04X}" for cp in sorted(keys)) + ";")


def main() -> None:
    release = read_release(
        sys.argv[1] if len(sys.argv) > 1 else None, RELEASE_URL, RELEASE_SHA256, "Geist"
    )
    inter = read_release(
        sys.argv[2] if len(sys.argv) > 2 else None,
        INTER_RELEASE_URL,
        INTER_RELEASE_SHA256,
        "Inter",
    )
    core = parse_ranges(CORE_RANGES)

    source = release.read(SOURCE)
    available = set(TTFont(io.BytesIO(source)).getBestCmap())
    parts = {"latin": available & core, "rest": available - core}

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    faces = [write_keys(inter, available)]

    # The latin face comes last so it wins wherever the two ranges meet.
    for part in ("rest", "latin"):
        filename = f"{NAME}-{part}.woff2"
        write_subset(TTFont(io.BytesIO(source)), parts[part], OUT_DIR / filename)
        other = parts["rest" if part == "latin" else "latin"]
        unicode_range = textwrap.fill(
            format_ranges(parts[part], other) + ";",
            width=80,
            initial_indent="\t\t",
            subsequent_indent="\t\t",
            break_long_words=False,
            break_on_hyphens=False,
        )
        faces.append(face(filename, "\n" + unicode_range))

    (OUT_DIR / "geist-mono.css").write_text(
        "/* Generated by scripts/subset-geist-mono.py. */\n\n" + "\n".join(faces)
    )
    (OUT_DIR / "LICENSE-GeistMono.txt").write_bytes(release.read(LICENSE))


if __name__ == "__main__":
    main()
