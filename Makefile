APP_NAME=pgmoreno
STACK_FILE=stack.yml

build:
	docker build -t pgmoreno:lates.

deploy:
	docker stack deploy --with-registry-auth -c stack.yml quinto

rm:
	docker stack rm quinto