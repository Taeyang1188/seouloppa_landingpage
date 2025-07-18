#!/usr/bin/env python3
"""
Test script to verify that the Korean text color has been changed from gray to white
in the index-new.html file.
"""

import re

def test_text_color_fix():
    """Test that the solution-preview text color has been fixed to white."""
    
    print("Testing text color fix in index-new.html...")
    
    try:
        with open('index-new.html', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Test 1: Check if the new CSS rule exists with higher specificity
        css_rule_pattern = r'\.problem-card\s+\.solution-preview\s+p\s*\{'
        if re.search(css_rule_pattern, content):
            print("✅ PASS: Found CSS rule with higher specificity (.problem-card .solution-preview p)")
        else:
            print("❌ FAIL: CSS rule with higher specificity not found")
            return False
        
        # Test 2: Check if the color is set to white with !important
        color_pattern = r'color:\s*#FFFFFF\s*!important'
        if re.search(color_pattern, content):
            print("✅ PASS: Found white color with !important declaration")
        else:
            print("❌ FAIL: White color with !important not found")
            return False
        
        # Test 3: Check if all the Korean text instances are present
        korean_texts = [
            "전문 인플루언서가 직접 체험하고",
            "체험단 1회 투자로 평균",
            "이미 검증된 체험단 네트워크를",
            "인플루언서가 인스타그램, 블로그에",
            "평균 2-3주 내 검색 노출"
        ]
        
        for text in korean_texts:
            if text in content:
                print(f"✅ PASS: Found Korean text: {text[:20]}...")
            else:
                print(f"❌ FAIL: Korean text not found: {text[:20]}...")
                return False
        
        # Test 4: Check if the problematic gray color rule still exists (it should, but with lower specificity)
        gray_rule_pattern = r'\.problem-card\s+p\s*\{[^}]*color:\s*#4a5568'
        if re.search(gray_rule_pattern, content, re.DOTALL):
            print("✅ PASS: Original gray color rule still exists (but will be overridden)")
        else:
            print("⚠️  WARNING: Original gray color rule not found (this is okay)")
        
        print("\n🎉 All tests passed! The text color fix has been successfully implemented.")
        print("The Korean text in solution-preview sections should now appear white instead of gray.")
        return True
        
    except FileNotFoundError:
        print("❌ FAIL: index-new.html file not found")
        return False
    except Exception as e:
        print(f"❌ FAIL: Error reading file: {e}")
        return False

if __name__ == "__main__":
    test_text_color_fix()