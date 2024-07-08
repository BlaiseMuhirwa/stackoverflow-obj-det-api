
generate-api:
	openapi-generator generate \
		-i src/spec/api.yaml \
		-g python \
		-o src/api
