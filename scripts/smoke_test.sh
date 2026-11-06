#! /usr/bin/env bash

IMAGE="${1:-tb:ci}"

function cleanup {
  echo -n "Cleaning up... "
  docker rm -f tb &> /dev/null
  echo "DONE!"
}

trap cleanup EXIT

docker run -d    \
  --name tb      \
  -v data0:/data \
  -p 5000:5000   \
  "$IMAGE" &> /dev/null

i=0
while [ $i -lt 5 ]
do
  ((i++))
  sleep 1
  if curl -sf -X GET -o /dev/null http://localhost:5000/api/tasks
  then
    echo "Attempt #${i}: SUCCESS!"
    exit 0
  fi
done

echo "FAILURE! (Total attempts: ${i})"
exit 1
