---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

<span class='anchor' id='about-me'></span>

I am a postdoctoral researcher in the Department of Computer Science at The University of Hong Kong, working with Prof. [Hengshuang Zhao](https://hszhao.github.io/). I received my Ph.D. from the School of Electronic Information and Communications at Huazhong University of Science and Technology, supervised by Prof. [Xiang Bai](https://xbai.vlrlab.net/).

My research studies embodied intelligence systems that connect spatial perception, multimodal reasoning, world modeling, and executable actions. I have worked on autonomous driving and 3D perception for eight years, with recent focus moving toward Embodied AI, Vision-Language-Action models, 4D MLLMs, and 4D world models. I have published 30+ papers in venues including TPAMI, TIP, CVPR, ICCV, ECCV, NeurIPS, AAAI, TITS, and ICRA. As of June 2026, Google Scholar reports 2,283 citations, an h-index of 16, and an i10-index of 16.

<div class="research-focus">
  <div><strong>3D Perception</strong><br>LiDAR, multi-view, multi-modal fusion, detection, tracking, occupancy, prediction, and planning.</div>
  <div><strong>Embodied AI</strong><br>Embodied data engines, spatial intelligence, robotic learning, and cross-embodiment generalization.</div>
  <div><strong>VLA / World-Action Models</strong><br>Vision-language-action models, world-action models, VLN, streaming policies, and efficient real-time inference.</div>
  <div><strong>4D World Models</strong><br>4D occupancy, physics-aware simulation, virtual evaluation, policy learning, and sim-to-real transfer.</div>
</div>

# Research Vision

My long-term goal is to build general-purpose embodied intelligence systems that integrate data, models, simulation, evaluation, and deployment. The current blueprint is organized around embodied data engines, embodied foundation models, 4D world models and simulation, efficient streaming inference, and an intelligent robotic OS for manipulation, navigation, autonomous driving, and cross-embodiment deployment.

<div class="vision-figure">
  <img src="Our_embodied_system.png" alt="Embodied intelligence system overview">
</div>

# News

- **May 2026:** MCNav and AlphaGRPO are released.
- **Mar 2026:** FASTER and ACE-Brain-0 are released.
- **Feb 2026:** DrivePI and GenieDrive are accepted by CVPR 2026.
- **Dec 2025:** DrivePI and GenieDrive are released.
- **Nov 2025:** UniLION and Visual Spatial Tuning are released.
- **Nov 2025:** Invited to give a talk at Huawei Yinwang Intelligent Technology, with over 100 researchers attending.
- **Sep 2024:** LION is accepted by NeurIPS 2024.
- **Jul 2024:** SEED and OPEN are accepted by ECCV 2024.
- **Sep 2023:** QTNet is accepted by NeurIPS 2023.
- **Nov 2022:** StereoDistill is accepted by AAAI 2023 and EPNet++ is accepted by TPAMI.
- **Nov 2019:** TANet is accepted by AAAI 2020 as an oral presentation.

# Publications

*: Equal contribution, +: Corresponding Author, †: Project Leader.

<div class='paper-box'>
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">arXiv 2026</div><img src='images/mcnav.png' alt="MCNav" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://arxiv.org/abs/2605.19594">MCNav: Memory-Aware Dynamic Cognitive Map for Zero-shot Goal-oriented Navigation</a></div>
    <div class='paper-authors'>Jingyu Li*, <strong>Zhe Liu*</strong>, Wenxiao Wu, Li Zhang</div>
    <div class='paper-venue'>arXiv preprint, 2026.</div>
    <div class='paper-links'><a href="https://arxiv.org/abs/2605.19594">[Paper]</a></div>
  </div>
</div>

<div class='paper-box'>
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">ICML 2026</div><img src='images/alphagrpo.png' alt="AlphaGRPO" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://arxiv.org/abs/2605.12495">AlphaGRPO: Unlocking Self-Reflective Multimodal Generation in UMMs via Decompositional Verifiable Reward</a></div>
    <div class='paper-authors'>Runhui Huang, Jie Wu, Rui Yang, <strong>Zhe Liu</strong>, Hengshuang Zhao</div>
    <div class='paper-venue'>International Conference on Machine Learning (<strong>ICML</strong>), 2026.</div>
    <div class='paper-links'><a href="https://huangrh99.github.io/AlphaGRPO/">[Project]</a><a href="https://arxiv.org/abs/2605.12495">[Paper]</a><a href="https://github.com/huangrh99/AlphaGRPO">[Code]</a></div>
  </div>
</div>

<div class='paper-box'>
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">arXiv 2026</div><img src='images/faster.png' alt="FASTER" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://arxiv.org/abs/2603.19199">FASTER: Rethinking Real-Time Flow VLAs</a></div>
    <div class='paper-authors'>Yuxiang Lu, <strong>Zhe Liu†</strong>, Xianzhe Fan, Zhenya Yang, Jinghua Hou, Junyi Li, Kaixin Ding, Hengshuang Zhao</div>
    <div class='paper-venue'>arXiv preprint, 2026.</div>
    <div class='paper-links'><a href="https://innovator-zero.github.io/FASTER/">[Project]</a><a href="https://arxiv.org/abs/2603.19199">[Paper]</a><a href="https://github.com/innovator-zero/FASTER">[Code]</a></div>
  </div>
</div>

<div class='paper-box'>
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">arXiv 2026</div><img src='images/acebrain.png' alt="ACE-Brain-0" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://arxiv.org/abs/2603.03198">ACE-Brain-0: Spatial Intelligence as a Shared Scaffold for Universal Embodiments</a></div>
    <div class='paper-authors'>Ziyang Gong*, Zehang Luo*, Anke Tang*, <strong>Zhe Liu*</strong>, Shi Fu, Zhi Hou, Ganlin Yang, Weiyun Wang, Xiaofeng Wang, Jianbo Liu, et al.</div>
    <div class='paper-venue'>arXiv preprint, 2026.</div>
    <div class='paper-links'><a href="https://arxiv.org/abs/2603.03198">[Paper]</a></div>
  </div>
</div>

<div class='paper-box'>
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">CVPR 2026</div><img src='images/geniedrive.png' alt="GenieDrive" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://arxiv.org/abs/2512.12751">GenieDrive: Towards Physics-Aware Driving World Model with 4D Occupancy Guided Video Generation</a></div>
    <div class='paper-authors'>Zhenya Yang, <strong>Zhe Liu†</strong>, Yuxiang Lu, Liping Hou, Chenxuan Miao, Siyi Peng, Bailan Feng, Xiang Bai, Hengshuang Zhao+</div>
    <div class='paper-venue'>Computer Vision and Pattern Recognition (<strong>CVPR</strong>), 2026.</div>
    <div class='paper-links'><a href="https://arxiv.org/abs/2512.12751">[Paper]</a><a href="https://github.com/Huster-YZY/GenieDrive">[Code]</a></div>
  </div>
</div>

<div class='paper-box'>
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">CVPR 2026</div><img src='images/drivepi.png' alt="DrivePI" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://arxiv.org/abs/2512.12799">DrivePI: Spatial-aware 4D MLLM for Unified Autonomous Driving Understanding, Perception, Prediction and Planning</a></div>
    <div class='paper-authors'><strong>Zhe Liu</strong>, Runhui Huang, Rui Yang, Siming Yan, Zining Wang, Lu Hou, Di Lin, Xiang Bai, Hengshuang Zhao+</div>
    <div class='paper-venue'>Computer Vision and Pattern Recognition (<strong>CVPR</strong>), 2026.</div>
    <div class='paper-links'><a href="https://github.com/happinesslz/DrivePI">[Project]</a><a href="https://arxiv.org/abs/2512.12799">[Paper]</a><a href="https://github.com/happinesslz/DrivePI">[Code]</a></div>
  </div>
</div>

<div class='paper-box'>
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">ICRA 2026</div><img src='images/geoteacher.png' alt="GeoTeacher" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://arxiv.org/abs/2512.23147">GeoTeacher: Geometry-Guided Semi-Supervised 3D Object Detection</a></div>
    <div class='paper-authors'>Jingyu Li, Xiaolong Zhao, <strong>Zhe Liu</strong>, Wenxiao Wu, Li Zhang</div>
    <div class='paper-venue'>International Conference on Robotics and Automation (<strong>ICRA</strong>), 2026.</div>
    <div class='paper-links'><a href="https://arxiv.org/abs/2512.23147">[Paper]</a><a href="https://github.com/SII-Whaleice/GeoTeacher">[Code]</a></div>
  </div>
</div>

<div class='paper-box'>
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">arXiv 2025</div><img src='images/vst.png' alt="Visual Spatial Tuning" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://arxiv.org/abs/2511.05491">Visual Spatial Tuning</a></div>
    <div class='paper-authors'>Rui Yang, Ziyu Zhu, Yanwei Li, Jingjia Huang, Shen Yan, Siyuan Zhou, <strong>Zhe Liu</strong>, Xiangtai Li, Shuangye Li, Wenqian Wang, Yi Lin, Hengshuang Zhao</div>
    <div class='paper-venue'>arXiv preprint, 2025.</div>
    <div class='paper-links'><a href="https://arxiv.org/abs/2511.05491">[Paper]</a></div>
  </div>
</div>

<div class='paper-box'>
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">arXiv 2025</div><img src='images/UniLION.png' alt="UniLION" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://arxiv.org/abs/2511.01768">UniLION: Towards Unified Autonomous Driving Model with Linear Group RNNs</a></div>
    <div class='paper-authors'><strong>Zhe Liu</strong>, Jinghua Hou, Xiaoqing Ye, Jingdong Wang, Hengshuang Zhao+, Xiang Bai+</div>
    <div class='paper-venue'>arXiv preprint, 2025.</div>
    <div class='paper-links'><a href="https://github.com/happinesslz/UniLION">[Project]</a><a href="https://arxiv.org/abs/2511.01768">[Paper]</a><a href="https://github.com/happinesslz/UniLION">[Code]</a></div>
  </div>
</div>

<div class='paper-box'>
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">ICCV 2025</div><img src='images/dac.png' alt="DAC" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://openaccess.thecvf.com/content/ICCV2025/html/Wang_Describe_Adapt_and_Combine_Empowering_CLIP_Encoders_for_Open-set_3D_ICCV_2025_paper.html">Describe, Adapt and Combine: Empowering CLIP Encoders for Open-set 3D Object Retrieval</a></div>
    <div class='paper-authors'>Zhichuan Wang, Yang Zhou, <strong>Zhe Liu</strong>, Rui Yu, Song Bai, Yulong Wang, Xinwei He, Xiang Bai</div>
    <div class='paper-venue'>International Conference on Computer Vision (<strong>ICCV</strong>), 2025.</div>
    <div class='paper-links'><a href="https://openaccess.thecvf.com/content/ICCV2025/html/Wang_Describe_Adapt_and_Combine_Empowering_CLIP_Encoders_for_Open-set_3D_ICCV_2025_paper.html">[Paper]</a><a href="https://github.com/wangzhichuan123/DAC">[Code]</a></div>
  </div>
</div>

<div class='paper-box'>
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">IROS 2025</div><img src='images/hybridtm.png' alt="HybridTM" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://arxiv.org/abs/2507.18575">HybridTM: Combining Transformer and Mamba for 3D Semantic Segmentation</a></div>
    <div class='paper-authors'>Xinyu Wang, Jinghua Hou, <strong>Zhe Liu</strong>, Yingying Zhu</div>
    <div class='paper-venue'>IEEE/RSJ International Conference on Intelligent Robots and Systems (<strong>IROS</strong>), 2025.</div>
    <div class='paper-links'><a href="https://arxiv.org/abs/2507.18575">[Paper]</a><a href="https://github.com/deepinact/HybridTM">[Code]</a></div>
  </div>
</div>

<div class='paper-box'>
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">NeurIPS 2024</div><img src='images/lion.png' alt="LION" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://arxiv.org/abs/2407.18232">LION: Linear Group RNN for 3D Object Detection in Point Clouds</a></div>
    <div class='paper-authors'><strong>Zhe Liu*</strong>, Jinghua Hou*, Xingyu Wang, Xiaoqing Ye, Jingdong Wang, Hengshuang Zhao, Xiang Bai</div>
    <div class='paper-venue'>Neural Information Processing Systems (<strong>NeurIPS</strong>), 2024.</div>
    <div class='paper-links'><a href="https://happinesslz.github.io/projects/LION/">[Project]</a><a href="https://arxiv.org/abs/2407.18232">[Paper]</a><a href="https://github.com/happinesslz/LION">[Code]</a></div>
  </div>
</div>

<div class='paper-box'>
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">ECCV 2024</div><img src='images/seed.png' alt="SEED" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://arxiv.org/pdf/2407.10749">SEED: A Simple and Effective 3D DETR in Point Clouds</a></div>
    <div class='paper-authors'><strong>Zhe Liu*</strong>, Jinghua Hou*, Xiaoqing Ye, Tong Wang, Jingdong Wang, Xiang Bai</div>
    <div class='paper-venue'>European Conference on Computer Vision (<strong>ECCV</strong>), 2024.</div>
    <div class='paper-links'><a href="https://arxiv.org/pdf/2407.10749">[Paper]</a><a href="https://github.com/happinesslz/SEED">[Code]</a></div>
  </div>
</div>

<div class='paper-box'>
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">ECCV 2024</div><img src='images/open.jpg' alt="OPEN" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://arxiv.org/pdf/2407.10753">OPEN: Object-wise Position Embedding for Multi-view 3D Object Detection</a></div>
    <div class='paper-authors'>Jinghua Hou, Tong Wang, Xiaoqing Ye, <strong>Zhe Liu</strong>, Shi Gong, Xiao Tan, Errui Ding, Jingdong Wang, Xiang Bai</div>
    <div class='paper-venue'>European Conference on Computer Vision (<strong>ECCV</strong>), 2024.</div>
    <div class='paper-links'><a href="https://arxiv.org/pdf/2407.10753">[Paper]</a><a href="https://github.com/AlmoonYsl/OPEN">[Code]</a></div>
  </div>
</div>

<div class='paper-box'>
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">TITS 2024</div><img src='images/fbmnet.png' alt="FBMNet" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://arxiv.org/pdf/2305.07713">Multi-Modal 3D Object Detection by Box Matching</a></div>
    <div class='paper-authors'><strong>Zhe Liu</strong>, Xiaoqing Ye, Zhikang Zou, Xinwei He, Xiao Tan, Errui Ding, Jingdong Wang, Xiang Bai</div>
    <div class='paper-venue'>IEEE Transactions on Intelligent Transportation Systems (<strong>TITS</strong>), 2024.</div>
    <div class='paper-links'><a href="https://arxiv.org/pdf/2305.07713">[Paper]</a><a href="https://github.com/happinesslz/FBMNet">[Code]</a></div>
  </div>
</div>

<div class='paper-box'>
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">NeurIPS 2023</div><img src='images/qtnet.png' alt="QTNet" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://openreview.net/pdf?id=gySmwdmVDF">Query-based Temporal Fusion with Explicit Motion for 3D Object Detection</a></div>
    <div class='paper-authors'>Jinghua Hou*, <strong>Zhe Liu*</strong>, Dingkang Liang, Zhikang Zou, Xiaoqing Ye, Xiang Bai</div>
    <div class='paper-venue'>Neural Information Processing Systems (<strong>NeurIPS</strong>), 2023.</div>
    <div class='paper-links'><a href="https://openreview.net/pdf?id=gySmwdmVDF">[Paper]</a><a href="https://github.com/AlmoonYsl/QTNet">[Code]</a></div>
  </div>
</div>

<div class='paper-box'>
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">ICCV 2023</div><img src='images/wss3d.jpg' alt="WSS3D" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://openaccess.thecvf.com/content/ICCV2023/papers/Zhang_A_Simple_Vision_Transformer_for_Weakly_Semi-supervised_3D_Object_Detection_ICCV_2023_paper.pdf">A Simple Vision Transformer for Weakly Semi-supervised 3D Object Detection</a></div>
    <div class='paper-authors'>Dingyuan Zhang*, Dingkang Liang*, Zhikang Zou*, Jingyu Li, Xiaoqing Ye, <strong>Zhe Liu</strong>, Xiao Tan, Xiang Bai</div>
    <div class='paper-venue'>International Conference on Computer Vision (<strong>ICCV</strong>), 2023.</div>
    <div class='paper-links'><a href="https://openaccess.thecvf.com/content/ICCV2023/papers/Zhang_A_Simple_Vision_Transformer_for_Weakly_Semi-supervised_3D_Object_Detection_ICCV_2023_paper.pdf">[Paper]</a></div>
  </div>
</div>

<div class='paper-box'>
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">ICRA 2023</div><img src='images/dds3d.png' alt="DDS3D" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://arxiv.org/pdf/2303.05079">DDS3D: Dense Pseudo-Labels with Dynamic Threshold for Semi-Supervised 3D Object Detection</a></div>
    <div class='paper-authors'>Jingyu Li*, <strong>Zhe Liu*</strong>, Jinghua Hou, Dingkang Liang</div>
    <div class='paper-venue'>International Conference on Robotics and Automation (<strong>ICRA</strong>), 2023.</div>
    <div class='paper-links'><a href="https://arxiv.org/pdf/2303.05079">[Paper]</a><a href="https://github.com/Whale-ice/DDS3D">[Code]</a></div>
  </div>
</div>

<div class='paper-box'>
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">AAAI 2023</div><img src='images/stereo_distill.png' alt="StereoDistill" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://ojs.aaai.org/index.php/AAAI/article/download/25268/25040">StereoDistill: Pick the Cream from LiDAR for Distilling Stereo-based 3D Object Detection</a></div>
    <div class='paper-authors'><strong>Zhe Liu</strong>, Xiaoqing Ye, Xiao Tan, Errui Ding, Xiang Bai</div>
    <div class='paper-venue'>AAAI Conference on Artificial Intelligence (<strong>AAAI</strong>), 2023.</div>
    <div class='paper-links'><a href="https://ojs.aaai.org/index.php/AAAI/article/download/25268/25040">[Paper]</a></div>
  </div>
</div>

<div class='paper-box'>
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">TPAMI 2022</div><img src='images/epnet++.png' alt="EPNet++" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://arxiv.org/pdf/2112.11088">EPNet++: Cascade Bi-directional Fusion for Multi-Modal 3D Object Detection</a></div>
    <div class='paper-authors'><strong>Zhe Liu</strong>, Tengteng Huang, Bingling Li, Xiwu Chen, Xi Wang, Xiang Bai</div>
    <div class='paper-venue'>IEEE Transactions on Pattern Analysis and Machine Intelligence (<strong>TPAMI</strong>), 2022.</div>
    <div class='paper-links'><a href="https://arxiv.org/pdf/2112.11088">[Paper]</a><a href="https://github.com/happinesslz/EPNetV2">[Code]</a></div>
  </div>
</div>

<div class='paper-box'>
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">ECCV 2020</div><img src='images/epnet.png' alt="EPNet" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://arxiv.org/pdf/2007.08856">EPNet: Enhancing Point Features with Image Semantics for 3D Object Detection</a></div>
    <div class='paper-authors'>Tengteng Huang*, <strong>Zhe Liu*</strong>, Xiwu Chen, Xiang Bai</div>
    <div class='paper-venue'>European Conference on Computer Vision (<strong>ECCV</strong>), 2020.</div>
    <div class='paper-links'><a href="https://arxiv.org/pdf/2007.08856">[Paper]</a><a href="https://github.com/happinesslz/EPNet">[Code]</a></div>
  </div>
</div>

<div class='paper-box'>
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">AAAI 2020</div><img src='images/tanet.jpg' alt="TANet" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://arxiv.org/pdf/1912.05163">TANet: Robust 3D Object Detection from Point Clouds with Triple Attention</a></div>
    <div class='paper-authors'><strong>Zhe Liu</strong>, Xin Zhao, Tengteng Huang, Ruolan Hu, Yu Zhou, Xiang Bai</div>
    <div class='paper-venue'>AAAI Conference on Artificial Intelligence (<strong>AAAI</strong>), 2020. Oral presentation.</div>
    <div class='paper-links'><a href="https://arxiv.org/pdf/1912.05163">[Paper]</a><a href="https://github.com/happinesslz/TANet">[Code]</a></div>
  </div>
</div>

<div class='paper-box'>
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">AAAI 2019</div><img src='images/SIFRNet.png' alt="SIFRNet" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://arxiv.org/abs/1901.02237">3D Object Detection Using Scale Invariant and Feature Reweighting Networks</a></div>
    <div class='paper-authors'>Xin Zhao, <strong>Zhe Liu+</strong>, Ruolan Hu, Kaiqi Huang</div>
    <div class='paper-venue'>AAAI Conference on Artificial Intelligence (<strong>AAAI</strong>), 2019.</div>
    <div class='paper-links'><a href="https://arxiv.org/abs/1901.02237">[Paper]</a></div>
  </div>
</div>

# Professional Service

- **Conference Reviewer:** CVPR, ICCV, ECCV, ICLR, NeurIPS, AAAI, IJCAI, ICRA, ICASSP, ACM Multimedia Asia.
- **Journal Reviewer:** TPAMI, TIP, TCSVT, TITS, RA-L, SCIS, TGRS.
- **Invited Talks:** Machine Intelligence, Midea Research Institute, 3D CVer, Shuzihuanyu, The Heart of Autonomous Driving, and Huawei Yinwang Intelligent Technology.

# Contact

- **Email:** [zheliu12@hku.hk](mailto:zheliu12@hku.hk)
- **CV:** [Download CV](data/cv_zheliu_hku.pdf)
- **Google Scholar:** [Profile](https://scholar.google.com/citations?hl=zh-CN&user=yprv7EsAAAAJ&view_op=list_works)
- **GitHub:** [happinesslz](https://github.com/happinesslz/)
