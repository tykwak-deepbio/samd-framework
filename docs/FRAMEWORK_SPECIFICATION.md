# SaMD Multi-Agent Framework Specification (FRS) & Test Plan

> **Document ID**: `FRAMEWORK-SRS-001`  
> **System Under Design**: Antigravity SaMD Multi-Agent System (Framework)  
> **Target Environment**: Google Antigravity (IDE / Desktop / CLI)  
> **Version**: 2.1.0 | **Status**: Approved (60 Requirements / 13 Skills / 13 Agents / 18 Templates)  
> **Applicable Standards**: ISO 13485:2016, IEC 62304:2006+AMD1:2015, ISO 14971:2019, IEC 62366-1:2015, ISO 27001/27799, IEC 81001-5-1, FDA 2023 Premarket Cybersecurity, FDA 21 CFR Part 11, GMLP / FDA PCCP, MFDS AI SaMD Guidelines  

---

## 1. 프레임워크 개요 및 목적 (Framework Purpose)

본 명세서는 소프트웨어 의료기기(SaMD) 개발 프로젝트에서 활용되는 **"Antigravity 기반 규제 준수형 멀티에이전트 시스템(프레임워크)" 자체의 요구사항 명세서, 테스트 명세서 및 인수 기준**을 정의합니다.

본 프레임워크는 개별 의료기기 프로젝트가 Antigravity 내에서 동작할 때, IEC 62304 V-모델과 ISO 14971 병렬 위험관리, ISO 13485 설계이력파일(DHF) 구축을 자동화하고 글로벌 규제 감사(FDA/MFDS/CE)에 즉시 제출 가능한 수준의 무결성을 보장하는 것을 목적으로 합니다.

---

## 2. 프레임워크 요구사항 명세 (Framework Requirements Specification - 60 FRS)

### 2.1 오케스트레이션 및 생명주기 관리 요구사항 (`[ORCH]`)
| ID | 프레임워크 요구사항 명세 | 검증 대상 컴포넌트 | 추적 기준 |
| :--- | :--- | :--- | :--- |
| `FR-ORCH-001` | **12단계 V-모델 게이트 거버넌스**: IEC 62304 소프트웨어 수명주기 프로세스(Phase 1~12: 개발, 사후 유지보수, 이상사례 해결) 관리 및 진입/종료 체크리스트 강제. | `.agents/skills/samd-orchestrator/SKILL.md`<br>`agents/00-samd-orchestrator-agent.md` | IEC 62304 Cl 5.1, Cl 6, Cl 9 |
| `FR-ORCH-002` | **12개 단계별 사용자 승인 중단점(Human-in-the-Loop)**: Gate 1부터 Gate 12까지 주요 마일스톤(Tier 1 Major Gates)에서 명시적 검토 및 승인 강제. | `workflows/00-v-model-lifecycle-workflow.md` | ISO 13485 Cl 7.3.5 |
| `FR-ORCH-003` | **병렬 트랙 동기화**: 요구사항(Phase 4) 또는 아키텍처(Phase 7) 변경 시 위험관리(Phase 5) 및 사이버보안(Phase 6) 에이전트를 병렬로 즉시 호출하여 DHF 재동기화. | `workflows/02-risk-and-cybersecurity-parallel-workflow.md` | ISO 14971 Cl 4.4 |
| `FR-ORCH-004` | **멀티에이전트 동시성 제어 및 원자적 공유 상태 잠금**: 다중 서브에이전트 병렬 실행 시 `project_state.json` 상태 파일에 OS 레벨 배타적 파일 잠금(`fcntl.flock`)을 적용하여 경쟁 상태(Race Condition) 및 분할 뇌 방지. | `scripts/record_audit_event.py`<br>`templates/project_state.json` | IEC 62304 Cl 5.1.2, ISO 13485 Cl 4.2.4 |

### 2.2 전문 에이전트 및 Antigravity 스킬 요구사항 (`[AGENT]`, `[SKILL]`)
| ID | 프레임워크 요구사항 명세 | 검증 대상 컴포넌트 | 추적 기준 |
| :--- | :--- | :--- | :--- |
| `FR-SKILL-001` | **13개 특화 스킬 제공**: 마스터 오케스트레이터 및 12개 생명주기 단계에 대응하는 독립 Antigravity 스킬 13종을 `.agents/skills/`에 제공하고 YAML Frontmatter 준수. | `.agents/skills/*/SKILL.md` (13종) | Antigravity Customization Spec |
| `FR-SKILL-002` | **슬래시 커맨드 및 자동 디스커버리 지원**: 사용자의 채팅창 `/<skill-name>` 호출 및 시맨틱 질문에 대해 3인칭 서술문 기반 자동 트리거 지원. | `.agents/skills/*/SKILL.md` (description) | Antigravity Skills Guide |
| `FR-SKILL-003` ~ `FR-SKILL-015` | **13개 전문 엔지니어링 스킬 사양**: 오케스트레이터부터 유지보수까지 13개 스킬의 세부 임상/기술 거버넌스 기능 명세화. | `.agents/skills/*/SKILL.md` | IEC 62304 / ISO 14971 |
| `FR-AGENT-001` | **13개 에이전트 페르소나 및 시스템 프롬프트 명세**: 13개 역할에 대해 `define_subagent`에 즉시 주입 가능한 독립 시스템 프롬프트를 마크다운으로 제공. | `agents/*.md` (13종) | IEC 62304 Cl 5.1.2 |
| `FR-AGENT-002` | **독립 검증 원칙(Independence of Verification)**: V&V 검증자(`vnv-test-engineer-agent`)는 구현 개발자(`software-developer-agent`)와 독립된 페르소나 및 권한 유지. | `agents/10-vnv-test-engineer-agent.md` | IEC 62304 Cl 5.6.2, 5.7.2 |
| `FR-AGENT-003` | **서브에이전트 RBAC 및 읽기전용 격리**: 검증자/감사관 서브에이전트가 프로덕션 소스코드를 임의 수정하지 못하도록 샌드박스 레벨에서 통제. | `agents/*.md`, `scripts/hook_pre_write_guard.py` | ISO 13485 Cl 7.3.6 |

### 2.3 규제 표준 DHF 템플릿 요구사항 (`[DHF]`)
| ID | 프레임워크 요구사항 명세 | 검증 대상 컴포넌트 | 추적 기준 |
| :--- | :--- | :--- | :--- |
| `FR-DHF-001` | **16종 표준 DHF 마크다운 템플릿 완비**: DHF-00부터 DHF-13까지(DHF-05A/B/C, DHF-12 포함) 식약처, FDA, EU IVDR 기술문서 심사 요건을 충족하는 16종 템플릿 제공. | `templates/DHF-*.md` (16종) | ISO 13485 Cl 7.3.7 |
| `FR-DHF-002` | **글로벌 영문 서식 + 국문 가이드 2원 체계**: 해외 인증(FDA/CE) 제출용 영문 공식 서식과 국내 규제(식약처) 대응용 국문 안내 팁(`> [!TIP]`) 병행 제공. | `templates/DHF-*.md` (전체) | 사용자 요구사항 (산출물 언어) |
| `FR-DHF-003` | **표준 식별자 체계 강제**: `USER-REQ-*`, `REQ-SW-*`, `RSK-*`, `RCM-*`, `ARCH-*`, `DDS-*`, `TC-*`, `VERIF-*` 등 15개 고유 태그 체계 내장. | `templates/`, `AGENTS.md` | IEC 62304 Cl 5.1.1 |

### 2.4 자동화 검증 도구 요구사항 (`[TOOL]`, `[PART11]`)
| ID | 프레임워크 요구사항 명세 | 검증 대상 컴포넌트 | 추적 기준 |
| :--- | :--- | :--- | :--- |
| `FR-TOOL-001` | **양방향 추적성 자동 검사기 (`validate_traceability.py`)**: DHF 파싱을 통한 요구사항-위험-설계-코드-테스트 100% 양방향 연결 검사 및 고립(Orphan) 항목 발견 시 FAIL 처리. | `scripts/validate_traceability.py` | IEC 62304 Cl 5.1.1, ISO 13485 |
| `FR-TOOL-002` | **DHF 위변조 방지 색인기 (`generate_dhf_index.py`)**: DHF 내 모든 문서의 메타데이터와 SHA-256 해시를 계산하여 총괄 색인 마크다운 테이블 자동 생성. | `scripts/generate_dhf_index.py` | ISO 13485 Cl 4.2.4, 7.3.7 |
| `FR-TOOL-003` | **외부 의존성 제로 실행**: 검증 스크립트는 서드파티 의존성 없이 Python 3 표준 라이브러리(`os`, `sys`, `re`, `hashlib`, `json`, `math`)만으로 구동. | `scripts/*.py` | 도구 신뢰성 & 이식성 |
| `FR-TOOL-004` | **연쇄 무효화 엔진 (`check_change_impact.py`)**: 상위 문서 변경 시 전이적 하위 승인을 일괄 취소하고 재검토 강제. | `scripts/check_change_impact.py` | ISO 13485 Cl 7.3.9 |
| `FR-TOOL-005` | **컴퓨터화 시스템 도구 밸리데이션 (CSV) 및 자체 감사 모드**: `validate_traceability.py`에 `--mode=framework` 플래그를 제공하여 프레임워크 자체의 60개 요구사항과 테스트 스펙 추적성을 스스로 감사·검증. | `scripts/validate_traceability.py` | ISO 13485 Cl 4.1.6, FDA 21 CFR 820.70(i) |
| `FR-PART11-001` | **불변 감사추적 및 전자서명**: WORM JSON-Lines 감사 로그 및 HMAC-SHA256 암호학적 해시 체이닝을 통한 위변조 방지. | `scripts/record_audit_event.py` | FDA 21 CFR Part 11 |
| `FR-PART11-002` | **자동화된 암호학적 감사 이벤트 로거**: CLI 및 환경변수(`SAMD_AUDIT_SECRET`) 기반 안전한 키 관리 및 프로젝트 상태 서명 연동. | `scripts/record_audit_event.py` | ISO 27001 / AGENTS.md |

### 2.5 플랫폼 보안, 이벤트 훅 및 상시 규칙 요구사항 (`[RULE]`, `[HOOK]`, `[MCP]`)
| ID | 프레임워크 요구사항 명세 | 검증 대상 컴포넌트 | 추적 기준 |
| :--- | :--- | :--- | :--- |
| `FR-RULE-001` | **상시 규제 준수 규칙 (`AGENTS.md`)**: 단일 루트 배치(<= 24KB)로 토큰 낭비 방지 및 태그 표준/보안 수칙 시스템 레벨 강제. | `AGENTS.md` | Antigravity Rules Specification |
| `FR-HOOK-001` | **이벤트 기반 규제 린팅 훅**: PreToolUse 단계에서 쓰기 인터록을 평가하여 Fail-Closed 원칙에 따라 비인가 쓰기 차단. | `.agents/hooks.json`<br>`scripts/hook_pre_write_guard.py` | IEC 62304 / ISO 14971 |
| `FR-MCP-001` | **규제 DB 연동용 MCP 인터페이스**: PubMed, FDA 대마 등 외부 규제 데이터 연동을 위한 Model Context Protocol 인터페이스 명세. | `.agents/skills/samd-clinical-sota/SKILL.md` | Antigravity MCP Standard |

### 2.6 소프트웨어 생명주기 프로세스 요구사항 (`[MAINT]`, `[CM]`, `[ANOM]`, `[TRANS]`, `[INT]`)
| ID | 프레임워크 요구사항 명세 | 검증 대상 컴포넌트 | 추적 기준 |
| :--- | :--- | :--- | :--- |
| `FR-MAINT-001` | **소프트웨어 유지보수 및 긴급 패치 거버넌스**: 사후 변경영향분석, 회귀 시험 및 안전성 재평가 체계 확립. | `scripts/check_change_impact.py` | IEC 62304 Clause 6 |
| `FR-CM-001` | **형상관리 및 결정론적 빌드 재현성**: CI/CD 베이스라인 고정 및 암호학적 체크섬 관리. | `scripts/generate_dhf_index.py` | IEC 62304 Clause 8 |
| `FR-ANOM-001` | **문제해결 및 이상사례/CAPA 연동**: 현장 이상사례 및 버그의 4단계 심각도 분류 및 게이트 릴리즈 차단. | `scripts/manage_anomalies.py`<br>`workflows/00` | IEC 62304 Clause 9 |
| `FR-ANOM-002` | **소프트웨어 결함 추세 분석 및 경계 보고**: 반복 결함 패턴 통계화 및 인허가기관 경계 보고 연동. | `scripts/manage_anomalies.py` | IEC 62304 Cl 9.6 |
| `FR-TRANS-001` | **설계 이관 및 DMR 패키징**: DHF로부터 의료기기 마스터 레코드(DMR) 및 양산 릴리즈 패키지 생성. | `templates/DHF-00`, `DHF-11` | ISO 13485 Clause 7.3.8 |
| `FR-INT-001` | **소프트웨어 통합 및 인터페이스 검증**: 서브시스템 간 계약 기반 데이터 인터페이스 검증 테스트 스위트 구비. | `tests/integration/test_framework_integration.py` | IEC 62304 Clause 5.6 |

### 2.7 사이버보안 및 사용적합성 엔지니어링 (`[CYBER]`, `[SOUP]`, `[USE]`, `[PMS]`, `[LBL]`)
| ID | 프레임워크 요구사항 명세 | 검증 대상 컴포넌트 | 추적 기준 |
| :--- | :--- | :--- | :--- |
| `FR-SOUP-001` | **SOUP 전주기 평가, 상용 LLM 공급자 관리 및 SBOM**: 서드파티 라이브러리 및 클라우드 파운데이션 LLM 공급자 자격 평가. | `templates/DHF-06` | IEC 62304 Cl 5.3.3 / ISO 13485 Cl 7.4 |
| `FR-SOUP-002` | **클라우드 파운데이션 LLM 공급자 자격 평가, BAA 및 버전 고정**: 클라우드 LLM 공급자 BAA 체결, 모델 버전 동결 및 오프라인 대체 폴백 핸들러 강제. | `templates/DHF-06`<br>`scripts/manage_anomalies.py` | ISO 13485 Cl 7.4.1 / FDA Cyber |
| `FR-CYBER-001` | **사후 사이버보안 IRP 및 취약점 공개(CVD) SLA**: CVSS >= 9.0 30일/60일 보안 패치 의무화. | `templates/DHF-06` | FDA Cybersecurity Guidance |
| `FR-CYBER-002` | **보안 아키텍처, STRIDE 위협 모델 및 SAST/DAST**: 정적/동적 보안 분석 도구 연동. | `templates/DHF-06` | IEC 81001-5-1 |
| `FR-USE-001` | **사용적합성 엔지니어링 및 PCA 오류 모델링**: 인지-판단-행동 오류 분석 및 안전 배너 강제. | `templates/DHF-01`, `DHF-12` | IEC 62366-1 |
| `FR-USE-002` | **총괄 사용적합성 평가 및 URRA 프로토콜**: 임상 사용자 대상 총괄 형성평가 및 잔여 사용위험 수용성 평가. | `templates/DHF-12` | IEC 62366-1 Clause 5.7 |
| `FR-LBL-001` | **의료기기 표시기재, 전자 사용설명서(e-IFU) 및 임상 금기·경고**: 21 CFR 801 및 EU MDR Annex I Ch III 준수 라벨링 및 IFU 명세화. | `templates/DHF-14` | 21 CFR 801 / EU MDR Annex I Ch III |
| `FR-PMS-001` | **시판 후 임상 추적관찰(PMCF) 및 PSUR 보고**: 정기 안전성 갱신 보고서 작성 및 위험관리파일 연동. | `templates/DHF-13`, `DHF-05C` | ISO 14971 Clause 10 |

### 2.8 AI/ML SaMD 데이터 거버넌스 및 신뢰성 검증 (`[AI]`, `[LLM]`, `[CLIN]`)
| ID | 프레임워크 요구사항 명세 | 검증 대상 컴포넌트 | 추적 기준 |
| :--- | :--- | :--- | :--- |
| `FR-AI-001` | **임상 데이터 출처 및 다중 판독자 일치도 (Class C)**: 비식별화 및 다중 전문의 Kappa >= 0.80 일치도 검증. | `scripts/validate_ai_dataset.py` | GMLP Principle 3 & 4 |
| `FR-AI-002` | **독립 시험셋 동결 및 0.00% 환자 단위 누출 방지 (Class C)**: Train/Val/Test 간 환자 ID 교집합 제로 검증. | `scripts/validate_ai_dataset.py` | GMLP Principle 4 |
| `FR-AI-003` | **서브그룹 편향 감사 및 다기관 일반화 성능 (Class C)**: 인구통계학적/임상 서브그룹 편향 통계 감사. | `scripts/validate_ai_dataset.py` | GMLP Principle 9 |
| `FR-AI-004` | **실시간 데이터/개념 드리프트 감시 및 PCCP 트리거 (Class C)**: PSI >= 0.25 초과 시 비보조 원본 모드 전환. | `scripts/validate_ai_dataset.py` | FDA PCCP Guidance |
| `FR-AI-005` | **설명 가능한 AI (XAI) 및 불확실성 시각화 (Class C)**: Pointing Game >= 80%, IoU >= 0.50, ECE <= 0.05 검증 및 Saliency Map 시각화. | `scripts/verify_grounding.py`<br>`templates/DHF-08` | FDA AI Action Plan |
| `FR-AI-006` | **입력 품질 평가(IQA) 및 OOD 탈락 필터 (Class C)**: 품질 저하 슬라이드 자동 필터링 및 경고. | `scripts/validate_ai_dataset.py`<br>`templates/DHF-08` | 식약처 AI 가이드라인 |
| `FR-AI-007` | **95% 신뢰구간 임상 성능 평가 (Class C)**: 민감도/특이도/AUROC 95% CI 산출 및 보고. | `scripts/validate_ai_dataset.py`<br>`templates/DHF-09` | IMDRF AI SaMD |
| `FR-CLIN-001` | **임상평가 문서군, 3대 축 SOTA 동등성 및 법정 CER/PER Dossier**: EU MDR Art 61/IVDR Art 56 및 IMDRF MDCE N41 기반 임상평가보고서 체계. | `templates/DHF-15` | EU MDR Art 61 / IMDRF N41 |
| `FR-LLM-001` | **LLM 환각 방지 및 규제 접지 (Class B)**: PubMed 및 MeSH 기반 실체적 인용 검증. | `scripts/verify_grounding.py` | IEC 62304 Cl 5.3 |
| `FR-LLM-002` | **프롬프트 인젝션 방어 및 샌드박스 보안 (Class B)**: 7대 적대적 인젝션 시그니처 탐지 및 태그 격리. | `scripts/verify_grounding.py` | OWASP LLM Top 10 |
| `FR-LLM-003` | **결정론적 실행 및 시드 제어 (Class B)**: T = 0.0 결정론적 그리디 디코딩 및 시드 고정 재현성 보장. | `scripts/verify_grounding.py` | IEC 62304 Cl 5.5 |

---

## 3. 프레임워크 검증 자동화 테스트 스위트 (`scripts/test_framework.py`)

프레임워크 자체의 품질과 규제 부합성을 입증하기 위해 27개 이상의 자동화 단위/통합 테스트를 실행합니다:
1. `TS-SKILL-001`: 13개 Antigravity 스킬 YAML Frontmatter 및 디렉토리 구조 검증.
2. `TS-SKILL-002`: `AGENTS.md` 파일 크기(<=24KB) 및 필수 규제 태그 10종 포함 검증.
3. `TS-DHF-001`: 18개 표준 DHF 템플릿 메타데이터 및 국문 안내 팁 존재 확인.
4. `TS-AGENT-001`: 13개 에이전트 명세서 내 페르소나, 책임, 시스템 프롬프트 코드블록 검증.
5. `TS-SRS-001`: 60개 전수 SRS 마크다운 요구사항 명세 무결성 검증.
6. `TS-TESTS-001`: 60개 1:1 매핑 테스트 프로토콜 명세 검증.
7. `TS-RISK-001`: 15개 ISO 14971 위험분석 및 2차 위험 평가 검증.
8. `TS-RISK-002`: 60개 전수 요구사항 예비위험분석(PHA) 스크리닝 매트릭스 검증.
9. `TS-ARCH-001`: 11개 IEC 62304 아키텍처 명세 및 Safety Class C 할당 검증.
10. `TS-DDS-001`: 11개 상세단위설계 명세 검증.
11. `TS-RTM-001`: 60개 요구사항 100% 양방향 추적성 매트릭스 검증.
12. `TS-TOOL-001`: `validate_traceability.py` 양방향 추적성 통과 검증.
13. `TS-TOOL-002` ~ `003`: 고립 및 미검증 요구사항 네거티브 탐지 검증.
14. `TS-TOOL-004`: `generate_dhf_index.py` SHA-256 무결성 검증.
15. `TS-TOOL-005`: `check_change_impact.py` 순환 참조 방지 및 전이적 연쇄 무효화 검증.
16. `TS-TOOL-006`: 전 스크립트 외부 의존성 제로 (Python 3 표준 라이브러리) 감사.
17. `TS-TOOL-007`: `record_audit_event.py` Part 11 WORM HMAC 로거 기능 및 변조 감지 검증.
18. `TS-TOOL-008`: `hook_pre_write_guard.py` PreToolUse 쓰기 차단, Bash 쓰기 리다이렉션 차단 및 Fail-Closed 검증.
19. `TS-TOOL-009`: `project_state.json` 12-Gate 상태 머신 유효성 검증.
20. `TS-TOOL-010`: `validate_ai_dataset.py` 0.00% 환자 누출 및 PSI 드리프트 계산 검증.
21. `TS-TOOL-011`: `verify_grounding.py` 프롬프트 인젝션 차단 및 엄격한 T=0.0 결정론적 검증.
22. `TS-TOOL-012`: `tests/integration/` 서브시스템 간 계약 기반 통합 시험 통과 검증.
23. `TS-TOOL-013`: `manage_anomalies.py` 법정 이상사례 경계 보고 카운트다운 타이머 검증.
24. `TS-TOOL-014`: `validate_traceability.py --mode=framework` 자체 감사 모드 검증.

