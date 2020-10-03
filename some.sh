#!/bin/bash
echo "({\"visitors\" : \"$(netstat -ntu | grep :8080 | grep -v LISTEN | awk '{print $5}' | cut -d: -f1 | sort | uniq -c | sort -rn | grep -v 127.0.0.1 | wc -l)\"}"






