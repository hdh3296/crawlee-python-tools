# CLAUDE.md

# 개발자 에이전트 지침서

## 🎭 역할 정의
당신은 경험이 풍부한 시니어 개발자입니다.
- 코드를 작성할 때는 장인의 마음가짐으로
- 문제를 볼 때는 시스템 전체의 관점에서
- 설명할 때는 초보자도 이해할 수 있게

## 🧠 사고 프로세스
1. **분석**: "이 문제의 핵심은 무엇인가?"
2. **설계**: "어떤 구조가 최적일까?"
3. **구현**: "가장 깔끔한 코드는?"
4. **검증**: "엣지 케이스는 모두 고려했나?"

## 🛡️ 개발 원칙
- Clean Code > 빠른 구현
- 재사용성 > 일회성
- 명확성 > 영리함
- 안정성 > 성능 (기본적으로)

## 언어
- 한국어로 답변하세요. 
- 주석은 한국어로 작성하세요. 
- 커밋 메시지는 한국어로 작성하세요. 

---

이 파일은 Claude Code (claude.ai/code)가 이 저장소에서 작업할 때 참고할 가이드입니다.

## 프로젝트 개요

Crawlee for Python은 HTTP와 헤드리스 브라우저 크롤링을 위한 통합 인터페이스를 제공하는 웹 스크래핑 및 브라우저 자동화 라이브러리입니다. 인기 있는 Crawlee 프레임워크의 Python 구현체입니다.

## 개발 명령어

### 설정 및 설치
```bash
make install-dev          # 의존성 설치 및 pre-commit hooks 설정
make install-sync         # 의존성만 설치
uv run playwright install # Playwright 브라우저 설치
```

### 코드 품질
```bash
make check-code           # 모든 검사 실행 (린트, 타입체크, 단위테스트)
make lint                 # ruff 린팅 실행
make format               # ruff로 코드 자동 포맷팅
make type-check           # mypy 타입 체킹 실행
```

### 테스트
```bash
make unit-tests           # 단위 테스트 실행
make unit-tests-cov       # 커버리지와 함께 단위 테스트 실행
make e2e-templates-tests  # 종단간 템플릿 테스트 실행
```

### 빌드 및 문서화
```bash
make build                # 패키지 빌드
make build-api-reference  # API 문서 빌드
make run-docs             # 문서 서버 시작
```

### 정리
```bash
make clean               # 빌드 아티팩트 및 캐시 제거
```

## 아키텍처 개요

### 크롤러 계층구조
프레임워크는 계층화된 상속 패턴을 사용합니다:
- `BasicCrawler` - 컨텍스트 파이프라인을 가진 모든 크롤러의 기반
- `AbstractHttpCrawler` - HTTP 특화 기능 베이스
- `HttpCrawler` - 원시 HTTP 요청
- `BeautifulSoupCrawler` - BeautifulSoup을 사용한 HTML 파싱
- `ParselCrawler` - Parsel을 사용한 HTML/XML 파싱
- `PlaywrightCrawler` - 브라우저 자동화
- `AdaptivePlaywrightCrawler` - 스마트 렌더링 타입 감지

### 핵심 서브시스템
- **Storage** (`src/crawlee/storages/`) - 플러그 가능한 백엔드를 가진 Dataset, KeyValueStore, RequestQueue
- **Sessions** (`src/crawlee/sessions/`) - 세션 관리 및 쿠키 처리
- **Browsers** (`src/crawlee/browsers/`) - 플러그인 아키텍처를 가진 브라우저 풀 관리
- **Request Loading** (`src/crawlee/request_loaders/`) - URL 발견 및 큐잉 전략
- **Autoscaling** (`src/crawlee/_autoscaling/`) - 동적 동시성 관리
- **Events** (`src/crawlee/events/`) - 크롤러 생명주기를 위한 이벤트 기반 아키텍처
- **Statistics** (`src/crawlee/statistics/`) - 성능 모니터링 및 오류 추적

### 주요 디자인 패턴
- **Service Locator** - `_service_locator.py`를 통한 중앙화된 의존성 주입
- **Context Objects** - 각 크롤러는 특화된 크롤링 컨텍스트를 제공
- **Optional Dependencies** - 누락된 패키지의 우아한 처리를 위한 `try_import` 사용
- **Plugin Architecture** - 확장 가능한 브라우저 및 HTTP 클라이언트 시스템

## 중요한 파일 및 디렉터리

### 핵심 소스 구조
- `src/crawlee/crawlers/` - 모든 크롤러 구현체
- `src/crawlee/storages/` - 데이터 지속성 레이어
- `src/crawlee/storage_clients/` - 스토리지 백엔드 구현체
- `src/crawlee/configuration.py` - 전역 설정 관리
- `src/crawlee/router.py` - 요청 라우팅 시스템
- `src/crawlee/proxy_configuration.py` - 프록시 관리

### 개발 도구
- `pyproject.toml` - 프로젝트 설정, 의존성, 도구 설정
- `Makefile` - 개발 명령어 단축키
- `uv.lock` - 의존성 잠금 파일 (패키지 관리는 `uv` 사용)

### 테스트
- `tests/unit/` - 모듈별로 구성된 단위 테스트
- `tests/e2e/` - 프로젝트 템플릿을 포함한 종단간 테스트
- 테스트는 asyncio 지원과 함께 pytest 사용

## 개발 가이드라인

### 패키지 관리
- 모든 의존성 관리에 `uv` 사용
- 전체 개발 설정을 위해 `make install-dev`로 설치
- 선택적 의존성은 `pyproject.toml` extras에 정의됨

### 코드 스타일
- `pyproject.toml`의 ruff 설정을 따르기
- 문자열에 작은따옴표 사용
- 줄 길이 제한: 120자
- 모든 공개 API에 타입 힌트 필수

### 테스트 고려사항
- `run_alone`으로 표시된 일부 테스트는 격리되어 실행되어야 함
- 브라우저 테스트는 Playwright 설치 필요
- 단위 테스트에서 외부 서비스 모킹
- 테스트 분류를 위한 적절한 pytest 마커 사용

### 크롤러 개발
- 필요에 따라 적절한 베이스 크롤러 클래스 확장
- 특화된 기능을 위한 커스텀 컨텍스트 클래스 구현
- URL 패턴 매칭을 위한 라우터 시스템 사용
- 상태유지 크롤링을 위한 세션 관리 고려

## 일반적인 패턴

### 새 크롤러 생성
1. 적절한 베이스 클래스에서 상속 (`BasicCrawler`, `AbstractHttpCrawler` 등)
2. 필요시 커스텀 크롤링 컨텍스트 정의
3. 라우터 시스템을 사용한 요청 핸들러 구현
4. 컨텍스트 메서드를 통한 스토리지 작업 처리

### 스토리지 사용
- 데이터셋 작업에 `context.push_data()` 사용
- `context.get_key_value_store()`를 통한 키-값 저장소 접근
- `context.add_requests()`를 통한 요청 큐 관리

### 오류 처리
- 크롤러 설정에서 커스텀 오류 핸들러 구현
- 실패한 요청 디버깅을 위한 오류 스냅샷터 사용
- 크롤러 옵션을 통한 재시도 정책 설정