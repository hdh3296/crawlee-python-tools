"""웹 스크래퍼 메인 실행 파일"""

import asyncio
import sys
from pathlib import Path
from .scraper import WebScraper
from .converter import MarkdownConverter
from .utils import generate_filename


async def main():
    """메인 함수"""
    
    # URL 입력 받기
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = input("🔗 스크래핑할 URL을 입력하세요: ").strip()
    
    if not url:
        print("❌ URL이 입력되지 않았습니다.")
        return
    
    # URL 유효성 검사
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    try:
        print("=" * 60)
        print("🚀 웹페이지 스크래핑 & 마크다운 변환 시작")
        print("=" * 60)
        
        # 1단계: 스크래핑
        scraper = WebScraper()
        scraped_data = await scraper.scrape(url)
        
        if not scraped_data:
            print("❌ 스크래핑 실패")
            return
        
        print("✅ 스크래핑 완료")
        
        # 2단계: 마크다운 변환
        converter = MarkdownConverter()
        markdown_content = converter.convert(scraped_data)
        
        if not markdown_content:
            print("❌ 마크다운 변환 실패")
            return
        
        print("✅ 마크다운 변환 완료")
        
        # 3단계: 파일 저장
        filename = generate_filename(url)
        output_path = Path(filename)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        file_size = output_path.stat().st_size
        line_count = len(markdown_content.split('\n'))
        
        print("=" * 60)
        print("🎉 변환 완료!")
        print(f"📁 출력 파일: {filename}")
        print(f"📊 줄 수: {line_count:,}")
        print(f"📏 크기: {file_size:,} bytes")
        print(f"🔗 원본 URL: {url}")
        print("=" * 60)
        
    except Exception as e:
        print(f"❌ 오류 발생: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main())