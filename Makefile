install:
	pip install -r requirements.txt

run:
	python aim_practice.py

format:
	black aim_practice.py --line-length 79

lint:
	flake8 aim_practice.py
