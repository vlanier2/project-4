#!/bin/bash

for t in tests/*.py
do
    nosetests --nologcapture $t
done
