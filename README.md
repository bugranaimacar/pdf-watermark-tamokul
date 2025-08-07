# PDF Watermark Tool

This project provides two methods to add the watermark "TAMOKUL" to PDF files starting from page 9.

## Files Overview

- `pdf_watermark_script.py` - Custom Python script using PyPDF2 and reportlab
- `watermark_cli_example.py` - Script using the [pdf-watermark](https://pypi.org/project/pdf-watermark/) CLI tool
- `requirements.txt` - Python dependencies
- `1_ELIFELAERDOGAN_9_2015.pdf` - Input PDF file

## Method 1: Custom Python Script

### Installation
```bash
pip install -r requirements.txt
```

### Usage
```bash
python pdf_watermark_script.py
```

This script will:
- Add watermark "TAMOKUL" starting from page 9
- Keep pages 1-8 unchanged
- Create output file: `1_ELIFELAERDOGAN_9_2015_watermarked.pdf`

## Method 2: Using pdf-watermark CLI Tool

### Installation
```bash
pip install pdf-watermark>=2.2.3
pip install PyPDF2
```

### Usage
```bash
python watermark_cli_example.py
```

Or use the CLI directly:
```bash
# Install the package
pip install pdf-watermark

# Add watermark to entire PDF
watermark grid "1_ELIFELAERDOGAN_9_2015.pdf" "TAMOKUL" -s "output_watermarked.pdf" --opacity 0.2 --angle 45
```

### CLI Features (from pdf-watermark package)

The [pdf-watermark](https://pypi.org/project/pdf-watermark/) package provides two main commands:

#### Grid Command (Recommended)
Adds watermark in a grid pattern across pages:
```bash
watermark grid input.pdf "TAMOKUL" -s output.pdf \
    --opacity 0.2 \
    --angle 45 \
    --text-size 40 \
    --horizontal-boxes 2 \
    --vertical-boxes 3
```

#### Insert Command
Adds watermark at a specific position:
```bash
watermark insert input.pdf "TAMOKUL" -s output.pdf \
    --opacity 0.2 \
    --angle 45 \
    --x 0.5 \
    --y 0.5
```

## Watermark Configuration

Both methods use these settings:
- **Text**: "TAMOKUL"
- **Starting Page**: 9
- **Opacity**: 0.2 (20% transparency)
- **Angle**: 45 degrees
- **Font Size**: 40pt
- **Color**: Gray

## Customization

You can modify the watermark settings by editing the scripts:

### Custom Script Settings
```python
watermark_text = "TAMOKUL"
start_page = 9
opacity = 0.2
angle = 45
font_size = 40
```

### CLI Tool Settings
```bash
--opacity 0.2          # Transparency (0-1)
--angle 45             # Rotation in degrees
--text-size 40         # Font size
--text-color "#808080" # Color in hex
--horizontal-boxes 2   # Grid columns
--vertical-boxes 3     # Grid rows
```

## Output

Both methods will create a watermarked PDF file:
- Pages 1-8: Original content (no watermark)
- Page 9+: Original content with "TAMOKUL" watermark

## Troubleshooting

1. **File not found**: Ensure `1_ELIFELAERDOGAN_9_2015.pdf` is in the current directory
2. **Permission errors**: Check file permissions and ensure PDF is not open in another application
3. **Installation issues**: Use `pip install --upgrade pip` and retry package installation

## Dependencies

- Python 3.7+
- PyPDF2: PDF manipulation
- reportlab: PDF generation and text rendering
- pdf-watermark: CLI tool for watermarking (optional)
