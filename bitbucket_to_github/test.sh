#!/bin/bash 

repo="deploy-test"
#repo="nexxis-care-deploy"
#repo="nexxis-ml-deploy"
#repo="radian-nexxis-ml-deploy"
#repo="Nexxis-care-ml-deploy"

if [[ "$repo" =~ ^radian ]]
then
        gh_repo="nexxiscare-radiance-logstash-helm-enp-charts"
elif [[ "$repo" =~ ^Nexxis-care ]]
then
	gh_repo=`echo $repo|sed s/Nexxis-care/nexxiscare/`
elif [[ ! "$repo" =~ ^nexxis ]]
then
	gh_repo="nexxiscare-${repo}"
elif [[ "$repo" =~ ^nexxis-care ]]
then
	gh_repo=`echo $repo|sed s/nexxis-care/nexxiscare/`
elif [[ "$repo" =~ ^nexxis ]]
then
	gh_repo=`echo $repo|sed s/nexxis/nexxiscare/`
fi

echo $gh_repo
