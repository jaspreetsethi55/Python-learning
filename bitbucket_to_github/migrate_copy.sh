#!/bin/bash

name_of_github_org="barcoemu"
#name_of_github_org="barcotestemu"
TEAM="Nexxis-Care"
#TEAM="GH-Users"

while IFS="" read -r p || [ -n "$p" ]
do
  git clone --mirror $p
  repo=`echo $p |cut -d'/' -f6`
  
  echo "Local repo created: $repo"

  cd ${repo}

  repo=`echo $repo|cut -d'.' -f1`

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

  gh repo create ${name_of_github_org}/${gh_repo} --private --team $TEAM
  #gh repo create ${name_of_github_org}/${gh_repo} --private
  git remote set-url origin https://jasset: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@github.com/${name_of_github_org}/${gh_repo}

  git remote add bitbucket $p
  git push origin --mirror
done < test_repos.txt
#done < remaining_repos.txt

#git clone --mirror {bitbucket-repo-clone-url}
#cd repo
#git remote set-url origin https://github.com/{name-of-github-org}/{repo-name-on-github}
#git remote add bitbucket {bitbucket-repo-clone-url}
#git push origin --mirror
