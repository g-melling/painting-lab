from painting_lab.paint_mixing import (
    STUDENT_PALETTE,
    MIXING_RATIOS,
    colour_distance,
    find_closest_paint,
    mix_two_colours,
    find_closest_two_paint_mix,
)

def test_student_palette_is_not_empty():
    assert len(STUDENT_PALETTE) > 0


def test_colour_distance_same_colour_is_zero():
    colour = (100, 120, 140)

    result = colour_distance(
        colour,
        colour,
    )

    assert result == 0


def test_mix_two_colours_returns_average():
    colour_a = (100, 50, 0)
    colour_b = (200, 150, 100)

    result = mix_two_colours(
        colour_a,
        colour_b,
    )

    assert result == (150, 100, 50)


def test_find_closest_paint_returns_exact_match():
    target = (190, 145, 55)

    result = find_closest_paint(target)

    assert result.name == "Yellow Ochre"


def test_two_paint_mix_returns_two_paints():
    target = (170, 110, 50)

    paints, ratio, mixed_colour, distance = (
        find_closest_two_paint_mix(target)
    )

    assert len(paints) == 2
    assert len(mixed_colour) == 3
    assert distance >= 0


def test_mix_two_colours_one_to_one():
    result = mix_two_colours(
        (100, 50, 0),
        (200, 150, 100),
        1,
        1,
    )

    assert result == (150, 100, 50)


def test_mix_two_colours_two_to_one():
    result = mix_two_colours(
        (100, 100, 100),
        (200, 200, 200),
        2,
        1,
    )

    assert result == (133, 133, 133)


def test_two_paint_mix_returns_ratio():
    target = (170, 110, 50)

    paints, ratio, mixed_colour, distance = (
        find_closest_two_paint_mix(target)
    )

    assert len(paints) == 2
    assert ratio in MIXING_RATIOS
    assert len(mixed_colour) == 3
    assert distance >= 0