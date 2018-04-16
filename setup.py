# Automatically created by: scrapyd-deploy

from setuptools import find_packages, setup

setup(
    name='app',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    packages=find_packages(),
    entry_points={'scrapy': ['settings = app.settings']},
)
