#!/usr/bin/env python3
"""
통합 웹페이지 스크래핑 & 마크다운 변환 도구

사용법:
    python3 all_in_one_scraper.py "https://example.com"
    python3 all_in_one_scraper.py  # URL 입력 프롬프트

기능:
    URL 입력 → 자동 스크래핑 → 마크다운 파일 생성 (원스텝)
"""

import asyncio
import sys
import re
import urllib.parse
from datetime import datetime
from pathlib import Path
from crawlee.crawlers import PlaywrightCrawler
from bs4 import BeautifulSoup, NavigableString, Tag


def clean_text(text: str) -> str:
    """텍스트 정리"""
    if not text:
        return ""
    
    # 보이지 않는 특수문자 제거
    text = re.sub(r'[\u200B-\u200F\uFEFF\u2060\u00AD]', '', text)  # Zero width characters, BOM, soft hyphen
    text = re.sub(r'[\u0000-\u001F\u007F-\u009F]', '', text)  # Control characters
    text = re.sub(r'[\uE000-\uF8FF]', '', text)  # Private Use Area
    text = re.sub(r'[\uFFF0-\uFFFF]', '', text)  # Specials block
    
    text = text.replace('\t', ' ')
    text = re.sub(r' +', ' ', text)  # 다중 공백을 단일로
    return text.strip()


def clean_code_text(text: str) -> str:
    """코드 블록 텍스트 정리 - 들여쓰기 보존"""
    if not text:
        return ""
    # 탭을 4개 공백으로 변환하되, 들여쓰기는 보존
    text = text.replace('\t', '    ')
    # 앞뒤 공백만 제거하고 내부 구조는 유지
    return text.strip()


def generate_output_paths(url: str) -> tuple[str, str, str]:
    """URL을 기반으로 출력 폴더와 파일 경로들 생성"""
    parsed = urllib.parse.urlparse(url)
    domain = parsed.netloc.replace('www.', '')
    
    # 도메인에서 특수 문자 제거
    clean_domain = re.sub(r'[^\w\-_.]', '_', domain)
    
    # 경로가 있으면 마지막 부분 추가
    if parsed.path and parsed.path != '/':
        path_part = parsed.path.strip('/').split('/')[-1]
        path_part = re.sub(r'[^\w\-_.]', '_', path_part)
        if path_part and len(path_part) < 20:
            clean_domain += f"_{path_part}"
    
    # 날짜/시간 추가
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    base_name = f"{clean_domain}_guide_{timestamp}"
    
    # 폴더 구조 생성
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)
    
    folder_path = output_dir / base_name
    folder_path.mkdir(exist_ok=True)
    
    markdown_path = folder_path / f"{base_name}.md"
    json_path = folder_path / f"{base_name}.json"
    
    return str(folder_path), str(markdown_path), str(json_path)


async def scrape_webpage_direct(url: str) -> dict:
    """웹페이지를 직접 스크래핑하여 메모리에 반환"""
    
    print(f"🔄 스크래핑 시작: {url}")
    
    crawler = PlaywrightCrawler(
        headless=True,
        browser_type='chromium',
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
    return scraped_data


def process_inline_elements(element):
    """문단 내 인라인 요소들을 마크다운으로 변환"""
    result = ""
    
    for child in element.children:
        if isinstance(child, NavigableString):
            result += clean_text(str(child))
        elif isinstance(child, Tag):
            tag_name = child.name.lower()
            text = clean_text(child.get_text())
            
            if tag_name in ['strong', 'b']:
                result += f"**{text}**"
            elif tag_name in ['em', 'i']:
                result += f"*{text}*"
            elif tag_name == 'code':
                result += f"`{text}`"
            else:
                result += text
    
    return clean_text(result)


def extract_all_text_content(element):
    """요소에서 모든 텍스트 콘텐츠를 순차적으로 추출"""
    content_items = []
    
    def process_element(elem, level=0):
        if isinstance(elem, NavigableString):
            text = clean_text(str(elem))
            if text and len(text) > 2:
                content_items.append({
                    'type': 'text',
                    'content': text,
                    'level': level
                })
                return
        
        if isinstance(elem, Tag):
            tag_name = elem.name.lower()
            
            # 헤딩 처리
            if tag_name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                text = clean_text(elem.get_text())
                if text:
                    content_items.append({
                        'type': 'heading',
                        'level': int(tag_name[1]),
                        'content': text,
                        'tag': tag_name
                    })
                return
            
            # 테이블 처리
            elif tag_name == 'table':
                table_data = extract_table_data(elem)
                if table_data:
                    content_items.append({
                        'type': 'table',
                        'content': table_data
                    })
                return
            
            # 리스트 처리
            elif tag_name in ['ul', 'ol']:
                list_items = extract_list_items(elem)
                if list_items:
                    content_items.append({
                        'type': 'list',
                        'content': list_items,
                        'ordered': tag_name == 'ol'
                    })
                return
            
            # 코드 블록 처리
            elif tag_name in ['pre', 'code']:
                text = clean_code_text(elem.get_text())  # 코드 전용 정리 함수 사용
                if text and len(text) > 5:
                    # pre 안의 code는 건너뛰기
                    if tag_name == 'code' and elem.parent and elem.parent.name == 'pre':
                        return
                    
                    language = 'javascript' if any(kw in text.lower() for kw in ['var', 'function', 'script', 'eformsign']) else 'text'
                    content_items.append({
                        'type': 'code',
                        'content': text,
                        'language': language
                    })
                return
            
            # Strong/Bold 텍스트 처리
            elif tag_name in ['strong', 'b']:
                text = clean_text(elem.get_text())
                if text and len(text) > 1:
                    content_items.append({
                        'type': 'bold',
                        'content': text
                    })
                return
            
            # Emphasis/Italic 텍스트 처리
            elif tag_name in ['em', 'i']:
                text = clean_text(elem.get_text())
                if text and len(text) > 1:
                    content_items.append({
                        'type': 'italic',
                        'content': text
                    })
                return
            
            # 문단 처리 (인라인 마크다운 지원)
            elif tag_name == 'p':
                markdown_text = process_inline_elements(elem)
                if markdown_text and len(markdown_text) > 1:
                    content_items.append({
                        'type': 'paragraph',
                        'content': markdown_text
                    })
                return
            
            # 스킵할 요소들
            elif tag_name in ['script', 'style', 'nav', 'header', 'footer']:
                return
            
            # 다른 모든 요소들의 자식을 재귀적으로 처리
            for child in elem.children:
                process_element(child, level + 1)
    
    process_element(element)
    return content_items


def extract_table_data(table_element):
    """테이블 데이터 추출"""
    rows = []
    headers = []
    
    # 모든 행 찾기
    all_rows = table_element.find_all('tr')
    
    for i, row in enumerate(all_rows):
        cells = row.find_all(['th', 'td'])
        if cells:
            cell_texts = [clean_text(cell.get_text()) for cell in cells]
            if any(cell for cell in cell_texts):  # 빈 행이 아닌 경우
                if i == 0 and row.find('th'):  # 첫 번째 행이 헤더인 경우
                    headers = cell_texts
                else:
                    rows.append(cell_texts)
    
    return {'headers': headers, 'rows': rows} if rows else None


def extract_list_items(list_element):
    """리스트 아이템 추출"""
    items = []
    list_items = list_element.find_all('li', recursive=False)
    
    for item in list_items:
        text = clean_text(item.get_text())
        if text:
            items.append(text)
    
    return items if items else None


def convert_to_markdown(scraped_data: dict) -> str:
    """스크래핑된 데이터를 마크다운으로 변환"""
    
    print("🔄 마크다운 변환 중...")
    
    # HTML 파싱
    html_content = scraped_data['raw_content']['full_html']
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # 메인 콘텐츠 영역 찾기
    main_area = soup.find('div', class_='document') or soup.find('main') or soup.find('article') or soup.find('body')
    
    if not main_area:
        print("❌ 메인 콘텐츠 영역을 찾을 수 없습니다.")
        return ""
    
    print(f"✅ 메인 영역 발견: {main_area.name}")
    
    # 콘텐츠 추출
    content_items = extract_all_text_content(main_area)
    print(f"📊 {len(content_items)}개 요소 추출 완료")
    
    # 마크다운 생성
    markdown_lines = []
    metadata = scraped_data['metadata']
    
    # 문서 헤더
    title = metadata['page_title'] or "웹페이지 가이드"
    markdown_lines.extend([
        f"# {title}",
        "",
        f"> **자동 생성된 가이드 문서**",
        "",
        f"**출처**: {metadata['url']}",
        f"**제목**: {metadata['page_title']}",
        f"**생성일**: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "---",
        ""
    ])
    
    # 콘텐츠 변환
    for item in content_items:
        item_type = item['type']
        
        if item_type == 'heading':
            level = item['level']
            content = item['content']
            prefix = '#' * level
            markdown_lines.extend([
                f"{prefix} {content}",
                ""
            ])
        
        elif item_type == 'paragraph' or item_type == 'text':
            markdown_lines.extend([
                item['content'],
                ""
            ])
        
        elif item_type == 'code':
            language = item.get('language', 'text')
            markdown_lines.extend([
                f"```{language}",
                item['content'],
                "```",
                ""
            ])
        
        elif item_type == 'table':
            table_data = item['content']
            
            # 헤더가 있으면 헤더부터
            if table_data['headers']:
                header_row = '| ' + ' | '.join(table_data['headers']) + ' |'
                separator = '|' + '---|' * len(table_data['headers'])
                markdown_lines.extend([header_row, separator])
            
            # 데이터 행들
            for row in table_data['rows']:
                if row:
                    row_text = '| ' + ' | '.join(str(cell) for cell in row) + ' |'
                    markdown_lines.append(row_text)
            
            markdown_lines.append("")
        
        elif item_type == 'bold':
            markdown_lines.extend([
                f"**{item['content']}**",
                ""
            ])
        
        elif item_type == 'italic':
            markdown_lines.extend([
                f"*{item['content']}*",
                ""
            ])
        
        elif item_type == 'list':
            items = item['content']
            ordered = item.get('ordered', False)
            
            for i, list_item in enumerate(items, 1):
                if ordered:
                    markdown_lines.append(f"{i}. {list_item}")
                else:
                    markdown_lines.append(f"- {list_item}")
            
            markdown_lines.append("")
    
    # 통계 정보
    type_counts = {}
    for item in content_items:
        t = item['type']
        type_counts[t] = type_counts.get(t, 0) + 1
    
    markdown_lines.extend([
        "---",
        "",
        "## 📊 문서 정보",
        "",
        f"- **추출된 총 요소**: {len(content_items)}개",
        f"- **헤딩**: {type_counts.get('heading', 0)}개",
        f"- **문단**: {type_counts.get('paragraph', 0) + type_counts.get('text', 0)}개",
        f"- **코드 블록**: {type_counts.get('code', 0)}개",
        f"- **테이블**: {type_counts.get('table', 0)}개",
        f"- **리스트**: {type_counts.get('list', 0)}개",
        "",
        "**✅ 자동 생성 완료**: 웹페이지를 완전히 마크다운으로 변환했습니다.",
        "",
        f"*생성 도구: all_in_one_scraper.py*",
        f"*생성 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*"
    ])
    
    return '\n'.join(markdown_lines)


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
        print("🚀 통합 웹페이지 스크래핑 & 마크다운 변환 시작")
        print("=" * 60)
        
        # 1단계: 스크래핑
        scraped_data = await scrape_webpage_direct(url)
        
        if not scraped_data:
            print("❌ 스크래핑 실패")
            return
        
        print("✅ 스크래핑 완료")
        
        # 2단계: 마크다운 변환
        markdown_content = convert_to_markdown(scraped_data)
        
        if not markdown_content:
            print("❌ 마크다운 변환 실패")
            return
        
        print("✅ 마크다운 변환 완료")
        
        # 3단계: 파일 저장
        folder_path, markdown_path, json_path = generate_output_paths(url)
        
        # 마크다운 파일 저장
        with open(markdown_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        # JSON 파일 저장
        import json
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(scraped_data, f, ensure_ascii=False, indent=2)
        
        # 파일 정보 수집
        md_size = Path(markdown_path).stat().st_size
        json_size = Path(json_path).stat().st_size
        line_count = len(markdown_content.split('\n'))
        
        print("=" * 60)
        print("🎉 변환 완료!")
        print(f"📁 출력 폴더: {folder_path}")
        print(f"📄 마크다운: {Path(markdown_path).name} ({md_size:,} bytes)")
        print(f"📋 JSON 데이터: {Path(json_path).name} ({json_size:,} bytes)")
        print(f"📊 줄 수: {line_count:,}")
        print(f"🔗 원본 URL: {url}")
        print("=" * 60)
        
    except Exception as e:
        print(f"❌ 오류 발생: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main())