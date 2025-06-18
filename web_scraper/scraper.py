"""웹 스크래핑 모듈"""

import asyncio
from typing import Dict, Optional
from datetime import datetime
from crawlee.crawlers import PlaywrightCrawler


class WebScraper:
    """웹페이지 스크래핑 클래스"""
    
    def __init__(self, headless: bool = True, browser_type: str = 'chromium'):
        """초기화
        
        Args:
            headless: 헤드리스 모드 여부
            browser_type: 브라우저 타입 ('chromium', 'firefox', 'webkit')
        """
        self.headless = headless
        self.browser_type = browser_type
        self.scraped_data: Optional[Dict] = None
    
    async def scrape(self, url: str) -> Dict:
        """웹페이지 스크래핑
        
        Args:
            url: 스크래핑할 URL
            
        Returns:
            스크래핑된 데이터 딕셔너리
        """
        print(f"🔄 스크래핑 시작: {url}")
        
        crawler = PlaywrightCrawler(
            headless=self.headless,
            browser_type=self.browser_type,
            max_requests_per_crawl=1,
        )

        scraped_data = {}

        @crawler.router.default_handler
        async def handler(context):
            nonlocal scraped_data
            
            print("  ⏳ 페이지 로딩 중...")
            
            # 페이지 로딩 대기
            await context.page.wait_for_load_state('load')
            await context.page.wait_for_load_state('domcontentloaded')
            
            # 메인 콘텐츠 로딩 대기
            try:
                await context.page.wait_for_selector('main, .content, .document, article, .container', timeout=5000)
                print("  ✅ 메인 콘텐츠 발견")
            except:
                print("  ⚠️ 메인 콘텐츠 선택자 대기 시간 초과 (계속 진행)")
            
            await context.page.wait_for_timeout(3000)
            
            # 전체 HTML 추출
            full_html = await context.page.content()
            page_title = await context.page.title()
            
            scraped_data = {
                'metadata': {
                    'url': str(context.request.url),
                    'page_title': page_title,
                    'timestamp': datetime.now().isoformat(),
                    'content_length': len(full_html)
                },
                'raw_content': {
                    'full_html': full_html,
                }
            }
            
            print(f"  📄 HTML 크기: {len(full_html):,}자")
            print(f"  📝 페이지 제목: {page_title}")

        await crawler.run([url])
        
        self.scraped_data = scraped_data
        return scraped_data