# INCEPTION

论文、中文译文、完整附录、可编辑流程图，以及原始研究材料。默认分支为 `main`。

## 当前版本

- [英文论文（56 页）](paper_acl/inception_acl_20261007_v3/build/main.pdf)
- [中文正文与英文对照](paper_acl/inception_acl_20261007_v3/zh.html)
- [附录：指定的九张图与完整提示词](paper_acl/inception_acl_20261007_v3/selected_appendix.html)
- [附录：侧卧提示词、13 张原图与批次记录](paper_acl/inception_acl_20261007_v3/side_prompt_appendix.html)
- [可编辑主流程图](paper_acl/inception_acl_20261007_v3/output/inception_pipeline_v2.pptx)
- [主流程图的矢量版本](paper_acl/inception_acl_20261007_v3/output/inception_pipeline_v2.pdf)
- [最终核验记录](paper_acl/inception_acl_20261007_v3/sources/final_materials_verification.json)

主文包含 50 条参考文献。新的侧卧附录在第 52–56 页；逐条记录区分出图、拒绝、配额或限流、超时。

## 本地阅读与构建

在仓库根目录运行 `python3 -m http.server 8110 --directory paper_acl`，再打开 `http://127.0.0.1:8110/inception_acl_20261007_v3/zh.html`。

英文编译入口是 `paper_acl/inception_acl_20261007_v3/build_document.py`，需要 Python 3、TeX Live 与 BibTeX。中文阅读页由同目录的 `build_zh_reader.py` 生成。主流程图保留可编辑演示文稿、脚本和矢量导出文件。

## 材料目录

- `paper_acl/`：本版及此前论文、文献库、翻译、图表和构建源文件。
- `l7_route/`：原始批次图像、完整提示词、返回记录和研究脚本。
- `experiments/`：实验代码、数据、评估与结果。
- `memory/`：中文项目记录。
- 其他研究图像与材料保留原目录结构。

文件清单及排除项见 [archive_manifest.json](archive_manifest.json)。运行环境、模型权重、认证文件不入库；认证值在归档副本中替换为占位符。原工作区说明保留为 [WORKSPACE_README.md](WORKSPACE_README.md)。
