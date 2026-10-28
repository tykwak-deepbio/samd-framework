---
name: samd-clinical-sota
description: Conducts systematic clinical literature reviews, State of the Art (SOTA) medical technology benchmarking, and clinical baseline performance analysis. Use this skill when establishing clinical safety/performance baselines or authoring DHF-02.
---

# SaMD Clinical Literature & SOTA Analysis

This skill executes Phase 2 of the SaMD lifecycle, complying with **EU IVDR 2017/746 Annex XIII (Performance Evaluation)**, **MDCG 2020-1 (Clinical Evaluation of SaMD)**, **IMDRF N41**, and **MFDS 가이드라인(인공지능 의료기기 임상평가)**.

## Goal
Establish the clinical and scientific validity of the SaMD, survey state-of-the-art diagnostic algorithms and clinical practices, define clinical acceptance thresholds, and author **`DHF-02-Clinical-Literature-and-SOTA.md`**.

## Research Protocol

1. **Systematic Search Strategy**:
   - Query databases (PubMed, IEEE Xplore, Google Scholar, arXiv, ClinicalTrials.gov).
   - Search strings: `("<clinical indication>" OR "<pathology modality>") AND ("deep learning" OR "segmentation" OR "color normalization" OR "whole slide imaging")`.
   - Inclusion / Exclusion criteria: Peer-reviewed clinical studies within past 5-7 years, representative multi-scanner cohorts.
2. **State of the Art (SOTA) Benchmarking**:
   - Identify existing approved devices or predicate devices (e.g. FDA 510(k)/De Novo cleared WSI viewers, MFDS cleared digital pathology software).
   - Document state-of-the-art algorithms:
     * Tissue segmentation: Otsu thresholding vs U-Net vs Vision Transformers (ViT).
     * Color normalization: Reinhard, Macenko, Vahadane, GAN-based stain transfer.
   - Benchmark performance metrics: Dice Similarity Coefficient (DSC), Intersection-over-Union (IoU), Structural Similarity Index (SSIM), Delta E color difference.
3. **Clinical Endpoints & Acceptance Baselines**:
   - Define objective minimum clinical thresholds (e.g. Tissue area Dice >= 0.92, Background artifact false positive rate < 3%).
   - Establish Benefit-Risk baseline comparing AI-assisted workflow vs. manual pathologist screening.

## Procedure

1. Execute literature review search and synthesize findings.
2. Tabulate predicate devices, comparative clinical trials, and algorithm benchmarks.
3. Populate `templates/DHF-02-Clinical-Literature-and-SOTA.md`.
4. Ensure all claims link to DOI/PMID citations.
5. Export clinical requirements (`CLIN-REQ-xxx`) for input into SRS (`DHF-04`).
