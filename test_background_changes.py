#!/usr/bin/env python3
"""
Test script to verify the background image changes in index-new.html
"""

import os
import re

def test_current_state():
    """Test the current state of the HTML file"""
    print("=== Testing Current State ===")
    
    # Check if files exist
    html_file = "index-new.html"
    old_image = "images/aad.png"
    new_image = "images/add.png"
    
    print(f"HTML file exists: {os.path.exists(html_file)}")
    print(f"Old image (aad.png) exists: {os.path.exists(old_image)}")
    print(f"New image (add.png) exists: {os.path.exists(new_image)}")
    
    # Read HTML content
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check current background settings
    print("\n=== Current Background Settings ===")
    
    # Find .problems section
    problems_match = re.search(r'\.problems\s*{[^}]+}', content, re.DOTALL)
    if problems_match:
        problems_css = problems_match.group(0)
        print("Found .problems section:")
        print(problems_css)
    
    # Find .problems::before section
    before_match = re.search(r'\.problems::before\s*{[^}]+}', content, re.DOTALL)
    if before_match:
        before_css = before_match.group(0)
        print("\nFound .problems::before section:")
        print(before_css)
    
    # Check for image references
    aad_count = content.count('images/aad.png')
    add_count = content.count('images/add.png')
    
    print(f"\n=== Image References ===")
    print(f"References to 'images/aad.png': {aad_count}")
    print(f"References to 'images/add.png': {add_count}")
    
    return content

def test_after_changes():
    """Test the state after changes are made"""
    print("\n=== Testing After Changes ===")
    
    with open("index-new.html", 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for required changes
    checks = {
        "Uses add.png": 'images/add.png' in content,
        "No aad.png references": 'images/aad.png' not in content,
        "Has grayscale filter": 'filter:' in content and 'grayscale' in content,
        "Has 90deg rotation": 'rotate(90deg)' in content,
        "Has 5% opacity": 'opacity: 0.05' in content,
        "Has no-repeat": 'no-repeat' in content,
        "Has center positioning": 'center' in content
    }
    
    print("Required changes verification:")
    for check, result in checks.items():
        status = "✓" if result else "✗"
        print(f"{status} {check}: {result}")
    
    return all(checks.values())

if __name__ == "__main__":
    # Test current state
    current_content = test_current_state()
    
    print("\n" + "="*50)
    print("Ready to make changes!")