+++
categories = ["site"]
date = "2016-05-08T08:48:39-07:00"
description = "Migrating to Hugo"
draft = false 
series = ["Migrating to Hugo"]
tags = ["hugo", "golang", "hakyll", "blogger"]
title = "Migrating to Hugo - Part I"
subtitle = "Finding a Home"
+++

Over the years I've tried a number of blogging services, but only Wordpress
and Blogger with any seriousness.  Roughly a year ago I made 
the decision to try a few static site generators.  In hindsight, this proved
to be a bold decision.  This post will chronicle some aspects
of this journey.

<!--more-->

# History

## Dawn 

I take a relatively optimistic view of the Web, particularly as a vehicle
for information.  When I was exposed to it for the first time many years ago
I did what many technically inclined individuals did: create ugly websites
using pure HTML.  Some of these were more niche than others, but usually
the batch contained some version of a personal home page for yours truly.

Wordcraft, digital archives, and content ownership are all long-standing
interests of mine, whence my desire to create an online journal that I 
had some measure of control over.  Since my writing often includes a
fair bit of mathematics, my needs are not necessarily served by 
existing solutions such as [Medium](https://medium.com).


## Wordpress and Blogger 

One of my favorite mathematicians, [Terry Tao](https://terrytao.wordpress.com)
writes a popular blog on research mathematics.  It is powered by Wordpress,
so when I decided to write about more math related topics, I first tried
Wordpress.  I found its rendering of $\LaTeX$ to be poor, and quickly ditched
it in favor of Google's Blogger around 2012.

After spending some time configuring [MathJax](https://www.mathjax.org)
to work with Blogger, I had a functional but already dated looking site.
While my experience with Blogger proved satisfactory, the editing process
itself was not to my liking.  Indeed, at the time many Google products had
somewhat arcane user interfaces.  Moreover, I wanted my writing to be in
a more portable format.  Enter the static site generators.


# Static Site Generators

A static site generator typically takes content written in a minimally
stylized format (such as Markdown) and produces a collection of
organized HTML files that consitute the site.  The site is static, in that
pages are not dynamically generated when someone visits.  

To say that there are many static site generators is a bit of an
understatement.  One of the most popular is [Jekyll](http://jekyllrb.com),
written in Ruby.  It's tight integration with 
[GitHub Pages](https://pages.github.com) makes it extremely popular.

## Hakyll

The first static site generator I explored in any depth was
[Hakyll](https://jaspervdj.be/hakyll/), partially because it served
as an excuse to learn some Haskell.  By utilizing the DSL provided by
Hakyll, you effectively create your own static site generator.  Since
Hakyll uses the Haskell document converter
[Pandoc](http://pandoc.org), which handles $\LaTeX$ in markdown fairly well,
I was eager to try it out.  After looking for inspiration from a few
Hakyll-generated sites, I ended up with a basic setup that automatically
deployed itself with [CircleCI](https://circleci.com).  

## Hugo

Shortly after getting a basic Hakyll site with MathJax support up and running,
I decided to check out [Hugo](https://gohugo.io), written in Go.
My desire was partly sparked by the fact that at this point much of my
work-related programming was in Go.  With Hugo it is easy to initialize
a basic site and apply themes.  The chance to easily apply nice looking
themes intrigued me, so I spent some time fiddling with a Hugo
configuration for my site.


# Theming

Since I need my site to support MathJax, many of the pre-built themes for
Hugo did not really fit my needs.  Moreover, my personality is such that
I like to tinker and configure, perhaps to the point of distraction.  I
ended up investing a considerable amount of time creating the
Hugo [Morphism](https://github.com/shawnohare/hugo-morphism) theme
that, despite the work, produces a very minimalist blog.

The maintenance costs associated with personalized configurations and projects
are very real.  These costs are exacerbated further by the fact that I
am not, nor pretend to be, very adept at web development.  Fortunatelly,
Hugo lets you do quite a bit with a little CSS, and HTML has come a long way
since the days of my first site. 

# Conclusion

So here we stand today.  A statically generated site powered by a pretty
good site generator and a custom theme.  Much of the time I would
have otherwise spent writing I have spent creating the Morphism theme.
I suspect it is relatively stable, but this depends somewhat on my
desire to try new Hugo features.  In any case, I hope to write anew
with a greater frequency.

