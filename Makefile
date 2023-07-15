.PHONY: test

format:
	black .
	isort .

watering_test:
	PYTHONPATH=. pytest -m "watering"
