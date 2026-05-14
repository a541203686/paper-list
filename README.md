![paper-list](https://github.com/isLinXu/issues/assets/59380685/dbd27f25-e7d7-4a0f-bdc2-d9b06fc03a2e)![GitHub stars](https://img.shields.io/github/stars/isLinXu/paper-list)![GitHub forks](https://img.shields.io/github/forks/isLinXu/paper-list)![GitHub watchers](https://img.shields.io/github/watchers/isLinXu/paper-list)[![Build Status](https://img.shields.io/endpoint.svg?url=https%3A%2F%2Factions-badge.atrox.dev%2Fatrox%2Fsync-dotenv%2Fbadge&style=flat)](https://github.com/isLinXu/paper-list)![img](https://badgen.net/badge/icon/learning?icon=deepscan&label)![GitHub repo size](https://img.shields.io/github/repo-size/isLinXu/paper-list.svg?style=flat-square)![GitHub language count](https://img.shields.io/github/languages/count/isLinXu/paper-list)![GitHub last commit](https://img.shields.io/github/last-commit/isLinXu/paper-list)![GitHub](https://img.shields.io/github/license/isLinXu/paper-list.svg?style=flat-square)![img](https://hits.dwyl.com/isLinXu/paper-list.svg)<p align="center"><h1 align="center"><br><ins>Paper-List-DAILY</ins><br>每日自动更新的论文列表</h1></p>
## 最后更新于 2026.05.14

![paper_list](https://github.com/isLinXu/issues/assets/59380685/0ab31126-9ef4-4c49-bf80-8dae2a3acaa8)

## 项目简介

本仓库提供每日更新的 arXiv 计算机视觉及人工智能领域论文列表，并按主题进行分类整理。每日更新由 GitHub Actions 自动化执行，帮助您及时掌握前沿研究动态。

在线文档：[https://islinxu.github.io/paper-list/](https://islinxu.github.io/paper-list/)

## 数据分析

- 数据面板：[docs/analytics/](docs/analytics/)

![trend_daily](docs/analytics/charts/trend_daily_zh.png)

![topic_rank](docs/analytics/charts/topic_rank_zh.png)

![code_coverage](docs/analytics/charts/code_coverage_trend_zh.png)

![top_authors](docs/analytics/charts/top_authors_zh.png)

## 使用方法

若要在本地生成论文列表，请执行以下步骤：

1. **安装依赖**
   ```bash
   pip install -r requirements.txt
   ```

2. **运行脚本**
   ```bash
   python get_paper.py
   ```

3. **自定义配置**
   您可以在 `config.yaml` 中自定义搜索关键词及其他设置。

### 进阶用法

您还可以使用 `scripts/` 目录下的脚本执行附加任务：

- **统计特定日期范围内的论文数量**：
  ```bash
  python scripts/count_range.py 2024-01-01 2024-12-31
  ```

## 论文列表

  <ol>
    <li><a href=docs/Classification.md>Classification</a></li>
    <li><a href=docs/Object_Detection.md>Object Detection</a></li>
    <li><a href=docs/Semantic_Segmentation.md>Semantic Segmentation</a></li>
    <li><a href=docs/Object_Tracking.md>Object Tracking</a></li>
    <li><a href=docs/Action_Recognition.md>Action Recognition</a></li>
    <li><a href=docs/Pose_Estimation.md>Pose Estimation</a></li>
    <li><a href=docs/Image_Generation.md>Image Generation</a></li>
    <li><a href=docs/LLM.md>LLM</a></li>
    <li><a href=docs/Scene_Understanding.md>Scene Understanding</a></li>
    <li><a href=docs/Depth_Estimation.md>Depth Estimation</a></li>
    <li><a href=docs/Audio_Processing.md>Audio Processing</a></li>
    <li><a href=docs/Multimodal.md>Multimodal</a></li>
    <li><a href=docs/Anomaly_Detection.md>Anomaly Detection</a></li>
    <li><a href=docs/Transfer_Learning.md>Transfer Learning</a></li>
    <li><a href=docs/Optical_Flow.md>Optical Flow</a></li>
    <li><a href=docs/Reinforcement_Learning.md>Reinforcement Learning</a></li>
    <li><a href=docs/Graph_Neural_Networks.md>Graph Neural Networks</a></li>
    <li><a href=docs/Latent_Space_LLM.md>Latent Space LLM</a></li>
    <li><a href=docs/Diffusion_Models.md>Diffusion Models</a></li>
    <li><a href=docs/Video_Understanding.md>Video Understanding</a></li>
    <li><a href=docs/Neural_Rendering.md>Neural Rendering</a></li>
  </ol>
