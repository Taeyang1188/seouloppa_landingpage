#!/usr/bin/env python3
"""
Verification script to check if the button implementation meets all requirements.
"""

import re

def verify_css_changes(file_path):
    """Verify that the CSS changes are correctly implemented."""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    results = {
        'solution_text_white': False,
        'problem_text_opacity': False,
        'transition_effect': False
    }
    
    # Check if solution description text has white color
    solution_p_pattern = r'\.solution-preview\s+p\s*{[^}]*color:\s*#FFFFFF[^}]*}'
    if re.search(solution_p_pattern, content, re.DOTALL):
        results['solution_text_white'] = True
        print("✅ Solution description text color set to white (#FFFFFF)")
    else:
        print("❌ Solution description text color not set to white")
    
    # Check if problem text has opacity when active
    active_p_pattern = r'\.problem-card\.active\s+p\s*{[^}]*opacity:\s*0\.4[^}]*}'
    if re.search(active_p_pattern, content, re.DOTALL):
        results['problem_text_opacity'] = True
        print("✅ Problem text opacity set to 0.4 when active")
    else:
        print("❌ Problem text opacity not set when active")
    
    # Check if transition effect is added
    transition_pattern = r'\.problem-card\.active\s+p\s*{[^}]*transition:\s*opacity\s+0\.3s\s+ease[^}]*}'
    if re.search(transition_pattern, content, re.DOTALL):
        results['transition_effect'] = True
        print("✅ Transition effect added for smooth opacity change")
    else:
        print("❌ Transition effect not found")
    
    return results

def verify_html_structure(file_path):
    """Verify that the HTML structure is intact."""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    results = {
        'button_text_present': False,
        'solution_text_present': False,
        'toggle_function_present': False
    }
    
    # Check if the button text is present
    if '나도 후기 남기고 싶지만' in content:
        results['button_text_present'] = True
        print("✅ Button text '나도 후기 남기고 싶지만...' found")
    else:
        print("❌ Button text not found")
    
    # Check if solution text is present
    if '전문 인플루언서가 직접 체험하고' in content:
        results['solution_text_present'] = True
        print("✅ Solution description text found")
    else:
        print("❌ Solution description text not found")
    
    # Check if toggleSolution function is present
    if 'function toggleSolution(card)' in content:
        results['toggle_function_present'] = True
        print("✅ toggleSolution function found")
    else:
        print("❌ toggleSolution function not found")
    
    return results

def main():
    print("=== Verifying Implementation ===\n")
    
    # Test main file
    print("Testing main file: index-new.html")
    css_results = verify_css_changes('index-new.html')
    html_results = verify_html_structure('index-new.html')
    
    print("\n" + "="*50)
    print("Testing test file: test_button_behavior.html")
    test_css_results = verify_css_changes('test_button_behavior.html')
    test_html_results = verify_html_structure('test_button_behavior.html')
    
    print("\n" + "="*50)
    print("SUMMARY:")
    
    all_passed = True
    requirements = [
        ("Solution text white color", css_results['solution_text_white']),
        ("Problem text opacity when active", css_results['problem_text_opacity']),
        ("Smooth transition effect", css_results['transition_effect']),
        ("HTML structure intact", all([html_results[k] for k in html_results]))
    ]
    
    for req_name, passed in requirements:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status}: {req_name}")
        if not passed:
            all_passed = False
    
    print("\n" + "="*50)
    if all_passed:
        print("🎉 ALL REQUIREMENTS MET! Implementation is ready.")
    else:
        print("⚠️  Some requirements not met. Please review the implementation.")
    
    return all_passed

if __name__ == "__main__":
    main()