.PHONY: run install

install:
	pip install fastapi uvicorn

run:
	python -c "import fastapi" 2>/dev/null || (echo "Run 'make install' first" && exit 1)
	uvicorn application_controller:app --reload