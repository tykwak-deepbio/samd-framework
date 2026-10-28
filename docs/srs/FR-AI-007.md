# Software Requirement: FR-AI-007

> **Requirement ID**: `FR-AI-007`  
> **Title**: Clinical Performance Evaluation & Statistical Confidence Intervals  
> **Category**: Clinical Performance Validation (`[AI]`)  
> **Safety Class**: Class C (IEC 62304 Clause 5.4)  
> **Parent Standard**: FDA Guidance on Clinical Evaluation of AI/ML SaMD, MFDS AI SaMD Guideline  
> **Version**: 1.0.0 | **Status**: Approved  
> **1:1 Mapped Test Case**: `docs/tests/TC-FR-AI-007.md`  
> **Allocated Architecture**: `docs/architecture/ARCH-FW-008.md`  
> **Allocated Detailed Design**: `docs/detailed_design/DDS-FW-008.md`  

---

## 1. Description & Technical Rationale
The framework shall mandate comprehensive clinical performance reporting for AI/ML SaMD on independent test sets, requiring exact statistical confidence intervals (95% CI) for all diagnostic sensitivity, specificity, PPV/NPV, and ROC-AUC metrics.

## 2. Detailed Functional Specifications
1. **Primary Diagnostic Metrics**:
   - Report Sensitivity (Recall), Specificity, PPV, NPV, Area Under the ROC Curve (AUROC), and Dice similarity coefficient.
2. **Statistical Confidence Intervals**:
   - Compute 95% Clopper-Pearson or Wilson score confidence intervals for all proportion metrics.
3. **Pre-specified Clinical Acceptance Thresholds**:
   - Verify that model metrics meet or exceed clinical thresholds defined in `DHF-02` (e.g., Sensitivity $\ge 90\%$, Specificity $\ge 90\%$, AUROC $\ge 0.95$).

## 3. Inputs, Processing & Outputs
- **Inputs**: Frozen test set ground truth masks, model prediction tensors.
- **Processing**: Confusion matrix calculation, Wilson score CI computation, ROC curve integration.
- **Outputs**: Clinical Performance Evaluation Report with 95% CIs in `DHF-09`.
