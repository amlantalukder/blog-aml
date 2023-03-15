install:
	# install commands
	pip install --upgrade pip &&\
	pip install -r requirements.txt
format:
	# format code
	black *.py templates/*.html
lint:
	# flake8 or pylint
	pylint --disable=R,C *.py
test:
	# test
deploy:
	# deploy
all: install lint test deploy