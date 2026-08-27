from typing import NamedTuple


class Paint(NamedTuple):
    name: str
    rgb: tuple[int, int, int]
    # suggestion: str
    
STUDENT_PALETTE = [
    Paint(
        "Titanium White",
        (245, 245, 240),
    ),
    
    Paint(
        "Yellow Ochre",
        (190, 145, 55),
    ),
    
    Paint(
        "Burnt Sienna",
        (145, 65, 40),
    ),
    
    Paint(
        "Raw Umber",
        (90, 75, 55),
    ),
    
    Paint(
        "Ultramarine Blue",
        (45, 55, 120),
    ),
    
    Paint(
        "Cadmium Red",
        (190, 45, 40),
    ),
    
    Paint(
        "Cadmium Yellow",
        (240, 190, 40),
    ),
]


MIXING_RATIOS = [
    (1, 1),
    (2, 1),
    (1, 2),
    (3, 1),
    (1, 3),
]
    
"""
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
"""


def colour_distance(
    colour_a: tuple[int, int, int],
    colour_b: tuple[int, int, int],
) -> float:
    
    return sum(
        (a - b) ** 2
        for a, b in zip(colour_a, colour_b)
    ) ** 0.5
      
   
def find_closest_paint(
    target_colour: tuple[int, int, int],
) -> Paint:
    
    return min(
        STUDENT_PALETTE,
        key=lambda paint: colour_distance(
            target_colour,
            paint.rgb
        ),
    )
    
    
def mix_two_colours(
    colour_a: tuple[int, int, int],
    colour_b: tuple[int, int, int],
    parts_a: int = 1,
    parts_b: int = 1,
) -> tuple[int, int, int]:
    
    total_parts = parts_a + parts_b
    
    return tuple(
        int(((a * parts_a) + (b * parts_b)) / total_parts) for a, b in zip(colour_a, colour_b)
    )


def find_closest_two_paint_mix(
    target_colour: tuple[int, int, int],
):
    best_paints = None
    best_ratio = None
    best_colour = None
    best_distance = float("inf")

    for index, paint_a in enumerate(STUDENT_PALETTE):
        for paint_b in STUDENT_PALETTE[index + 1:]:

            for parts_a, parts_b in MIXING_RATIOS:

                mixed_colour = mix_two_colours(
                    paint_a.rgb,
                    paint_b.rgb,
                    parts_a,
                    parts_b,
                )

                distance = colour_distance(
                    target_colour,
                    mixed_colour,
                )

                if distance < best_distance:
                    best_distance = distance
                    best_paints = (
                        paint_a,
                        paint_b,
                    )
                    best_ratio = (
                        parts_a,
                        parts_b,
                    )
                    best_colour = mixed_colour

    return (
        best_paints,
        best_ratio,
        best_colour,
        best_distance,
    )
