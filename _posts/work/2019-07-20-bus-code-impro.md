---
layout: post
title: "Business Code - BCD Ui - Repo impr"
excerpt: "Interview prep & questions"
categories: work
tags: [ work ]
date: 2019-07-20T08:08:50-04:00

---

#### Question

* BCD-UI - mobile video missing file

* schema files sent over http : move to https

* Last update to docs shows - 2017. Needs update

* How to bundle BCD-UI as standard - apache library rep hosting

* No Test cases ? Run SonarQube scanner ?
  * gradle build option
    * bcduiBuildBin
    * bcduiBuildDoc
    * bcduiClean
    * bcduiClean3rdParty
    * bcduiClientEcma50ne2One ?
    * bcdUIxxxxCollect3rdPartyJars


#### Improvements

* Add SonarQube plugin to Grade
  * find all code smells
  * Write UT's for APIs
      * Nobody will use code, if test cases are not available
      * Dangerous to use non-tested code, will lead to long term support issues

* Lite Version
  * 3rd party binary downloads ? nodejs security issues
  * Live demo version site
  * doc update sample project to test binaries

* JDK 12 container optimised deployment
  * move to alpine linux - saves AWS cloud costs
  * jenkins docker CI/CD for clean builds

* Security
  * xml schemas move to https, currently served via http

* Container
  * docker build for plug & play for API developer to use codebase/libraries
  

* improvements
  * OpenJDK - linux compliance with BCD-UI
  * CI/CD + SonarQube integration
  * Test case suite

* TODO
  * Fork the repo
  * Send pull request
