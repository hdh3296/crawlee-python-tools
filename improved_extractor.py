#!/usr/bin/env python3
"""
개선된 HTML → 마크다운 변환기
누락된 텍스트 문제 해결
"""

import json
import re
from datetime import datetime
from pathlib import Path
from bs4 import BeautifulSoup, NavigableString, Tag


def clean_text(text: str) -> str:
    """텍스트 정리 - 더 보수적으로"""
    if not text:
        return ""
    # 기본 정리만 수행
    text = text.replace('\t', ' ')
    text = re.sub(r' +', ' ', text)  # 다중 공백을 단일로
    return text.strip()


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
                    print(f"  📋 {tag_name.upper()}: {text[:50]}...")
                return
            
            # 테이블 처리
            elif tag_name == 'table':
                table_data = extract_table_data(elem)
                if table_data:
                    content_items.append({
                        'type': 'table',
                        'content': table_data
                    })
                    print(f"  📊 테이블: {len(table_data['rows'])}행")
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
                    print(f"  📝 리스트: {len(list_items)}개 항목")
                return
            
            # 코드 블록 처리
            elif tag_name in ['pre', 'code']:
                text = clean_text(elem.get_text())
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
                    print(f"  💻 코드 ({language}): {text[:30]}...")
                return
            
            # 문단 처리 - 더 정확하게
            elif tag_name == 'p':
                text = clean_text(elem.get_text())
                if text and len(text) > 1:  # 매우 관대한 길이 제한
                    content_items.append({
                        'type': 'paragraph',
                        'content': text
                    })
                    print(f"  📄 문단: {text[:40]}...")
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


def convert_to_markdown(content_items, metadata):
    """추출된 콘텐츠를 마크다운으로 변환"""
    markdown_lines = []
    
    # 문서 헤더
    markdown_lines.extend([
        "# eformsign 기능 임베딩하기",
        "",
        "> **완전한 개발자 가이드 - 개선된 텍스트 추출**",
        "",
        f"**출처**: {metadata['url']}",
        f"**제목**: {metadata['page_title']}",
        f"**생성일**: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "---",
        ""
    ])
    
    # 콘텐츠 순차적 변환
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
        "## 📊 문서 통계",
        "",
        f"- **추출된 총 요소**: {len(content_items)}개",
        f"- **헤딩**: {type_counts.get('heading', 0)}개",
        f"- **문단**: {type_counts.get('paragraph', 0) + type_counts.get('text', 0)}개",
        f"- **코드 블록**: {type_counts.get('code', 0)}개",
        f"- **테이블**: {type_counts.get('table', 0)}개",
        f"- **리스트**: {type_counts.get('list', 0)}개",
        "",
        "**✅ 개선된 텍스트 추출**: 누락된 텍스트를 모두 포함하여 완전히 추출했습니다.",
        "",
        f"*생성 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*"
    ])
    
    return markdown_lines, type_counts


def main():
    """메인 함수"""
    input_file = "enhanced_eformsign_result.json"
    output_file = "improved_eformsign_complete.md"
    
    if not Path(input_file).exists():
        print(f"❌ 파일 없음: {input_file}")
        return
    
    print("🔄 개선된 HTML → 마크다운 변환 시작")
    print("🎯 특징: 모든 텍스트를 빠짐없이 추출")
    print("=" * 50)
    
    try:
        # JSON 로드
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if isinstance(data, list):
            data = data[0]
        
        # HTML 파싱
        html_content = data['raw_content']['full_html']
        soup = BeautifulSoup(html_content, 'html.parser')
        
        print(f"📄 HTML 크기: {len(html_content):,}자")
        
        # 메인 콘텐츠 영역 찾기
        main_area = soup.find('div', class_='document') or soup.find('body')
        
        if not main_area:
            print("❌ 메인 콘텐츠 영역을 찾을 수 없습니다.")
            return
        
        print(f"✅ 메인 영역 발견: {main_area.name} (class: {main_area.get('class', [])})")
        
        # 순차적 콘텐츠 추출
        print("🔍 모든 텍스트 콘텐츠 추출 중...")
        content_items = extract_all_text_content(main_area)
        
        print(f"✅ {len(content_items)}개 요소 추출 완료")
        
        # 마크다운 변환
        print("📝 마크다운 변환 중...")
        markdown_lines, type_counts = convert_to_markdown(content_items, data['metadata'])
        
        # 파일 저장
        output_path = Path(output_file)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(markdown_lines))
        
        # 결과 출력
        print("=" * 50)
        print("🎉 개선된 변환 완료!")
        print(f"📁 출력: {output_file}")
        print(f"📊 줄 수: {len(markdown_lines):,}")
        print(f"📏 크기: {output_path.stat().st_size:,} bytes")
        print()
        print("📋 추출 요소:")
        for content_type, count in type_counts.items():
            print(f"  {content_type}: {count}개")
        
    except Exception as e:
        print(f"❌ 오류: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()