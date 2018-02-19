[![Stories in Ready](https://badge.waffle.io/Seolhun/classico-project.png?label=ready&title=Ready)](https://waffle.io/Seolhun/classico-project?utm_source=badge)
# classico-project(Will be updated, Not working exactly now)
> 'Classico', Big data proejct using Python 3.6 and Vue JS 2

## Environment
- Production Server
    - GCP(Google Cloud Platform)
- Version Controll
    - Git-Flow
- CI & CD
    - Circle CI
    - Docker
- Project Manager
    - Waffle
    - Slack
- IDE
    - IntelliJ
- Back-end
    - Back-end Language : Python 3.6
    - Back-end Framework : Django 1.11, Flask 0.12.1
- Front-end
    - Front-end : Vue JS

### Member
- Back-end(Python), Infra : SeolHun
- Front-end : SeolHun

### History
- Start : 2017-05-04
- GCP setting : 2017-07-14

### Function
`Crawling`, `Searching`, `Caching`, `Security`, `User Managing`, `NLP`

---
## Installation : Backend(Classico)
    `Backend build REST API Server using Flask 1.11. That will perform dealing with request from client, producing data from MongoDB, Redis using GraphQL.`

### Pre-requirement
`Python3.6`, `Django 1.11`, Flask 0.12.1, MariaDB, MongoDB

### How to run?
* First, You must be installed pre-requirement that I wrote.

* `pip install -r requirements.txt` is download all packages
* `python app.py` is starting local server `localhost:5000`

### Environment
- OS : Ubuntu 16.04
- Docker : Docker Compose

---
## Installation : Frontend

### Pre-requirement

`nodeJs`, `npm`, `Vue JS 2 cli`

### How to run?

in the dev environment
* `npm install` is download all modules
* `npm start` is starting local server `localhost:3000`
* `npm run watch` is watching css, scss in project folder

in the production environment
* `npm run build` is building cmd, it will automatically make a build file in build folder
* copy this build folder to front-end server

- if you want to run in production with nodejs

```
npm install -g serve
serve -s build
```

### Environment
- OS : just need nodejs and npm.
