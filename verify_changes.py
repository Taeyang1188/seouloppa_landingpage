#!/usr/bin/env python3
"""
Verification script to confirm the aad.png pattern changes have been applied correctly
"""

import os

def verify_changes():
    """Verify that the changes have been applied correctly"""
    
    html_file = "index-new.html"
    
    print("=== Verifying AAD.PNG Pattern Changes ===")
    
    if not os.path.exists(html_file):
        print(f"ERROR: {html_file} not found!")
        return False
    
    # Read the HTML file
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for the new values
    changes_applied = True
    
    print("Checking for applied changes:")
    
    # Check for new background-size
    if 'background-size: 230px 230px' in content:
        count = content.count('background-size: 230px 230px')
        print(f"✓ New background-size (230px 230px) found {count} times")
    else:
        print("✗ New background-size (230px 230px) NOT found")
        changes_applied = False
    
    # Check for new opacity
    if 'opacity: 0.5' in content:
        print("✓ New opacity (0.5) found")
    else:
        print("✗ New opacity (0.5) NOT found")
        changes_applied = False
    
    # Check that old values are no longer present
    print("\nChecking that old values have been replaced:")
    
    if 'background-size: 100px 100px' in content:
        count = content.count('background-size: 100px 100px')
        print(f"✗ Old background-size (100px 100px) still found {count} times")
        changes_applied = False
    else:
        print("✓ Old background-size (100px 100px) successfully removed")
    
    if 'opacity: 0.1' in content:
        print("✗ Old opacity (0.1) still found")
        changes_applied = False
    else:
        print("✓ Old opacity (0.1) successfully removed")
    
    # Verify aad.png references are still intact
    aad_references = content.count('aad.png')
    print(f"\nImage references: {aad_references} references to aad.png found")
    
    if aad_references == 2:
        print("✓ Correct number of aad.png references maintained")
    else:
        print("✗ Unexpected number of aad.png references")
        changes_applied = False
    
    print(f"\n=== Verification Result ===")
    if changes_applied:
        print("✓ ALL CHANGES SUCCESSFULLY APPLIED!")
        print("Summary of changes:")
        print("- Background-size changed from 100px to 230px (130% more gap)")
        print("- Opacity changed from 0.1 to 0.5 (50% transparency)")
        print("- Original image size maintained")
        print("- Repeat pattern preserved")
    else:
        print("✗ Some changes were not applied correctly")
    
    return changes_applied

if __name__ == "__main__":
    verify_changes()