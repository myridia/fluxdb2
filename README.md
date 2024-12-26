# python script to access fluxdb

## Install fluxdb example and setup python 
```
git clone https://github.com/veto8/fluxdb2.git
cd fluxdb2
python3.12 -m venv env 
. env/bin/activate
pip install pip --upgrade
pip install -r requirements.txt 
```


## Run the Docker via a docker-compose file

The command will run a docker compose file.
* Download the latest influxdb images
* Create an docker influxdb  with name myridia_influxdb 
* It will init the Db with default settings
* user: admin
* password: passpass
* org: test
* bucket: rate
* token: ****

```bash
docker-compose up -d
```

## Test import/write data with
```
 python enter.py
```

## After test read the data with
```
 python get.py
```





