TASK=docker-compose.task.yml
API=docker-compose.yml
API_TEST=docker-compose.test.yml

tasks:
	docker-compose -f ${TASK} up --build
task1:
	docker-compose -f ${TASK} run task-1 --build
task2:
	docker-compose -f ${TASK} run task-2 --build

api:
	docker-compose -f ${API} up --build
api-test:
	docker-compose -f ${API_TEST} up --build
