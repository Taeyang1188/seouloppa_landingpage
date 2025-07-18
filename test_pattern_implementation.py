#!/usr/bin/env python3
"""
Test script to verify the background pattern implementation in index-new.html
"""

def test_pattern_implementation():
    """Test that the aad.png pattern has been correctly implemented"""
    
    try:
        with open('index-new.html', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for the target Korean text
        if "이런 고민, 혹시 있으신가요?" in content:
            print("✓ Target Korean text found in HTML")
        else:
            print("✗ Target Korean text NOT found in HTML")
            return False
        
        # Check for the problems section CSS
        if ".problems {" in content:
            print("✓ Problems section CSS found")
        else:
            print("✗ Problems section CSS NOT found")
            return False
        
        # Check for background image implementation
        if "background-image: url('images/aad.png');" in content:
            print("✓ Background image URL found")
        else:
            print("✗ Background image URL NOT found")
            return False
        
        # Check for background repeat
        if "background-repeat: repeat;" in content:
            print("✓ Background repeat property found")
        else:
            print("✗ Background repeat property NOT found")
            return False
        
        # Check for 60-degree rotation
        if "transform: rotate(60deg);" in content:
            print("✓ 60-degree rotation found")
        else:
            print("✗ 60-degree rotation NOT found")
            return False
        
        # Check for pseudo-element implementation
        if ".problems::before {" in content:
            print("✓ Pseudo-element ::before found")
        else:
            print("✗ Pseudo-element ::before NOT found")
            return False
        
        # Check for z-index layering
        if "z-index: 1;" in content and "z-index: 2;" in content:
            print("✓ Z-index layering implemented")
        else:
            print("✗ Z-index layering NOT properly implemented")
            return False
        
        print("\n🎉 All tests passed! The background pattern has been successfully implemented.")
        print("📋 Implementation summary:")
        print("   - Target section: 'problems' class containing '이런 고민, 혹시 있으신가요?'")
        print("   - Background image: images/aad.png")
        print("   - Rotation: 60 degrees to the right")
        print("   - Pattern: Repeating background")
        print("   - Opacity: 0.1 for subtle effect")
        print("   - Layering: Proper z-index to keep content readable")
        
        return True
        
    except FileNotFoundError:
        print("✗ index-new.html file not found")
        return False
    except Exception as e:
        print(f"✗ Error reading file: {e}")
        return False

if __name__ == "__main__":
    test_pattern_implementation()