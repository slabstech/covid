---
layout: post
title: "Deploying app to Heroku"
excerpt: "Steps to deploy app to heroku for js13kgames "
categories: projects
tags: [ projects ]

date: 2018-08-05T08:08:50-04:00

---

## Deploying App to Heroku

-----

```
1. Create a free account from [Heroku](https://www.heroku.com)
2. Follow steps from [Heroku Dev Center](https://devcenter.heroku.com/)
3. Below are steps to deploy a sample node-js application to heroku.  
4. Install heroku from [install](https://devcenter.heroku.com/articles/heroku-cli#download-and-install)
5. From CommandLine
  a.  heroku login
      Enter mailid and password  used for heroku login
  b. Check if node, npm and git are installed in local machine
      node --version
      npm --version
      git --version
  c. git clone https://github.com/heroku/node-js-getting-started.git
  d. cd node-js-getting-started
  e. heroku create
  f. git push heroku master
  g. To run a dyno
    heroku ps:scale web=1
  h. To view in browser
      heroku open
  i. To stop dyno
    heroku ps:scale web=0

4. To run locally
  a. npm install
  b. heroku local web

5. Heroku configuration for github project
  a. From heroku [dashboard](https://dashboard.heroku.com/) select create app
  b. Enter App Name
  c. Click "Create App" button"
  d. Go to project -> Deployment method -select github and enter github repo details
  e. Enable Automatic Deploys
  f. Manually deploy app first time

```
