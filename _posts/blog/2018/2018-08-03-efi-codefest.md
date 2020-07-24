---
layout: post
title: "CodeFEst @ EFI : 2018"
excerpt: "Brief commentary of tools usage during codefest"
categories: blog
tags: [ research ]
image:
  feature:
date: 2018-08-03T08:08:50-04:00
---

Codefest was looming in the weekend. Our plan was to build a git inspired Webbased workflow tool to annotate PDF files required for Approval.

My task was to find an appropriate PDF annnotation tool, which helps the parties to highlight corrections w/o losing changes that are frequently encountered while using emails.

Few online editors, do an amazing for annotation like smallpdf.com and sejda.com. They come with subscription based usage and also with issue of being in public access.

Next our search discovered OpenSource implementations. Our project was based on Java, which led to pdfjs-annotator. After fixing version dependancy, it had to be dropped as no support was available to start the project. Next option were a combination of two project which would fit right into our product. react-pdf-highlighter would capture metadata for highlighting and pdf-annotation-service would embed highlights into the pdf. These tools only provided text-highlighting which would require additional work. The future scope is to merge these projects into a single project and also solve CORS dependancy as were unable to access files from different url's. We finally integrated with sejda api. 

P.S : Update on the merge will be available in a few weeks
