#!/usr/bin/env bash
set -euo pipefail

install_dir="${WV_INSTALL_DIR:-${HOME}/.local/workvault-maintenance}"
mkdir -p "$install_dir"
python3 -m venv "$install_dir/venv"
"$install_dir/venv/bin/python" -m pip install --upgrade pip
"$install_dir/venv/bin/python" -m pip install .
mkdir -p "${HOME}/.local/bin"
ln -sf "$install_dir/venv/bin/wv" "${HOME}/.local/bin/wv"
echo "Installed WorkVault Maintenance. Ensure ${HOME}/.local/bin is in PATH."
