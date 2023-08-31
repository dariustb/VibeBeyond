---
layout: default
title: FAQ
permalink: /faq
has_children: false
has_toc: false
nav_order: 4
---

# FAQ & Common Issues
Not too many people asking questions here.

## Empty asset folders found!
### Problem
When running the app for the first time, the app doesn't run. Instead, a line is printed into your stdout before the app exits:
```sh
    Empty asset folders found:
        (some list of folder names/directories)
    Go to https://dariustb.github.io/VibeBeyond/faq for more information
```

### Reason
![It's too much gif](https://media2.giphy.com/media/25pONnxiVNYbLJWO41/giphy.gif?cid=ecf05e47o4f2cajgxd71tfhhbaf7lx2hxvakpbwbdalui5jn&rid=giphy.gif&ct=g)

Between the large file sizes & likely copyright issues from distributing soundfont files as open source, I'm not adding them into this repo. Sorry!

### Solution
What you can do to have this project work locally is to create these folders and populate them with the information below

| Folder | Location | What to Populate | Valid Filetypes |
|--------|----------|------------------|-----------------|
|Keys|`src/assets/sf2/`|Soundfonts to produce chord progressions|`.sf2`|
|Lead|`src/assets/sf2/`|Soundfonts to produce melodies|`.sf2`|
|Kick|`src/assets/drums/kicks/`|Samples of kick/bass drums|`.wav`|
|Hat|`src/assets/drums/hat/`|Samples of closed hi-hats|`.wav`|
|Snare|`src/assets/drums/snare/`|Samples of snares/rimshots|`.wav`|

This will pass validation, and allow proper generation of songs. The more files, the higher variety of song results.

For best results, use sub-1-second samples for the kick/hat/snare.
