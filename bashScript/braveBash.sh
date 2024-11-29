#! /bin/bash

source braveEnv/bin/activate
python3 Desktop/pythonScripts/braveScript.py &

flatpak run info.puredata.Pd Desktop/pdPatches/bravePatch.pd

