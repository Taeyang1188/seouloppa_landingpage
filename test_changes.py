#!/usr/bin/env python3
"""
Test script to verify the changes made to index-new.html
"""

def test_html_changes():
    """Test that the required changes have been applied"""
    
    with open('index-new.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Test 1: Check if problem-card background is changed to purple gradient
    if 'background: linear-gradient(135deg, #4F46E5 0%, #7C3AED 100%);' in content:
        print("✅ Problem card background changed to purple gradient")
    else:
        print("❌ Problem card background not found with purple gradient")
    
    # Test 2: Check if problem-card has white text color
    if '.problem-card {' in content and 'color: white;' in content:
        print("✅ Problem card has white text color")
    else:
        print("❌ Problem card white text color not found")
    
    # Test 3: Check if problem-card p has white color
    if '.problem-card p {' in content and 'color: white;' in content:
        print("✅ Problem card paragraph text is white")
    else:
        print("❌ Problem card paragraph text color not properly set")
    
    # Test 4: Check if solution-preview sections have white text
    if '.solution-preview h4 {' in content and 'color: white;' in content:
        print("✅ Solution preview heading has white text")
    else:
        print("❌ Solution preview heading text color issue")
    
    if '.solution-preview p {' in content and 'color: white;' in content:
        print("✅ Solution preview paragraph has white text")
    else:
        print("❌ Solution preview paragraph text color issue")
    
    # Test 5: Check for 해결책 content
    if '해결책' in content:
        print("✅ Korean content '해결책' found in HTML")
    else:
        print("❌ Korean content '해결책' not found")
    
    print("\nTest completed!")

if __name__ == "__main__":
    test_html_changes()