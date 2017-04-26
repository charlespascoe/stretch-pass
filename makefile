PUBLISH=python3 setup.py sdist upload --sign

setup:
	pip3 install -r requirements.txt

publish:
	${PUBLISH}

publish-test:
	${PUBLISH} -r pypitest

clean:
	rm -rf dist/ stretch_pass.egg-info/
