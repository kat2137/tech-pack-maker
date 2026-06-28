import dataclasses

@dataclass
class Attribute:
    name: str            # "seam_type", "pocket_type", "topstitched"...
    value: str
    source: str          # observed | inferred | manual
    confidence: float = 1.0
    note: str = ""       # which rule produced it

@dataclass
class Element:
    kind: str            # "seam" | "pocket" | "hem" | "dart" | "placket" | "edge"
    location: str        # "outseam" | "inseam" | "back right" | "neckline" | "hem"
    attributes: list     # list of Attribute
    region: tuple = None # optional point/box on the drawing for the arrow