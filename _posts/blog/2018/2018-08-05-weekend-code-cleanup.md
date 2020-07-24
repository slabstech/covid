---
layout: post
title: "Weekend Cleanup - Github repo"
excerpt: "Cleanup of Github repo to focus on active projects"
categories: blog
tags: [ research ]
image:
  feature:
date: 2018-08-05T08:08:50-04:00

---

Weekend Cleanup

-----
* Table of Contents
{:toc}

## Taking backup of All Repo
	This command clones all user's REPO to provided directory. Helps to take periodic backup.
	GHUSER=sachinsshetty; curl "https://api.github.com/users/$GHUSER/repos?per_page=1000" | grep -w clone_url | grep -o '[^"]\+://.\+.git' | xargs -L1 git clone

## Removed Unused Repo
	Removed few jekyll templates that are no longer being used. These repo was introduced to implement a static webcommerce. The project did not go further. 
	
## Updated bucketlist contents
	Now idea list contains dates and status.
	

