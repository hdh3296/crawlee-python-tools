"""마크다운 변환 모듈"""

import re
from typing import List, Dict, Any, Optional
from datetime import datetime
from bs4 import BeautifulSoup, NavigableString, Tag
from .utils import clean_text, clean_code_text


class MarkdownConverter:
    """HTML을 마크다운으로 변환하는 클래스"""
    
    def __init__(self):
        """초기화"""
        self.content_items: List[Dict[str, Any]] = []
        self.markdown_lines: List[str] = []
    
    def convert(self, scraped_data: Dict) -> str:
        """스크래핑된 데이터를 마크다운으로 변환
        
        Args:
            scraped_data: 스크래핑된 데이터 딕셔너리
            
        Returns:
            마크다운 문자열
        """
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
        self.content_items = self._extract_all_text_content(main_area)
        print(f"📊 {len(self.content_items)}개 요소 추출 완료")
        
        # 마크다운 생성
        self._create_markdown(scraped_data['metadata'])
        
        return '\n'.join(self.markdown_lines)
    
    def _process_inline_elements(self, element):
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
    
    def _extract_all_text_content(self, element) -> List[Dict[str, Any]]:
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
                    table_data = self._extract_table_data(elem)
                    if table_data:
                        content_items.append({
                            'type': 'table',
                            'content': table_data
                        })
                    return
                
                # 리스트 처리
                elif tag_name in ['ul', 'ol']:
                    list_items = self._extract_list_items(elem)
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
                    markdown_text = self._process_inline_elements(elem)
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
    
    def _extract_table_data(self, table_element) -> Optional[Dict[str, Any]]:
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
    
    def _extract_list_items(self, list_element) -> Optional[List[str]]:
        """리스트 아이템 추출"""
        items = []
        list_items = list_element.find_all('li', recursive=False)
        
        for item in list_items:
            text = clean_text(item.get_text())
            if text:
                items.append(text)
        
        return items if items else None
    
    def _create_markdown(self, metadata: Dict[str, Any]):
        """마크다운 생성"""
        self.markdown_lines = []
        
        # 문서 헤더
        title = metadata['page_title'] or "웹페이지 가이드"
        self.markdown_lines.extend([
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
        for item in self.content_items:
            item_type = item['type']
            
            if item_type == 'heading':
                level = item['level']
                content = item['content']
                prefix = '#' * level
                self.markdown_lines.extend([
                    f"{prefix} {content}",
                    ""
                ])
            
            elif item_type == 'paragraph' or item_type == 'text':
                self.markdown_lines.extend([
                    item['content'],
                    ""
                ])
            
            elif item_type == 'code':
                language = item.get('language', 'text')
                self.markdown_lines.extend([
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
                    self.markdown_lines.extend([header_row, separator])
                
                # 데이터 행들
                for row in table_data['rows']:
                    if row:
                        row_text = '| ' + ' | '.join(str(cell) for cell in row) + ' |'
                        self.markdown_lines.append(row_text)
                
                self.markdown_lines.append("")
            
            elif item_type == 'bold':
                self.markdown_lines.extend([
                    f"**{item['content']}**",
                    ""
                ])
            
            elif item_type == 'italic':
                self.markdown_lines.extend([
                    f"*{item['content']}*",
                    ""
                ])
            
            elif item_type == 'list':
                items = item['content']
                ordered = item.get('ordered', False)
                
                for i, list_item in enumerate(items, 1):
                    if ordered:
                        self.markdown_lines.append(f"{i}. {list_item}")
                    else:
                        self.markdown_lines.append(f"- {list_item}")
                
                self.markdown_lines.append("")
        
        # 통계 정보
        type_counts = {}
        for item in self.content_items:
            t = item['type']
            type_counts[t] = type_counts.get(t, 0) + 1
        
        self.markdown_lines.extend([
            "---",
            "",
            "## 📊 문서 정보",
            "",
            f"- **추출된 총 요소**: {len(self.content_items)}개",
            f"- **헤딩**: {type_counts.get('heading', 0)}개",
            f"- **문단**: {type_counts.get('paragraph', 0) + type_counts.get('text', 0)}개",
            f"- **코드 블록**: {type_counts.get('code', 0)}개",
            f"- **테이블**: {type_counts.get('table', 0)}개",
            f"- **리스트**: {type_counts.get('list', 0)}개",
            "",
            "**✅ 자동 생성 완료**: 웹페이지를 완전히 마크다운으로 변환했습니다.",
            "",
            f"*생성 도구: web_scraper 모듈*",
            f"*생성 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*"
        ])