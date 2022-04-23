```
docker-compose -f docker-compose.test.yml build
docker-compose -f docker-compose.test.yml run web python3 -m manage makemigrations
docker-compose -f docker-compose.test.yml run web python3 -m manage migrate
docker-compose -f docker-compose.test.yml run web python3 -m manage test
docker-compose -f docker-compose.test.yml down
```
