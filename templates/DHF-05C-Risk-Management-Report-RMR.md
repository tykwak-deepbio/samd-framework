# Risk Management Report (RMR)

> **Document ID**: `DHF-05C-RMR`  
> **Applicable Standards**: ISO 14971:2019 Clause 9, ISO/TR 24971:2020  
> **Project Name**: `[Project / Device Name]`  
> **Revision**: `[e.g., 1.0]` | **Effective Date**: `[YYYY-MM-DD]`  
> **Document Status**: `[Draft / In-Review / Approved]`  

---

> [!TIP]
> **국문 작성 가이드 (Korean Guidance)**:
> - 본 문서는 ISO 14971 Clause 9에 따른 위험관리보고서(Risk Management Report)로, 전체 위험관리 생명주기 수행 결과를 종합 평가합니다.
> - 위험관리계획(RMP)이 계획대로 실행되었는지, 모든 위험통제조치(RCM)가 검증되었는지, 모든 잔여 위험이 수용 가능한지, 최종 편익-위험 분석(Benefit-Risk Analysis) 결과가 긍정적인지를 최종 결론짓습니다.

---

## 1. Document Control & Approvals

| Role | Name | Title / Department | Signature / Approval | Date |
| :--- | :--- | :--- | :--- | :--- |
| **Author** | `[Author Name]` | Risk Management Lead | Approved | `[YYYY-MM-DD]` |
| **Reviewer** | `[Reviewer Name]`| Quality Assurance Director | Approved | `[YYYY-MM-DD]` |
| **Approver** | `[Approver Name]`| Chief Medical Officer | Approved | `[YYYY-MM-DD]` |

---

## 2. Risk Management Lifecycle Summary
- All phases of the Risk Management Plan (`DHF-05A-RMP`) have been successfully executed.
- Hazard identification, Preliminary Hazard Analysis (PHA), and Software Failure Modes and Effects Analysis (FMEA) were conducted (`DHF-05B-FMEA`).
- Total Hazards Identified: `[e.g., 4 items]`
- Total Risk Control Measures Implemented: `[e.g., 4 measures]`
- Unmitigated Unacceptable Risks: **0 items (100% mitigated)**.

---

## 3. Overall Residual Risk Evaluation & Benefit-Risk Analysis (BRA)
1. **Residual Risk Acceptability**:
   - Following implementation of `RCM-001` through `RCM-004`, all individual residual risks have been reduced to the "Broadly Acceptable" region.
   - No new hazards or secondary failure modes were introduced by the implemented risk control measures.
2. **Benefit-Risk Determination**:
   - **Clinical Benefits**: Automated tissue detection significantly accelerates pathologist review time (estimated 30-40% reduction in slide screening time) while Macenko color normalization standardizes inter-laboratory staining discrepancy.
   - **Residual Risks**: Minimized to remote probabilities through defensive software bounding, automated low-confidence alerting, and user override capabilities.
   - **Conclusion**: The clinical diagnostic benefits decisively outweigh all residual risks.

---

## 4. Post-Market Risk Monitoring Plan
- Continuous surveillance of field issue reports, bug tickets, and customer complaints related to image artifacts or performance degradation.
- Biannual review of new CVE vulnerabilities and algorithm edge-case reports.
