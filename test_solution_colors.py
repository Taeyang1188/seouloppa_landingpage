#!/usr/bin/env python3
"""
Test script to verify that the solution box text colors are set to bright white (#FFFFFF)
when the button is in expanded state.
"""

import re

def test_solution_colors():
    """Test that solution preview text has bright white color."""
    
    print("Testing solution box text colors...")
    
    # Read the HTML file
    try:
        with open('index-new.html', 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print("❌ Error: index-new.html file not found")
        return False
    
    # Check if the button text exists
    if "나도 후기 남기고 싶지만" not in content:
        print("❌ Error: Button text '나도 후기 남기고 싶지만' not found")
        return False
    else:
        print("✅ Button text '나도 후기 남기고 싶지만' found")
    
    # Check if the solution box title exists
    if "✅ 해결책" not in content:
        print("❌ Error: Solution box title '✅ 해결책' not found")
        return False
    else:
        print("✅ Solution box title '✅ 해결책' found")
    
    # Check CSS for solution-preview h4 color
    h4_pattern = r'\.solution-preview\s+h4\s*\{[^}]*color:\s*#FFFFFF[^}]*\}'
    if re.search(h4_pattern, content, re.DOTALL | re.IGNORECASE):
        print("✅ Solution preview h4 (title) has bright white color (#FFFFFF)")
    else:
        print("❌ Error: Solution preview h4 (title) does not have bright white color")
        return False
    
    # Check CSS for solution-preview p color
    p_pattern = r'\.solution-preview\s+p\s*\{[^}]*color:\s*#FFFFFF[^}]*\}'
    if re.search(p_pattern, content, re.DOTALL | re.IGNORECASE):
        print("✅ Solution preview p (description) has bright white color (#FFFFFF)")
    else:
        print("❌ Error: Solution preview p (description) does not have bright white color")
        return False
    
    # Check that toggleSolution function exists
    if "function toggleSolution(card)" in content:
        print("✅ toggleSolution function found")
    else:
        print("❌ Error: toggleSolution function not found")
        return False
    
    # Check that active class mechanism exists
    if ".problem-card.active .solution-preview" in content:
        print("✅ Active class mechanism for solution preview found")
    else:
        print("❌ Error: Active class mechanism not found")
        return False
    
    print("\n🎉 All tests passed! The solution box text colors are correctly set to bright white (#FFFFFF) when expanded.")
    return True

if __name__ == "__main__":
    success = test_solution_colors()
    if not success:
        exit(1)