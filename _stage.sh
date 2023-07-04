#!/bin/bash

# used to test if installing with pipx works
# stage is, very much so, a bad name for this script

poetry build
pipx install dist/$(ls dist | grep .whl)
~/.local/bin/ksliln                 # does this work on linux?
pipx uninstall ksliln