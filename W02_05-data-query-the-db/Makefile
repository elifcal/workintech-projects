default: pylint pytest

pylint:
	find . -iname "*.py" -not -path "./tests/*" | xargs -n1 -I {}  pylint --output-format=colorized {}; true

pytest:
	@if [ ! -e data/school.sqlite ]; then \
		curl -s https://wagon-public-datasets.s3.amazonaws.com/sql_databases/ecommerce.sqlite > data/ecommerce.sqlite; \
	fi
	PYTHONDONTWRITEBYTECODE=1 pytest -v --color=yes
