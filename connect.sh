#!/bin/bash

if [ $# -lt 2 ]
then
	echo "Usage: ./connect {user} {database} [password]"
	exit 0
	fi

PASSWORD=""
USER=$1
DATABASE=$2

if [ $# -eq 3 ]
then
	PASSWORD="-password $3"
	fi

COMMAND="influx -username $USER $PASSWORD -database $DATABASE"
eval $COMMAND
