#!/usr/bin/env python3
"""
피드백 기능이 추가된 이메일 에이전트 테스트 스크립트
"""

import os
import sys

# 현재 스크립트와 같은 디렉토리에서 email_fetcher.py 임포트를 위한 경로 설정
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

try:
    from email_fetcher import email_fetcher_agent
except ImportError as e:
    print(f"❌ email_fetcher.py 임포트 오류: {e}")
    print(f"현재 디렉토리: {current_dir}")
    sys.exit(1)

def test_feedback_agent():
    """피드백 기능이 포함된 에이전트 테스트"""
    
    print("=" * 70)
    print("🚀 피드백 기능이 추가된 이메일 검색 에이전트 테스트")
    print("=" * 70)
    
    print("""
이제 에이전트는 다음과 같이 작동합니다:

1. 📝 초기 쿼리로 이메일 검색
2. 📧 검색 결과를 사용자에게 보여줌
3. 💬 사용자 피드백 수집:
   - "예" 또는 "확인": 해당 이메일이 맞음
   - 기타: 구체적인 피드백 (예: "더 최근 메일", "다른 발신자" 등)
4. 🔄 피드백을 반영하여 재검색 (이전 검색 결과와 피드백을 모두 고려)
5. 🎯 만족할 때까지 반복

피드백 예시:
- "더 최근에 온 메일로 찾아줘"
- "제목에 '긴급'이 포함된 메일"
- "다른 발신자의 메일"
- "내용이 더 긴 메일"
- "어제 온 메일 말고 오늘 온 메일"
""")
    
    # 테스트 쿼리 입력
    query = input("\n검색하고 싶은 이메일에 대해 설명해주세요: ").strip()
    
    if not query:
        query = "최근에 온 미팅 관련 메일"
        print(f"기본 쿼리 사용: {query}")
    
    print(f"\n📝 쿼리: {query}")
    print("\n🔄 피드백 기능이 포함된 에이전트 시작...")
    print("(피드백을 통해 더 정확한 이메일을 찾을 수 있습니다!)")
    
    try:
        agent = email_fetcher_agent()
        result = agent.invoke({"query": query})
        
        print("\n" + "="*70)
        print("📊 최종 결과")
        print("="*70)
        print(f"상태: {result.get('status', 'UNKNOWN')}")
        
        if result.get('fetched_email'):
            email = result['fetched_email']
            print(f"최종 선택된 이메일:")
            print(f"  - 제목: {email.subject}")
            print(f"  - 보낸 사람: {email.sender}")
            print(f"  - 내용: {email.content[:100]}...")
        
        # 피드백 히스토리 출력
        if result.get('feedback_history'):
            print(f"\n📝 사용자 피드백 히스토리:")
            for i, feedback in enumerate(result['feedback_history'], 1):
                print(f"  {i}. {feedback}")
        
        return result
        
    except Exception as e:
        print(f"\n❌ 에이전트 실행 중 오류: {str(e)}")
        return None

def demo_workflow():
    """워크플로우 데모"""
    print("\n" + "="*70)
    print("🎯 피드백 기반 이메일 검색 워크플로우")
    print("="*70)
    
    print("""
개선된 워크플로우:

1. query_parser → 쿼리 파싱
2. email_collector → 이메일 수집  
3. email_fetcher → 초기 이메일 검색
4. email_fetch_feedback → 사용자 확인 및 피드백 수집
5. 조건부 분기:
   ✅ "확인" → completed (완료)
   🔄 "피드백" → feedback_search (피드백 기반 재검색)
   🔄 "재시도" → email_fetcher (일반 재검색)
6. feedback_search → 피드백을 반영한 개선된 검색
7. 4번으로 돌아가서 반복...

핵심 개선사항:
- 🧠 이전 검색 결과를 기억
- 💬 사용자 피드백을 프롬프트에 반영
- 🎯 점진적으로 더 정확한 결과 제공
""")

if __name__ == "__main__":
    demo_workflow()
    
    choice = input("\n테스트를 실행하시겠습니까? (y/n): ").strip().lower()
    if choice in ['y', 'yes', '예']:
        test_feedback_agent()
    else:
        print("👋 테스트를 종료합니다.")
