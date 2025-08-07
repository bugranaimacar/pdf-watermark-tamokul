#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PDF Watermark Script
Adds watermark 'TAMOKUL' to PDF pages starting from page 9
Supports UTF-8 encoding for Turkish characters
"""

import os
import sys
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import gray
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import io


def create_watermark_pdf(text, page_width, page_height, opacity=0.3, angle=45):
    """
    Create a watermark PDF with three diagonal watermarks (top, middle, bottom)
    """
    packet = io.BytesIO()
    
    # Create a new PDF with the watermark
    can = canvas.Canvas(packet, pagesize=(page_width, page_height))
    
    # Set watermark properties
    can.setFillColor(gray, alpha=opacity)
    
    # Use Helvetica-Bold which supports basic Latin characters
    # For better UTF-8 support, we could register a TTF font, but Helvetica works for most cases
    font_name = "Helvetica-Bold"
    font_size = 64
    can.setFont(font_name, font_size)
    
    # Calculate text width for centering
    text_width = can.stringWidth(text, font_name, font_size)
    
    # First watermark - Top position
    can.saveState()
    # Position at top part of the page
    can.translate(page_width / 2, page_height * 0.75)
    can.rotate(angle)
    can.drawString(-text_width / 2, 0, text)
    can.restoreState()
    
    # Second watermark - Middle position
    can.saveState()
    # Position at center of the page
    can.translate(page_width / 2, page_height * 0.5)
    can.rotate(angle)
    can.drawString(-text_width / 2, 0, text)
    can.restoreState()
    
    # Third watermark - Bottom position
    can.saveState()
    # Position at bottom part of the page
    can.translate(page_width / 2, page_height * 0.25)
    can.rotate(angle)
    can.drawString(-text_width / 2, 0, text)
    can.restoreState()
    
    can.save()
    
    # Move to the beginning of the BytesIO buffer
    packet.seek(0)
    return packet


def add_watermark_to_pdf(input_path, output_path, watermark_text="TAMOKUL", start_page=9):
    """
    Add watermark to PDF starting from specified page
    
    Args:
        input_path (str): Path to input PDF file
        output_path (str): Path to output PDF file
        watermark_text (str): Text to use as watermark
        start_page (int): Page number to start watermarking (1-indexed)
    """
    try:
        # Read the input PDF
        reader = PdfReader(input_path)
        writer = PdfWriter()
        
        total_pages = len(reader.pages)
        print(f"Total pages in PDF: {total_pages}")
        
        if start_page > total_pages:
            print(f"Warning: Start page {start_page} is greater than total pages {total_pages}")
            print("No watermark will be added.")
            return False
        
        # Process each page
        for page_num in range(total_pages):
            page = reader.pages[page_num]
            
            # Add watermark only from the specified start page onwards
            if page_num + 1 >= start_page:  # Convert to 1-indexed
                # Get page dimensions
                page_box = page.mediabox
                page_width = float(page_box.width)
                page_height = float(page_box.height)
                
                # Create watermark for this page
                watermark_pdf = create_watermark_pdf(
                    watermark_text, 
                    page_width, 
                    page_height,
                    opacity=0.15,
                    angle=45
                )
                
                # Read the watermark PDF
                watermark_reader = PdfReader(watermark_pdf)
                watermark_page = watermark_reader.pages[0]
                
                # Merge the watermark with the original page
                page.merge_page(watermark_page)
                
                print(f"Added watermark to page {page_num + 1}")
            else:
                print(f"Skipped page {page_num + 1} (before start page)")
            
            # Add the page to the writer
            writer.add_page(page)
        
        # Write the output PDF
        with open(output_path, 'wb') as output_file:
            writer.write(output_file)
        
        print(f"Watermarked PDF saved as: {output_path}")
        return True
        
    except Exception as e:
        print(f"Error processing PDF: {str(e)}")
        return False


def main():
    """
    Main function to run the watermarking process
    """
    # Default file paths
    input_file = "kitap.pdf"
    output_file = "kitap_watermarked.pdf"
    watermark_text = "Tamokul    Tamokul"
    start_page = 9
    
    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found!")
        print("Please make sure the PDF file is in the current directory.")
        return
    
    print(f"Adding watermark '{watermark_text}' to '{input_file}'")
    print(f"Starting from page {start_page}")
    print("-" * 50)
    
    # Add watermark to PDF
    success = add_watermark_to_pdf(
        input_file, 
        output_file, 
        watermark_text, 
        start_page
    )
    
    if success:
        print("-" * 50)
        print("Watermarking completed successfully!")
        print(f"Original file: {input_file}")
        print(f"Watermarked file: {output_file}")
    else:
        print("Watermarking failed!")


if __name__ == "__main__":
    main()
