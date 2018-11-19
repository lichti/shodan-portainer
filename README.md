Responsible Disclosure

# Portainer - Check if admin already created by a public API endpoint

## PRODUCT DESCRIPTION

[PORTAINER](https://portainer.io) IS AN OPEN-SOURCE LIGHTWEIGHT MANAGEMENT UI WHICH ALLOWS YOU TO EASILY MANAGE YOUR DOCKER HOSTS OR SWARM CLUSTERS

## BACKGROUND

- Portainer until 1.19.2

## VULNERABILITY DETAILS

Portainer provides an API endpoint (/api/users/admin/check) to verify that the admin user is already created. This API endpoint will return 404 if admin was not created and 204 if it was already created. This "feature" allows anyone to receive unauthorized access on the host when the portainer is configured incorrectly.

## PROOF OF CONCEPT

Manual steps to reproduce the vulnerability:

```bash
git clone git@github.com:lichti/shodan-portainer.git
virtualenv --python python3 .venv
source .venv/bin/activate
pip install -r requirements.txt
export SHODAN_API_KEY=xxxxxxxxxxxxxxxxxxxxxxx
python portainer.py
```

If you has a paid plan, you can use a filters:

```bash
export SHODAN_FILTER = 'country:"BR"'
python portainer.py
```

Output example:

```txt
Country: US | ISP: Digital Ocean | http://142.x.y.158:9001/
Country: CA | ISP: Atlantic.net  | http://45.x.y.165:9000/
Error: skipping 206.x.y.63
```

## WORKAROUND

Forcing the admin password by extra parameter on portainer CLI - [configuration.html#admin-password](https://portainer.readthedocs.io/en/stable/configuration.html#admin-password). On source code [portainer.go#L13-L14](https://github.com/portainer/portainer/blob/develop/api/portainer.go#L13-L14).

## VULNERABILITY DISCLOSURE TIMELINE

**2018-11-19:** Vendor was contacted

## AUTHOR & REVISION

**Author:** Gustavo Lichti <gustavo.lichti@gmail.com>

**Revision:** 
