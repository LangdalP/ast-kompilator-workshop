#! /usr/bin/env bash

antlr -Dlanguage=Python3 -no-listener -visitor Math.g4

rm *.interp
rm *.tokens
