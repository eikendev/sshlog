#!/usr/bin/env bash

filename="$1"

if ! [ -f "$filename" ] ; then
	printf "Usage: %s <filename>\n" "$0" >&2
	exit 1
fi

# shellcheck disable=SC2016
rg \
	--no-config \
	--invert-match \
	'input_userauth_request' \
	| rg \
	--ignore-case \
	--no-config \
	--only-matching \
	--replace '$name' \
	'user (?P<name>\S+)' "$filename" \
	| sort \
	| uniq -c \
	| sort --ignore-leading-blanks --numeric-sort --reverse
