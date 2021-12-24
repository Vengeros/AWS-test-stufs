SHELL := /bin/bash


install-serverless-local:
	curl -o- -L https://slss.io/install | bash || npm install -g serverless
	npm install

deploy-local:
	serverless deploy
