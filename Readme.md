# Check company by voen

### Installing
Clone repository

```
cd check-voen
virtualenv -p python3 envname
source ./envname/bin activate
pip install -r requirements.txt
flask run
```

Post voen to 127.0.0.1:5000/check-voen as json
```
{
	"voen": 111111
}
```
Response
```
{
  "message": "Belə ödəyici mövcud deyildir.",
  "status": 0
}
```