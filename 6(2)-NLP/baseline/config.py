"""
KorNLI Configuration - 설정값 관리
"""

import torch

# Label Mapping
LABEL2ID = {"entailment": 0, "neutral": 1, "contradiction": 2}
ID2LABEL = {v: k for k, v in LABEL2ID.items()}
NUM_LABELS = len(LABEL2ID)

# Device
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
if torch.backends.mps.is_available():
    DEVICE = torch.device("mps")

# Paths
DEFAULT_DATA_DIR = "../data"
DEFAULT_OUTPUT_DIR = "../submission"
DEFAULT_CHECKPOINT_DIR = "./checkpoints"

# Configuration Presets
CONFIGS = {
    "default": {
        "model_name": "monologg/koelectra-small-v3-discriminator",
        "max_length": 128,
        "batch_size": 64,
        "learning_rate": 2e-5,
        "epochs": 5,
        "warmup_ratio": 0.1,
        "weight_decay": 0.01,
        "classifier_dropout": 0.2,
        "early_stopping_patience": 3,
        "preprocess": False,
        "train_file": "train.tsv",
        "dev_file": "val.tsv",
        "test_file": "test_unlabeled.tsv",
    },
}


def get_config(preset: str = "default", **overrides) -> dict:
    """설정 프리셋 로드 + override 적용"""
    if preset not in CONFIGS:
        raise ValueError(f"Unknown preset: {preset}. Available: {list(CONFIGS.keys())}")
    config = CONFIGS[preset].copy()
    config.update(overrides)
    return config
