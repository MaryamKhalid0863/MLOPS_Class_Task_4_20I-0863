install:
	pip install -r requirements.txt

run:
	python app.py

docker-build:
	docker build -t iris-flask-app .

docker-run:
	docker run -p 5000:5000 iris-flask-app
