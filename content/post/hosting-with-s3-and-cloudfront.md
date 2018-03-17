---
title: "Hosting With S3 and Cloudfront"
date: 2018-01-10T20:12:12-08:00
description: Hosting shawnohare.com using AWS S3 and CloudFront.
draft: true
math: true
toc:  false 
categories: []
groups: []
tags: []
series: []
markup: mmark
slug: a24bf28a-bb0b-4f11-97a6-fbd4f6bd2f55

---

As of this writing, S3-backed site distrubted via CloudFront do not easily
support default directory indexes the same way a standard S3 static site does.
Consequently, `https://example.com/path/to/page` will not automatically map to
`https://example.com/path/to/page/index.html`, which is where `hugo` and
similar site generators place a rendered page. 
