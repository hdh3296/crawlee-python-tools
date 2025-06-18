#!/usr/bin/env python3
"""
빠른 웹페이지 스크래핑 도구
사용법: python3 quick_scraper.py "https://example.com"
"""

import asyncio
import sys
import json
from pathlib import Path
from crawlee.playwright_crawler import PlaywrightCrawler


async def scrape_webpage(url: str, output_name: str = "scraped_result"):
    """웹페이지 스크래핑"""
    
    print(f"🔄 스크래핑 시작: {url}")
    
    crawler = PlaywrightCrawler(
        headless=True,
        browser_type='chromium',
        max_requests_per_crawl=1,
    )

    @crawler.router.default_handler
    async def handler(context):
        # 페이지 로딩 대기
        await context.page.wait_for_load_state('load')
        await context.page.wait_for_load_state('domcontentloaded')
        
        # 메인 콘텐츠 로딩 대기
        try:
            await context.page.wait_for_selector('main, .content, .document, article', timeout=5000)
        except:
            pass
        
        await context.page.wait_for_timeout(3000)
        
        # 전체 HTML 추출
        full_html = await context.page.content()
        
        result = {
            'metadata': {
                'url': str(context.request.url),
                'page_title': await context.page.title(),
                'timestamp': context.request.loaded_at.isoformat() if context.request.loaded_at else None,
                'content_length': len(full_html)
            },
            'raw_content': {
                'full_html': full_html,
            }
        }
        
        # JSON 파일로 저장
        output_file = f"{output_name}.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump([result], f, ensure_ascii=False, indent=2)
        
        print(f"✅ 스크래핑 완료: {output_file}")
        print(f"📄 HTML 크기: {len(full_html):,}자")
        print(f"📝 페이지 제목: {await context.page.title()}")

    await crawler.run([url])


def main():
    if len(sys.argv) < 2:
        print("사용법: python3 quick_scraper.py 'https://example.com' [출력파일명]")
        print("예시: python3 quick_scraper.py 'https://docs.python.org' python_docs")
        return
    
    url = sys.argv[1]
    output_name = sys.argv[2] if len(sys.argv) > 2 else "scraped_result"
    
    asyncio.run(scrape_webpage(url, output_name))
    print(f"\n🎯 다음 단계:")
    print(f"1. improved_extractor.py 파일에서 input_file을 '{output_name}.json'으로 수정")
    print(f"2. python3 improved_extractor.py 실행")


if __name__ == "__main__":
    main()