# Software Requirement: FR-AI-005

> **Requirement ID**: `FR-AI-005`  
> **Title**: Explainable AI (XAI) Saliency Map Generation & Uncertainty Display  
> **Category**: AI/ML SaMD Transparency (`[AI]`)  
> **Safety Class**: Class C (IEC 62304 Clause 5.4)  
> **Parent Standard**: FDA Good Machine Learning Practice (GMLP) Principle 9, MFDS AI SaMD Guideline  
> **Version**: 1.0.0 | **Status**: Approved  
> **1:1 Mapped Test Case**: `docs/tests/TC-FR-AI-005.md`  
> **Allocated Architecture**: `docs/architecture/ARCH-FW-008.md`  
> **Allocated Detailed Design**: `docs/detailed_design/DDS-FW-008.md`  

---

## 1. Description & Technical Rationale
The framework shall require diagnostic AI algorithms to provide explainability mechanisms (such as Grad-CAM or integrated gradients saliency maps) and model confidence/uncertainty metrics to prevent automation bias and enable clinicians to independently scrutinize AI suggestions.

## 2. Detailed Functional Specifications
1. **Visual Attention Map Generation & Quantitative Localization**:
   - Compute normalized feature attribution heatmaps (Grad-CAM / Integrated Gradients) overlaid on medical image inputs.
   - Saliency map attribution must achieve Pointing Game hit rate $\ge 80.0\%$ within annotated pathological lesion boundaries.
   - Bounding box / contour overlap with expert pathologist ground truth tumor focus must achieve Intersection-over-Union $\text{IoU} \ge 0.50$.
2. **Uncertainty Quantification & Calibration**:
   - Display numerical prediction confidence (softmax probability or Bayesian credible interval) alongside every inference output.
   - Model prediction probability must be calibrated to achieve Expected Calibration Error $\text{ECE} \le 0.05$.
3. **Low-Confidence Transparency**:
   - When confidence drops below clinical safety thresholds ($\tau < 0.70$), present a prominent visual warning instructing mandatory manual review.

## 3. Inputs, Processing & Outputs
- **Inputs**: Input medical image tensors, trained deep neural network feature maps.
- **Processing**: Gradient backpropagation attribution calculation, threshold comparison.
- **Outputs**: Bounded saliency heatmaps, uncertainty scores, clinician warning flags.
