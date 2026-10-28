# Software Requirement: FR-SOUP-002

> **Requirement ID**: `FR-SOUP-002`  
> **Title**: Third-Party Cloud Foundation Model & External LLM Provider Qualification  
> **Category**: Supplier Management & SOUP Governance (`[SOUP]`)  
> **Safety Class**: Class B (IEC 62304)  
> **Parent Standard**: ISO 13485:2016 Clause 7.4 (Purchasing & Supplier Control), IEC 62304:2006 Clause 5.3.3 & 5.3.4 (SOUP Requirements and Anomaly Evaluation), HIPAA / GDPR Article 28 (Data Processing Agreements)  
> **Version**: 1.0.0 | **Status**: Approved  
> **1:1 Mapped Test Case**: `docs/tests/TC-FR-SOUP-002.md`  

---

## 1. Description & Regulatory Rationale
Under ISO 13485:2016 Clause 7.4 and IEC 62304 Clause 5.3.3, third-party software components and cloud service providers whose products affect medical device safety or performance must be formally qualified, evaluated, and controlled. When commercial cloud foundation models (e.g. Google Cloud Vertex AI, OpenAI, Anthropic) are used for SaMD clinical inference, automated documentation, or clinical decision support, the provider is legally classified as a Critical Supplier and SOUP provider. The framework shall mandate formal supplier qualification, Data Processing Agreement (DPA/BAA) verification, model version pinning, deprecation sunset notification SLAs, and network outage fail-safe mechanisms.

## 2. Detailed Functional Specifications
1. **Critical Supplier Evaluation & SLA Mandate**:
   - For every external cloud foundation model utilized:
     * Execute formal supplier risk assessment evaluating data privacy, regulatory clearance, and service availability SLAs ($\ge 99.9\%$).
     * Mandate signed Business Associate Agreement (BAA) / HIPAA / GDPR compliance prohibiting training on patient health data (PHI/PII zero-retention guarantee).
2. **Model Version Pinning & Sunset Deprecation Policy**:
   - The framework shall enforce exact model snapshot version pinning (e.g., `gemini-1.5-pro-002` or `claude-3-5-sonnet-20241022`) instead of generic pointer tags (e.g., `latest`), preventing unverified model drift.
   - The supplier agreement or risk mitigation plan must mandate a minimum of 6 months advance notice prior to model deprecation/sunset, allowing adequate time for SaMD change impact analysis and re-verification.
3. **Graceful Degradation & Network Disconnection Fail-Safe**:
   - In accordance with IEC 62304 Clause 5.2.2, if external cloud foundation model connectivity is severed, the system shall execute graceful degradation:
     * Safely disengage automated AI assistance without software crash or silent hanging.
     * Display a high-contrast non-modal status banner: `AI Cloud Service Unavailable - Raw Manual Viewer Active`.
     * Maintain all core non-AI diagnostic viewing and manual measurement functions operational.

## 3. Inputs, Processing & Outputs
- **Inputs**: Cloud LLM API configurations, supplier BAA agreements, model version descriptors.
- **Processing**: Model version verification, network timeout detection, offline fallback activation.
- **Outputs**: Supplier qualification records in `DHF-06`, pinned model baseline, offline fail-safe handler.
