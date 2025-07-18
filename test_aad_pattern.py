#!/usr/bin/env python3
"""
Test script to verify the aad.png pattern implementation
"""

import os
import webbrowser
import time

def test_current_implementation():
    """Test the current implementation of aad.png pattern"""
    
    # Check if the files exist
    html_file = "index-new.html"
    image_file = os.path.join("images", "aad.png")
    
    print("Testing current aad.png pattern implementation...")
    print(f"Checking if {html_file} exists: {os.path.exists(html_file)}")
    print(f"Checking if {image_file} exists: {os.path.exists(image_file)}")
    
    if not os.path.exists(html_file):
        print(f"ERROR: {html_file} not found!")
        return False
        
    if not os.path.exists(image_file):
        print(f"ERROR: {image_file} not found!")
        return False
    
    # Read the HTML file and check for aad.png references
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    aad_references = content.count('aad.png')
    print(f"Found {aad_references} references to aad.png in the HTML file")
    
    # Check current CSS properties
    if 'background-size: 100px 100px' in content:
        print("✓ Current background-size: 100px 100px")
    
    if 'background-repeat: repeat' in content:
        print("✓ Current background-repeat: repeat")
        
    if 'opacity: 0.1' in content:
        print("✓ Current opacity for pseudo-element: 0.1 (10%)")
    
    print("\nCurrent implementation analysis complete.")
    return True

def calculate_new_values():
    """Calculate the new values for the modifications"""
    
    print("\nCalculating new values:")
    
    # Original size: 100px x 100px
    original_size = 100
    
    # For 130% more gap, we need to increase the background-size
    # Gap increase of 130% means the new size should be 100px + (100px * 1.3) = 230px
    new_size = original_size + (original_size * 1.3)
    
    print(f"Original background-size: {original_size}px x {original_size}px")
    print(f"New background-size (130% more gap): {new_size}px x {new_size}px")
    
    # Transparency: 50% = opacity 0.5
    new_opacity = 0.5
    print(f"New opacity: {new_opacity} (50% transparency)")
    
    return int(new_size), new_opacity

if __name__ == "__main__":
    print("=== AAD.PNG Pattern Test Script ===")
    
    # Test current implementation
    if test_current_implementation():
        # Calculate new values
        new_size, new_opacity = calculate_new_values()
        
        print(f"\nRecommended changes:")
        print(f"1. Change background-size from '100px 100px' to '{new_size}px {new_size}px'")
        print(f"2. Change opacity from '0.1' to '{new_opacity}' for 50% transparency")
        print(f"3. Keep original image size but increase spacing between repetitions")
    
    print("\nTest completed.")