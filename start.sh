#!/bin/bash
if [ $INIT_DATABASE ];
then
    python setup.py;
fi
python run.py;