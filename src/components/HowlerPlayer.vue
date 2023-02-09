<template>
  <button
    @click="playAudio()"
    class="bg-white hover:bg-gray-100 text-gray-800 font-semibold py-2 px-4 border border-gray-400 rounded shadow"
  >
    Click to play
  </button>
</template>

<script>
  import { Howl } from 'howler';
  export default {
    name: "HowlerPlayer",
    data() {
      return {};
    },
    methods: {
      playAudio: function () {
        var sound = new Howl({
          src: ["/src/assets/gigi.mp3"]
        });
        sound.play();
      }
    }
  };
</script>

<style></style>
