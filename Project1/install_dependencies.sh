#!/bin/bash

echo 'Updating pip...'
pip install --upgrade pip

echo 'Installing requests package...'
pip install beautifulsoup4 requests

echo 'Installing packages from requirements.txt...'
pip install -r requirements.txt

echo 'Installation complete.'
