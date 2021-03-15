## ProxySite (PET PROJECT)
##### Project for parsing fresh Socks 4,5 proxies and uploading to your own online server (VPS, VDS)
#### Technology stack:
- Django RESTframework (Backend)
- Vue.js (Frontend) - RESTful
- Postgres
- Nginx 
- Docker-compose(for one command RUN)

#### Functional:
- Multi-threading parse and check ~2000 good proxies with ping to Google and Yandex
- Filtering by SOCKS5, SOCKS4
- Download TXT-file with proxy


![](https://raw.githubusercontent.com/a6m5zero/ProxySite/master/Screenshoot.png)

### HOW TO RUN
1. Install docker and docker-compose to your system.
2. Clone this repo
3. Go to proxysite/backend/
4. Run docker-compose.prod.yml file 
`sudo docker-compose -f docker-compose.prod.yml up --build`
`sudo docker-compose -f docker-compose.prod.yml exec backend python manage.py migrate`
`sudo docker-compose -f docker-compose.prod.yml exec backend python manage.py collectstatic`
5. Go to localhost:80

### SETTINGS
Proxy update time
*EDIT FILE /backend/proxyscraper/crontab
*Default every 5 minutes:
`*/5 * * * *`
Every 30 minutes, etc:
`*/30 * * * *`