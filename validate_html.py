#!/usr/bin/env python3
"""
Simple HTML validation script to check the landing page structure
"""

import re
import os

def validate_html_file(file_path):
    """Validate HTML file structure and content"""
    
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return False
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("🔍 Validating HTML structure...")
    
    # Check basic HTML structure
    checks = [
        (r'<!DOCTYPE html>', "DOCTYPE declaration"),
        (r'<html lang="ko">', "Korean language attribute"),
        (r'<meta charset="UTF-8">', "UTF-8 encoding"),
        (r'<meta name="viewport"', "Viewport meta tag"),
        (r'서울오빠', "Brand name present"),
        (r'체험단 연결 요청하기', "CTA button text"),
        (r'class="hero"', "Hero section"),
        (r'class="problems"', "Problems section"),
        (r'class="solution"', "Solution section"),
        (r'class="data"', "Data section"),
        (r'class="reviews"', "Reviews section"),
        (r'class="cta-section"', "CTA section"),
        (r'class="footer"', "Footer section"),
        (r'function toggleFaq', "FAQ toggle function"),
        (r'function scrollToContact', "Scroll to contact function"),
        (r'addEventListener.*submit', "Form submit handler"),
    ]
    
    passed = 0
    total = len(checks)
    
    for pattern, description in checks:
        if re.search(pattern, content, re.IGNORECASE):
            print(f"✅ {description}")
            passed += 1
        else:
            print(f"❌ {description}")
    
    print(f"\n📊 Validation Results: {passed}/{total} checks passed")
    
    # Check for potential issues
    print("\n🔍 Checking for potential issues...")
    
    issues = []
    
    # Check for unclosed tags (basic check)
    open_tags = re.findall(r'<(\w+)[^>]*>', content)
    close_tags = re.findall(r'</(\w+)>', content)
    
    # Count occurrences
    tag_counts = {}
    for tag in open_tags:
        if tag not in ['meta', 'link', 'input', 'br', 'hr', 'img']:  # Self-closing tags
            tag_counts[tag] = tag_counts.get(tag, 0) + 1
    
    for tag in close_tags:
        tag_counts[tag] = tag_counts.get(tag, 0) - 1
    
    unmatched_tags = [tag for tag, count in tag_counts.items() if count != 0]
    
    if unmatched_tags:
        issues.append(f"Potentially unmatched tags: {unmatched_tags}")
    else:
        print("✅ No unmatched HTML tags detected")
    
    # Check for required Korean content
    korean_content = [
        "우리 공방, 요즘 블로그/인스타 검색에",
        "마케팅은 잘 몰라요",
        "재료비만 나가고",
        "안 합니다",
        "체험용 제품 또는 클래스",
        "인플루언서가 남깁니다",
        "데이터로 증명하는 효과",
        "실제 후기 사례",
        "자주 묻는 질문"
    ]
    
    missing_content = []
    for text in korean_content:
        if text not in content:
            missing_content.append(text)
    
    if missing_content:
        issues.append(f"Missing Korean content: {missing_content}")
    else:
        print("✅ All required Korean content present")
    
    # Check CSS and JavaScript
    if 'background: linear-gradient' in content:
        print("✅ CSS gradients implemented")
    else:
        issues.append("CSS gradients not found")
    
    if '#FF7043' in content:
        print("✅ Brand color (#FF7043) used")
    else:
        issues.append("Brand color not found")
    
    if issues:
        print("\n⚠️  Issues found:")
        for issue in issues:
            print(f"   - {issue}")
        return False
    else:
        print("\n🎉 No issues found! HTML appears to be well-formed.")
        return True

if __name__ == "__main__":
    file_path = "seouloppa landing page.html"
    validate_html_file(file_path)