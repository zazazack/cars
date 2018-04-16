.PHONY: build deploy clean test release

help:
	@echo "build	run the build script"
	@echo "clean	rm build files"
	@echo "deploy deploy scrapy project to scrapyd"
	@echo "test 	run tests"
	@help "release update the version number"

build:
	scrapyd-deploy

clean:
	rm -r build project.egg-info project dbs

deploy:
	scrapyd-deploy -p project

release:
	bumpversion release

test:
	pytest
