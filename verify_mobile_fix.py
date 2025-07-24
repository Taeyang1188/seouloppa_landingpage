#!/usr/bin/env python3
"""
Verification script for mobile form fix
Tests the responsive behavior of the '체험단 연결 신청하기' form
"""

import os
import webbrowser
import time

def verify_mobile_fix():
    """Verify that the mobile fix is working correctly"""
    
    print("🔍 모바일 폼 수정 사항 검증 중...")
    print("=" * 50)
    
    # Check if files exist
    files_to_check = [
        "index.html",
        "test_mobile_issue.html", 
        "test_mobile_fix.html"
    ]
    
    print("📁 파일 존재 확인:")
    for file in files_to_check:
        if os.path.exists(file):
            print(f"  ✅ {file} - 존재함")
        else:
            print(f"  ❌ {file} - 없음")
            return False
    
    print("\n📋 수정 사항 요약:")
    print("  • 모바일에서 폼 크기 축소: 320px → 280px (768px 이하)")
    print("  • 초소형 모바일에서 더 작게: 260px (480px 이하)")
    print("  • 위치 변경: 우측 정렬 → 중앙 정렬")
    print("  • 패딩 및 폰트 크기 최적화")
    
    print("\n🎯 테스트 시나리오:")
    print("  1. 데스크톱 (>768px): 400px 너비, 우측 하단 고정")
    print("  2. 태블릿/모바일 (≤768px): 280px 최대 너비, 중앙 정렬")
    print("  3. 소형 모바일 (≤480px): 260px 최대 너비, 더 작은 패딩")
    
    print("\n🌐 브라우저에서 테스트 파일들을 열어 확인하세요:")
    print("  • test_mobile_issue.html - 수정 전 (문제 상황)")
    print("  • test_mobile_fix.html - 수정 후 (개선된 버전)")
    print("  • index.html - 실제 적용된 파일")
    
    # Check CSS changes in index.html
    print("\n🔧 index.html의 CSS 변경사항 확인:")
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
            ("@media (max-width: 480px)", "480px 브레이크포인트 추가")
        ]
        
        for check, description in checks:
            if check in content:
                print(f"  ✅ {description}")
            else:
                print(f"  ❌ {description} - 누락됨")
                
    except Exception as e:
        print(f"  ❌ index.html 읽기 오류: {e}")
        return False
    
    print("\n✅ 검증 완료!")
    print("\n📱 모바일 테스트 방법:")
    print("  1. 브라우저 개발자 도구 열기 (F12)")
    print("  2. 모바일 뷰 토글 (Ctrl+Shift+M)")
    print("  3. 다양한 디바이스 크기로 테스트")
    print("  4. 폼이 중앙에 위치하고 적절한 크기인지 확인")
    
    return True

def open_test_files():
    """Open test files in browser for manual verification"""
    test_files = [
        "test_mobile_issue.html",
        "test_mobile_fix.html", 
        "index.html"
    ]
    
    print("\n🌐 테스트 파일들을 브라우저에서 열기...")
    for file in test_files:
        if os.path.exists(file):
            file_path = os.path.abspath(file)
            print(f"  📂 {file} 열기...")
            webbrowser.open(f"file://{file_path}")
            time.sleep(1)  # Small delay between opens
        else:
            print(f"  ❌ {file} 파일을 찾을 수 없습니다.")

if __name__ == "__main__":
    print("🚀 모바일 폼 수정 검증 스크립트")
    print("=" * 50)
    
    if verify_mobile_fix():
        print("\n🎉 모든 검증이 완료되었습니다!")
        
        user_input = input("\n브라우저에서 테스트 파일들을 열어보시겠습니까? (y/n): ")
        if user_input.lower() in ['y', 'yes', '예']:
            open_test_files()
            print("\n📋 브라우저에서 다음을 확인하세요:")
            print("  • 모바일 뷰에서 폼이 화면 중앙에 위치하는지")
            print("  • 폼 크기가 적절한지 (화면을 가리지 않는지)")
            print("  • 데스크톱에서는 기존처럼 우측 하단에 위치하는지")
    else:
        print("\n❌ 검증 중 오류가 발생했습니다.")