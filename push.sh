#/bin/bash
git add . && git commit -m "Update $(date +"%Y%m%d%H%M%S%N")" && git push
exit $?
