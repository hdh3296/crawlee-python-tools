"""웹 스크래퍼 유틸리티 함수들"""

import re
import urllib.parse


def clean_text(text: str) -> str:
    """일반 텍스트 정리
    
    Args:
        text: 정리할 텍스트
        
    Returns:
        정리된 텍스트
    """
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
    """코드 블록 텍스트 정리 - 들여쓰기 보존
    
    Args:
        text: 정리할 코드 텍스트
        
    Returns:
        들여쓰기가 보존된 정리된 코드
    """
    if not text:
        return ""
    # 탭을 4개 공백으로 변환하되, 들여쓰기는 보존
    text = text.replace('\t', '    ')
    # 앞뒤 공백만 제거하고 내부 구조는 유지
    return text.strip()


def generate_output_paths(url: str, suffix: str = "_guide") -> tuple[str, str, str]:
    """URL을 기반으로 출력 폴더와 파일 경로들 생성
    
    Args:
        url: 원본 URL
        suffix: 파일명 접미사 (기본값: "_guide")
        
    Returns:
        (폴더경로, 마크다운경로, JSON경로) 튜플
    """
    from datetime import datetime
    from pathlib import Path
    
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
    base_name = f"{clean_domain}{suffix}_{timestamp}"
    
    # 폴더 구조 생성
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)
    
    folder_path = output_dir / base_name
    folder_path.mkdir(exist_ok=True)
    
    markdown_path = folder_path / f"{base_name}.md"
    json_path = folder_path / f"{base_name}.json"
    
    return str(folder_path), str(markdown_path), str(json_path)