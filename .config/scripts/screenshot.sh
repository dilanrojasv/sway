#!/bin/bash
FILENAME="screenshot-`date +%F-%T`"
grim -g "$(slurp)" ~/Imágenes/Capturas\ de\ pantalla/$FILENAME.png
