import os

from setuptools import setup

setup(
    name='ascii_image',
    version='1.0',
    description='Make any image file to ascii art format.',
    long_description=open(
        os.path.join(os.path.dirname(__file__), "README.md"),
        "r",
        encoding="utf-8"
    ).read(),
    url='https://github.com/Henry0526/ascii_image',
    author='Hao-Wei Li',
    author_email='henryliking@gmail.com',
    install_requires=["numpy", "pillow"],
    license='MIT',
    packages=['ascii_image'],
    zip_safe=False,
    keywords=['ASCII-art', "image", "ascii"],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)