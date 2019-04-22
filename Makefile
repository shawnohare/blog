.PHONY: deps

themes/hugo-morphism:
	git clone "https://github.com/shawnohare/hugo-morphism" "themes/hugo-morphism"

public:
	git clone "https://github.com/shawnohare/shawnohare.github.io" "public"

clean-public:
	find public ! -path "*git*" -delete

deps: themes/hugo-morphism public
