tasks:
	docker-compose -f docker-compose.tasks.yml up --build
task1:
	docker-compose -f docker-compose.tasks.yml run task-1 --build
task2:
	docker-compose -f docker-compose.tasks.yml run task-2 --build

http:
	docker-compose -f docker-compose.yml up --build
