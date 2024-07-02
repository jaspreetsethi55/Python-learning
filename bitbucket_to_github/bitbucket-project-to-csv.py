import sys
import requests
import json

def main():
    if len(sys.argv) != 3:
        print("Please provide exactly two arguments: token, bitbucket project")
        return
    else:
        token = sys.argv[1]
        project = sys.argv[2]
    
    baseurl = 'git.barco.com'
    headers = {'Authorization': f'Bearer {token}'}
    projectKey = project
    url = f'http://{baseurl}/rest/api/latest/projects/{projectKey}/repos'
    response = requests.get(f'{url}', headers=headers)
    json_data = json.loads(response.content)
    repositories = json_data["values"]
    result = []

    for repo in repositories:
        slug = repo["slug"]        
        for href in repo["links"]["clone"]:      
            if href['name'] == 'ssh':
                ssh_href = href['href']
                break
        print(ssh_href)
        result.append({"slug": slug, "ssh_href": ssh_href})

    with open('repos-from-' + project + '.csv', 'w') as csv:
        # headings: original_name ; link; readers_team; writers_team; admins_team; new_name; prefix; skip; archive
        csv.write("original_name;link;readers_team;writers_team;admins_team;new_name;prefix;skip;archive\n")
        for r in result:
            csv.write("{};{};;;;;;N;N\n".format(r["slug"], r["ssh_href"]))

if __name__ == "__main__":
    main()
