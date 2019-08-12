#!/bin/bash

# png logo
inkscape -z -e logo.png -w 512 -h 512 logo.svg

# favicon
convert -background none logo.svg -define icon:auto-resize ../../public/favicon.ico
