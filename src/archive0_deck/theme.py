"""Visual identity of the deck: palette, fonts and slide geometry.

Pure data. Measurement lives in :mod:`archive0_deck.typography`; drawing lives in
:mod:`archive0_deck.layout`.
"""

from pptx2.dml.color import RGBColor

# --- slide geometry (inches) --------------------------------------------------
SLIDE_WIDTH = 13.333
SLIDE_HEIGHT = 7.5
CONTENT_LEFT = 0.75
CONTENT_RIGHT = 12.58
CONTENT_WIDTH = CONTENT_RIGHT - CONTENT_LEFT

# --- typefaces ----------------------------------------------------------------
# Arial/Calibri are used because they ship with Office and cover Vietnamese.
FONT_HEAD = "Arial"
FONT_BODY = "Calibri"

# --- palette ------------------------------------------------------------------
BG = RGBColor(0x0A, 0x0F, 0x1F)       # deep navy background
PANEL = RGBColor(0x14, 0x1B, 0x33)    # card background
PANEL2 = RGBColor(0x1B, 0x24, 0x40)   # alternate card background
EDGE = RGBColor(0x2A, 0x35, 0x55)     # card border
LIME = RGBColor(0xC9, 0xF3, 0x1D)     # primary accent
CYAN = RGBColor(0x22, 0xD3, 0xEE)     # secondary accent
PINK = RGBColor(0xFF, 0x3D, 0x81)     # third accent
AMBER = RGBColor(0xFF, 0xB7, 0x03)    # fourth accent
WHITE = RGBColor(0xF7, 0xF9, 0xFC)
BODY = RGBColor(0xC7, 0xCF, 0xE0)
MUTED = RGBColor(0x8A, 0x94, 0xAB)
MUTED2 = RGBColor(0x6E, 0x78, 0x91)
