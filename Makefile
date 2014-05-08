VIRTUALENV=$(shell which virtualenv)
PYTHON=$(shell which python2)
PYGMENTS_REVISION=121c75491e0d

test:

setup: setup_pygments

setup_pygments:
	$(VIRTUALENV) -p $(PYTHON) .env
	.env/bin/pip install hg+https://bitbucket.org/birkenfeld/pygments-main@$(PYGMENTS_REVISION)
