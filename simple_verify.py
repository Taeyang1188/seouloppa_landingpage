#!/usr/bin/env python3
"""
Simple verification script for mobile form fix
"""

import os

def verify_css_changes():
    """Verify that the CSS changes are present in index.html"""
    
    print("🔍 CSS 변경사항 검증 중...")
    print("=" * 40)
    
    if not os.path.exists("index.html"):
        print("❌ index.html 파일을 찾을 수 없습니다.")
        return False
    
    try:
        with open("index.html", "r", encoding="utf-8") as f:
            content = f.read()
            
        # Check for the new mobile responsive rules
        checks = [
            ("max-width: 280px", "모바일 최대 너비 280px 설정"),
            ("width: 90%", "모바일 너비 90% 설정"),
            ("left: 50%", "중앙 정렬을 위한 left: 50% 설정"),
            ("transform: translateX(-50%)", "중앙 정렬을 위한 transform 설정"),
            ("max-width: 260px", "초소형 모바일 260px 설정"),
            ("@media (max-width: 480px)", "480px 브레이크포인트 추가"),
            ("right: auto", "우측 정렬 해제")
        ]
        
        all_passed = True
        for check, description in checks:
            if check in content:
                print(f"✅ {description}")
            else:
                print(f"❌ {description} - 누락됨")
                all_passed = False
                
        return all_passed
                
    except Exception as e:
        print(f"❌ index.html 읽기 오류: {e}")
        return False

def check_test_files():
    """Check if test files exist"""
    test_files = [
        "test_mobile_issue.html",
        "test_mobile_fix.html"
    ]
    
    print("\n📁 테스트 파일 확인:")
    for file in test_files:
        if os.path.exists(file):
            print(f"✅ {file} - 존재함")
        else:
            print(f"❌ {file} - 없음")

if __name__ == "__main__":
    print("🚀 모바일 폼 수정 검증")
    print("=" * 40)
    
    css_ok = verify_css_changes()
    check_test_files()
    
    print("\n📋 수정 사항 요약:")
    print("• 모바일에서 폼 크기: 320px → 280px")
    print("• 초소형 모바일: 260px")
    print("• 위치: 우측 정렬 → 중앙 정렬")
    print("• 패딩 및 폰트 크기 최적화")
    
    if css_ok:
        print("\n✅ 모든 CSS 변경사항이 올바르게 적용되었습니다!")
        print("\n📱 테스트 방법:")
        print("1. 브라우저에서 index.html 열기")
        print("2. 개발자 도구 (F12) → 모바일 뷰 (Ctrl+Shift+M)")
        print("3. 다양한 화면 크기에서 폼 위치와 크기 확인")
    else:
        print("\n❌ 일부 변경사항이 누락되었습니다.")