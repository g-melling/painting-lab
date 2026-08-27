from typing import NamedTuple


class PaintMix(NamedTuple):
    name: str
    rgb: tuple[int, int, int]
    suggestion: str
    
PAINT_MIXES = [
    PaintMix(
        "Light warm neutral",
        (220, 190, 160),
        "Titanium White + Yellow Ochre + a little Burnt Sienna",
    ),
    
    PaintMix(
        "warm midtone",
        (175, 125, 85),
        "Yellow Ochre + Burnt Sienna + a little Titanium White",
    ),
    
    PaintMix(
        "Warm dark",
        (105, 65, 45),
        "Burnt Sienna + Raw Umber",
    ),
    
    PaintMix(
        "Cool dark",
        (55, 65, 75),
        "Ultramarine Blue + Raw Umber",
    ),
    
    PaintMix(
        "Muted Red",
        (150, 70, 60),
        "Cadmium Red + Burnt Sienna + a little Raw Umber",
    ),
    
    PaintMix(
        "Muted Yellow",
        (185, 150, 65),
        "Yellow Ochre + Cadmium Yellow + a little Raw Umber",
    ),
    
    PaintMix(
        "Cool light",
        (185, 195, 205),
        "Titanium White + Ultramarine Blue + a tiny amount of Raw Umber",
    ),
]


def colour_distance(
    colour_a: tuple[int, int, int],
    colour_b: tuple[int, int, int],
) -> float:
    
    return sum(
        (a - b) ** 2
        for a, b in zip(colour_a, colour_b)
    ) ** 0.5
    

def suggest_paint_mix(
    target_colour: tuple[int, int, int],
) -> PaintMix:
    
    return min(
        PAINT_MIXES,
        key=lambda mix: colour_distance(
            target_colour,
            mix.rgb
        ),
    )
