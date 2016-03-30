SHELL=/bin/bash

.PHONY: all deploy provision reload-nginx

all:
	@echo Run \`make deploy\` to deploy to staging.

deploy:
	ansible-playbook -i ansible/staging ansible/deploy.yaml --ask-become-pass --ask-vault-pass

provision:
	ansible-playbook -i ansible/staging ansible/site.yaml --ask-become-pass --ask-vault-pass

reload-nginx:
	ansible -i ansible/staging webservers -m service -a "name=nginx state=reloaded" --ask-become-pass --ask-vault-pass
