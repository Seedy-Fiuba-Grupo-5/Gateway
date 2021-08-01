#!/bin/sh
docker-compose exec test pytest "dev/tests" -p no:warnings
