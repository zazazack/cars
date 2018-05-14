.PHONY: build deploy clean test release

help:
	@echo "build	run the build script"
	@echo "clean	rm build files"
	@echo "deploy deploy scrapy project to scrapyd"
	@echo "test 	run tests"
	@echo "release update the version number"

build:
	pipenv lock -r requirements.txt && docker-compose build

clean:
	@echo "Not implemented"

deploy:
	@echo "Not implemented"

release:
	bumpversion release

test:
	pytest
