# ClipDropSDXL <img src="https://github.com/fredi-python/ClipDropSDXL/assets/83492589/b3d508ee-d810-4b8b-9d1b-87a4b84967a2" width="2.5%"></img>

Selenium Wrapper for ClipDrop: Unlocking High-Resolution Text-to-Image Creation with StableDiffusionXL (SDXL)
## Installation
```
python3 -m pip install --upgrade git+https://github.com/fredi-python/ClipDropSDXL.git
```
## Usage
```
$ python3 -m ClipDropSDXL --help
usage: ClipDropSDXL.py [-h] [--headless] [--style STYLE] --prompt PROMPT [--output-dir OUTPUT_DIR] [--browser BROWSER]

options:
  -h, --help            show this help message and exit
  --headless            Run Browser in headless mode
  --style STYLE         Style option, default: no style
  --prompt PROMPT       Prompt to send to Clipdrop
  --output-dir OUTPUT_DIR
                        Output Directory
  --browser BROWSER     Browser to use (default: chrome)
```
### Working with styles
**Available styles:** <br>`anime`, `photographic`, `digital-art`, `comic-book`, `fantasy-art`, `analog-film`, `neonpunk`, `isometric`, `lowpoly`, `origami`, `line-art`, `cinematic`, `3d-model`, `pixel-art`

## Usage Examples


**NEONPUNK**

```
python3 -m ClipDropSDXL --prompt 'Man in hoodie walking away from camera' --style neonpunk
```

![140](https://github.com/fredi-python/ClipDropSDXL/assets/83492589/a21abb9f-101b-4151-b35a-47fcbb40afb7)

```
python3 -m ClipDropSDXL --prompt 'stunning sunset over a calm beach with palm trees.' --style neonpunk
```
![118](https://github.com/fredi-python/ClipDropSDXL/assets/83492589/caa69965-ac40-4813-bbe2-abeb7b12dfb5)






**PHOTOGRAPHIC**

```
python3 -m ClipDropSDXL --prompt 'Car' --style photographic
```

![170](https://github.com/fredi-python/ClipDropSDXL/assets/83492589/be95eb54-6608-42cd-82fb-1e12f57bbceb)

```
python3 -m ClipDropSDXL --prompt 'landscape of a Japanese garden in autumn' --style photographic
```
![183](https://github.com/fredi-python/ClipDropSDXL/assets/83492589/3c833388-5b23-4194-9f0c-d3d46b53bf2f)

