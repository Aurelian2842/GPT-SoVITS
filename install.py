import argparse
import sys

import requests
import zipfile
import tarfile
import os
import pyopenjtalk

def download_and_unzip(url, filename, path):
    print(f"Downloading {filename}")
    if os.path.exists(filename):
        os.remove(filename)
    with requests.get(url, stream=True, timeout=60) as r:
        r.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    os.makedirs(path, exist_ok=True)
    print(f"Extracting {filename}")
    with zipfile.ZipFile(filename, 'r') as zip_ref:
        zip_ref.extractall(path)
    os.remove(filename)
    print(f"Successfully downloaded {filename}")

def download_and_extract_tar_gz(url, filename, path):
    print(f"Downloading {filename}")
    if os.path.exists(filename):
        os.remove(filename)
    with requests.get(url, stream=True, timeout=60) as r:
        r.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    os.makedirs(path, exist_ok=True)
    print(f"Extracting {filename}")
    with tarfile.open(filename, "r:gz") as tar:
        tar.extractall(path=path)
    os.remove(filename)
    print(f"Successfully downloaded {filename}")

def main():
    parser = argparse.ArgumentParser(description="GPT-SoVITS Pre-Installation Script")

    parser.add_argument("-s", "--source", type=str, required=True, help="The model source (Available: HF (HuggingFace), HF-Mirror, ModelScope)")    # 可选参数

    args = parser.parse_args()

    if args.source == "HF":
        print("Downloading model from HuggingFace ...")
        pretrained_url="https://huggingface.co/XXXXRT/GPT-SoVITS-Pretrained/resolve/main/pretrained_models.zip"
        g2pw_url="https://huggingface.co/XXXXRT/GPT-SoVITS-Pretrained/resolve/main/G2PWModel.zip"
        nltk_url="https://huggingface.co/XXXXRT/GPT-SoVITS-Pretrained/resolve/main/nltk_data.zip"
        pyopenjtalk_url="https://huggingface.co/XXXXRT/GPT-SoVITS-Pretrained/resolve/main/open_jtalk_dic_utf_8-1.11.tar.gz"
    elif args.source == "HF-Mirror":
        print("Downloading model from HuggingFace-Mirror ...")
        pretrained_url="https://hf-mirror.com/XXXXRT/GPT-SoVITS-Pretrained/resolve/main/pretrained_models.zip"
        g2pw_url="https://hf-mirror.com/XXXXRT/GPT-SoVITS-Pretrained/resolve/main/G2PWModel.zip"
        nltk_url="https://hf-mirror.com/XXXXRT/GPT-SoVITS-Pretrained/resolve/main/nltk_data.zip"
        pyopenjtalk_url="https://hf-mirror.com/XXXXRT/GPT-SoVITS-Pretrained/resolve/main/open_jtalk_dic_utf_8-1.11.tar.gz"
    elif args.source == "ModelScope":
        print("Downloading model from ModelScope ...")
        pretrained_url="https://www.modelscope.cn/models/XXXXRT/GPT-SoVITS-Pretrained/resolve/master/pretrained_models.zip"
        g2pw_url="https://www.modelscope.cn/models/XXXXRT/GPT-SoVITS-Pretrained/resolve/master/G2PWModel.zip"
        nltk_url="https://www.modelscope.cn/models/XXXXRT/GPT-SoVITS-Pretrained/resolve/master/nltk_data.zip"
        pyopenjtalk_url="https://www.modelscope.cn/models/XXXXRT/GPT-SoVITS-Pretrained/resolve/master/open_jtalk_dic_utf_8-1.11.tar.gz"
    else:
        print("Invalid source. Please choose from HF, HF-Mirror, ModelScope.")
        return
    download_and_unzip(pretrained_url, "pretrained_models.zip", "GPT_SoVITS")
    download_and_unzip(g2pw_url, "G2PWModel.zip", "GPT_SoVITS/text")
    download_and_unzip(nltk_url, "nltk_data.zip", sys.prefix)
    download_and_extract_tar_gz(pyopenjtalk_url, "open_jtalk_dic_utf_8-1.11.tar.gz", os.path.dirname(pyopenjtalk.__file__))

if __name__ == "__main__":
    main()