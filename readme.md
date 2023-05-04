# Finding piospheres (livestock concentration areas) in NAIP imagery

## Installation instructions

1. Install [Conda](http://conda.io/)

2. Create environment and install requirements

```bash
conda create -n cv4ecology python=3.8 -y
conda activate cv4ecology
pip install -r requirements.txt
```

3. Download dataset



## Reproduce results

1. Train

```bash
python piosfinder/train.py --config configs/exp_piosfinder.yaml
```

2. Test/inference
