# mergekit（二次开发版）

本仓库基于开源项目 **[arcee-ai/mergekit](https://github.com/arcee-ai/mergekit)** 进行二次开发与适配，面向本团队实际模型合并流程做了扩展与维护。

## 1. 原始来源与二次开发说明

- 原始项目：`arcee-ai/mergekit`
- 本仓库定位：在原项目基础上持续进行工程化改造、模型适配与算法支持扩展。

## 2. 使用方法

### 安装

```bash
git clone <your-repo-url>
cd mergekit
pip install -e .
pip install -U transformers peft
```

> 说明：`transformers` 与 `peft` 请保持**最新版本**，避免模型结构与权重加载不兼容。

### 执行

使用 `mergekit-yaml` 作为主入口：

```bash
mergekit-yaml path/to/config.yml ./output-model-directory --cuda
```

常用说明：
- `path/to/config.yml`：合并配置文件
- `./output-model-directory`：输出目录
- `--cuda`：启用 GPU（可选）

## 3. 已支持模型

当前已支持（含已验证或已接入架构）的主流模型系列包括：

- Llama / Llama2 / Llama3 系列
- Mistral 系列
- Qwen 系列
- GLM / StableLM / GPT-NeoX 等

其中：
- **Qwen3.5 目前仅支持 Dense 版本**
- **Qwen3.5-MoE 正在适配中**

## 4. 已支持合并算法

当前已支持的主要合并算法包括：

- linear
- slerp
- nuslerp
- passthrough
- model_stock
- arcee_fusion
- karcher
- task_arithmetic
- ties
- dare_ties
- dare_linear
- breadcrumbs
- breadcrumbs_ties
- della
- della_linear

---

如需新增模型架构或合并算法，请在对应模块中扩展并补充配置示例。
