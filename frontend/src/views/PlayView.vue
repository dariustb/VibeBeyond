<script>
import axios from "axios";
import { Howl } from "howler";
import DateTime from "../components/DateTime.vue";

export default {
  name: "PlayView",
  data() {
    return {
      start_radio: false,
      show_play_button: true,
      song_name: "",
      song_artist: "",
      song_length: "",
      song_path: "",
    };
  },
  methods: {
    // GETs message from Flask localhost
    getMessage() {
      const flask_path = "http://localhost:5000/song_gen";
      axios
        .get(flask_path)
        .then((flask_response) => {
          this.song_name = flask_response.data.name;
          this.song_artist = flask_response.data.artist;
          this.song_length = flask_response.data.length;
          this.song_path = flask_response.data.path;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    // Plays soundfile using howlerJS
    playAudio() {
      console.log("playAudio() started.");
      if (this.start_radio == false) {
        this.start_radio = true;
        var sound = new Howl({
          src: [this.song_path],
        });
        sound.play();
      }
    },
  },
  created() {
    this.getMessage();
  },
  components: {
    DateTime,
  },
};
</script>

<template>
  <main>
    <!-- Play button -->
    <div
      class="flex items-center justify-center h-screen"
      v-show="show_play_button"
    >
      <button
        class="bg-yellow-500 hover:bg-yellow-700 text-white font-bold py-2 px-4 rounded-full"
        @click="
          playAudio();
          show_play_button = false;
        "
      >
        <h1 class="text-[64px]">&nbsp;▶&nbsp;</h1>
      </button>
    </div>

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
      <p id="song-name" class="text-[22px]">{{ song_name }}</p>
      <p id="artist-name" class="text-[22px] font-semibold">
        {{ song_artist }}
      </p>
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
      <p id="play-time">0:00 / {{ song_length }}</p>
    </div>
  </main>
</template>
