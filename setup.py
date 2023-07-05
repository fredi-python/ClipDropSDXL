# setup.py
from setuptools import setup, find_packages

setup(
    name='ClipDropSDXL',
    version='0.0.2',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'ClipDropSDXL = ClipDropSDXL.main:main'
        ]
    },
    install_requires=[
        "selenium>=4.8.0",
        "argparse"
    ],
    author='Your Name',
    author_email='fredi@mt-oneblock.net',
    py_modules=["ClipDropSDXL"],
    description='Selenium Wrapper for ClipDrop: Unlocking High-Resolution Text-to-Image Creation with Stable Diffusion XL (SDXL)',
    url='https://github.com/fredi-python/ClipDropSDXL',
)
