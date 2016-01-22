from fabric.api import local

def prepare_deploy():
	local("./devm.py test apps")
	local("git add -p && git commit")
	local("git push")