from transformers import PretrainedConfig

from mergekit.architecture import arch_info_for_config


def test_qwen3_architecture_alias_prefers_qwen3_by_model_type():
    cfg = PretrainedConfig(
        model_type="qwen3",
        architectures=["Qwen2ForCausalLM"],
    )

    arch_info = arch_info_for_config(cfg)

    assert arch_info is not None
    assert arch_info.expected_model_type == "qwen3"


def test_qwen3_5_architecture_supported():
    cfg = PretrainedConfig(
        model_type="qwen3_5",
        architectures=["Qwen3ForCausalLM"],
    )

    arch_info = arch_info_for_config(cfg)

    assert arch_info is not None
    assert arch_info.expected_model_type == "qwen3_5"
