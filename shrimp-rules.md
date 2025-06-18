# 개발 가이드라인

## 프로젝트 개요

### 기술 스택
- **언어**: Python 3.9+
- **패키지 매니저**: uv
- **비동기 프레임워크**: asyncio
- **타입 검사**: 엄격 모드의 mypy
- **린팅**: 모든 규칙이 활성화된 ruff
- **테스팅**: 비동기 지원을 가진 pytest

### 핵심 구성요소
- `src/crawlee/` - 메인 소스 디렉터리
- `tests/unit/` - 소스 구조를 미러링한 단위 테스트
- `tests/e2e/` - 종단간 테스트
- `docs/` - 문서 소스 파일
- `website/` - Docusaurus 문서 사이트

## 코드 표준

### Import 구조
- 모든 파일 상단에 `from __future__ import annotations` 배치
- import 순서: 표준 라이브러리 → 서드파티 → crawlee
- TYPE_CHECKING import는 끝에 별도 블록으로 배치
- import에 작은따옴표 사용

### 타입 어노테이션
- 모든 함수 매개변수와 반환 타입에 어노테이션 추가
- 순환 import 방지를 위해 `TYPE_CHECKING` 블록 사용
- 구조화된 딕셔너리에 TypedDict 적용
- Pydantic 모델에 Field와 함께 Annotated 활용

### 문자열 포맷팅
- 문자열에 작은따옴표 사용
- 독스트링에 큰따옴표 사용
- 최대 줄 길이: 120자
- 포맷팅에 f-string 적용

### 클래스 문서화
- Google 독스트링 형식 적용
- 한 줄 요약 후 자세한 설명 포함
- API 문서 분류를 위한 `@docs_group` 데코레이터 추가
- 모든 공개 메서드와 클래스 문서화

## 기능 구현 표준

### 새 크롤러 생성
1. `src/crawlee/crawlers/_<name>/` 디렉터리 생성
2. 조건부 import가 있는 `__init__.py` 생성
3. 적절한 베이스에서 상속하는 크롤러 클래스 생성:
   - HTTP 기반 크롤러의 경우 `AbstractHttpCrawler`
   - 브라우저 기반 크롤러의 경우 `BasicCrawler`
4. 적절한 베이스 컨텍스트를 확장하는 컨텍스트 클래스 생성
5. `_context_pipeline` 메서드 오버라이드
6. `src/crawlee/crawlers/__init__.py`에 export 추가
7. `tests/unit/crawlers/_<name>/` 테스트 디렉터리 생성
8. BeautifulSoupCrawler 또는 PlaywrightCrawler의 기존 크롤러 패턴 따르기

### 요청 핸들러 추가
```python
@crawler.router.default_handler
async def handler(context: BasicCrawlingContext) -> None:
    # 구현
```
- 항상 비동기 함수 사용
- 크롤러 타입에 맞는 컨텍스트 매개변수 수용
- None 반환

### 스토리지 구성요소 수정
- `context.session.kvs` 또는 `context.session.dataset`을 통한 스토리지 접근
- 크롤러 코드에서 스토리지 클래스를 직접 import하지 않기
- 설정에 서비스 로케이터 패턴 사용

### 에러 처리
- `src/crawlee/errors.py`에 커스텀 예외 생성
- 적절한 베이스 예외에서 상속
- 설명적인 오류 메시지 포함
- 특정 예외 catch, bare except 사용 금지

## 프레임워크/플러그인 사용 표준

### Pydantic 모델
- `BaseModel`에서 상속
- API 호환성을 위해 별칭과 함께 `Field` 사용
- 커스텀 검증을 위해 `BeforeValidator` 적용
- 필요시 `ConfigDict`로 설정
- 크롤러 파일이 아닌 적절한 모듈에 모델 배치

### 비동기 작업
- 모든 I/O 작업을 async로 표시
- 컨텍스트 매니저에 `async with` 사용
- 동시 작업에 `asyncio.create_task` 적용
- 비동기 함수에서 블로킹 I/O 사용 금지

### HTTP 클라이언트
- `context.session.http_client`를 통한 접근
- HTTP 클라이언트를 직접 인스턴스화하지 않기
- HttpxHttpClient와 CurlImpersonateHttpClient 모두 지원

## 워크플로우 표준

### 요청 처리 플로우
1. crawler.run() 또는 crawler.add_requests()를 통한 요청 진입
2. RequestManager가 큐 작업 처리
3. 크롤러가 라벨에 따라 핸들러에 요청 할당
4. 핸들러가 컨텍스트를 사용하여 요청 처리
5. Dataset 또는 KeyValueStore를 통한 결과 저장

### 컨텍스트 파이프라인 플로우
- BasicCrawler가 BasicCrawlingContext 생성
- 크롤러별 파이프라인이 컨텍스트 변환
- 각 파이프라인이 순차적으로 기능 추가
- 최종 컨텍스트가 핸들러에 전달

## 핵심 파일 상호작용 표준

### 다중 파일 조정 요구사항

#### 새 기능 추가 시
- 공개 API export 추가 시 **`src/crawlee/__init__.py` 수정**
- 새 크롤러 타입 추가 시 **`src/crawlee/crawlers/__init__.py` 업데이트**
- 소스 구조와 정확히 일치하는 **테스트 구조 유지**
- 해당 `__init__.pyi` 파일의 **타입 스텁 업데이트**

#### 핵심 구성요소 수정 시
- **BasicCrawler 변경**은 모든 크롤러 구현에 영향
- **Router 수정**은 모든 요청 처리에 영향
- **Context 베이스 클래스 변경**은 모든 컨텍스트 구현 업데이트 필요
- **Storage 인터페이스 변경**은 서비스 로케이터와 모든 크롤러에 영향

#### 문서 업데이트
- 명시적으로 요청되지 않는 한 **문서 생성 금지**
- **공개 API 수정 시** 독스트링만 업데이트
- **README 파일 생성 금지** 또는 마크다운 문서

## AI 의사결정 표준

### 우선순위 계층
1. 사용자의 명시적 지시사항
2. 같은 모듈의 기존 코드 패턴
3. 유사한 모듈의 패턴
4. 베이스 클래스 구현

### 불확실성 존재 시
1. 유사한 파일의 기존 구현 확인
2. 코드베이스에서 가장 일반적인 패턴 따르기
3. 상속보다 컴포지션 선호
4. 하위 호환성 유지

### 코드 생성 규칙
- 기존 유사 코드의 패턴 복사
- 모듈 규칙과 일치하는 일관된 네이밍 유지
- 확립된 오류 처리 패턴 따르기
- 새로운 유틸리티 함수 생성보다 기존 함수 사용

## 금지된 행동

### 절대 하지 말 것
- ❌ 명시적으로 요청되지 않는 한 문서 파일(*.md) 생성
- ❌ `src/crawlee/project_template/` 디렉터리 내용 수정
- ❌ 패키지 외부에서 내부 모듈(`_` 접두사) import
- ❌ 테스트 외부에서 `assert` 문 사용
- ❌ 재발생 없이 일반 Exception catch
- ❌ 클래스 외부에서 비공개 속성(`_` 접두사) 접근
- ❌ 모듈 간 순환 import 생성
- ❌ 비동기 함수에서 동기 I/O 작업 사용
- ❌ 적절한 컨텍스트 없이 크롤러 인스턴스화
- ❌ 자동 생성된 파일(*.pyi 스텁) 수정

### 항상 할 것
- ✅ 코드 커밋 전 `make format` 실행
- ✅ 모든 검사가 통과하는지 확인하기 위해 `make check-code` 실행
- ✅ 공유 리소스 접근에 서비스 로케이터 사용
- ✅ 같은 모듈의 기존 패턴 따르기
- ✅ 모든 새 코드에 타입 어노테이션 추가
- ✅ 새 기능에 대한 단위 테스트 생성
- ✅ 모든 I/O 작업에 async/await 사용
- ✅ 특정 예외 타입으로 오류 처리
- ✅ 내부 모듈이 아닌 공개 API(`crawlee`)에서 import
- ✅ 공개 API의 하위 호환성 유지

## 명령어 참조

### 개발 명령어
- `make install-dev` - 개발 환경 설정
- `make format` - 코드 자동 포맷팅
- `make lint` - 코드 스타일 검사
- `make type-check` - 타입 어노테이션 검증
- `make check-code` - 모든 검사 실행
- `make unit-tests` - 단위 테스트 실행
- `make unit-tests-cov` - 커버리지 리포트 생성

### 빌드 명령어
- `make build-docs` - API 문서 생성
- `make clean` - 빌드 아티팩트 제거

## 테스트 표준

### 단위 테스트 요구사항
- 소스 디렉터리 구조를 정확히 미러링
- 테스트 파일에 `test_` 접두사
- 테스트 함수에 `test_` 접두사
- 외부 의존성 모킹
- 성공과 오류 사례 모두 테스트
- 비동기 테스트에 `pytest.mark.asyncio` 사용

### 테스트 구성
```
tests/unit/crawlers/_beautifulsoup/test_beautifulsoup_crawler.py
tests/unit/crawlers/_beautifulsoup/test_beautifulsoup_crawler_context.py
```
- 각 소스 파일에 대한 별도 테스트 파일
- 클래스에서 관련 테스트 그룹화
- 동작을 나타내는 설명적인 테스트 이름 사용

## 버전 제어 표준

### 커밋 메시지
- conventional commits 형식 따르기
- 타입: feat, fix, docs, style, refactor, test, chore
- 해당 시 범위 포함: `feat(crawler): add new feature`
- 제목 줄을 72자 미만으로 유지

### 브랜치 전략
- main에서 기능 브랜치 생성
- main 또는 master에 직접 커밋 금지
- 해당 시 브랜치 이름에 이슈 번호 포함