#/bin/bash
git add . && git commit -m "Regular update ($(date +"%Y%m%d%H%M%S%N"))" && git push
exit $?
