.PHONY: build deploy clean test release

help:
	@echo "build	run the build script"
	@echo "clean	rm build files"
	@echo "deploy	deploy scrapy project to scrapyd"

install:
	python -m pip install -r requirements.txt

clean:
	find . -name '__pycache__' -type d -name '*.pyc' -type f -exec -v -rf {} +
	rm -rf *_cache/ .eggs/ .scrapy/ .DS_Store

deploy:
	@echo "Not implemented"
