#!/bin/bash
cd `dirname $0`
cd dist/pyserial-3.2.1
python3.7 setup.py install
cd ../roboid-1.5.2
python3.7 setup.py install
