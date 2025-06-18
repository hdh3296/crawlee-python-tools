# eformsign 기능 임베딩하기 — eformsign API 가이드 2024.12.27 documentation

> **자동 생성된 가이드 문서**

**출처**: https://eformsignkr.github.io/developers/help/eformsign_embedding_v2.html#eformsign
**제목**: eformsign 기능 임베딩하기 — eformsign API 가이드 2024.12.27 documentation
**생성일**: 2025-06-18 16:29

---

# eformsign 기능 임베딩하기

eformsign 기능을 임베딩하게 되면, 고객이 제공하고 있는 서비스(혹은 사이트) 내에서 고객사의 사용자(최종 사용자)가 eformsign 서비스 사이트를 통하지 않고 고객의 서비스를 통해 eformsign 전자문서를 사용할 수 있습니다.

예를 들면, 내 블로그에서 특정 YouTube 동영상을 소개하고자 할 때, 블로그에서 YouTube 동영상을 임베딩하여 해당 동영상을 블로그 내에서 바로 재생할 수 있도록 하는 방식과 유사합니다.

## 설치하기

### 개요

eformsign 임베딩은 현재 다음의 기능을 지원하고 있습니다.

- 템플릿으로 문서 작성
- 내 파일로 문서 작성
- 문서 처리
- 문서 미리보기
- 템플릿 생성
- 템플릿 수정
- 템플릿 복제

위의 기능을 임베딩하기 위한 객체는 현재 EformSignDocument와 EformSignTemplate 두 종류를 제공하고 있습니다. 각 객체가 담당하고 있는 기능을 확인 후 설치해 주세요.

#### eformsign 임베딩용 객체

| 객체명 | 담당 기능 |
|---|---|
| EformSignDocument | 템플릿으로 문서 작성문서 처리문서 미리보기 |
| EformSignTemplate | 내 파일로 문서 작성템플릿 생성템플릿 수정템플릿 복제 |

### 설치 방법

eformsign의 기능을 사용하고자 하는 웹 페이지에 다음의 스크립트를 추가합니다.

```javascript
<!--jQuery-->
<script src="https://www.eformsign.com/plugins/jquery/jquery.min.js"/>
<!--EformSignDocument 객체-->
<script src="https://www.eformsign.com/lib/js/efs_embedded_v2.js"/>
<!--EformSignTemplate 객체-->
<script src="https://www.eformsign.com/lib/js/efs_embedded_form.js"/>
```

Note

eformsign 기능을 삽입하고자 하는 페이지에 이 스크립트를 추가하면 eformsign 임베딩용 객체를 전역변수로 사용할 수 있습니다.스크립트는 HTML 파일 내 head, body 등 어떤 위치에 추가하여도 무관하나, eformsign 임베딩용 객체를 사용하기 전에 먼저 선언하여야 합니다.jQuery의 경우, 이미 다른 방식으로 웹페이지에 추가되어 있다면 중복으로 추가 필요는 없습니다.

## 임베딩 옵션 설정하기

eformsign 기능 임베딩 시, 임베딩하는 기능에 대한 상세 옵션을 JSON 형태로 설정해야 합니다.회사 정보, 임베딩 모드, 사용자 정보, 레이아웃, 자동 기입 등을 설정할 수 있습니다.

### 기능별 설정값

eformsign 기능 임베딩은 어떤 객체를 사용하고, 어떤 모드를 설정하는 지에 따라 구동되는 기능이 달라집니다.다음 표에서 각 기능별로 사용해야 할 객체와 임베딩 모드를 확인해 주세요.

Note

임베딩 모드 설정은 document_option 혹은 template_option 하위의 “mode” Object에 값을 입력하는 것을 의미합니다. 자세한 설정 방법은 각 기능별 페이지를 참고해주세요.

| 임베딩할 기능 | 사용할 객체 | 임베딩 모드 |
|---|---|---|
| 템플릿으로 문서 작성 | EformSignDocument | “type”: “01” |
| 문서 처리 | EformSignDocument | “type”: “02” |
| 문서 미리 보기 | EformSignDocument | “type”: “03” |
| 내 파일로 문서 작성 | EformSignTemplate | “type”: “01”, “template_type”: “unstructured_form” |
| 템플릿 생성 | EformSignTemplate | “type”: “01”, “template_type”: “form” |
| 템플릿 수정 | EformSignTemplate | “type”: “02”, “template_type”: “form” |
| 템플릿 복제 | EformSignTemplate | “type”: “03”, “template_type”: “form” |

### 필요한 값 확인

임베딩 옵션 설정 시, 삽입하는 기능에 따라 회사 ID, 템플릿 ID, 문서 ID를 입력해야 할 때가 있습니다.

#### 회사 ID 확인 방법

회사 ID는 회사 관리자 혹은 대표 관리자 계정으로 로그인 후**회사 관리 > 회사 정보 > 기본 정보**에서 회사 ID를 확인할 수 있습니다.

1. eformsign 사이드바 메뉴에서 회사 정보 메뉴를 클릭합니다.

1. 회사 정보 > 기본 정보에서 회사 ID를 확인합니다.

#### 템플릿 ID 확인 방법

템플릿 관리 메뉴로 이동하여 사용하려는 템플릿의 설정 아이콘을 클릭하면 해당 템플릿의 URL에서 form_id를 확인할 수 있습니다.

1. eformsign 사이드바 메뉴에서 템플릿 관리를 클릭합니다.

1. eformsign 템플릿 관리 화면에서 해당 템플릿의 설정 버튼을 클릭합니다.

1. 템플릿의 URL에서 템플릿 ID(=form_id)를 확인합니다.

#### 문서 ID 확인 방법

문서 ID는 해당 문서가 있는 문서함 목록에서 확인할 수 있습니다.

1. eformsign 사이드바 메뉴에서 해당 문서가 있는 문서함 메뉴를 클릭합니다.

1. 문서함의 우측 상단의 컬럼 선택 아이콘 ()을 클릭 후 문서 ID를 체크하면 목록에 문서 ID 컬럼이 추가되어 문서 ID를 확인할 수 있습니다.

### 템플릿 문서 작성, 문서 처리, 문서 미리보기

eformsign을 임베딩하여 템플릿으로 문서를 작성하거나, 수신한 문서를 처리 또는 생성된 문서를 미리보기하는 기능을 삽입하는 경우에 대해 설명합니다.

```javascript
var eformsign = new EformSignDocument();

var document_option = {
   "company" : {
      "id" : "",            // Company ID 입력
      "country_code" : "",  // 국가 코드 입력 (ex: kr)
      "user_key": ""        // 임베딩한 고객 측 시스템에 로그인한 사용자의 unique key. 브라우저 쿠키의 이폼사인 로그인 정보와 비교
   },
   "user" : {
        "type" : "01" ,         // 사용자 구분 (01: 멤버, 02: 외부자)
        "id": "test1@forcs.com" // 사용자 ID(이메일)
        "access_token" : "",    // Access Token 입력 (eformsign API 사용하기 - Access Token 발급 참조)
        "refresh_token" : "",   // Refresh Token 입력 (eformsign API 사용하기 - Access Token 발급 참조)
        "external_token" : "",  // 외부자 처리 시 사용자를 인증할 External Token 입력 (Webhook에서 제공)
        "external_user_info" : {
           "name" : ""          // 외부자 처리 시 외부자 이름 입력
        }
    },
    "mode" : {
        "type" : "02",      // 모드 (01: 새 문서 작성, 02: 문서 처리, 03: 문서 미리보기)
        "template_id" : "", // template id 입력
        "document_id" : ""  // document_id 입력
    },
    "layout" : {
        "lang_code" : "ko" // 이폼사인 언어. ko, en, ja
    },
    "prefill" : {
        "document_name": "", // 문서 제목 입력
        "fields": [
            {
                "id" ; "고객명",       // 필드명
                "value" : "홍길동",    // 필드값
                "enabled" : true,   // 활성화 여부
                "required" : true   // 필수 여부
            }
        ],
        "recipients": [
            {
                "step_idx" : "2",       // 워크플로우 순서. 수신자가 있을 경우 2부터 시작
                "step_type": "06",      // 단계 종류. 05: 참여자, 06: 검토자
                "name" : '김테스트',        // 수신자 이름
                "id": "test@forcs.com", // 수신자 ID/이메일
                "sms": "01023456789",   // 수신자 핸드폰 번호
                "use_mail": true,       // 이메일 알림 사용 여부
                "use_sms": true,        // SMS 알림 사용 여부
                "auth": {
                    "password": "",     // 워크플로우 설정에서 문서 열람 전 본인확인 설정 - 본인확인 정보에 체크한 경우 비밀번호 입력
                    "password_hint": "",// 위 조건에 따라 비밀번호를 입력한 경우, 비밀번호 힌트
                    "valid": {
                        "day": 7,       // 문서 전송 기한 (일)
                        "hour": 0       // 문서 전송 기한 (시간)
                    }
                }
            }
        ],
        "comment": "여기에 코멘트 입력"     // 메시지
    },
    "return_fields" : ['고객명']           // Success Callback에서 값을 확인할 수 있도록 넘겨줄 필드명
};

//callback option
var success_callback = function(response){
    console.log(response.code);
    if( response.code == "-1"){
        //문서 작성 성공
        console.log(response.document_id);
        // return_fields에 넘긴 데이터를 조회 가능함. fields는 폼을 작성할 때 만든 입력 컴포넌트의 id를 의미함.
        console.log(response.field_values["company_name"]);
        console.log(response.field_values["position"]);
    }
};

var error_callback = function(response){
    console.log(response.code);
    //문서 작성 실패
    alert(response.message);
};


var action_callback = function (response) {
    console.table(response.data);
};

eformsign.document(document_option, "eformsign_iframe", success_callback, error_callback, action_callback);
eformsign.open();
```

#### document_option

옵션 설정을 위한 JSON은 다음과 같은 구조로 이루어져 있습니다.

| 변수명 | 설명 | 데이터 타입 | 필수 | 하위 옵션 |
|---|---|---|---|---|
| company | 회사 정보 | Object | O | id, country_code, user_key |
| mode | 임베딩 모드 | Object | O | type, template_id, document_id |
| user | 사용자 정보 | Object | X | type, id, access_token, refresh_token, external_token, external_user_info |
| layout | 레이아웃 | Object | X | lang_code |
| prefill | 자동 기입 | Object | X | document_name, fields, recipients, comment |
| return_fields | 리턴 필드 | Array | X |  |

Note

회사 정보와 모드는 필수 입력정보입니다.

##### 1. company(회사 정보/필수)

| 변수명 | 설명 | 데이터 타입 | 필수 | 비고 |
|---|---|---|---|---|
| id | 회사 ID | String | O | 회사 관리 - 회사 정보에서 확인 |
| country_code | 국가 코드 | String | X | 회사 관리 - 회사 정보의 국가에 대한 코드를 지정. 비필수이나, 입력 시 빠른 open이 가능함 |
| user_key | 고객시스템 사용자 고유 키 | String | X | 임베딩하는 고객사의 시스템에서 해당 유저가 누구인지를 명확히 설정하기 위해 eformsign에 넘겨주는 사용자 계정 정보임브라우저에 이미 로그인 정보가 있을 경우, 해당 key와 비교하여 일치하지 않는 경우 로그아웃 처리됨 |

```javascript
var document_option = {
      "company" : {
          "id" : 'f9aec832efef4133a1e849efaf8a9aed',
          "country_code" : "kr",
          "user_key": "eformsign@forcs.com"
      }
 };
```

##### 2. mode(임베딩 모드/필수)

| 변수명 | 설명 | 데이터 타입 | 필수 | 비고 |
|---|---|---|---|---|
| type | 기능 타입 | String | O | 01: 문서 작성, 02: 문서 처리, 03: 미리 보기 |
| template_id | 템플릿 ID | String | O |  |
| document_id | 문서 ID | String | X | 문서 처리, 미리 보기 시 필수 입력 |

**템플릿을 이용한 신규 작성**

템플릿을 이용하여 문서를 새로 작성합니다.

```javascript
var document_option = {
   "mode" : {
    "type" : "01" ,  // 01 : 문서 작성 , 02 : 문서 처리 , 03 : 미리 보기
    "template_id" : "a2c6ed9df9b642f2ade43c7efe58c9a3" // template id 입력
  }
}
```

**수신한 문서를 이용한 추가 작성**

수신한 문서를 이용하여 추가로 문서를 작성합니다.

```javascript
var document_option = {
   "mode" : {
    "type" : "02" ,  // 01 : 문서 작성 , 02 : 문서 처리 , 03 : 미리 보기
    "template_id" : "a2c6ed9df9b642f2ade43c7efe58c9a3", // template id 입력
    "document_id" : "5c19ff8c703f401c968236837d701e92"  // document_id 입력
  }
}
```

**특정 문서를 미리보기**

작성된 문서를 미리보기합니다.

```javascript
var document_option = {
   "mode" : {
    "type" : "03" ,  // 01 : 문서 작성 , 02 : 문서 처리 , 03 : 미리 보기
    "template_id" : "a2c6ed9df9b642f2ade43c7efe58c9a3", // template id 입력
    "document_id" : "5c19ff8c703f401c968236837d701e92"  // document_id 입력
  }
}
```

##### 3. user(사용자 정보/비필수)

| 변수명 | 설명 | 데이터 타입 | 필수 | 비고 |
|---|---|---|---|---|
| type | 사용자 타입 | String | O | 01: 회사 멤버, 02: 외부 작성자 |
| id | 계정(이메일) | String | X | 사용자 ID/이메일 입력 |
| access_token | Access Token | String | X | Open API > Access Token 발급 참조 |
| refresh_token | Refresh Token | String | X | Open API > Access Token 발급 참조 |
| external_token | 외부자 처리용 토큰 | String | X | 멤버가 아닌 사용자가 수신한 문서 처리 시 필수 입력 (Webhook에서 제공) |
| external_user_info | 외부 작성자 정보 | Object | X | 멤버가 아닌 사용자가 문서 작성 또는 처리 시 필수 입력 |
| external_user_info.name | 외부 작성자 이름 | String | X | 멤버가 아닌 사용자가 문서 작성 또는 처리 시 필수 입력 |

**회사 내 멤버 로그인을 통한 작성 또는 처리**

유저 정보를 지정하지 않을 경우에 해당합니다.이 경우, eformsign 로그인 페이지가 구동되며 로그인 과정 이후에 문서를 작성할 수 있습니다.

**회사 내 멤버 로그인을 통한 작성 또는 처리 (ID 사전 입력)**

임베딩 시, eformsign 로그인 페이지가 구동되어 로그인 과정 이후에 문서를 작성할 수 있습니다. 이때, ID가 로그인 화면에 미리 입력되어 있습니다.

```javascript
var document_option = {
    "user":{
        "type" : "01",
        "id" : "eformsign@forcs.com"
    }
};
```

**회사 내 멤버의 토큰을 이용한 작성 또는 처리**

임베딩 시, eformsign 로그인 과정없이, 특정 계정의 token을 이용하여 문서를 작성 및 수신한 문서를 작성합니다.토큰 발급 방법은 eformsign API 사용하기 -Access Token 발급을 확인해 주세요.

```javascript
var document_option = {
    "user":{
        "type" : "01",
        "id" : "eformsign@forcs.com",
        "access_token" : "eyJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJlZ...",
        "refresh_token" : "0161ac6c-0f47-4cc3-9301-381f57c41495"
    }
};
```

**회사 내 멤버가 아닌 사용자가 신규 문서 작성**

eformsign의 회원이 아닌 사용자가 문서를 작성할 수 있도록 하는 방식입니다.

```javascript
var document_option = {
    "user":{
        "type" : "02",
        "external_user_info" : {
           "name" : "홍길동"
        }
    }
};
```

**회사 내 멤버가 아닌 사용자가 수신한 문서를 작성**

임베딩 시, eformsign의 회원이 아닌 사용자가 수신한 문서를 작성할 수 있도록 하는 방식입니다.

```javascript
var document_option = {
    "user":{
        "type" : "02",
        "external_token" : "f8e2ff29114445dcac1e2889ac2f8a5e",
        "external_user_info" : {
            "name" : "홍길동"
        }
    }
};
```

##### 4. layout(레이아웃/비필수)

| 변수명 | 설명 | 데이터 타입 | 필수 | 비고 |
|---|---|---|---|---|
| lang_code | eformsign 언어 | String | X | ko: 한국어, en: 영어, ja: 일본어 |
| header | 헤더(상단바) 표시 여부 | Boolean | X | 미입력 시 기본값: true헤더 미표시(false) 시 ‘전송’ 등의 기능 버튼도 표시되지 않으므로, 별도로 기능 버튼을 생성해주어야 함(화면 로드 시_액션 버튼 생성 참조) |
| footer | 푸터 표시 여부 | Boolean | X | 미입력 시 기본값: true |

```javascript
var document_option = {
    "layout" : {
          "lang_code" : "ko",
          "header" : false,
          "footer" : true
    }
}
```

##### 5. prefill(자동 기입/비필수)

문서 작성 과정 중에 자동으로 입력될 수 있도록 처리 시 사용합니다.

Important

mode.type이 “03”일 경우(문서 미리보기 시)에는 작동하지 않습니다.

| 변수명 | 설명 | 데이터 타입 | 필수 | 비고 |
|---|---|---|---|---|
| document_name | 문서 제목 | String | X |  |
| fields | 필드 목록 | Array | X | 필드 설정 Object의 목록 |
| fields[].id | 필드명 | String | X | 필드 설정 Object내에서는 필수 (필드명을 기준으로 설정 적용) |
| fields[].value | 필드값 | String | X | -지정하지 않을 경우, 신규 작성 시 템플릿 설정의 필드 설정 옵션을 따름-설정할 경우, 템플릿 설정의 필드 설정보다 우선 순위 높음 |
| fields[].enabled | 필드 활성화 여부 | Boolean | X | -지정하지 않을 경우, 템플릿 설정의 항목 제어 옵션에 따름-설정할 경우, 템플릿 설정의 항목 제어 옵션보다 우선 순위 높음 |
| fields[].required | 필드 필수 여부 | Boolean | X | -지정하지 않을 경우, 템플릿 설정의 항목 제어 옵션에 따름-설정할 경우, 템플릿 설정의 항목 제어 옵션보다 우선 순위 높음 |
| recipients | 수신자 목록 | Array | X | 수신자 정보 Object의 목록 |
| recipients[].step_idx | 워크플로우 순서 | String | X | recipients 내 각 객체에 필수 설정되어야 함-첫 번째 수신자: “2”-두 번째 이후 수신자: 순서에 따라 1씩 증가 |
| recipients[].step_type | 워크플로우 수신자 유형 | String | X | recipients 내 각 객체에 필수 설정되어야 함-기존 워크플로우: “01”(완료), “02”(결재), “03”(외부 수신자), “04”(내부 수신자)-신규 워크플로우: “01”(완료), “05”(참여자), “06”(검토자) |
| recipients[].recipient_type | 수신자 구분 | String | X | step_type이 02(결재), 03(외부 수신자), 04(내부 수신자)인 경우에만 필수 입력-“01”: 수신자가 회사 멤버인 경우-“02”: 외부 수신자인 경우 |
| recipients[].name | 수신자 이름 | String | X |  |
| recipients[].id | 계정(이메일) | String | X | -회사 멤버의 계정 정보 (ID/이메일) 입력-step_type이 05(참여자) 혹은 06(검토자)인 경우, 멤버 여부 관계없이 이메일 주소 입력 가능 |
| recipients[].email | 이메일 주소 | String | X | step_type이 03(외부 수신자)인 경우에만 사용-외부 수신자의 이메일 주소 입력 |
| recipients[].sms | 휴대폰 번호 | String | X |  |
| recipients[].use_mail | 이메일 발송 여부 | Boolean | X | step_type이 05(참여자) 혹은 06(검토자)인 경우에만 사용 |
| recipients[].use_sms | SMS 발송 여부 | Boolean | X | step_type이 05(참여자) 혹은 06(검토자)인 경우에만 사용 |
| recipients[].auth | 본인 확인 및문서 전송 기한 정보 | Object | X |  |
| recipients[].auth.password | 본인 확인 정보 (비밀번호) | String | X | 워크플로우 설정에서 문서 열람 전 본인확인 설정 - 문서 접근 암호에 체크한 경우 비밀번호 입력 |
| recipients[].auth.password_hint | 본인 확인 정보 도움말(비밀번호 힌트) | String | X | 위 조건에 따라 비밀번호를 입력한 경우, 비밀번호 힌트 |
| recipients[].auth.valid | 문서 전송 기한 정보 | Object | X | 미 입력시 기본값: 0일 0시간 (멤버의 경우 무제한, 외부 수신자의 경우 화면 상에서 재입력 필요) |
| recipients[].auth.valid.day | 문서 전송 기한 (일) | Integer | X |  |
| recipients[].auth.valid.hour | 문서 전송 기한 (시간) | Integer | X |  |
| comment | 다음 수신자에게 전달할 메시지 | String | X |  |

```javascript
var document_option = {
    "prefill" : {
        "document_name": "개인정보활용동의서",   // 문서 제목 입력
        "fields": [
            {
                "id" ; "고객명",       // 필드명
                "value" : "홍길동",    // 필드값
                "enabled" : true,   // 활성화 여부
                "required" : true   // 필수 여부
            }
        ],
        "recipients": [
            {
                "step_idx" : "2",       // 워크플로우 순서. 수신자가 있을 경우 2부터 시작
                "step_type": "06",      // 워크플로우 수신자 유형. 05: 참여자, 06: 검토자
                "name" : "홍길동",        // 수신자 이름
                "id": "test@forcs.com", // 수신자 ID/이메일
                "sms": "01023456789",   // 수신자 핸드폰 번호
                "use_mail": true,       // 이메일 알림 사용 여부
                "use_sms": true,        // SMS 알림 사용 여부
                "auth": {
                    "password": "6789", // 워크플로우 설정에서 문서 열람 전 본인확인 설정 - 본인확인 정보에 체크한 경우 비밀번호 입력
                    "password_hint": "핸드폰 뒷자리를 입력하세요.", // 위 조건에 따라 비밀번호를 입력한 경우, 비밀번호 힌트
                    "valid": {
                        "day": 7,       // 문서 전송 기한(일)
                        "hour": 0       // 문서 전송 기한(시간)
                    }
                }
            }
        ],
        "comment": "확인 및 서명 바랍니다."  // 메시지
    }
};
```

##### 6. return_fields(리턴 필드/비필수)

문서 작성 및 수정 후, 사용자가 작성한 필드의 내용을 Response를 통해 전달할 항목을 지정합니다.“return_fields” Array 내에 필드명을 String 형태로 입력합니다.

Note

미 지정시 기본 필드만 제공합니다. 관련 내용은작업 성공 실패 시를 참고하세요.

Note

mode.type이 “03”일 경우(문서 미리보기 시)에는 작동하지 않습니다.

```javascript
var document_option = {
   "return_fields" : ['고객명']
}
```

### 내 파일로 문서 작성

eformsign을 임베딩하여 내 파일로 문서 작성 기능을 사용할 수 있습니다.

```javascript
var eformsign = new EformSignTemplate();

var template_option = {
   "company" : {
      "id" : "76440d70fae242e09c4b0fac40b6a6be",            // Company ID 입력
      "country_code" : "kr",    // 국가 코드 입력 (ex: kr)
      "user_key": ""        // 임베딩한 고객 측 시스템에 로그인한 사용자의 unique key. 브라우저 쿠키의 이폼사인 로그인 정보와 비교
   },
   "user" : {
        "id": "test1@forcs.com"
        "access_token" : "",    // Access Token 입력 (OpenAPI Access Token 참조)
        "refresh_token" : "",   // Refresh Token 입력 (OpenAPI Access Token 참조)
    },
    "mode" : {
        "type" : "01",      // 01 : 생성
        "template_id" : "", // template id 입력
        "template_type": "unstructured_form"    // form : 템플릿 관리, unstructured_form: 내 파일로 문서 작성
    },
    "layout" : {
        "lang_code" : "ko", // 이폼사인 언어. ko, en, ja
        "header" : true,    // 상단바 (푸른색) 표시 여부. 미표시 시 액션 버튼을 통해 전송 등 동작 가능
        "footer" : true     // 하단바 (이폼사인 로고, 언어 설정 등) 표시 여부.
    },
    "prefill": {
        "template_name": "템플릿 임베딩 테스트_신규",
        "fields": [
            {
                "id": "텍스트 1",
                "value": "가나다",
                "enabled": true,
                "required": true
            },
            {
                "id": "텍스트 2",
                "value": "라마바",
                "enabled": true,
                "required": true
            }
        ],
        "step_settings": [
            {
                "step_type": "05", // 05: 참여자, 06: 검토자
                "step_name": "참여자 2",
                "use_mail": true,
                "use_sms": true,
                "use_alimtalk" : true,
                "recipients" : [
                    {
                        "id": "test2@forcs.com",
                        "name" : 'John Doe'
                    },
                    {
                        "id" : "5a3e47a2f5a04909836ddf4189d10fc4",
                        "name" : '그룹3'
                    }
                ],
                "auth": {
                    "valid": {
                        "day": '7',
                        "hour": '7'
                    }
                },
                "additional_auth" : {  // 추가 인증 수단
                    use_pincode : true, //이메일/SMS 핀코드 인증
                    use_pincode_result : true, //문서 최종 완료 시 이메일/SMS 핀코드 인증 사용
                    use_mobile_verifyAuth : true, //휴대폰 본인 확인
                    use_mobile_verifyAuth_result : true //문서 최종 완료 시 휴대폰 본인 확인 사용
                }
            }
        ],
        "is_form_id_numbering" : false,
        "disabled_form_id" : true,
        "quick_processing" : false
    },
    "template_file": {
        "name": "첨부테스트.pdf",
        "mime": "@file/octet-stream",
        "data": "JVBERi0xLjUNCiW1tbW1DQoxIDAgb2JqDQo8PC9UeXBlL0NhdGFsb2cvUGFnZXMgMiAwIFIvTGFuZyhrby1LUikgL1N0cnVjdFRyZWVSb290IDE1IDAgUi..."
    }
};

//callback option
var sucess_callback = function (response) {
    if (response.type ==='template'){
        console.log(response.template_id);
        console.log(response.template_name);
        console.table(response.step_settings);
        if ("-1" == response.code) {
            alert("템플릿 생성되었습니다.\n" + "- document_id : " + response.template_id + "\n- title : " + response.template_name);
        } else {
            alert("템플릿 생성에 실패하였습니다.\n" + "- code : " + response.code + "\n- message : " + response.message);
        }
    }
    window.close();
};


var error_callback = function (response) {
    alert("템플릿 생성에 실패하였습니다.\n" + "- code : " + response.code + "\n- message : " + response.message);
    console.log(response.code);
    console.log(response.message);
    window.close();
};

var action_callback = function (response) {
    console.table(response.data);
};

eformsign.template(template_option, "eformsign_iframe", success_callback, error_callback, action_callback);
eformsign.open();
```

#### template_option

옵션 설정을 위한 JSON은 다음과 같은 구조로 이루어져 있습니다.

| 변수명 | 설명 | 데이터 타입 | 필수 | 하위 옵션 |
|---|---|---|---|---|
| company | 회사 정보 | Object | O | id, country_code, user_key |
| mode | 임베딩 모드 | Object | O | type, template_id, document_id |
| user | 사용자 정보 | Object | X | type, id, access_token, refresh_token, external_token, external_user_info |
| layout | 레이아웃 | Object | X | lang_code |
| prefill | 자동 기입 | Object | X | document_name, fields, recipients, comment |
| template_file | 템플릿 파일 | Object | X | name, mime, data |

Note

회사 정보와 모드는 필수 입력정보입니다.

##### 1. company(회사 정보/필수)

| 변수명 | 설명 | 데이터 타입 | 필수 | 비고 |
|---|---|---|---|---|
| id | 회사 ID | String | O | 회사 관리 - 회사 정보에서 확인 |
| country_code | 국가 코드 | String | X | 회사 관리 - 회사 정보의 국가에 대한 코드를 지정. 비필수이나, 입력 시 빠른 open이 가능함 |
| user_key | 고객시스템 사용자 고유 키 | String | X | 임베딩하는 고객사의 시스템에서 해당 유저가 누구인지를 명확히 설정하기 위해 eformsign에 넘겨주는 사용자 계정 정보임브라우저에 이미 로그인 정보가 있을 경우, 해당 key와 비교하여 일치하지 않는 경우 로그아웃 처리됨 |

```javascript
var template_option= {
     "company" : {
         "id" : 'f9aec832efef4133a1e849efaf8a9aed',
         "country_code" : "kr",
         "user_key": "eformsign@forcs.com"
     }
};
```

##### 2. mode(임베딩 모드/필수)

| 변수명 | 설명 | 데이터 타입 | 필수 | 비고 |
|---|---|---|---|---|
| type | 기능 타입 | String | O | 01: 생성 |
| template_type | 임베딩 종류 | String | O | “unstructured_form”: 내 파일로 문서 작성 |

**내 파일로 문서 작성**

내 파일로 문서 작성을 통해 문서를 새로 작성합니다.

```javascript
var template_option= {
   "mode" : {
    "type" : "01",
    "template_type" : "unstructured_form"
  }
}
```

##### 3. user(사용자 정보/비필수)

| 변수명 | 설명 | 데이터 타입 | 필수 | 비고 |
|---|---|---|---|---|
| id | 계정(이메일) | String | X | 사용자 ID/이메일 입력 |
| access_token | Access Token | String | X | Open API > Access Token 발급 참조 |
| refresh_token | Refresh Token | String | X | Open API > Access Token 발급 참조 |

**회사 내 멤버 로그인을 통한 작업 (ID 사전 입력)**

임베딩 시, eformsign 로그인 페이지가 구동되어 로그인 과정 이후에 템플릿 관리 작업을 할 수 있습니다. 이때, ID가 로그인 화면에 미리 입력되어 있습니다.

```javascript
var document_option = {
    "user":{
        "id" : "eformsign@forcs.com"
    }
};
```

**회사 내 멤버의 토큰을 이용한 작업**

임베딩 시, eformsign 로그인 과정없이, 특정 계정의 token을 이용하여 템플릿 관리 작업을 수행합니다.토큰 발급 방법은 eformsign API 사용하기 -Access Token 발급을 확인해 주세요.

```javascript
var document_option = {
    "user":{
        "id" : "eformsign@forcs.com",
        "access_token" : "eyJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJlZ...",
        "refresh_token" : "0161ac6c-0f47-4cc3-9301-381f57c41495"
    }
};
```

##### 4. layout(레이아웃/비필수)

| 변수명 | 설명 | 데이터 타입 | 필수 | 비고 |
|---|---|---|---|---|
| lang_code | eformsign 언어 | String | X | ko: 한국어, en: 영어, ja: 일본어 |
| header | 헤더(상단바) 표시 여부 | Boolean | X | 미입력 시 기본값: true헤더 미표시(false) 시 ‘전송’ 등의 기능 버튼도 표시되지 않으므로, 별도로 기능 버튼을 생성해주어야 함(화면 로드 시_액션 버튼 생성 참조) |
| footer | 푸터 표시 여부 | Boolean | X | 미입력 시 기본값: true |

```javascript
var template_option = {
    "layout" : {
          "lang_code" : "ko",
          "header" : true,
          "footer" : true
    }
}
```

##### 5. prefill(자동 기입/비필수)

문서 작성 과정 중에 자동으로 입력될 수 있도록 처리 시 사용합니다.

| 변수명 | 설명 | 데이터 타입 | 필수 | 비고 |
|---|---|---|---|---|
| template_name | 문서 제목 | String | X |  |
| fields | 문서 작성 시 기본값 목록 | Array | X | 필드 설정 Object의 목록 |
| fields[].id | 기본값을 입력할 필드명 | String | X |  |
| fields[].value | 필드에 입력할 기본값 | String | X |  |
| fields[].enabled | 문서 작성 시 필드 활성화 여부 | Boolean | X | -지정하지 않을 경우, 폼 디자인하기 단계의 항목 제어 옵션에 따름-설정할 경우, 폼 디자인하기 단계의 항목 제어 옵션보다 우선 순위 높음 |
| fields[].required | 문서 작성 시 필드 필수 입력 여부 | Boolean | X | -지정하지 않을 경우, 폼 디자인하기 단계의 항목 제어 옵션에 따름-설정할 경우, 폼 디자인하기 단계의 항목 제어 옵션보다 우선 순위 높음 |
| step_settings | 워크플로우 단계 목록 | Array | X | 단계 정보 Object의 목록 |
| step_settings[].step_type | 워크플로우 수신자 유형 | String | X | -기존 워크플로우: “02”(결재), “03”(내부 수신자), “04”(외부 수신자)-신형 워크플로우: “05”(참여자), “06”(검토자)step_settings내 각 객체에 필수 설정되어야 함 |
| step_settings[].step_name | 워크플로우 단계 이름 | String | X |  |
| step_settings[].selected | 폼 디자인하기 단계에서기본 문서 참여자로 표시 여부 | Boolean | X | -미 입력 시 기본값: false-모든 단계에서 미 입력 혹은 false일 시 시작/발송인 단계가 기본으로 표시됨 |
| step_settings[].recipient | 수신자 정보 | Object | X | 수신자 정보 |
| step_settings[].recipient.id | 수신자 이메일 또는 ID | String | X | 해당 단계 수신자 이메일 또는 아이디 입력 |
| step_settings[].recipient.name | 수신자 이름 | String | X |  |
| step_settings[].recipient.sms | 수신자 휴대폰 번호 | String | X | “+821022223333” 형태로 입력 |
| step_settings[].recipient.use_mail | 이메일 발송 여부 | Boolean | X | 미 입력 시 기본값: false |
| step_settings[].recipient.use_sms | SMS 발송 여부 | Boolean | X | 미 입력 시 기본값: false |
| step_settings[].recipient.use_alimtalk | SMS 발송으로 카카오톡 사용 여부 | Boolean | X | 미 입력 시 기본값: falsetrue로 설정 시 카카오톡으로 우선 발송, 실패 시 SMS로 발송함 |
| step_settings[].recipient.auth | 본인 확인 및 문서 전송 기한 정보 | Object | X | type, password, password_hint 모두 미 입력 시: 본인 확인 정보 사용 안 함 |
| step_settings[].recipient.auth.type | 본인 확인 방법 | String | X | 미 입력 시 기본값: password (단, type, password, password_hint 모두 미 입력 시: 본인 확인 정보 사용 안 함)-qna: 수신자 이름-field: 입력 필드 중 선택-password: 보내는 사람이 직접 입력 |
| step_settings[].recipient.auth.password | 본인 확인 정보 | String | X | 미 입력 시 기본값: 빈 값-type이 qna인 경우: 빈 값 입력-type이 field인 경우: 필드명 입력-type이 password인 경우: 빈 값 입력 |
| step_settings[].recipient.auth.password_hint | 본인 확인 정보에 대한 힌트 | String | X | 미 입력 시 기본값: 빈 값 |
| step_settings[].recipient.auth.valid | 문서 전송 기한 정보 | Object | X | 미 입력시 기본값: 7일 0시간 |
| step_settings[].recipient.auth.valid.day | 문서 전송 기한 (일) | Integer | X |  |
| step_settings[].recipient.auth.valid.hour | 문서 전송 기한 (시간) | Integer | X |  |
| step_settings[].recipient.additional_auth | 추가 인증 수단 (비정형) | Object | X |  |
| step_settings[].recipient.additional_auth.use_pincode | 이메일/SMS 인증 사용 여부 | Boolean | X |  |
| step_settings[].recipient.additional_auth.use_pincode_result | 완료 문서 열람 시에도이메일/SMS 인증 사용 여부 | Boolean | X |  |
| step_settings[].recipient.additional_auth.use_mobile_verifyAuth | 휴대폰 본인확인 사용 여부 | Boolean | X |  |
| step_settings[].recipient.additional_auth.use_mobile_verifyAuth_result | 완료 문서 열람 시에도휴대폰 본인확인 사용 여부 | Boolean | X |  |
| is_form_id_numbering | 컴포넌트 추가 시 기본 ID에서번호 부여 여부 | Boolean | X | 텍스트 컴포넌트 추가 시, 컴포넌트 ID의 기본값-is_form_id_numbering이 true일 때: ‘텍스트 1’, ‘텍스트 2’, ‘텍스트 3’-is_form_id_numbering이 false일 때: ‘텍스트’, ‘텍스트’, ‘텍스트’미 입력 시 기본값: true |
| disabled_form_id | 폼 디자인하기 단계에서컴포넌트 ID 입력란 비활성화 여부 | Booelan | X | 미 입력 시 기본값: false |

**문서 이름 기입**

**옵션 > 문서 제목**에 구매신청서가 입력됩니다.

```javascript
var template_option = {
   "prefill" : {
       "template_name": "구매신청서"
    }
}
```

**문서 참여자 및 수신자 지정(본인 확인 정보, 추가 인증 수단 미사용)**

다음과 같이 워크플로우 단계를 추가합니다

- 단계 종류: 참여자
- 단계명: 참여자 1
- 이메일 알림: 사용
- SMS 알림: 미사용
- 수신자 이름: 홍길동
- 수신자 이메일: test1@forcs.com
- 요청 유효기간: 7일 7시간
- 본인 확인 정보: 미사용
- 추가 인증 수단: 미사용

임베딩하여 실행 시 다음과 같이 설정됩니다.

- 문서 참여자: 2명 (발송인, 참여자 1)
- 폼 디자인하기 단계에서 기본으로 표시할 문서 참여자: 발송인
- 워크플로우: 발송인-참여자 1-완료

```javascript
var template_option = {
    "prefill": {
        "step_settings": [
            {
                "step_type": "05",
                "step_name": "참여자 1",
                "selected": false,
                "recipient": {
                    "id": "test1@forcs.com",
                    "name": "홍길동",
                    "sms": "",
                    "use_mail": true,
                    "use_sms": false,
                    "auth": {
                        "valid": {
                            "day": "7",
                            "hour": "7",
                        },
                    }
                }
            }
        ]
    }
};
```

**문서 참여자 및 수신자 지정(본인 확인 정보, 추가 인증 수단 사용)**

다음과 같이 워크플로우 단계를 추가합니다

- 단계 종류: 참여자
- 단계명: 참여자 1
- 이메일 알림: 사용
- SMS 알림: 사용 (카카오톡 우선)
- 수신자 이름: 홍길동
- 수신자 이메일: test1@forcs.com
- 수신자 휴대폰 번호: 010-2222-3333
- 요청 유효기간: 7일 7시간
- 본인 확인 정보: 사용 (입력 필드 중 선택 - 텍스트 1)
- 추가 인증 수단: 사용 (이메일/SMS 인증 사용, 완료 문서 열람 시에는 이메일/SMS 인증 미사용, 휴대폰 본인확인 사용, 완료 문서 열람 시에도 휴대폰 본인확인 사용)

임베딩하여 실행 시 다음과 같이 설정됩니다.

- 문서 참여자: 2명 (발송인, 참여자 1)
- 폼 디자인하기 단계에서 기본으로 표시할 문서 참여자: 참여자 1
- 워크플로우: 발송인-참여자 1-완료

```javascript
var template_option = {
    "prefill": {
        "step_settings": [
            {
                "step_type": "05",
                "step_name": "참여자 1",
                "selected": true,
                "recipient": {
                    "id": "test1@forcs.com",
                    "name": "홍길동",
                    "sms": "+821022223333",
                    "use_mail": true,
                    "use_sms": true,
                    "use_alimtalk" : true,
                    "auth": {
                        "type": "field",
                        "password": "텍스트 1",
                        "password_hint": "생년월일 6자리를 입력하세요",
                        "valid": {
                            "day": "7",
                            "hour": "7",
                        },
                    },
                    "additional_auth" : {
                        "use_pincode": true,
                        "use_pincode_result": false
                        "use_mobile_verifyAuth": true,
                        "use_mobile_verifyAuth_result" : true
                    }
                }
            }
        ]
    }
};
```

**폼 디자인하기 단계에서 컴포넌트 ID 입력란 비활성화 여부 설정**

폼 디자인하기 단계에서 컴포넌트 ID 입력란이 비활성화됩니다. (기본 ID로 고정됨)

```javascript
var template_option = {
    "prefill" : {
        "disabled_form_id" : true
    }
}
```

```javascript
var template_option = {
    "prefill": {
        "template_name": "구매신청서",
        "step_settings": [
            {
                "step_type": "05",
                "step_name": "참여자 1",
                "selected": true,
                "recipient": {
                    "id": "test1@forcs.com",
                    "name": "홍길동",
                    "sms": "+821022223333",
                    "use_mail": true,
                    "use_sms": true,
                    "use_alimtalk" : true,
                    "auth": {
                        "type": "field",
                        "password": "텍스트 1",
                        "password_hint": "생년월일 6자리를 입력하세요",
                        "valid": {
                            "day": "7",
                            "hour": "7",
                        },
                    },
                    "additional_auth" : {
                        "use_pincode": true,
                        "use_pincode_result": false
                        "use_mobile_verifyAuth": true,
                        "use_mobile_verifyAuth_result" : true
                    }
                }
            },
            {
                "step_type": "06",
                "step_name": "검토자 1",
                "selected": false,
                "recipient": {
                    "id": "test2@forcs.com",
                    "name": "김철수",
                    "sms": "",
                    "use_mail": true,
                    "use_sms": false,
                    "auth": {
                        "valid": {
                            "day": "3",
                            "hour": "0",
                        },
                    }
                }
            }
        ],
        disabled_form_id : true
    }
};
```

##### 6. template_file(템플릿 파일/비필수)

템플릿에 사용될 파일이 자동으로 업로드되도록 설정합니다.

| 변수명 | 설명 | 데이터 타입 | 필수 | 비고 |
|---|---|---|---|---|
| name | 파일명 | String | O |  |
| mime | MIME 데이터 형식 | String | O | -PDF: “application/pdf”-지원하는 모든 확장자(OZR, PDF): “@file/octet-stream” |
| data | Base64로 변환한 파일 데이터 | String | O |  |

```javascript
var template_option = {
    "template_file": {
          "name": "첨부테스트.pdf",
          "mime": "@file/octet-stream",
          "data": "JVBERi0xLjUNCiW1tbW1DQoxIDAgb2JqDQo8PC9UeXBlL0NhdGFsb2cvUGFnZXMgMiAwIFIvTGFuZyhrby1LUikgL1N0cnVjdFRyZWVSb290IDE1IDAgUi9NY...(후략)"
    }
}
```

### 템플릿 생성, 템플릿 수정, 템플릿 복제

eformsign을 임베딩하여 템플릿을 생성, 수정, 복제하는 경우에 대해 설명합니다.

```javascript
var eformsign = new EformSignTemplate();

var template_option = {
   "company" : {
      "id" : "76440d70fae242e09c4b0fac40b6a6be",            // Company ID 입력
      "country_code" : "kr",    // 국가 코드 입력 (ex: kr)
      "user_key": ""        // 임베딩한 고객 측 시스템에 로그인한 사용자의 unique key. 브라우저 쿠키의 이폼사인 로그인 정보와 비교
   },
   "user" : {
        "id": "test1@forcs.com"
        "access_token" : "",    // Access Token 입력 (OpenAPI Access Token 참조)
        "refresh_token" : "",   // Refresh Token 입력 (OpenAPI Access Token 참조)
    },
    "mode" : {
        "type" : "01",      // 01 : 생성 , 02 : 수정, 03 : 복제
        "template_id" : "", // template id 입력
        "template_type": "form" // form : 템플릿 관리, unstructured_form: 내 파일로 문서 작성
    },
    "layout" : {
        "lang_code" : "ko", // 이폼사인 언어. ko, en, ja
        "header" : true,    // 상단바 (푸른색) 표시 여부. 미표시 시 액션 버튼을 통해 전송 등 동작 가능
        "footer" : true     // 하단바 (이폼사인 로고, 언어 설정 등) 표시 여부.
    },
    "prefill": {
        "template_name": "템플릿 임베딩 테스트_신규",
        "step_settings": [
            {
                "step_type": "05", // 05: 참여자, 06: 검토자
                "step_name": "참여자 2",
                "use_mail": true,
                "use_sms": true,
                "use_alimtalk" : true,
                "recipients" : [
                    {
                        "id": "test2@forcs.com",
                        "name" : 'John Doe'
                    },
                    {
                        "id" : "5a3e47a2f5a04909836ddf4189d10fc4",
                        "name" : '그룹3'
                    }
                ],
                "auth": {
                    "valid": {
                        "day": '7',
                        "hour": '7'
                    }
                }
            }
        ],
        "quick_processing" : false
    },
    "template_file": {
        "name": "첨부테스트.pdf",
        "mime": "@file/octet-stream",
        "data": "JVBERi0xLjUNCiW1tbW1DQoxIDAgb2JqDQo8PC9UeXBlL0NhdGFsb2cvUGFnZXMgMiAwIFIvTGFuZyhrby1LUikgL1N0cnVjdFRyZWVSb290IDE1IDAgUi..."
    }
};

//callback option
var sucess_callback = function (response) {
    if (response.type ==='template'){
        console.log(response.template_id);
        console.log(response.template_name);
        console.table(response.step_settings);
        if ("-1" == response.code) {
            alert("템플릿 생성되었습니다.\n" + "- document_id : " + response.template_id + "\n- title : " + response.template_name);
        } else {
            alert("템플릿 생성에 실패하였습니다.\n" + "- code : " + response.code + "\n- message : " + response.message);
        }
    }
    window.close();
};


var error_callback = function (response) {
    alert("템플릿 생성에 실패하였습니다.\n" + "- code : " + response.code + "\n- message : " + response.message);
    console.log(response.code);
    console.log(response.message);
    window.close();
};

var action_callback = function (response) {
    console.table(response.data);
};

eformsign.template(template_option, "eformsign_iframe", success_callback, error_callback, action_callback);
```

#### template_option

옵션 설정을 위한 JSON은 다음과 같은 구조로 이루어져 있습니다.

| 변수명 | 설명 | 데이터 타입 | 필수 | 하위 옵션 |
|---|---|---|---|---|
| company | 회사 정보 | Object | O | id, country_code, user_key |
| mode | 임베딩 모드 | Object | O | type, template_id, document_id |
| user | 사용자 정보 | Object | X | type, id, access_token, refresh_token, internal_token, external_token, external_user_info |
| layout | 레이아웃 | Object | X | lang_code, header, footer |
| prefill | 자동 기입 | Object | X | document_name, fields, recipients, comment |
| template_file | 템플릿 파일 | Object | X | name, mime, data |

Note

회사 정보와 모드는 필수 입력정보입니다.

##### 1. company(회사 정보/필수)

| 변수명 | 설명 | 데이터 타입 | 필수 | 비고 |
|---|---|---|---|---|
| id | 회사 ID | String | O | 회사 관리 - 회사 정보에서 확인 |
| country_code | 국가 코드 | String | X | 회사 관리 - 회사 정보의 국가에 대한 코드를 지정. 비필수이나, 입력 시 빠른 open이 가능함 |
| user_key | 고객시스템 사용자 고유 키 | String | X | 임베딩하는 고객사의 시스템에서 해당 유저가 누구인지를 명확히 설정하기 위해 eformsign에 넘겨주는 사용자 계정 정보임브라우저에 이미 로그인 정보가 있을 경우, 해당 key와 비교하여 일치하지 않는 경우 로그아웃 처리됨 |

```javascript
var document_option = {
     "company" : {
         "id" : 'f9aec832efef4133a1e849efaf8a9aed',
         "country_code" : "kr",
         "user_key": "eformsign@forcs.com"
     }
};
```

##### 2. mode(임베딩 모드/필수)

| 변수명 | 설명 | 데이터 타입 | 필수 | 비고 |
|---|---|---|---|---|
| type | 기능 타입 | String | O | 01: 생성, 02: 수정, 03: 복제 |
| template_id | 템플릿 ID | String | X | type이 02, 03일 경우 필수 입력 |
| template_type | 임베딩 종류 | String | O | “form”: 템플릿 관리 |

**템플릿 신규 생성**

템플릿을 새로 생성합니다.

```javascript
var document_option = {
   "mode" : {
    "type" : "01",   // 01 : 생성 , 02 : 수정, 03 : 복제
    "template_type" : "form"
  }
}
```

**템플릿 수정**

기존 템플릿을 수정합니다.

```javascript
var document_option = {
   "mode" : {
    "type" : "02",  // 01 : 생성 , 02 : 수정, 03 : 복제
    "template_id" : "a2c6ed9df9b642f2ade43c7efe58c9a3", // template id 입력
    "template_type" : "form"
  }
}
```

**템플릿 복제**

기존 템플릿을 복제하여 새 템플릿으로 생성합니다.

```javascript
var document_option = {
   "mode" : {
    "type" : "03",  // 01 : 생성 , 02 : 수정, 03 : 복제
    "template_id" : "a2c6ed9df9b642f2ade43c7efe58c9a3", // template id 입력
    "template_type" : "form"
  }
}
```

##### 3. user(사용자 정보/비필수)

| 변수명 | 설명 | 데이터 타입 | 필수 | 비고 |
|---|---|---|---|---|
| id | 계정(이메일) | String | X | 사용자 ID/이메일 입력 |
| access_token | Access Token | String | X | Open API > Access Token 발급 참조 |
| refresh_token | Refresh Token | String | X | Open API > Access Token 발급 참조 |

**템플릿 관리 권한이 있는 멤버 로그인을 통한 작업 (ID 사전 입력)**

임베딩 시, eformsign 로그인 페이지가 구동되어 로그인 과정 이후에 템플릿 관리 작업을 할 수 있습니다. 이때, ID가 로그인 화면에 미리 입력되어 있습니다.

```javascript
var document_option = {
    "user":{
        "id" : "eformsign@forcs.com"
    }
};
```

**템플릿 관리 권한이 있는 멤버의 토큰을 이용한 작업**

임베딩 시, eformsign 로그인 과정없이, 특정 계정의 token을 이용하여 템플릿 관리 작업을 수행합니다.토큰 발급 방법은 eformsign API 사용하기 -Access Token 발급을 확인해 주세요.

```javascript
var document_option = {
    "user":{
        "id" : "eformsign@forcs.com",
        "access_token" : "eyJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJlZ...",
        "refresh_token" : "0161ac6c-0f47-4cc3-9301-381f57c41495"
    }
};
```

##### 4. layout(레이아웃/비필수)

| 변수명 | 설명 | 데이터 타입 | 필수 | 비고 |
|---|---|---|---|---|
| lang_code | eformsign 언어 | String | X | ko: 한국어, en: 영어, ja: 일본어 |
| header | 헤더(상단바) 표시 여부 | Boolean | X | 미입력 시 기본값: true헤더 미표시(false) 시 ‘저장’ 등의 기능 버튼도 표시되지 않으므로, 별도로 기능 버튼을 생성해주어야 함(화면 로드 시_액션 버튼 생성 참조) |
| footer | 푸터 표시 여부 | Boolean | X | 미입력 시 기본값: true |

```javascript
var document_option = {
    "layout" : {
          "lang_code" : "ko",
          "header" : true,
          "footer" : true
    }
}
```

##### 5. prefill(자동 기입/비필수)

문서 작성 과정 중에 자동으로 입력될 수 있도록 처리 시 사용합니다.

| 변수명 | 설명 | 데이터 타입 | 필수 | 비고 |
|---|---|---|---|---|
| template_name | 문서 제목 | String | X |  |
| step_settings | 워크플로우 단계 목록 | Array | X | 단계 정보 Object의 목록 |
| step_settings[].step_type | 워크플로우 수신자 유형 | String | X | -기존 워크플로우: “02”(결재), “03”(내부 수신자), “04”(외부 수신자)-신형 워크플로우: “05”(참여자), “06”(검토자)step_settings내 각 객체에 필수 설정되어야 함 |
| step_settings[].step_name | 워크플로우 단계 이름 | String | X |  |
| step_settings[].selected | 폼 디자인하기 단계에서기본 문서 참여자로 표시 여부 | Boolean | X | 미 입력 시 기본값: false-모든 단계에서 미 입력 혹은 false일 시 시작/발송인 단계가 기본으로 표시됨 |
| step_settings[].use_mail | 이메일 발송 여부 | Boolean | X | 미 입력 시 기본값: false |
| step_settings[].use_sms | SMS 발송 여부 | Boolean | X | 미 입력 시 기본값: false |
| step_settings[].use_alimtalk | SMS 발송으로 카카오톡 사용 여부 | Boolean | X | 미 입력 시 기본값: falsetrue로 설정 시 카카오톡으로 우선 발송, 실패 시 SMS로 발송함 |
| step_settings[].recipient[] | 수신자 정보 목록 | Object | X | 해당 단계 수신자 지정 시 전용수신자 정보 Object의 목록 |
| step_settings[].recipient[].id | 수신자로 지정할 그룹 또는 멤버 ID | String | X | 해당 단계 수신자 지정 시 전용-멤버: 회사 멤버의 계정 정보(ID/이메일) 입력-그룹: 그룹 ID 입력 |
| step_settings[].recipient[].auth | 본인 확인 및 문서 전송 기한 정보 | Object | X | 해당 단계 수신자 지정 시 전용 |
| step_settings[].recipient[].auth.valid | 문서 전송 기한 정보 | Object | X | 해당 단계 수신자 지정 시 전용미 입력시 기본값: 7일 0시간 |
| step_settings[].recipient[].auth.valid.day | 문서 전송 기한 (일) | Integer | X | 해당 단계 수신자 지정 시 전용 |
| step_settings[].recipient[].auth.valid.hour | 문서 전송 기한 (시간) | Integer | X | 해당 단계 수신자 지정 시 전용 |
| step_settings[].auth | 본인 확인 및 문서 전송 기한 정보 | Object | X | 해당 단계의 수신자 지정을 하지 않을 경우 전용type, password, password_hint 모두 미 입력 시: 본인 확인 정보 사용 안 함 |
| step_settings[].auth.type | 본인 확인 방법 | String | X | 해당 단계의 수신자 지정을 하지 않을 경우 전용미 입력 시 기본값: password (단, type, password, password_hint 모두 미 입력 시: 본인 확인 정보 사용 안 함)-qna: 수신자 이름-field: 입력 필드 중 선택-password: 보내는 사람이 직접 입력 |
| step_settings[].auth.password | 본인 확인 정보 | String | X | 해당 단계의 수신자 지정을 하지 않을 경우 전용미 입력 시 기본값: 빈 값-type이 qna인 경우: 빈 값 입력-type이 field인 경우: 필드명 입력-type이 password인 경우: 빈 값 입력 |
| step_settings[].auth.password_hint | 본인 확인 정보에 대한 힌트 | String | X | 해당 단계의 수신자 지정을 하지 않을 경우 전용미 입력 시 기본값: 빈 값 |
| step_settings[].auth.valid | 문서 전송 기한 정보 | Object | X | 해당 단계의 수신자 지정을 하지 않을 경우 전용미 입력시 기본값: 7일 0시간 |
| step_settings[].auth.valid.day | 문서 전송 기한 (일) | Integer | X | 해당 단계의 수신자 지정을 하지 않을 경우 전용 |
| step_settings[].auth.valid.hour | 문서 전송 기한 (시간) | Integer | X | 해당 단계의 수신자 지정을 하지 않을 경우 전용 |
| step_settings[].additional_auth | 추가 인증 수단 (비정형) | Object | X | 해당 단계의 수신자 지정을 하지 않을 경우 전용 |
| step_settings[].additional_auth.use_pincode | 이메일/SMS 인증 사용 여부 | Boolean | X | 해당 단계의 수신자 지정을 하지 않을 경우 전용(구. use_mail) |
| step_settings[].additional_auth.use_pincode_result | 완료 문서 열람 시에도이메일/SMS 인증 사용 여부 | Boolean | X | 해당 단계의 수신자 지정을 하지 않을 경우 전용 |
| step_settings[].additional_auth.use_mobile_verifyAuth | 휴대폰 본인확인 사용 여부 | Boolean | X | 해당 단계의 수신자 지정을 하지 않을 경우 전용(구. use_sms) |
| step_settings[].additional_auth.use_mobile_verifyAuth_result | 완료 문서 열람 시에도휴대폰 본인확인 사용 여부 | Boolean | X | 해당 단계의 수신자 지정을 하지 않을 경우 전용 (구. use_sms_result) |
| is_form_id_numbering | 컴포넌트 추가 시 기본 ID에서번호 부여 여부 | Boolean | X | 텍스트 컴포넌트 추가 시, 컴포넌트 ID의 기본값-is_form_id_numbering이 true일 때: ‘텍스트 1’, ‘텍스트 2’, ‘텍스트 3’-is_form_id_numbering이 false일 때: ‘텍스트’, ‘텍스트’, ‘텍스트’미 입력 시 기본값: true |
| quick_processing | 문서 전송 시 팝업 생략 여부 | Booelan | X | 미 입력 시 기본값: false |

**템플릿 이름 기입**

**일반 설정 > 기본 설정 > 템플릿 이름**에 구매신청서가 입력됩니다.

```javascript
var template_option = {
   "prefill" : {
       "template_name": "구매신청서"
    }
}
```

**워크플로우 단계 설정 (수신자 지정 안 함)**

다음과 같이 워크플로우 단계를 추가합니다

- 단계 종류: 참여자
- 단계명: 참여자 1
- 이메일 알림: 사용
- SMS 알림: 사용 (카카오톡 우선)
- 수신자 지정: X
- 요청 유효기간: 7일 0시간

임베딩하여 실행 시 다음과 같이 설정됩니다.

- 문서 참여자: 2명 (시작, 참여자1)
- 워크플로우: 시작-참여자 1-완료

```javascript
var template_option = {
    "prefill": {
        "step_settings": [
            {
                "step_type": "05",
                "step_name": "참여자 1",
                "use_mail": true,
                "use_sms": true,
                "use_alimtalk" : true,
                "auth": {
                    "valid": {
                        "day": 7,
                        "hour": 0
                    }
                }
            }
        ]
    }
};
```

**워크플로우 단계 설정 (수신자로 멤버 지정)**

다음과 같이 워크플로우 단계를 추가합니다

- 단계 종류: 참여자
- 단계명: 참여자 1
- 이메일 알림: 사용
- SMS 알림: 사용 (카카오톡 우선)
- 수신자 지정: test2@forcs.com 멤버 지정
- 요청 유효기간: 7일 0시간

임베딩하여 실행 시 다음과 같이 설정됩니다.

- 문서 참여자: 2명 (시작, 참여자1)
- 워크플로우: 시작-참여자 1-완료

```javascript
var template_option = {
    "prefill": {
        "step_settings": [
            {
                "step_type": "05",
                "step_name": "참여자 1",
                "use_mail": true,
                "use_sms": true,
                "use_alimtalk" : true,
                "recipients" : [
                    {
                        "id": "test2@forcs.com"
                    }
                ],
                "auth": {
                    "valid": {
                        "day": 7,
                        "hour": 0
                    }
                }
            }
        ]
    }
};
```

**워크플로우 단계 설정 (수신자로 그룹 지정)**

다음과 같이 워크플로우 단계를 추가합니다

- 단계 종류: 참여자
- 단계명: 참여자 1
- 이메일 알림: 사용
- SMS 알림: 사용 (카카오톡 우선)
- 수신자 지정: 5a3e47a2f5a04909836ddf4189d10fc4 그룹 지정
- 요청 유효기간: 7일 0시간

임베딩하여 실행 시 다음과 같이 설정됩니다.

- 문서 참여자: 2명 (시작, 참여자1)
- 워크플로우: 시작-참여자 1-완료

```javascript
var template_option = {
    "prefill": {
        "step_settings": [
            {
                "step_type": "05",
                "step_name": "참여자 1",
                "use_mail": true,
                "use_sms": true,
                "use_alimtalk" : true,
                "recipients" : [
                    {
                        "id": "5a3e47a2f5a04909836ddf4189d10fc4"
                    }
                ],
                "auth": {
                    "valid": {
                        "day": 7,
                        "hour": 0
                    }
                }
            }
        ]
    }
};
```

**워크플로우 단계 설정 (수신자로 멤버와 그룹 지정)**

다음과 같이 워크플로우 단계를 추가합니다

- 단계 종류: 참여자
- 단계명: 참여자 1
- 이메일 알림: 사용
- SMS 알림: 사용 (카카오톡 우선)
- 수신자 지정: test2@forcs.com 멤버, 5a3e47a2f5a04909836ddf4189d10fc4 그룹 지정
- 요청 유효기간: 7일 0시간

임베딩하여 실행 시 다음과 같이 설정됩니다.

- 문서 참여자: 2명 (시작, 참여자1)
- 워크플로우: 시작-참여자 1-완료

```javascript
var template_option = {
    "prefill": {
        "template_name": "구매신청서",
        "step_settings": [
            {
                "step_type": "05",
                "step_name": "참여자 1",
                "use_mail": true,
                "use_sms": true,
                "use_alimtalk" : true,
                "recipients" : [
                    {
                        "id": "test2@forcs.com"
                    },
                    {
                        "id": "5a3e47a2f5a04909836ddf4189d10fc4"
                    }
                ],
                "auth": {
                    "valid": {
                        "day": 7,
                        "hour": 0
                    }
                }
            }
        ]
    }
};
```

**문서 전송 시 팝업 생략 여부 설정**

**일반 설정 > 문서 설정 > 문서 전송**시 팝업 생략에 체크됩니다.

```javascript
var template_option = {
    "prefill" : {
        "quick_processing" : true
    }
}
```

```javascript
var template_option = {
    "prefill": {
        "template_name": "구매신청서",
        "step_settings": [
            {
                "step_type": "05",
                "step_name": "참여자 1",
                "use_mail": true,
                "use_sms": true,
                "use_alimtalk" : true,
                "recipients" : [
                    {
                        "id": "test2@forcs.com"
                    }
                ],
                "auth": {
                    "valid": {
                        "day": 7,
                        "hour": 0
                    }
                }
            },
            {
                "step_type": "06",
                "step_name": "검토자 1",
                "use_mail": true,
                "use_sms": false,
                "use_alimtalk" : false,
                "recipients" : [
                    {
                        "id": "5a3e47a2f5a04909836ddf4189d10fc4"
                    }
                ],
                "auth": {
                    "valid": {
                        "day": 7,
                        "hour": 0
                    }
                }
            }
        ],
        quick_processing : true
    }
};
```

##### 6. template_file(템플릿 파일/비필수)

템플릿에 사용될 파일이 자동으로 업로드되도록 설정합니다.

| 변수명 | 설명 | 데이터 타입 | 필수 | 비고 |
|---|---|---|---|---|
| name | 파일명 | String | O |  |
| mime | MIME 데이터 형식 | String | O | -PDF: “application/pdf”-지원하는 모든 확장자(OZR, PDF): “@file/octet-stream” |
| data | Base64로 변환한 파일 데이터 | String | O |  |

```javascript
var document_option = {
    "tempalte_file": {
          "name": "첨부테스트.pdf",
          "mime": "@file/octet-stream",
          "data": "JVBERi0xLjUNCiW1tbW1DQoxIDAgb2JqDQo8PC9UeXBlL0NhdGFsb2cvUGFnZXMgMiAwIFIvTGFuZyhrby1LUikgL1N0cnVjdFRyZWVSb290IDE1IDAgUi9NY...(후략)"
    }
}
```

## 응답 확인 및 콜백 설정하기(옵션)

eformsign 기능을 임베딩하여 사용 시, 특정 상황에서 eformsign으로부터 정보를 담은 응답을 수신할 수 있습니다.또한, 해당 응답을 활용하여 특정 동작을 실행하도록 콜백을 설정할 수 있습니다.

**응답 및 콜백의 종류**

**- 작업 성공 시 (Success Callback)**

임베딩하여 수행하는 작업이 성공했을 때 해당 작업의 결과 정보를 담은 응답이 수신되고, 콜백을 사용할 수 있습니다.문서 미리 보기와 같이 추가적으로 수행할 수 있는 작업이 없는 기능을 임베딩하였을 경우에는 사용할 수 없습니다.

**- 작업 실패 시 (Error Callback)**

임베딩하여 수행하는 작업이 실패했을 때 해당 정보를 담은 응답이 수신되고, 콜백을 사용할 수 있습니다.문서 미리 보기와 같이 추가적으로 수행할 수 있는 작업이 없는 경우에는 사용할 수 없습니다.

**- 화면 로드 시 (Action Callback)**

임베딩한 화면이 로드되면서 해당 화면에서 수행할 수 있는 작업의 목록 정보를 담은 응답이 수신되고, 콜백을 사용할 수 있습니다.수신한 응답의 작업 목록을 기반으로, 상단바의 액션 버튼을 대체할 수 있는 버튼을 설정할 수 있습니다.

### 작업 성공/실패 시

eformsign을 임베딩하여 수행한 작업을 성공 혹은 실패 했을 때 반환되는 응답과, 응답 수신 후 특정 기능을 실행할 수 있는 콜백 함수인 Success Callback / Error Callback에 대해 설명합니다.

#### 응답(Response)

문서 작성/처리, 템플릿 생성/수정/복제 등의 작업을 성공하거나 실패했을 때, 다음과 같은 response가 반환됩니다.

##### EformSignDocument(템플릿 문서 작성, 문서 처리)

| 변수명 | 타입 | 설명 | 비고 |
|---|---|---|---|
| type | String | 임베딩하여 작성한 작업의 종류 | -“document”-이외 기능은 추후 제공 예정 |
| fn | String | 수행한 기능 | -“saveSuccess” : 저장 성공-그 외 : 오류 |
| code | String | 문서 작성 혹은 처리 시 결과 코드를 반환 | -“-1” : 문서 작성/처리 성공-“0” : 로그아웃 성공-그 외: 오류 |
| message | String | 문서 작성 혹은 처리 시 성공/오류 메시지를 반환 | -“성공하였습니다.”” : 문서 작성/처리 성공-그 외: 오류 |
| document_id | String | 문서 제출 성공 시, 작성한 문서의 document_id 반환 | ex) “910b8a965f9402b82152f48c6da5a5c” |
| title | String | 문서 제출 성공 시, 작성한 문서의 제목을 반환 | ex) “계약서” |
| values | Object | document_option에 정의한 return_fields에입력한 필드명에 대해 사용자가 입력한 값을 반환 | {“필드명”: “필드값”} 형태의 Object로 제공ex) {“성함”: “홍길동”} |
| recipients | Array | 다음 수신자 정보 Object 목록을 반환 |  |
| recipients[].step_idx | String | 워크플로우 순서 | 첫 번째 수신자: “2”, 두 번째 이후 수신자: 순서에 따라 1씩 증가 |
| recipients[].step_type | String | 수신자 종류 | 기존 워크플로우: “01”(완료), “02”(결재), “03”(외부 수신자), “04”(내부 수신자)신규 워크플로우: “01”(완료), “05”(참여자), “06”(검토자) |
| recipients[].recipient_type | String | 수신자 유형 | “01” : 회사 멤버“02” : 외부 수신자 |
| recipients[].use_mail | Boolean | 이메일 발송 여부 |  |
| recipients[].use_sms | Boolean | SMS 발송 여부 |  |
| recipients[].id | String | 계정(이메일) |  |
| recipients[].name | String | 수신자 이름 |  |
| recipients[].sms | String | 휴대폰 번호 |  |
| recipients[].auth | Object | 본인확인 및 문서 전송 기한 정보 |  |
| recipients[].auth.password | String | 본인확인 정보 (비밀번호) |  |
| recipients[].auth.password_hint | String | 본인확인 정보 도움말 (비밀번호 힌트) |  |
| recipients[].auth.valid | Object | 문서 전송 기한 정보 |  |
| recipients[].auth.valid.day | Integer | 문서 전송 기한 (일) |  |
| recipients[].auth.valid.hour | Integer | 문서 전송 기한 (시간) |  |

```text
{
  "type": "document",
  "fn": "saveSuccess",
  "code": "-1",
  "message": "성공하였습니다.",
  "document_id": "c59c522ea9294660bfa84263c95c4e54",
  "title": "개인정보활용동의서",
  "values": {
    "성함": "홍길동"
  },
  "recipients": [
    {
      "step_idx": 2,
      "step_type": "06",
      "recipient_type": "02",
      "use_mail": true,
      "use_sms": true,
      "id": "test@forcs.com",
      "name": "홍길동",
      "sms": "+821023456789",
      "auth": {
        "password": "",
        "password_hint": "",
        "valid": {
          "day": 7,
          "hour": 0
        }
      }
    }
  ]
}
```

##### EformSignTemplate (내 파일로 문서 작성, 템플릿 생성, 템플릿 수정, 템플릿 복제)

| 변수명 | 타입 | 설명 | 비고 |
|---|---|---|---|
| type | String | 임베딩하여 작성한 작업의 종류 | -“template” |
| fn | String | 수행한 기능 | -“saveSuccess” : 저장 성공-그 외 : 오류 |
| code | String | 템플릿 작업 시 결과 코드를 반환 | -“-1” : 템플릿 작업 성공-“0” : 로그아웃 성공-그 외: 오류 |
| message | String | 템플릿 작업 시 성공/오류 메시지를 반환 | -“성공하였습니다.”” : 문서 작성/처리 성공-그 외: 오류 |
| template_id | String | 템플릿 작업 성공시, 작업한 템플릿의 ID 반환 | ex) “910b8a965f9402b82152f48c6da5a5c” |
| template_name | String | 템플릿 작업 성공 시, 작업한 템플릿의 이름 반환 | ex) “계약서” |
| step_settings | Array | 워크플로우 단계 목록 |  |
| step_settings[].step_type | String | 워크플로우 단계 종류 | -공통: “00”(시작), “01”(완료)-기존 워크플로우: “02”(결재), “03”(외부 수신자), “04”(내부 수신자)-신규 워크플로우: “05”(참여자), “06”(검토자) |
| step_settings[].step_name | String | 워크플로우 단계명 | ex) “참여자 1” |

```text
{
    "type": "template",
    "fn": "saveSuccess",
    "code": "-1",
    "message": "성공하였습니다.",
    "template_id": "9a368e9409bc4351865637e85882cf01",
    "template_name": "템플릿 임베딩 테스트_신규",
    "step_settings": [
        {
            "step_type": "00",
            "step_name": "시작"
        },
        {
            "step_type": "05",
            "step_name": "참여자 2"
        },
        {
            "step_type": "06",
            "step_name": "검토자 1"
        },
        {
            "step_type": "05",
            "step_name": "참여자 3"
        },
        {
            "step_type": "01",
            "step_name": "완료"
        }
    ]
}
```

#### 콜백 (Callback)

Success Callback과 Error Callback은 각각 작업을 성공했을 때 또는 실패했을 때 실행되는 함수입니다.작업 성공/실패 시 반환되는 response를 받아 원하는 작업을 수행하도록 설정할 수 있습니다.

예를 들어 필요에 따라 원하는 값을 콘솔에 출력하거나 (console.log) 경고창을 표출할 수 있으며(alert), 조건문 등을 이용해 원하는 상황에 원하는 기능을 수행하도록 할 수 있습니다.

##### EformSignDocument 예시

```javascript
var eformsign = new EformSignDocument();

var document_option = { /* 생략 */ };

var success_callback= function(response){
    console.log(response.document_id);
    console.log(response.title);
    console.log(response.values["성함"]);
};

var error_callback= function(response){
    alert(response.message);
    console.log(response.code);
    console.log(response.message);
};

eformsign.document(document_option, "eformsign_iframe", success_callback, error_callback);

eformsign.open();
```

##### EformSignTemplate 예시

```javascript
var eformsign = new EformSignTemplate();

var document_option = { /* 생략 */ };

var success_callback= function(response){
    if (response.type ==='template'){
        console.log(response.template_id);
        console.log(response.template_name);
        console.table(response.step_settings);
        if ("-1" == response.code) {
            alert("템플릿 생성되었습니다.\n" + "- document_id : " + response.template_id + "\n- title : " + response.template_name);
        } else {
            alert("템플릿 생성에 실패하였습니다.\n" + "- code : " + response.code + "\n- message : " + response.message);
        }
    }
};

var error_callback= function(response){
    alert(response.message);
    console.log(response.code);
    console.log(response.message);
};

eformsign.document(document_option, "eformsign_iframe", success_callback, error_callback);
```

### 화면 로드 시

eformsign을 임베딩한 화면이 로드 되었을 때의 응답과, 응답 수신 후 특정 기능을 실행할 수 있는 콜백 함수인 Action Callback에 대해 설명합니다.또한, 상단바(헤더)에 위치한 액션 버튼을 대체할 버튼을 생성하는 방법에 대해서 설명합니다.

#### 응답(Response)

임베딩한 eformsign 기능의 화면이 로드될 때, response를 통해 해당 화면에서 수행할 수 있는 기능에 대한 정보가 반환됩니다.Response의 구조 및 예시는 다음과 같습니다.

##### EformSignDocument (템플릿 문서 작성, 문서 처리)

| 변수명 | 타입 | 설명 | 비고 |
|---|---|---|---|
| type | String | 임베딩하여 작성한 작업의 종류 | -EformSignDocument 사용 작업: “document”-EformSignTemplate 사용 작업: “template” |
| fn | String | 수행한 기능 | -“actionCallback”-그 외 : 오류 |
| data | Array | 해당 화면에서 수행할 수 있는 기능 목록 | -{“name”:”이름”, “code”:”00”} 형태 Object의 목록-{“name”: “func_get_return_fields”, code: “99”}는 리턴 필드를 처리하기 위한 기능으로, 항상 표시됨 |
| data[].name | String | 기능 명칭 |  |
| data[].code | String | 기능 코드 |  |

```text
{
  "type": "document",
  "fn": "actionCallback",
  "data": [
    {
      "name": "전송",
      "code": "21"
    },
    {
      "name": "func_get_return_fields",
      "code": "99"
    }
  ]
}
```

#### 콜백 (Callback)

Action Callback은 기능 화면이 로드될 때, response 수신 후 실행되는 함수입니다.Response와 무관한 별도의 작업을 자동으로 수행하도록 설정하거나, 문서 화면 로드 시 반환되는 response를 받아서 그에 따라 원하는 작업을 수행하도록 설정할 수 있습니다.

##### 예시

```javascript
var eformsign = new EformSignDocument();

var document_option = { /* 생략 */ };

var success_callback= function(response){
    // 생략
};

var error_callback= function(response){
    // 생략
};


var action_callback= function(response){
    alert("붉은 색으로 강조된 입력란에 값을 입력해주세요.");
    console.table(response.data);   // 기능 목록 출력
}

eformsign.document(document_option, "eformsign_iframe", success_callback, error_callback, action_callback);
```

#### 액션 버튼 생성

기능 옵션 설정 시, 상단 헤더를 숨길 수 있는 옵션이 존재합니다.그러나 상단 헤더를 숨길 시, 상단 헤더에 존재하는 액션 버튼(제출, 요청 등)이 함께 숨겨지기에 별도로 액션 버튼을 생성해주어야 합니다.

EformsignDocument 객체와 EformsignTemplate 객체에 모두 존재하는 sendAction 함수를 사용하면, 특정 액션을 실행할 수 있습니다.따라서 원하는 형태로 버튼을 생성 후, 클릭 시 sendAction 함수가 실행되도록 설정하시면 됩니다.

- EformSignDocument.sendAction(action)
- EformSignTemplate.sendAction(action)

| 패러미터명 | 패러미터 종류 | 필수 여부 | 설명 |
|---|---|---|---|
| action | JSON | 필수 | 액션 정보 |
| action.type | String | 필수 | 구분 (01: 문서, 02: 템플릿) |
| action.code | String | 필수 | 액션 코드 |

sendAction 함수에서 사용할 수 있는 액션 코드의 목록은 다음과 같습니다.

| action.type | action.code | 버튼명 | 버튼 텍스트 | 설명 |
|---|---|---|---|---|
| 01 | 00 | btn_close |  | 닫기 |
| 01 | 01 | btn_save_as_draft | 임시 저장 | 문서 작성 중 임시 저장 |
| 01 | 02 | btn_process_request | 요청 | 내부 수신자 혹은 내부 수신자를 포함한 여러 수신자에게 문서 요청 (구형 워크플로우 사용 문서 작성 시) |
| 01 | 03 | btn_outsider | 요청 | 외부 수신자에게 문서 요청 (구형 워크플로우 사용 문서 작성 시) |
| 01 | 04 | btn_approval | 요청 | 결재자에게 문서 요청 (구형 워크플로우 사용 문서 작성 시) |
| 01 | 05 | btn_write_complete | 완료 | 문서 작성 완료 (워크플로우 상 다음 수신자가 없을 경우) |
| 01 | 06 | btn_acceptStepReject | 승인 | 반려 요청 승인 |
| 01 | 07 | btn_stepReject | 반려 | 문서 반려 (내부 수신자) |
| 01 | 08 | btn_cancelStepReject | 반려 | 반려 요청 반려 |
| 01 | 09 | btn_active | 승인 | 문서 승인 (구형 워크플로우 사용 문서 결재 시) |
| 01 | 10 | btn_approvalReject | 반려 | 문서 반려 (결재자) |
| 01 | 11 | btn_delete_approval | 승인 | 문서 삭제 승인 |
| 01 | 12 | btn_delete_refuse | 반려 | 문서 삭제 반려 |
| 01 | 13 | btn_revoke_approval | 승인 | 문서 취소 승인 |
| 01 | 14 | btn_revoke_refuse | 반려 | 문서 취소 반려 |
| 01 | 15 | btn_change_title | 제목 변경 | 제목 변경 |
| 01 | 16 | btn_show_history | 이력 보기 | 문서 미리보기 임베딩 시, 더 보기( ⋮ ) → 이력 보기 버튼 |
| 01 | 18 | btn_send_pdf | 완료 문서 전송 | 더 보기( ⋮ ) → 완료 문서 전송 버튼 |
| 01 | 19 | btn_draft | 임시 저장 | 문서 처리 중 임시 저장 |
| 01 | 20 | btn_unstructured_write_complete | 전송 | 문서 작성 완료 (내 파일로 문서 작성 시, 수신자가 없을 경우) |
| 01 | 21 | btn_unstructured_process_request | 전송 | 문서 전송 (신형 워크플로우 사용 문서 작성 시, 다음 수신자가 있을 경우) |
| 01 | 22 | btn_unstructured_active | 전송 | 문서 전송 (신형 워크플로우 사용 문서 처리 시) |
| 01 | 99 | func_get_return_fields |  | 리턴 필드 가져오기 (문서 전송/완료/요청 시 자동 실행) |
| 02 | 00 |  | 나가기 | 문서 작성 화면에서 나가 폼 설정으로 돌아가기 (내 파일로 문서 작성 시) |
| 02 | 01 | anotherTemplateBtn | 완료 | 템플릿 목록으로 돌아가기 (템플릿 관리) |
| 02 | 02 | saveFormBtn | 저장 | 템플릿 저장 (템플릿 관리) |
| 02 | 03 | designTab | 폼 디자인하기 | 폼 디자인하기 탭 |
| 02 | 04 | setupTab | 설정하기 / 옵션 | 설정하기 탭(템플릿 관리) / 옵션 탭(내 파일로 문서 작성) |
| 02 | 05 | receipientTab | 수신자 지정하기 | 수신자 지정하기 탭 (내 파일로 문서 작성) |
| 02 | 06 | writeDocumentBtn | 문서 작성 시작하기 | 문서 작성 시작하기 버튼 (내 파일로 문서 작성) |
| 02 | 99 | func_get_return_fields |  | 리턴 필드 가져오기 (문서 전송/완료/요청 시 자동 실행) |

예를 들어, 클릭 시 (신형 워크플로우를 사용하며, 다음 수신자가 있는 문서를 작성 후) 전송하는 버튼은 다음과 같이 생성할 수 있습니다.

```javascript
<button id="btn_21" onclick="eformsign.sendAction({type: '01', code: '21'});">전송</button>
```

Tip

위 액션 코드 목록에서 확인하실 수 있듯, 워크플로우 구성과 문서 상태 등에 따라 사용해야 할 버튼의 종류가 달라집니다.또한 같은 텍스트의 버튼이더라도 상황에 따라 다른 액션 코드를 사용해야 하는 경우가 존재합니다.따라서 특정 기능을 수행하는 버튼을 고정적으로 배치해둘 경우, 버튼이 해당 상황에 맞지 않아 오작동하는 경우가 발생할 수 있습니다.오류 발생 가능성을 줄이기 위해 화면 로드 시 수신되는 response에서 해당 화면에서 수행할 수 있는 작업 목록을 확인하신 후, 해당 목록을 기반으로 버튼을 생성 또는 표시하는 가변형 방식을 사용하기를 권장드립니다.

다음 예시에서 모든 액션 코드에 대해 보이지 않는 버튼을 생성해둔 후, 해당 화면에서 수행할 수 있는 작업에 해당하는 버튼만 보이도록 설정하는 가변형 버튼 사례를 확인하실 수 있습니다.

```javascript
var eformsign = new EformSignDocument();

var document_option = { /* 생략 */ };

var success_callback= function(response){
    // 생략
};

var error_callback= function(response){
    // 생략
};


var action_callback= function(response){
    $('#buttonList').find('button').css('display','none');      // div id=buttonList의 모든 버튼을 보이지 않도록 설정
    $(response.data).each(function(idx, action){                // response.data의 각 값에 대해
        $('#buttonList').find('button').each(function(idx, btn){    // div id=buttonList의 모든 버튼에서
            if ($(btn).attr('id').replace('btn_','') === action.code){  // 만약 data[].code에 해당하는 버튼이 있으면
                $(btn).attr('title',action.name).text(action.name);     // 버튼 title을 data[].name으로 설정하고
                $(btn).css('display', '');                              // 버튼을 보이도록 설정
            }
        });
    });
    console.table(response.data);
}


function actionTest(action) {   // 보다 간편하게 sendAction 함수에 JSON을 입력 후 실행하기 위한 예시 함수로, 반드시 이와 같은 형태로 사용하실 필요는 없습니다.
    var action = {
        type : '01',    // type : 01 : 문서 , 02 : 템플릿
        code : action
    }
    eformsign.sendAction(action);
}

eformsign.document(document_option, "eformsign_iframe", success_callback, error_callback, action_callback);
```

```javascript
<!-- 모든 액션에 대한 버튼을 생성해두고, 보이지 않도록 설정한 후 action_callback에서 필요한 버튼만 표시하도록 처리 -->
<div id="buttonList" style="padding: 10px;">
    <button id="btn_01" style="width:80px; height:30px; display: none;" onclick="actionTest('01');"></button>
    <button id="btn_02" style="width:80px; height:30px; display: none;" onclick="actionTest('02');"></button>
    <button id="btn_03" style="width:80px; height:30px; display: none;" onclick="actionTest('03');"></button>
    <button id="btn_04" style="width:80px; height:30px; display: none;" onclick="actionTest('04');"></button>
    <button id="btn_05" style="width:80px; height:30px; display: none;" onclick="actionTest('05');"></button>
    <button id="btn_06" style="width:80px; height:30px; display: none;" onclick="actionTest('06');"></button>
    <button id="btn_07" style="width:80px; height:30px; display: none;" onclick="actionTest('07');"></button>
    <button id="btn_08" style="width:80px; height:30px; display: none;" onclick="actionTest('08');"></button>
    <button id="btn_09" style="width:80px; height:30px; display: none;" onclick="actionTest('09');"></button>
    <button id="btn_10" style="width:80px; height:30px; display: none;" onclick="actionTest('10');"></button>
    <button id="btn_11" style="width:80px; height:30px; display: none;" onclick="actionTest('11');"></button>
    <button id="btn_12" style="width:80px; height:30px; display: none;" onclick="actionTest('12');"></button>
    <button id="btn_13" style="width:80px; height:30px; display: none;" onclick="actionTest('13');"></button>
    <button id="btn_14" style="width:80px; height:30px; display: none;" onclick="actionTest('14');"></button>
    <button id="btn_15" style="width:80px; height:30px; display: none;" onclick="actionTest('15');"></button>
    <button id="btn_16" style="width:80px; height:30px; display: none;" onclick="actionTest('16');"></button>
    <button id="btn_17" style="width:80px; height:30px; display: none;" onclick="actionTest('17');"></button>
    <button id="btn_18" style="width:80px; height:30px; display: none;" onclick="actionTest('18');"></button>
    <button id="btn_19" style="width:80px; height:30px; display: none;" onclick="actionTest('19');"></button>
    <button id="btn_20" style="width:80px; height:30px; display: none;" onclick="actionTest('20');"></button>
    <button id="btn_21" style="width:80px; height:30px; display: none;" onclick="actionTest('21');"></button>
    <button id="btn_22" style="width:150px; height:30px; display: none;" onclick="actionTest('22');"></button>
</div>


<!-- 임베딩할 iframe 생성 -->
<iframe id="eformsign_iframe" name="eformsign_iframe" style="width: 100%; height: 700px;"></iframe>
```

## 기능 임베딩 및 구동하기

앞서 생성한 옵션과 콜백을 사용하여 eformsign 기능을 실제로 임베딩 및 구동하기 위한 코드를 작성합니다.

### eformsign 기능을 임베딩할 영역 생성

먼저 eformsign 기능을 임베딩하여 표시할 영역을 생성해야 합니다.eformsign 기능 임베딩을 위한 영역은 iframe 형태를 지원하고 있습니다.

```javascript
<iframe id="eformsign_iframe" width="1440" height="1024"> </iframe>
```

예를 들어, 위와 같이 가로 1440픽셀, 세로 1024픽셀의 iframe을 생성할 수 있습니다.영역 생성 시 id를 설정해야 합니다. 위 예시에서는 id를 “eformsign_iframe”으로 설정하였습니다.

### eformsign 기능 임베딩용 코드 작성

앞서 생성한 iframe 영역에 eformsign 기능을 임베딩하여 표시되도록 코드를 작성하여야 합니다.먼저 임베딩하고자 하는 기능에 맞는 객체를 변수 형태로 생성합니다. 아래 예시에서는 변수명을 “eformsign”으로 설정하였습니다.

```javascript
var eformsign = new EformSignDocument();
```

앞서 생성한 임베딩 옵션과 콜백 함수를 변수 형태로 입력합니다.

```javascript
var document_option = {
    // 중략
    "mode" : {
        "type" : "01",
        "template_id" : "a2c6ed9df9b642f2ade43c7efe58c9a3"
    },
    // 중략
}


var success_callback= function(response){
    // 생략
};

var error_callback= function(response){
    //생략
};

var action_callback= function(response){
    //생략
};
```

eformsign 기능의 구동을 위한 옵션을 설정하는 함수를 작성합니다. 이 때, 앞서 생성한 iframe 영역 및 각종 변수와 함수를 사용하게 됩니다.기능 구동을 위한 함수는**EformsignDocument 객체**의 경우**document 함수**,**EformSignTemplate 객체**의 경우**template 함수**를 사용합니다.

EformSignDocument.document(document_option, iframe_id, success_callback , error_callback, action_callback)

| 패러미터명 | 패러미터 종류 | 필수 여부 | 설명 |
|---|---|---|---|
| document_option | JSON | 필수 | eformsign을 임베딩하여 구동할 회사, 사용자, 템플릿 등의 옵션을 지정 |
| iframe_id | String | 필수 | eformsign이 임베딩되어 표시될 iframe의 ID |
| success_callback | Function | 비필수 | eformsign 문서 작업 성공 시, 호출될 callback 함수 |
| error_callback | Function | 비필수 | eformsign 문서 작업 실패 시, 호출될 callback 함수 |
| action_callback | Function | 비필수 | eformsign 화면 로드 시, 호출될 callback 함수 |

EformSignTemplate.template(template_option, iframe_id, success_callback , error_callback, action_callback)

| 패러미터명 | 패러미터 종류 | 필수 여부 | 설명 |
|---|---|---|---|
| template_option | JSON | 필수 | eformsign을 임베딩하여 구동할 회사, 사용자, 템플릿 등의 옵션을 지정 |
| iframe_id | String | 필수 | eformsign이 임베딩되어 표시될 iframe의 ID |
| success_callback | Function | 비필수 | eformsign 템플릿/문서 작업 성공 시, 호출될 callback 함수 |
| error_callback | Function | 비필수 | eformsign 템플릿/문서 작업 실패 시, 호출될 callback 함수 |
| action_callback | Function | 비필수 | eformsign 화면 로드 시, 호출될 callback 함수 |

```javascript
eformsign.document(document_option, "eformsign_iframe", success_callback, error_callback, action_callback);
```

### eformsign 기능 구동하기

eformsign 기능을 구동하기 위해서는 open 함수의 호출이 필요합니다.open 함수는 설정해야 할 패러미터가 없으며, 옵션 설정을 마친 EformSignDocument 객체 혹은 EformSignTemplate 객체에 사용하여 삽입된 기능을 구동하는 역할을 합니다.기능 구동을 위한 옵션을 설정하는 document 혹은 template 함수 작성을 마쳤다면, 그 후에 open 함수를 작성합니다.

```javascript
eformsign.open();
```

#### 예시

설치 작업을 포함한 전체 예시 코드는 다음과 같습니다.

```javascript
<html>
<head>
    <title>embedding test</title>

    <script src="https://www.eformsign.com/plugins/jquery/jquery.min.js"></script>
    <script src="https://www.eformsign.com/lib/js/efs_embedded_v2.js"></script>
</head>

<body>
    <iframe id="eformsign_iframe" width="1440" height="1024"> </iframe>

    <script>
        var eformsign = new EformSignDocument();

        var document_option = {
            // 중략
            "mode" : {
               "type" : "01",
               "template_id" : "a2c6ed9df9b642f2ade43c7efe58c9a3"
            },
            // 중략
        };

        var success_callback= function(response){
            // 생략
        };

        var error_callback= function(response){
            //생략
        };

        var action_callback= function(response){
            //생략
        };

        eformsign.document(document_option, "eformsign_iframe", success_callback, error_callback, action_callback);
        eformsign.open();
    </script>
</body>
</html>
```

<Page contents

>Page contents:

- eformsign 기능 임베딩하기설치하기개요eformsign 임베딩용 객체설치 방법임베딩 옵션 설정하기기능별 설정값필요한 값 확인회사 ID 확인 방법템플릿 ID 확인 방법문서 ID 확인 방법템플릿 문서 작성, 문서 처리, 문서 미리보기document_option1. company(회사 정보/필수)2. mode(임베딩 모드/필수)3. user(사용자 정보/비필수)4. layout(레이아웃/비필수)5. prefill(자동 기입/비필수)6. return_fields(리턴 필드/비필수)내 파일로 문서 작성template_option1. company(회사 정보/필수)2. mode(임베딩 모드/필수)3. user(사용자 정보/비필수)4. layout(레이아웃/비필수)5. prefill(자동 기입/비필수)6. template_file(템플릿 파일/비필수)템플릿 생성, 템플릿 수정, 템플릿 복제template_option1. company(회사 정보/필수)2. mode(임베딩 모드/필수)3. user(사용자 정보/비필수)4. layout(레이아웃/비필수)5. prefill(자동 기입/비필수)6. template_file(템플릿 파일/비필수)응답 확인 및 콜백 설정하기(옵션)작업 성공/실패 시응답(Response)EformSignDocument(템플릿 문서 작성, 문서 처리)EformSignTemplate (내 파일로 문서 작성, 템플릿 생성, 템플릿 수정, 템플릿 복제)콜백 (Callback)EformSignDocument 예시EformSignTemplate 예시화면 로드 시응답(Response)EformSignDocument (템플릿 문서 작성, 문서 처리)콜백 (Callback)예시액션 버튼 생성기능 임베딩 및 구동하기eformsign 기능을 임베딩할 영역 생성eformsign 기능 임베딩용 코드 작성eformsign 기능 구동하기예시

---

## 📊 문서 정보

- **추출된 총 요소**: 292개
- **헤딩**: 54개
- **문단**: 131개
- **코드 블록**: 56개
- **테이블**: 29개
- **리스트**: 22개

**✅ 자동 생성 완료**: 웹페이지를 완전히 마크다운으로 변환했습니다.

*생성 도구: all_in_one_scraper.py*
*생성 시간: 2025-06-18 16:29:37*