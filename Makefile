test:

setup: setup_pygments

setup_pygments:
	$(VIRTUALENV) -p $(PYTHON) .env
	.env/bin/pip install hg+https://bitbucket.org/birkenfeld/pygments-main@121c75491e0d
