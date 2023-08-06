---
layout: default
title: Architecture
permalink: /architecture
has_children: true
has_toc: true
nav_order: 3
---

# Backend Architecture

This page will explain how the *backend* code functions to create the music from the highest level on down.

## Highest Level

Vibe Beyond works in this process:
1. Create MIDI
1. Process MIDI into Audio
1. Create Drum Audio
1. Combine Audio into Song

### Create MIDI
The source code uses RNG and (hard-coded) music theory to create midi information (via [mido](https://mido.readthedocs.io/)) representing the chords/melody/rhythm/etc of the song.

### Process MIDI into Audio
The midi information is processed through acquired soundfonts (via [sf2-loader](https://pypi.org/project/sf2-loader/)) to create the individual instruments tracks as audio files.

### Create Drum Audio
Drums loops are created by using a pattern system with [AudioSegment](https://audiosegment.readthedocs.io/en/latest/audiosegment.html) on one-shot kick/hat/snare audio to make a tempo-flexible drum machine.

### Combine Audio into Song
The audio files are then combined to create a complete song.
