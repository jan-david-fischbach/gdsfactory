sphinx:
	cd api && uv run sphinx-build -b myst . myst
	cd routing-api && uv run sphinx-build -b myst . myst

repair-plot-directive:
	uv run python repair_plot_directive.py

repair-code-blocks:
	uv run python repair_code_blocks.py

build: sphinx repair-plot-directive repair-code-blocks
	uv run myst build --execute
