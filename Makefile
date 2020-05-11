run:
	docker-compose run --rm app python main.py

flush:
	docker-compose down -v --rmi all
