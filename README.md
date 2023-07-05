
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
**Available styles:** <br>`anime`, `photographic`, `digitalart`, `comicbook`, `fantasyart`, `analogfilm`, `neonpunk`, `isometric`, `lowpoly`, `origami`, `lineart`, `cinematic`, `(3)dmodel`, `pixelart`

## Usage Examples


**NEONPUNK**
```
python3 -m ClipDropSDXL --headless --prompt "golden retriever" --style neonpunk
```
![10](https://github.com/fredi-python/ClipDropSDXL/assets/83492589/84e5c0d7-2d73-447d-9b89-809b94c66376)




**ANIME**
```
python3 -m ClipDropSDXL --headless --prompt "golden retriever" --style anime
```
![4](https://github.com/fredi-python/ClipDropSDXL/assets/83492589/f668675d-6d61-4a34-91f6-88ae618761da)

**PHOTOGRAPHIC**
```
python3 -m ClipDropSDXL --headless --prompt "golden retriever" --style photographic
```
![18](https://github.com/fredi-python/ClipDropSDXL/assets/83492589/62464108-a99d-4e77-8dce-c31d1f026948)


**LOWPOLY**
```
python3 -m ClipDropSDXL --headless --prompt "golden retriever" --style lowpoly
```
![13](https://github.com/fredi-python/ClipDropSDXL/assets/83492589/d5951054-14c1-48e5-84be-973e64cf889f)

**ORIGAMI**
```
python3 -m ClipDropSDXL --headless --prompt "golden retriever" --style origami
```
![20](https://github.com/fredi-python/ClipDropSDXL/assets/83492589/bf3eb88a-a3c2-4393-8d3c-caed595874ef)

**COMICBOOK**
```
python3 -m ClipDropSDXL --headless --prompt "golden retriever" --style comicbook
```
![30](https://github.com/fredi-python/ClipDropSDXL/assets/83492589/14eb55a2-86f2-43df-b10b-5f9c35479cbc)

**LINEART**
```
python3 -m ClipDropSDXL --headless --prompt "golden retriever" --style lineart
```

![35](https://github.com/fredi-python/ClipDropSDXL/assets/83492589/bdf2af18-d378-4b6b-87db-223da7a337e9)

