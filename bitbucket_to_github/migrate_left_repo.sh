#!/bin/bash

name_of_github_org="barcoemu"
#name_of_github_org="barcotestemu"
TEAM="Nexxis-Care"
#TEAM="GH-Users"
mycwd=`pwd`
while IFS="" read -r p || [ -n "$p" ]
do
  cd $mycwd
  git clone --mirror $p
  repo=`echo $p |cut -d'/' -f6`
  
  echo "Local repo created: $repo"

  cd ${repo}

  repo=`echo $repo|cut -d'.' -f1`

  gh_repo="dior-${repo}"

  #gh repo create ${name_of_github_org}/${gh_repo} --private --team $TEAM
  gh repo create ${name_of_github_org}/${gh_repo} --private
  git remote set-url origin https://jasset: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@github.com/${name_of_github_org}/${gh_repo}

  git remote add bitbucket $p
  git push origin --mirror
done < left_dior_repos.txt

#done < remaining_repos.txt

#git clone --mirror {bitbucket-repo-clone-url}
#cd repo
#git remote set-url origin https://github.com/{name-of-github-org}/{repo-name-on-github}
#git remote add bitbucket {bitbucket-repo-clone-url}
#git push origin --mirror
