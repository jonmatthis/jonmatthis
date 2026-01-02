.PHONY: dev build lab clean serve-dag

dev:
	uv run myst start --execute

build:
	uv run myst build --html

lab:
	uv run jupyter lab

clean:
	rm -rf _build .myst

# Serve the DAG visualization on port 8080 (run in separate terminal)
serve-dag:
	@echo "Serving DAG at http://localhost:8080/curriculum-dag.html"
	@cd _static && python3 -m http.server 8080
