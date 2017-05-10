unalias d
alias d="docker $@"
alias dc="docker-compose $@"

docker-sa(){
	export DOCKER_HOST=tcp://docker-sa.avenuecode.com:2376
	export DOCKER_TLS_VERIFY=1
	export DOCKER_CERT_PATH=/Users/bvale/.docker/docker-sa.avenuecode.com
}

site-release(){
	export DOCKER_HOST=tcp://site-release.avenuecode.com:2376
	export DOCKER_TLS_VERIFY=1
	export DOCKER_CERT_PATH=/Users/bvale/.docker/site-release.avenuecode.com
}

dhost(){
	if [ "$1" = "local" ]; then
		unset DOCKER_HOST
		unset DOCKER_TLS_VERIFY
		unset DOCKER_CERT_PATH
	fi
	for site in $(ls ~/.docker/); do
		echo "Site: $site"
	done
}
