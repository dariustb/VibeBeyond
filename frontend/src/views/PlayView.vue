<script>
import DateTime from "../components/DateTime.vue";
import { Howl } from "howler";

export default {
  data() {
    return {
    };
  },
  methods: {
    // Plays soundfile using howlerJS
    playAudio: function () {
      var sound = new Howl({
        src: ["/src/assets/gigi.mp3"],
      });
      sound.play();
    },
  },
  components: {
    DateTime
  },
}
</script>

<template>
  <main>
    <!-- White corners -->
    <div>
      <div id="line-vert" class="absolute left-5 top-5"></div>
      <div id="line-horz" class="absolute left-5 top-5"></div>

      <div id="line-vert" class="absolute right-5 top-5"></div>
      <div id="line-horz" class="absolute right-5 top-5"></div>

      <div id="line-vert" class="absolute left-5 bottom-5"></div>
      <div id="line-horz" class="absolute left-5 bottom-5"></div>

      <div id="line-vert" class="absolute right-5 bottom-5"></div>
      <div id="line-horz" class="absolute right-5 bottom-5"></div>
    </div>
  
    <!-- TL: Play and Volume -->
    <div
      class="absolute left-9 top-9 text-xs opacity-50 font-semibold drop-shadow-[0_4px_4px_rgba(0,0,0,0.25)]"
    >
      <p>PLAY ▶<br />VOL IIIIIIII</p>
    </div>
  
    <!-- TR: Now Playing, Song title, Artist name -->
    <div
      class="absolute right-9 top-9 text-right drop-shadow-[0_4px_4px_rgba(0,0,0,0.25)]"
    >
      <p class="text-xs opacity-50 font-semibold">NOW PLAYING</p>
      <p id="song-name" class="text-[22px]">Dancing Droplets</p>
      <p id="artist-name" class="text-[22px] font-semibold">Leavv</p>
    </div>

    <!-- BL: Current Time & Date -->
    <div
      class="absolute left-9 bottom-9 text-xs opacity-50 font-semibold drop-shadow-[0_4px_4px_rgba(0,0,0,0.25)]"
    >
      <DateTime></DateTime>
    </div>

    <!-- BR: Time on song -->
    <div
      class="absolute right-9 bottom-9 text-xs opacity-50 font-semibold drop-shadow-[0_4px_4px_rgba(0,0,0,0.25)]"
    >
      <p id="play-time">0:00 / 3:14</p>
    </div>
  </main>
</template>