# SHODAN - Portainer 

## This script search at shodan for portainer poorly configured and vulnerable

## Author

- Gustavo Lichti
- gustavo.lichti@gmail.com


## Usage: 

```bash
virtualenv --python python3 .venv
source .venv/bin/activate
pip install -r requirements.txt
export SHODAN_API_KEY=xxxxxxxxxxxxxxxxxxxxxxx
python portainer.py 
```

## Output example:

```txt
Country: US | ISP: Digital Ocean | http://142.x.y.158:9001/
Country: CA | ISP: Atlantic.net | http://45.x.y.165:9000/
Error: skipping 206.x.y.63
```
