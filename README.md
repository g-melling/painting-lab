# 🎨 PaintPal

PaintPal is a Python-based educational application designed to help students understand how a reference photograph can be simplified and developed into a drawing or painting. The app can be used in combination with Painting Lab's **GLIMPSE** comparator mirror. 

Rather than simply applying artistic filters, the project aims to break an image into useful learning stages, helping students observe shape, value, colour relationships and traditional painting processes.

The project is currently under active development. Core image-processing, colour-analysis and paint-mixing functionality has been implemented, with GUI development planned as the next major stage.

---

## Project Aim

Learning to draw or paint realistically from a photograph can be difficult because photographs contain a large amount of visual information. PaintPal aims to help students simplify that information.

A reference image can be transformed into a series of studies that emphasise different aspects of the painting process, including:

- major shapes and contours;
- simplified tonal values;
- grayscale studies;
- traditional underpainting approaches;
- dominant colour relationships;
- limited colour palettes;
- suggested starting paint mixtures.

The intention is not for the application to make artistic decisions for the student. Instead, it provides a structured starting point from which students can continue through observation, experimentation and judgement.

---

## Current Features

### Image Loading and Saving

PaintPal supports loading and saving images using Pillow.

Core image I/O functionality includes:

- loading reference images;
- validating image files;
- saving generated studies;
- handling invalid or missing files.

---

### Basic Image Transformations

Several transformations have been implemented to help students examine their reference image in different ways.

These currently include:

- image mirroring;
- grayscale conversion;
- simplified value studies;
- 3-value and 5-value studies.

Reducing an image to a limited number of values can help students identify the major relationships between highlights, midtones and shadows without becoming distracted by photographic detail.

---

## Line Drawing Studies

PaintPal currently contains several experimental approaches to generating line drawings from a reference image.

These include:

- Original Line Drawing
- Detailed Line Drawing
- Simple Line Drawing
- Value-Based Line Drawing

## Traditional Painting Stages

PaintPal also explores several traditional painting methods.

### Grisaille

A grayscale painting study created entirely from light and dark values.

The current implementation:

1. converts the reference image to grayscale;
2. slightly softens photographic detail;
3. reduces the image to a configurable number of tonal steps.

The number of tones can be adjusted to create either a more simplified or more detailed study.

---

### Imprimatura

An imprimatura is a thin initial stain traditionally applied to a painting surface.

PaintPal maps the tonal structure of the grisaille onto an earth-colour scale while preserving the lightest areas.

Current colour options include:

- Burnt Sienna;
- Raw Umber.

---

### Verdaccio

Verdaccio traditionally uses muted green tones as an underpainting, particularly in figurative painting.

The current implementation maps the grisaille structure onto a green tonal range while maintaining lighter values.

---

## Colour Block-In

Painting Lab can simplify a reference photograph into its dominant colour regions.

The current implementation uses **K-means clustering** in the **LAB colour space**.

To improve performance, the image is temporarily reduced in size before clustering rather than processing every pixel of a full-resolution photograph.

The resulting colour block-in is designed to help students identify large colour relationships before concentrating on smaller accents and details.

Small colour accents may intentionally be omitted, encouraging students to continue observing the original reference.

---

## Palette Extraction

The same K-means colour analysis can extract a limited palette from the reference image.

For example, a photograph can be reduced to:

- 8 dominant colours;
- a simplified colour block-in;
- an ordered palette of representative colour swatches.

The extracted colours are ordered according to their prevalence in the analysed image.

The palette is intended to provide the student with clear colour targets rather than reproduce every colour variation in the photograph.

---

## Paint Mixing Guide

The application also contains an experimental paint-mixing assistant.

A basic student palette is currently defined using common painting colours:

- Titanium White;
- Yellow Ochre;
- Burnt Sienna;
- Raw Umber;
- Ultramarine Blue;
- Cadmium Red;
- Cadmium Yellow.

For each colour extracted from the reference photograph, the application searches for an approximate starting mixture using these paints.

The current system considers:

- individual paints;
- two-paint mixtures;
- simple two-paint ratios;
- three-paint mixtures;
- simple three-paint ratios.

The algorithm compares candidate mixtures with the target palette colour and selects the closest available starting recipe.

For example:

```text
Target: Colour 3

Suggested starting mixture:

3 parts Titanium White
1 part Yellow Ochre
1 part Burnt Sienna
```

These recipes are **starting suggestions rather than exact paint formulas**.

Real pigments do not behave in exactly the same way as digital RGB values, and part of the learning process is for the student to compare their physical mixture against the target swatch and adjust it through observation, rather than an identical digital colour match.

---

## Colour Analysis

The project uses both RGB and LAB colour representations for different stages of image analysis.

LAB is particularly useful when comparing colours because it represents perceptual colour relationships more effectively than simply comparing raw RGB channel values.

OpenCV and NumPy are used for colour-space conversion, clustering and numerical image processing.

---

## Testing

The project uses **pytest** for automated testing.

Tests currently cover areas including:

- image loading;
- image saving;
- invalid image handling;
- mirroring;
- grayscale conversion;
- value studies;
- drawing transformations;
- traditional painting-stage transformations;
- paint palette behaviour;
- colour-distance calculations;
- two-colour mixing;
- weighted mixing ratios;
- three-colour mixing;
- RGB range validation;
- selection of paint-mixing recommendations.

Run the test suite with:

```bash
PYTHONPATH=src python -m pytest
```

---

## Project Structure

The project currently follows a `src`-based structure:

```text
painting_lab/
│
├── src/
│   └── painting_lab/
│       ├── __init__.py
│       ├── image_io.py
│       ├── basic_transformations.py
│       ├── drawing.py
│       ├── painting_stages.py
│       └── paint_mixing.py
│
├── tests/
│   ├── test_image_io.py
│   ├── test_basic_transformations.py
│   ├── test_drawing.py
│   ├── test_painting_stages.py
│   └── test_paint_mixing.py
│
├── preview_values.py
├── preview_line_drawing.py
├── preview_imprimatura.py
├── preview_palette.py
├── preview_paint_mixing.py
├── preview_mixing_chart.py
│
├── requirements.txt
└── README.md
```

Preview scripts are currently used during development to evaluate transformations before they are integrated into the final graphical interface.

---

## Technologies

PaintPal currently uses:

- **Python**
- **Pillow** – image loading, manipulation and transformation
- **OpenCV** – image processing, edge detection, colour conversion and K-means clustering
- **NumPy** – numerical image processing
- **pytest** – automated testing

---

## Installation

Clone the repository:

```bash
git clone https://github.com/g-melling/painting-lab.git
cd painting-lab
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it on macOS/Linux:

```bash
source .venv/bin/activate
```

Install the project dependencies:

```bash
pip install -r requirements.txt
```

Run the tests:

```bash
PYTHONPATH=src python -m pytest
```

---

## License

A licence has not yet been specified for this project.