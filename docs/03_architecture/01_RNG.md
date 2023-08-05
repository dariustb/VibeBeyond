---
layout: default
title: RNG
permalink: /architecture/rng
has_children: false
has_toc: false
nav_order: 1
parent: Architecture
---

# How the RNG works

Lo-fi hip hop songs include elements of music that come together to make a cohesive work. We used RNG here to make those combinations of songs organic, original, and high in variety. These are some of the elements that were randomly generated:

- [BPM (Beats per minute)](#bpm-beats-per-minute)
- [Time Signature](#time-signature)
- [Key / Key Signature](#key--key-signature)
- [Instruments for...](#instruments)
    - Keys & Synth
        - Melody / Lead
        - Chords
    - Drums
        - Kick
        - Snare
        - Hat
- [Chord Progression](#chord-progression)
- [Drum pattern](#drum-pattern)
- [Song title](#song-title)

## BPM (Beats per minute)
The tempo is kept in a range that's good for lo-fi hip-hop beats. Between *andante* and *andantino*.

## Time Signature
4/4 is the current time, though we may expand to 6/8 and other signatures in the future.

## Key / Key Signature
All keys are used in this selection. See [this page about valid midi keys notations](#) for more info on its implementation

## Instruments
All the SF2 files are gathered into a folder and selected at random for the lead and the chords. The drum one-shots are stored separately and chosen through the same method.

## Chord Progression
Chords are written in Roman numeric notation. In the key of *C*, a notation of "bVI7" would mean the 6th scale degree (*VI*) lowered by half a step (*b* meaning the flat symbol, ♭) played as a major (*VI* is uppercase -- *vi* would mean a minor chord) dominant 7th chord (*7*). If the key is *C*, the "bVI7" is an `A♭7` chord. 

![A♭7 Chord](https://www.pianochord.org/images/a_flat_7.png)

Chords were decided and pre-written beforehand. The RNG chooses which chord progression to play and base the melody on. The chord itself is based on the key and used in Roman numeric notation for portability across any single key. ii-V-I will always be a 2-5-1 progression in any key

## Drum pattern
As of right now the drum pattern is hard-coded. Will need to debug timing issue then proceed into other drum rhythm ideas.

## Song title
At this point, it's just a random string generator. Will add a feature to create more realistic sounding names with real English words later.
