# Image Downloader for [wallhaven.cc](https://wallhaven.cc)
#### Please don't misuse this to put pressure on the website
Havendl simply downloads images from wallhaven (with or without API key) and uses IPTC tags to save keywords of the image that are provided by wallhaven.

## Installation
This is a simple script. Just make sure you have `pyexiv2` installed. You can install it using `pip`:

```pip3 install pyexiv2```

I suggest you to create a symlink:

```ln -s path/to/main.py ~/.local/bin/havendl```

## Usage
See help:

```havendl --help```