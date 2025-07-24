#!/usr/bin/env python3
"""
Test script to verify the implementation of mobile responsiveness and button functionality
"""

import os
import webbrowser
import time
from pathlib import Path

def test_implementation():
    """Test the updated index.html implementation"""
    
    # Get the path to index.html
    current_dir = Path(__file__).parent
    index_path = current_dir / "index.html"
    
    if not index_path.exists():
        print("❌ Error: index.html not found!")
        return False
    
    print("🧪 Testing Implementation...")
    print("=" * 50)
    
    # Check if mobile-specific pulse animation was added
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    tests_passed = 0
    total_tests = 4
    
    # Test 1: Check for mobile-specific pulse animation
    if "translateX(-50%) scale(1)" in content and "@media (max-width: 768px)" in content:
        print("✅ Test 1 PASSED: Mobile-specific pulse animation found")
        tests_passed += 1
    else:
        print("❌ Test 1 FAILED: Mobile-specific pulse animation missing")
    
    # Test 2: Check for CTA message function
    if "showCTAMessage" in content and "공방명부터 입력해주세요" in content:
        print("✅ Test 2 PASSED: CTA message functionality found")
        tests_passed += 1
    else:
        print("❌ Test 2 FAILED: CTA message functionality missing")
    
    # Test 3: Check for mobile responsive styles
    if "max-width: 280px" in content and "width: 90%" in content:
        print("✅ Test 3 PASSED: Mobile responsive styles found")
        tests_passed += 1
    else:
        print("❌ Test 3 FAILED: Mobile responsive styles missing")
    
    # Test 4: Check for button functionality
    if "scrollToContact()" in content and "지금 바로 신청하고 혜택 받기" in content:
        print("✅ Test 4 PASSED: Button functionality found")
        tests_passed += 1
    else:
        print("❌ Test 4 FAILED: Button functionality missing")
    
    print("=" * 50)
    print(f"📊 Test Results: {tests_passed}/{total_tests} tests passed")
    
    if tests_passed == total_tests:
        print("🎉 All tests passed! Implementation is complete.")
        
        # Open the file in browser for manual testing
        print("\n🌐 Opening index.html in browser for manual testing...")
        print("📱 To test mobile view:")
        print("   1. Open browser developer tools (F12)")
        print("   2. Toggle device toolbar (Ctrl+Shift+M)")
        print("   3. Select a mobile device (e.g., iPhone 12)")
        print("   4. Click '지금 바로 신청하고 혜택 받기' button")
        print("   5. Verify the form animates and CTA message appears")
        
        file_url = f"file:///{index_path.absolute()}"
        webbrowser.open(file_url)
        return True
    else:
        print("❌ Some tests failed. Please check the implementation.")
        return False

if __name__ == "__main__":
    test_implementation()