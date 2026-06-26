# LLM Watermark Papers

This repository tracks papers related to LLM watermarking. The main list is sorted by venue or journal time. Topic-specific views are generated from the same data source.

> Note: We believe that KGW is the starting point of LLM Watermark, so we only collect watermarking work after KGW.

## Topic Pages

- [![Survey](https://img.shields.io/badge/Survey-brightgreen)](topics/survey.md)
- [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- [![Multi-bit](https://img.shields.io/badge/Multi--bit-orange)](topics/multi-bit.md)
- [![Attack](https://img.shields.io/badge/Attack-red)](topics/attack.md)
- [![Backdoor Watermark](https://img.shields.io/badge/Backdoor%20Watermark-blueviolet)](topics/backdoor-watermark.md)

## Maintenance

After manually editing `data/papers.yml` or adding a new venue-year entry to `data/venues.yml`, run:

```powershell
python scripts\pipeline.py --skip-git
```

## Timeline

### 2023

#### ICML 2023 (July)

- **A Watermark for Large Language Models**  
  [paper](https://arxiv.org/pdf/2301.10226) | ICML 2023 (Outstanding Paper) | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)

#### WIFS 2023 (December)

- **Three Bricks to Consolidate Watermarks for Large Language Models**  
  [paper](https://arxiv.org/pdf/2308.00113) | WIFS 2023 | [![Multi-bit](https://img.shields.io/badge/Multi--bit-orange)](topics/multi-bit.md)

### 2024

#### NDSS 2024 (February)

- **SSL-WM: A Black-Box Watermarking Approach for Encoders Pre-trained by Self-Supervised Learning**  
  [paper](https://www.ndss-symposium.org/wp-content/uploads/2024-374-paper.pdf) | NDSS 2024 | [![Backdoor Watermark](https://img.shields.io/badge/Backdoor%20Watermark-blueviolet)](topics/backdoor-watermark.md)

#### ICLR 2024 (May)

- **A Semantic Invariant Robust Watermark for Large Language Models**  
  [paper](https://openreview.net/pdf?id=6p8lpe4MNf) | ICLR 2024 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **An Unforgeable Publicly Verifiable Watermark for Large Language Models**  
  [paper](https://openreview.net/pdf?id=gMLQwKDY3N) | ICLR 2024 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **On the Learnability of Watermarks for Language Models**  
  [paper](https://openreview.net/pdf?id=9k0krNzvlV) | ICLR 2024 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **On the Reliability of Watermarks for Large Language Models**  
  [paper](https://openreview.net/pdf?id=DEJIDCmWOz) | ICLR 2024 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **Provable Robust Watermarking for AI-Generated Text**  
  [paper](https://openreview.net/pdf?id=SsmT8aO45L) | ICLR 2024 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **Towards Codable Watermarking for Injecting Multi-Bits Information to LLMs**  
  [paper](https://openreview.net/pdf?id=JYu5Flqm9D) | ICLR 2024 | [![Multi-bit](https://img.shields.io/badge/Multi--bit-orange)](topics/multi-bit.md)
- **Towards Faithful XAI Evaluation via Generalization-Limited Backdoor Watermark**  
  [paper](https://openreview.net/pdf?id=cObFETcoeW) | ICLR 2024 | [![Backdoor Watermark](https://img.shields.io/badge/Backdoor%20Watermark-blueviolet)](topics/backdoor-watermark.md)
- **Unbiased Watermark for Large Language Models**  
  [paper](https://openreview.net/pdf?id=uWVC5FVidc) | ICLR 2024 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)

#### S&P 2024 (May)

- **MEA-Defender: A Robust Watermark against Model Extraction Attack**  
  [paper](https://arxiv.org/pdf/2401.15239) | S&P 2024 | [![Backdoor Watermark](https://img.shields.io/badge/Backdoor%20Watermark-blueviolet)](topics/backdoor-watermark.md)
- **PromptCARE: Prompt Copyright Protection by Watermark Injection and Verification**  
  [paper](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10646612) | S&P 2024 | [![Backdoor Watermark](https://img.shields.io/badge/Backdoor%20Watermark-blueviolet)](topics/backdoor-watermark.md)

#### NAACL 2024 (June)

- **Advancing Beyond Identification: Multi-bit Watermark for Large Language Models**  
  [paper](https://arxiv.org/pdf/2308.00221) | NAACL 2024 | [![Multi-bit](https://img.shields.io/badge/Multi--bit-orange)](topics/multi-bit.md)
- **SemStamp: A Semantic Watermark with Paraphrastic Robustness for Text Generation**  
  [paper](https://arxiv.org/pdf/2310.03991.pdf) | NAACL 2024 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **A Robust Semantics-based Watermark for Large Language Model against Paraphrasing**  
  [paper](https://arxiv.org/pdf/2311.08721.pdf) | NAACL 2024 Findings | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **WaterJudge: Quality-Detection Trade-off when Watermarking Large Language Models**  
  [paper](https://arxiv.org/pdf/2403.19548) | NAACL 2024 Findings | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)

#### ICML 2024 (July)

- **A Resilient and Accessible Distribution-Preserving Watermark for Large Language Models**  
  [paper](https://arxiv.org/pdf/2310.07710.pdf) | ICML 2024 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **Adaptive Text Watermark for Large Language Models**  
  [paper](https://arxiv.org/pdf/2401.13927.pdf) | ICML 2024 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **Optimizing Watermarks for Large Language Models**  
  [paper](https://arxiv.org/pdf/2312.17295) | ICML 2024 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **Token-Specific Watermarking with Enhanced Detectability and Semantic Coherence for Large Language Models**  
  [paper](https://arxiv.org/pdf/2402.18059.pdf) | ICML 2024 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **Watermark Stealing in Large Language Models**  
  [paper](https://arxiv.org/pdf/2402.19361) | ICML 2024 | [![Attack](https://img.shields.io/badge/Attack-red)](topics/attack.md)
- **Watermarks in the Sand: Impossibility of Strong Watermarking for Language Models**  
  [paper](https://arxiv.org/pdf/2311.04378) | ICML 2024 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)

#### ACL 2024 (August)

- **An Entropy-based Text Watermarking Detection Method**  
  [paper](https://aclanthology.org/2024.acl-long.630.pdf) | ACL 2024 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **Bypassing LLM Watermarks with Color-Aware Substitutions**  
  [paper](https://aclanthology.org/2024.acl-long.464.pdf) | ACL 2024 | [![Attack](https://img.shields.io/badge/Attack-red)](topics/attack.md)
- **Can Watermarks Survive Translation? On the Cross-lingual Consistency of Text Watermark for Large Language Models**  
  [paper](https://aclanthology.org/2024.acl-long.226.pdf) | ACL 2024 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **GumbelSoft: Diversified Language Model Watermarking via the GumbelMax-trick**  
  [paper](https://arxiv.org/pdf/2402.12948.pdf) | ACL 2024 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **WARDEN: Multi-Directional Backdoor Watermarks for Embedding-as-a-Service Copyright Protection**  
  [paper](https://aclanthology.org/2024.acl-long.725.pdf) | ACL 2024 | [![Backdoor Watermark](https://img.shields.io/badge/Backdoor%20Watermark-blueviolet)](topics/backdoor-watermark.md)
- **WaterBench: Towards Holistic Evaluation of Watermarks for Large Language Models**  
  [paper](https://arxiv.org/pdf/2311.07138.pdf) | ACL 2024 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **WatME: Towards Lossless Watermarking Through Lexical Redundancy**  
  [paper](https://aclanthology.org/2024.acl-long.496.pdf) | ACL 2024 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **Who Wrote this Code? Watermarking for Code Generation**  
  [paper](https://aclanthology.org/2024.acl-long.268.pdf) | ACL 2024 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **Duwak: Dual Watermarks in Large Language Models**  
  [paper](https://arxiv.org/pdf/2403.13000) | ACL 2024 Findings | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **k-SemStamp: A Clustering-Based Semantic Watermark for Detection of Machine-Generated Text**  
  [paper](https://arxiv.org/pdf/2402.11399.pdf) | ACL 2024 Findings | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **Subtle Signatures, Strong Shields: Advancing Robust and Imperceptible Watermarking in Large Language Models**  
  [paper](https://aclanthology.org/2024.findings-acl.327.pdf) | ACL 2024 Findings | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)

#### USENIX 2024 (August)

- **DeepEclipse: How to Break White-Box DNN-Watermarking Schemes**  
  [paper](https://www.usenix.org/system/files/usenixsecurity24-pegoraro.pdf) | USENIX 2024 | [![Backdoor Watermark](https://img.shields.io/badge/Backdoor%20Watermark-blueviolet)](topics/backdoor-watermark.md)
- **REMARK-LLM: A Robust and Efficient Watermarking Framework for Generative Large Language Models**  
  [paper](https://arxiv.org/pdf/2310.12362.pdf) | USENIX 2024 | [![Multi-bit](https://img.shields.io/badge/Multi--bit-orange)](topics/multi-bit.md)

#### CCS 2024 (October)

- **Neural Dehydration: Effective Erasure of Black-box Watermarks from DNNs with Limited Data**  
  [paper](https://arxiv.org/pdf/2309.03466) | CCS 2024 | [![Backdoor Watermark](https://img.shields.io/badge/Backdoor%20Watermark-blueviolet)](topics/backdoor-watermark.md)
- **TabularMark: Watermarking Tabular Datasets for Machine Learning**  
  [paper](https://arxiv.org/pdf/2406.14841) | CCS 2024 | [![Backdoor Watermark](https://img.shields.io/badge/Backdoor%20Watermark-blueviolet)](topics/backdoor-watermark.md)

#### EMNLP 2024 (November)

- **Context-aware Watermark with Semantic Balanced Green-red Lists for Large Language Models**  
  [paper](https://aclanthology.org/2024.emnlp-main.1260/) | EMNLP 2024 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **PostMark: A Robust Blackbox Watermark for Large Language Models**  
  [paper](https://arxiv.org/pdf/2406.14517) | EMNLP 2024 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **Revisiting the Robustness of Watermarking to Paraphrasing Attacks**  
  [paper](https://aclanthology.org/2024.emnlp-main.1005.pdf) | EMNLP 2024 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **Waterfall: Scalable Framework for Robust Text Watermarking and Provenance for LLMs**  
  [paper](https://aclanthology.org/2024.emnlp-main.1138.pdf) | EMNLP 2024 | [![Multi-bit](https://img.shields.io/badge/Multi--bit-orange)](topics/multi-bit.md)
- **CodeIP: A Grammar-Guided Multi-Bit Watermark for Large Language Models of Code**  
  [paper](https://aclanthology.org/2024.findings-emnlp.541.pdf) | EMNLP 2024 Findings | [![Multi-bit](https://img.shields.io/badge/Multi--bit-orange)](topics/multi-bit.md)
- **Downstream Trade-offs of a Family of Text Watermarks**  
  [paper](https://aclanthology.org/2024.findings-emnlp.821.pdf) | EMNLP 2024 Findings | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **GuardEmb: Dynamic Watermark for Safeguarding Large Language Model Embedding Service Against Model Stealing Attack**  
  [paper](https://aclanthology.org/2024.findings-emnlp.441.pdf) | EMNLP 2024 Findings | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)

#### NeurIPS 2024 (December)

- **Inevitable Trade-off between Watermark Strength and Speculative Sampling Efficiency for Language Models**  
  [paper](https://openreview.net/pdf?id=6YKMBUiIsG) | NeurIPS 2024 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **No Free Lunch in LLM Watermarking: Trade-offs in Watermarking Design Choices**  
  [paper](https://openreview.net/pdf?id=rIOl7KbSkv) | NeurIPS 2024 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **Watermarking Makes Language Models Radioactive**  
  [paper](https://arxiv.org/pdf/2402.14904.pdf) | NeurIPS 2024 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **WaterMax: breaking the LLM watermark detectability-robustness-quality trade-off**  
  [paper](https://arxiv.org/pdf/2403.04808) | NeurIPS 2024 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **ZeroMark: Towards Dataset Ownership Verification without Disclosing Watermark**  
  [paper](https://openreview.net/pdf?id=Eyyt3ZmNV6) | NeurIPS 2024 | [![Backdoor Watermark](https://img.shields.io/badge/Backdoor%20Watermark-blueviolet)](topics/backdoor-watermark.md)

#### TMLR 2024

- **Robust Distortion-free Watermarks for Language Models**  
  [paper](https://openreview.net/pdf?id=FpaCL1MO2C) | TMLR 2024 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)

#### TIFS 2024

- **PointNCBW: Toward Dataset Ownership Verification for Point Clouds via Negative Clean-Label Backdoor Watermark**  
  [paper](https://arxiv.org/pdf/2408.05500) | TIFS 2024 | [![Backdoor Watermark](https://img.shields.io/badge/Backdoor%20Watermark-blueviolet)](topics/backdoor-watermark.md)

#### Nature 2024

- **Scalable watermarking for identifying large language model outputs**  
  [paper](https://www.nature.com/articles/s41586-024-08025-4) | Nature 2024 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)

#### PMLR 2024

- **Undetectable Watermarks for Language Models**  
  [paper](https://proceedings.mlr.press/v247/christ24a/christ24a.pdf) | PMLR 2024 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)

#### ACM Computing Surveys 2024

- **A Survey of Text Watermarking in the Era of Large Language Models**  
  [paper](https://dl.acm.org/doi/pdf/10.1145/3691626) | ACM Computing Surveys 2024 | [![Survey](https://img.shields.io/badge/Survey-brightgreen)](topics/survey.md)

### 2025

#### NDSS 2025 (February)

- **Explanation as a Watermark: Towards Harmless and Multi-bit Model Ownership Verification via Watermarking Feature Attribution**  
  [paper](https://www.ndss-symposium.org/wp-content/uploads/2025-338-paper.pdf) | NDSS 2025 | [![Backdoor Watermark](https://img.shields.io/badge/Backdoor%20Watermark-blueviolet)](topics/backdoor-watermark.md)

#### ICLR 2025 (April)

- **A Watermark for Order-Agnostic Language Models**  
  [paper](https://openreview.net/pdf?id=Nlm3Xf0W9S) | ICLR 2025 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **Black-Box Detection of Language Model Watermarks**  
  [paper](https://arxiv.org/pdf/2405.20777) | ICLR 2025 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **Can Watermarked LLMs be Identified by Users via Crafted Prompts?**  
  [paper](https://openreview.net/pdf?id=ujpAYpFDEA) | ICLR 2025 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **Can Watermarks be Used to Detect LLM IP Infringement For Free?**  
  [paper](https://openreview.net/pdf?id=KRMSH1GxUK) | ICLR 2025 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **Permute-and-Flip: An optimally stable and watermarkable decoder for LLMs**  
  [paper](https://openreview.net/pdf?id=YyVVicZ32M) | ICLR 2025 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **Ward: Provable RAG Dataset Inference via LLM Watermarks**  
  [paper](https://openreview.net/pdf?id=kVrwHLAb20) | ICLR 2025 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)

#### NAACL 2025 (April)

- **$B^4$: A Black-Box Scrubbing Attack on LLM Watermarks**  
  [paper](https://aclanthology.org/2025.naacl-long.460/) | NAACL 2025 | [![Attack](https://img.shields.io/badge/Attack-red)](topics/attack.md)
- **WaterPool: A Language Model Watermark Mitigating Trade-Offs among Imperceptibility, Efficacy and Robustness**  
  [paper](https://aclanthology.org/2025.naacl-long.209/) | NAACL 2025 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **From Intentions to Techniques: A Comprehensive Taxonomy and Challenges in Text Watermarking for Large Language Models**  
  [paper](https://aclanthology.org/2025.findings-naacl.343.pdf) | NAACL 2025 Findings | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **Lost in Overlap: Exploring Logit-based Watermark Collision in LLMs**  
  [paper](https://arxiv.org/pdf/2403.10020) | NAACL 2025 Findings | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **WaterSeeker: Pioneering Efficient Detection of Watermarked Segments in Large Documents**  
  [paper](https://aclanthology.org/2025.findings-naacl.156.pdf) | NAACL 2025 Findings | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)

#### S&P 2025 (May)

- **SoK: Watermarking for AI-Generated Content**  
  [paper](https://arxiv.org/pdf/2411.18479) | S&P 2025 | [![Survey](https://img.shields.io/badge/Survey-brightgreen)](topics/survey.md)
- **Watermarking Language Models for Many Adaptive Users**  
  [paper](https://arxiv.org/pdf/2405.11109) | S&P 2025 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)

#### ACL 2025 (July)

- **Can LLM Watermarks Robustly Prevent Unauthorized Knowledge Distillation?**  
  [paper](https://aclanthology.org/2025.acl-long.648.pdf) | ACL 2025 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **Efficiently Identifying Watermarked Segments in Mixed-Source Texts**  
  [paper](https://aclanthology.org/2025.acl-long.316.pdf) | ACL 2025 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **Ensemble Watermarks for Large Language Models**  
  [paper](https://arxiv.org/pdf/2411.19563) | ACL 2025 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **From Trade-off to Synergy: A Versatile Symbiotic Watermarking Framework for Large Language Models**  
  [paper](https://aclanthology.org/2025.acl-long.509.pdf) | ACL 2025 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **Improved Unbiased Watermark for Large Language Models**  
  [paper](https://aclanthology.org/2025.acl-long.1005.pdf) | ACL 2025 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **MorphMark: Flexible Adaptive Watermarking for Large Language Models**  
  [paper](https://aclanthology.org/2025.acl-long.240.pdf) | ACL 2025 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **Sandcastles in the Storm: Revisiting the (Im)possibility of Strong Watermarking**  
  [paper](https://aclanthology.org/2025.acl-long.1436.pdf) | ACL 2025 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **Watermarking Large Language Models: An Unbiased and Low-risk Method**  
  [paper](https://aclanthology.org/2025.acl-long.391.pdf) | ACL 2025 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)

#### ICML 2025 (July)

- **An End-to-End Model For Logits Based Large Language Models Watermarking**  
  [paper](https://openreview.net/attachment?id=9sNiCqi2RD&name=pdf) | ICML 2025 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **BiMark: Unbiased Multilayer Watermarking for Large Language Models**  
  [paper](https://openreview.net/pdf?id=Zvyb3WAg03) | ICML 2025 | [![Multi-bit](https://img.shields.io/badge/Multi--bit-orange)](topics/multi-bit.md)
- **De-mark: Watermark Removal in Large Language Models**  
  [paper](https://openreview.net/attachment?id=5dF4mqVVqK&name=pdf) | ICML 2025 | [![Attack](https://img.shields.io/badge/Attack-red)](topics/attack.md)
- **Discovering Spoofing Attempts on Language Model Watermarks**  
  [paper](https://openreview.net/attachment?id=hSCxEZLvxI&name=pdf) | ICML 2025 | [![Attack](https://img.shields.io/badge/Attack-red)](topics/attack.md)
- **GaussMark: A Practical Approach for Structural Watermarking of Language Models**  
  [paper](https://openreview.net/attachment?id=YG3DbpAQBf&name=pdf) | ICML 2025 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **Lightweight-Mark: Rethinking Deep Learning-Based Watermarking**  
  [paper](https://openreview.net/attachment?id=ag3uveGZCb&name=pdf) | ICML 2025 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **Optimizing Adaptive Attacks against Watermarks for Language Models**  
  [paper](https://openreview.net/pdf?id=AsODat0dkE) | ICML 2025 | [![Attack](https://img.shields.io/badge/Attack-red)](topics/attack.md)
- **Revealing Weaknesses in Text Watermarking Through Self-Information Rewrite Attacks**  
  [paper](https://openreview.net/attachment?id=fE3kgW7kMp&name=pdf) | ICML 2025 | [![Attack](https://img.shields.io/badge/Attack-red)](topics/attack.md)
- **Robust Multi-bit Text Watermark with LLM-based Paraphrasers**  
  [paper](https://openreview.net/attachment?id=DVjkling5x&name=pdf) | ICML 2025 | [![Multi-bit](https://img.shields.io/badge/Multi--bit-orange)](topics/multi-bit.md)
- **StealthInk: A Multi-bit and Stealthy Watermark for Large Language Models**  
  [paper](https://openreview.net/attachment?id=dktpDfUTtj&name=pdf) | ICML 2025 | [![Multi-bit](https://img.shields.io/badge/Multi--bit-orange)](topics/multi-bit.md)

#### USENIX 2025 (August)

- **Provably Robust Multi-bit Watermarking for AI-generated Text**  
  [paper](https://arxiv.org/pdf/2401.16820.pdf) | USENIX 2025 | [![Multi-bit](https://img.shields.io/badge/Multi--bit-orange)](topics/multi-bit.md)

#### CCS 2025 (October)

- **RAG-WM: An Efficient Black-Box Watermarking Approach for Retrieval-Augmented Generation of Large Language Models**  
  [paper](https://arxiv.org/pdf/2501.05249) | CCS 2025 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)

#### EMNLP 2025 (November)

- **Addressing Tokenization Inconsistency in Steganography and Watermarking Based on Large Language Models**  
  [paper](https://aclanthology.org/2025.emnlp-main.361.pdf) | EMNLP 2025 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **CLMTracing: Black-box User-level Watermarking for Code Language Model Tracing**  
  [paper](https://aclanthology.org/2025.emnlp-main.1475.pdf) | EMNLP 2025 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **Invisible Entropy: Towards Safe and Efficient Low-Entropy LLM Watermarking**  
  [paper](https://aclanthology.org/2025.emnlp-main.341.pdf) | EMNLP 2025 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **SimMark: A Robust Sentence-Level Similarity-Based Watermarking Algorithm for Large Language Models**  
  [paper](https://aclanthology.org/2025.emnlp-main.1567.pdf) | EMNLP 2025 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **Evaluating the Robustness and Accuracy of Text Watermarking Under Real-World Cross-Lingual Manipulations**  
  [paper](https://aclanthology.org/2025.findings-emnlp.390.pdf) | EMNLP 2025 Findings | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **Factuality Beyond Coherence: Evaluating LLM Watermarking Methods for Medical Texts**  
  [paper](https://aclanthology.org/2025.findings-emnlp.818.pdf) | EMNLP 2025 Findings | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **Watermark Smoothing Attacks against Language Models**  
  [paper](https://aclanthology.org/2025.findings-emnlp.264.pdf) | EMNLP 2025 Findings | [![Attack](https://img.shields.io/badge/Attack-red)](topics/attack.md)
- **Watermark under Fire: A Robustness Evaluation of LLM Watermarking**  
  [paper](https://aclanthology.org/2025.findings-emnlp.1148.pdf) | EMNLP 2025 Findings | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **Watermarking with Low-Entropy POS-Guided Token Partitioning and Z-Score-Driven Dynamic Bias for Large Language Models**  
  [paper](https://aclanthology.org/2025.findings-emnlp.260.pdf) | EMNLP 2025 Findings | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)

#### NeurIPS 2025 (December)

- **Enhancing LLM Watermark Resilience Against Both Scrubbing and Spoofing Attacks**  
  [paper](https://openreview.net/pdf?id=RbdLnwEEjk) | NeurIPS 2025 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **HeavyWater and SimplexWater: Distortion-free LLM Watermarks for Low-Entropy Distributions**  
  [paper](https://openreview.net/pdf?id=R5EBtNE2Y9) | NeurIPS 2025 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **Learning to Watermark: A Selective Watermarking Framework for Large Language Models via Multi-Objective Optimization**  
  [paper](https://openreview.net/pdf?id=nJq5z21eUk) | NeurIPS 2025 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **On the Empirical Power of Goodness-of-Fit Tests in Watermark Detection**  
  [paper](https://openreview.net/pdf?id=YES7VDXPV8) | NeurIPS 2025 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **Practical and Effective Code Watermarking for Large Language Models**  
  [paper](https://openreview.net/pdf?id=RpE4HeuX69) | NeurIPS 2025 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **SAEMARK: Steering Personalized Multilingual LLMWatermarks with Sparse Autoencoders**  
  [paper](https://openreview.net/pdf?id=tXnyVPNOfa) | NeurIPS 2025 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **Theoretically Grounded Framework for LLM Watermarking: A Distribution-Adaptive Approach**  
  [paper](https://openreview.net/pdf?id=CMmKcHFDKL) | NeurIPS 2025 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)

#### TIFS 2025

- **ModelShield: Adaptive and Robust Watermark Against Model Extraction Attack**  
  [paper](https://arxiv.org/pdf/2405.02365) | TIFS 2025 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)

### 2026

#### AAAI 2026 (January)

- **WaterMod: Modular Token-Rank Partitioning for Probability-Balanced LLM Watermarking**  
  [paper](https://ojs.aaai.org/index.php/AAAI/article/view/40546/44507) | AAAI 2026 | [![Multi-bit](https://img.shields.io/badge/Multi--bit-orange)](topics/multi-bit.md)

#### NDSS 2026 (February)

- **Character-Level Perturbations Disrupt LLM Watermarks**  
  [paper](https://www.ndss-symposium.org/wp-content/uploads/2026-s138-paper.pdf) | NDSS 2026 | [![Attack](https://img.shields.io/badge/Attack-red)](topics/attack.md)

#### ICLR 2026 (April)

- **An Ensemble Framework for Unbiased Language Model Watermarking**  
  [paper](https://openreview.net/attachment?id=iZ7i2y1YxO&name=pdf) | ICLR 2026 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **Analyzing and Evaluating Unbiased Language Model Watermark**  
  [paper](https://openreview.net/attachment?id=6T4LR1oRwA&name=pdf) | ICLR 2026 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **Break the Trade-off Between Watermark Strength and Speculative Sampling Efficiency for Language Models**  
  [paper](https://openreview.net/attachment?id=HA8vzzT6Ax&name=pdf) | ICLR 2026 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **Distilling the Thought, Watermarking the Answer: A Principle Semantic Guided Watermark for Reasoning Large Language Models**  
  [paper](https://openreview.net/attachment?id=T6NVogsXCZ&name=pdf) | ICLR 2026 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **Every Language Model Has a Forgery-Resistant Signature**  
  [paper](https://openreview.net/attachment?id=vLFqOoMBol&name=pdf) | ICLR 2026 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **In-Context Watermarks for Large Language Models**  
  [paper](https://openreview.net/attachment?id=fD9YRHazW3&name=pdf) | ICLR 2026 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **LLM Fingerprinting via Semantically Conditioned Watermarks**  
  [paper](https://openreview.net/attachment?id=t38nZqqi3Z&name=pdf) | ICLR 2026 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **PMark: Towards Robust and Distortion-free Semantic-level Watermarking with Channel Constraints**  
  [paper](https://openreview.net/attachment?id=EhDgP69DJG&name=pdf) | ICLR 2026 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **Watermarking Diffusion Language Models**  
  [paper](https://openreview.net/attachment?id=3aBWTYGcaT&name=pdf) | ICLR 2026 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)

#### ACL 2026 (July)

- **A Linguistics-Aware LLM Watermarking via Syntactic Predictability**  
  [paper](https://aclanthology.org/2026.acl-long.2115.pdf) | ACL 2026 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **AgentMark: Utility-Preserving Behavioral Watermarking for Agents**  
  [paper](https://aclanthology.org/2026.acl-long.573.pdf) | ACL 2026 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **Don’t Corrupt the Fact: A Trustworthy RAG Watermarking Framework based on Dual Factual Shield**  
  [paper](https://aclanthology.org/2026.acl-long.2075.pdf) | ACL 2026 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **Knowledge-Infused Multi-Bit Watermarking for RAG Knowledge Bases**  
  [paper](https://aclanthology.org/2026.acl-long.1298.pdf) | ACL 2026 | [![Multi-bit](https://img.shields.io/badge/Multi--bit-orange)](topics/multi-bit.md)
- **QuantileMark: A Message-Symmetric Multi-bit Watermark for LLMs**  
  [paper](https://aclanthology.org/2026.acl-long.308.pdf) | ACL 2026 | [![Multi-bit](https://img.shields.io/badge/Multi--bit-orange)](topics/multi-bit.md)
- **ReasMark: A Robust Watermark for Attributing LLM Reasoning Under Knowledge Distillation Attacks**  
  [paper](https://aclanthology.org/2026.acl-long.2185.pdf) | ACL 2026 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **SSG: Logit-Balanced Vocabulary Partitioning for LLM Watermarking**  
  [paper](https://aclanthology.org/2026.acl-long.1702.pdf) | ACL 2026 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **SWAN: Semantic Watermarking with Abstract Meaning Representation**  
  [paper](https://aclanthology.org/2026.acl-long.1681.pdf) | ACL 2026 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **XMark: Reliable Multi-Bit Watermarking for LLM-Generated Texts**  
  [paper](https://aclanthology.org/2026.acl-long.672.pdf) | ACL 2026 | [![Multi-bit](https://img.shields.io/badge/Multi--bit-orange)](topics/multi-bit.md)
- **You Can Have a Second Chance: Unbiased and Multi-bit Watermarking for Diffusion Language Models with Regret-based Remasking**  
  [paper](https://aclanthology.org/2026.acl-long.1297.pdf) | ACL 2026 | [![Multi-bit](https://img.shields.io/badge/Multi--bit-orange)](topics/multi-bit.md)
- **Beyond A Fixed Seal: Adaptive Stealing Watermark in Large Language Models**  
  [paper](https://aclanthology.org/2026.findings-acl.1036.pdf) | ACL 2026 Findings | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **DualGuard: Dual-stream Large Language Model Watermarking Defense against Paraphrase and Spoofing Attack**  
  [paper](https://aclanthology.org/2026.findings-acl.1169.pdf) | ACL 2026 Findings | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **EntroBench: Evaluating LLM Watermarking Under Multi-Entropy Scenarios and Practical User Operations**  
  [paper](https://aclanthology.org/2026.findings-acl.2089.pdf) | ACL 2026 Findings | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **From TDMA to CDMA: A Multi-bit Watermark for Diffusion Language Models**  
  [paper](https://aclanthology.org/2026.findings-acl.1066.pdf) | ACL 2026 Findings | [![Multi-bit](https://img.shields.io/badge/Multi--bit-orange)](topics/multi-bit.md)
- **LR-DWM: Efficient Watermarking for Diffusion Language Models**  
  [paper](https://aclanthology.org/2026.findings-acl.2161.pdf) | ACL 2026 Findings | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **Measuring Watermarking under Jailbreaking: ASR Inflation and Goal-Compliance Mismatch**  
  [paper](https://aclanthology.org/2026.findings-acl.1797.pdf) | ACL 2026 Findings | [![Attack](https://img.shields.io/badge/Attack-red)](topics/attack.md)
- **Position: LLM Watermarking Should Align Stakeholders' Incentives for Practical Adoption**  
  [paper](https://aclanthology.org/2026.findings-acl.1290.pdf) | ACL 2026 Findings | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **Rethinking LLM Watermark Detection in Black-Box Settings: A Non-Intrusive Third-Party Framework**  
  [paper](https://aclanthology.org/2026.findings-acl.990.pdf) | ACL 2026 Findings | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **RShield: A User-level Traceable Backdoor Watermark for LLMs in Embedding-as-a-Service**  
  [paper](https://aclanthology.org/2026.findings-acl.1347.pdf) | ACL 2026 Findings | [![Backdoor Watermark](https://img.shields.io/badge/Backdoor%20Watermark-blueviolet)](topics/backdoor-watermark.md)
- **The Mark Fades: Adaptive Evolutionary Paraphrase-based Attack against LLM Watermarks**  
  [paper](https://aclanthology.org/2026.findings-acl.459.pdf) | ACL 2026 Findings | [![Attack](https://img.shields.io/badge/Attack-red)](topics/attack.md)
- **Topic-Based Watermarks for Large Language Models**  
  [paper](https://aclanthology.org/2026.findings-acl.1220.pdf) | ACL 2026 Findings | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)

#### ICML 2026 (July)

- **Adaptive Code Watermarking Through Reinforcement Learning**  
  paper: TBD | ICML 2026 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **AliMark: Enhancing Robustness of Sentence-Level Watermarks Against Text Paraphrasing**  
  [paper](https://arxiv.org/abs/2605.29434) | ICML 2026 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **Block-wise Codeword Embedding for Reliable Multi-bit Text Watermarking**  
  paper: TBD | ICML 2026 | [![Multi-bit](https://img.shields.io/badge/Multi--bit-orange)](topics/multi-bit.md)
- **Catch-22: On the Fundamental Tradeoff Between Detectability and Robustness in LLM Watermarking**  
  paper: TBD | ICML 2026 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **dgMARK: Decoding-Guided Watermarking for Diffusion Language Models**  
  [paper](https://arxiv.org/abs/2601.22985) | ICML 2026 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **Echoes within the Reasoning: Stealth and Effective Watermarking via Chain of Thought**  
  [paper](https://arxiv.org/abs/2605.28890) | ICML 2026 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **How Good is Post-Hoc Watermarking With Language Model Rephrasing?**  
  [paper](https://arxiv.org/abs/2512.16904) | ICML 2026 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **IACW: Intent-Aware Controllable Watermarking for Scalable Authorial Intent Attribution**  
  paper: TBD | ICML 2026 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **Ideal Attribution and Faithful Watermarks for Language Models**  
  [paper](https://arxiv.org/abs/2512.07038) | ICML 2026 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **IPMark: A Sentence-Level Watermark for LLMs with Hierarchical Personalization and Efficient Detection**  
  paper: TBD | ICML 2026 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **Linear Ensembles Wash Away Watermarks: On the Fragility of Distributional Perturbations in LLMs**  
  [paper](https://arxiv.org/abs/2605.30501) | ICML 2026 | [![Attack](https://img.shields.io/badge/Attack-red)](topics/attack.md)
- **LORD-GoF: A Robust Online Detection Approach for LLM Watermarks in Sparse and Mixed Streams**  
  paper: TBD | ICML 2026 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **PASA: A Principled Embedding-Space Watermarking Approach for LLM-Generated Text under Semantic-Invariant Attacks**  
  [paper](https://arxiv.org/abs/2605.10977) | ICML 2026 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **Power-Calibrated LLM Watermarking: A Statistical Framework**  
  paper: TBD | ICML 2026 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **Rethinking Forgery Attacks on Semantic Watermarks in Black-Box Settings: A Geometric Distortion Perspective**  
  paper: TBD | ICML 2026 | [![Attack](https://img.shields.io/badge/Attack-red)](topics/attack.md)
- **Revisiting Coding-Based Approaches to Overcome the Curse of Dimensionality in Learning-Based Watermarking**  
  paper: TBD | ICML 2026 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **Selective Disclosure Watermarking for Large Language Models**  
  paper: TBD | ICML 2026 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **Stability-Aware Feature Design for Robust Watermark Detection in Machine-Generated Text**  
  paper: TBD | ICML 2026 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **Towards Reliable Marking and Verification of AI-Generated Text via Geometry-aware Sentence-level Watermarking**  
  paper: TBD | ICML 2026 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)
- **Watermarking LLM Agent Trajectories**  
  [paper](https://arxiv.org/abs/2602.18700) | ICML 2026 | [![Zero-bit](https://img.shields.io/badge/Zero--bit-yellowgreen)](topics/zero-bit.md)

