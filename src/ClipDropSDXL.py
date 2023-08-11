import argparse
import base64
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--headless', action='store_true', help='Run Browser in headless mode')
    parser.add_argument('--style', default='shrink-0', help='Style option')
    parser.add_argument('--prompt', help='Prompt to send to Clipdrop', required=True, type=str)
    parser.add_argument('--output-dir', help='Output Directory', type=str, default=os.getcwd()+"/outputs")
    parser.add_argument('--browser', default='firefox', help='Browser to use (default: firefox)')
    args = parser.parse_args()


    if args.browser.lower() in ['chrome', 'chromium']:
        options = ChromeOptions()
    elif args.browser.lower() == 'firefox':
        options = FirefoxOptions()
    else:
        raise ValueError("Invalid browser option. Supported options are 'chrome' and 'firefox'.")

    argstyle = args.style.replace("3dmodel", "dmodel")
    styles = ["shrink-0", "anime", "photographic", "digitalart", "comicbook", "fantasyart", "analogfilm", "neonpunk", "isometric", "lowpoly", "origami", "lineart", "cinematic", "dmodel", "pixelart"]
    if argstyle not in styles:
        raise ValueError("Invalid Style option, valid styles are:\nanime\nphotographic\ndigitalart\ncomicbook\nfantasyart\nanalogfilm\nneonpunk\nisometric\nlowpoly\norigami\nlineart\ncinematic\n(3)dmodel\npixelart")

    options.headless = args.headless

    if args.browser.lower() == 'chrome':
        driver = webdriver.Chrome(options=options)
    else:
        driver = webdriver.Firefox(options=options)


    driver.get("https://clipdrop.co/stable-diffusion")

    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.termly-styles-module-root-f61419:nth-child(3)"))).click()

    input_prompt = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "prompt")))
    input_prompt.click()

    input_prompt.send_keys(args.prompt)

    WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.bg-primary-500:nth-child(2)"))).click()

    style = args.style

    WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CLASS_NAME, style))).click()

    WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".hover\\3A bg-primary-400:nth-child(2)"))).click()

    def get_file_content_chrome(driver, uri):
        result = driver.execute_async_script("""
            var uri = arguments[0];
            var callback = arguments[1];
            var toBase64 = function(buffer){for(var r,n=new Uint8Array(buffer),t=n.length,a=new Uint8Array(4*Math.ceil(t/3)),i=new Uint8Array(64),o=0,c=0;64>c;++c)i[c]="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/".charCodeAt(c);for(c=0;t-t%3>c;c+=3,o+=4)r=n[c]<<16|n[c+1]<<8|n[c+2],a[o]=i[r>>18],a[o+1]=i[r>>12&63],a[o+2]=i[r>>6&63],a[o+3]=i[63&r];return t%3===1?(r=n[t-1],a[o]=i[r>>2],a[o+1]=i[r<<4&63],a[o+2]=61,a[o+3]=61):t%3===2&&(r=(n[t-2]<<8)+n[t-1],a[o]=i[r>>10],a[o+1]=i[r>>4&63],a[o+2]=i[r<<2&63],a[o+3]=61),new TextDecoder("ascii").decode(a)};
            var xhr = new XMLHttpRequest();
            xhr.responseType = 'arraybuffer';
            xhr.onload = function(){ callback(toBase64(xhr.response)) };
            xhr.onerror = function(){ callback(xhr.status) };
            xhr.open('GET', uri);
            xhr.send();
        """, uri)
        if type(result) == int:
            raise Exception("Request failed with status %s" % result)
        return base64.b64decode(result)


    output_dir = args.output_dir
    os.makedirs(output_dir, exist_ok=True)

    image_elements = [WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button.absolute:nth-child(1) > img:nth-child(1)"))),
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button.absolute:nth-child(2) > img:nth-child(1)"))),
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button.absolute:nth-child(3) > img:nth-child(1)"))),
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button.absolute:nth-child(4) > img:nth-child(1)")))]

    for i, image_element in enumerate(image_elements):
        image_url = image_element.get_attribute('src')
        bytes = get_file_content_chrome(driver, image_url)
        file_name = f"{i}.jpg"
        file_path = os.path.join(output_dir, file_name)

        if os.path.exists(file_path):
            # Find the next available number
            count = 1
            while os.path.exists(os.path.join(output_dir, f"{i + count}.jpg")):
                count += 1
            file_name = f"{i + count}.jpg"
            file_path = os.path.join(output_dir, file_name)

        with open(file_path, 'wb') as file:
            file.write(bytes)

    driver.quit()

if __name__ == "__main__":
    main()