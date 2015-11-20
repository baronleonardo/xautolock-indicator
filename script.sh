#!/bin/bash

if [ $1 == "enable" ]; then
		xset +dpms

else
	xset -dpms
fi

xautolock -$1