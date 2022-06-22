#!/bin/bash

filepath="$(pwd)"

function activate () {
	cd "$filepath"
	pwd
	python3.10 -m venv sierpinski-triangle-venv
	source sierpinski-triangle-venv/bin/activate
	python3.10 -m pip install --upgrade pip
	python3.10 -m pip install -r requirements.txt
}
activate
