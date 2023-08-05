---
layout: default
title: Song Generation
permalink: /architecture/song-generation
has_children: false
has_toc: true
nav_order: 1
parent: Architecture
---

# How the Songs are Generated

Deeper dive into the music generating process.

*See [Backend Architecture](/docs/03_architecture/00_architecture.md) to view the highest level explanation.*

Each song is generated through this process:
1. [RNG the Puzzle Pieces](#rng-the-puzzle-pieces)
1. [Generate the Song Structure](#generate-the-song-structure)
1. [Generate the Chord Progression](#generate-the-chord-progression)
1. [Generate the Melody/Countermelody/Ambient](#generate-the-melodycountermelodyambient)
1. [Generate the Bassline](#generate-the-bassline)
1. [Generate the Drumloop](#generate-the-drumloop)
1. [Produce Audio tracks from MIDI](#produce-audio-tracks-from-midi)
1. [Combine the tracks](#combine-the-tracks)

## RNG the Puzzle Pieces
Use simple RNG to create values for these base song elements:
- BPM (beats per minute)
- Key
- Time Signature
- Instrument choices
    - Lead soundfont
    - Chord soundfont
    - Ambient soundfont
    - Bass soundfont
- Drumkit choices
    - Kick audio
    - Hat audio
    - Snare audio

## Generate the Song Structure
The song structure here is the pattern used of these different higher-level elements:
- Drums
- Bass
- Chords
- Melody
- Countermelody
- Ambient tones

These parts will be taken in and out of the song to give the song a sense of direction. Choosing early will allow us to make the song elements all at once and streamline the process a bit.

### Example
Here's a visual of how the song structure will work:

![Song structure visual](/docs/images/song_structure_example.png)
> Structure of lo-fi song, [*The Far Side*](https://www.youtube.com/watch?v=xocnshwEbrM&t=0s) by Comus

Each square represents the duration of a sigle chord progression (which we'll call a "loop"). The parts that are filled in are the actively played elements during that point in the song; empty squares are silent. This will be the basis of how the songs will work from beginning to end.

The structures are hard-coded because there's not much variety in lo-fi hip-hop, and people are probably not going to notice the difference anyway.

## Generate the Chord Progression
Chord progressions are chosen from a list and are implemented based on the song's key.

Chords are written in Roman numeric notation, functionally between "I" and "VII" including the accidental and chord type. This allows the progressions to be transposed into any key that's RNG'd.

### Example
Given the key is *C*, and the notation is "bVI7", here's how we'd find the chord in terms of the key:
 - (*VI*) - **VI** is Roman numeral for 6, so we'd base the root of our chord on the 6th scale degree of *C*, which is `A`.
 - (*b*) - **b** is an alpha representation of the flat symbol, ♭. This means the scale is lowered by half a step, so *A* is lowered into `A♭`
 - (*VI* is uppercase) - Uppercase means that the chord is major, and lowercase *vi* means the chord is minor. So we have an `A♭ major` chord
 - (*7*) - 7 directly after the chord here will mean the chord is a dominant chord (major chord with a ♭7). So we have an `A♭ Dominant 7th`

Key=*C* + Chord=*bVI7* = Chord is `A♭7`

![A♭7 Chord](https://www.pianochord.org/images/a_flat_7.png)
> A♭7 chord on piano

There's a collection of suitable chord progressions that are hard-coded into the program. This will make the generation process much easier than programming even more theory to build chord progressions from sctratch. Using **root position** only -- again, for simplicity. 

![Root Position](https://blog.flat.io/content/images/2016/10/first-and-second-inversion.png)
> Root position vs. 1st and 2nd inversion

The RNG chooses which chord progression to use for the song and the chords will be built based on the song's key.

## Generate the Melody/Countermelody/Ambient
These are functionally the same things -- just increasingly simpler in complexity, respectively. These are based on the chord progression of the song.

## Generate the Bassline
I'm just going to do root notes whenever I add this feature. Playing bass is hard :(

## Generate the Drumloop
My options at first were either:
- Use a soundfont for the drumkit
    - Probably will sound fake and unimpressive
- Use live drum loops and squash/stretch to tempo
    - May sound realer within a certain space around the original BPM, becoming more cartoony with larger distances in the BPM used.
    - This means way more loops are necessary to be comfortably within the tempo, and that means fewer options of drums per a tempo.

I found this great idea in between! We use a collection of one-shots for kicks, hats, and snares and build the beats based on the tempo. That way, there's the realism of the live drum sounds, the tempo versatility/variety of the midi drums, and less storage is used in comparison to the number of possible loop combinations that can be made.

This drum loop will mix & match different kick patterns, hat patterns, and snare patterns, between any of the randomly chosen kick/hat/snare sounds.

## Produce Audio tracks from MIDI
This is where the soundfonts come into play.

Every track (except drums tracks) will be created for the duration of a loop/chord progression. Then those loops are repeated muted & unmuted based on the [song structure](#generate-the-song-structure). Now we have the song length of each track.

The drums are similarly looped and created, without the MIDI component.

## Combine the tracks
Turning the tracks into one single audio file will give us the end product. 
