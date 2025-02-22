import datasets
import json
import os


def download_dataset(output_dir="./data/iwslt14"):
    """下载数据集并保存到本地"""
    # 创建输出目录
    os.makedirs(output_dir, exist_ok=True)

    # 下载数据集
    dataset = {
        split: datasets.load_dataset("bbaaaa/iwslt14-de-en-preprocess", split=split, trust_remote_code=True)[
            'translation']
        for split in ['train', 'validation', 'test']
    }

    # 保存到本地文件
    for split in dataset.keys():
        output_file = os.path.join(output_dir, f"{split}.json")
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(dataset[split], f, ensure_ascii=False, indent=2)

    print(f"Dataset saved to {output_dir}")


if __name__ == "__main__":
    download_dataset()