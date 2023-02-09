<script>
  export default {
      data() {
          return {
              // Bool values for v-show in the template section below
              startPage: true,
              playingPage: false,
              // NOTE: Just for dev, remove when ready for prod
              buttonsForTesting: true
          };
      },
      methods: {
          // Makes start page hidden & play page visible
          // Effectively transitioning content in the same page
          togglePlayingPage() {
              this.startPage = !this.startPage;
              this.playingPage = !this.playingPage;
          }
      },
      components: {

      }
  };
</script>

<template>
  <!-- Start Page -->
  <div v-show="startPage" class="flex items-center justify-center h-screen shadow-[inset_0_0px_0px_1000px_rgba(217,217,217,0.2)]">
    <!-- vibe beyond title -->
    <h1 class="text-[64px] drop-shadow-[0_4px_4px_rgba(0,0,0,0.25)]">
        <b class="font-light">vibe </b><b>beyond.</b>
    </h1>

    <!-- play button + text -->
    <button @click="togglePlayingPage()" class="absolute bottom-52 drop-shadow-[0_4px_4px_rgba(0,0,0,0.25)]" id="play-button">
        <p class="text-2xl text-[#4F3247] opacity-80 tracking-wider text-center relative bottom-4">play</p>            
    </button>

    <!-- Darius / Linh -->
    <div class ="absolute right-5 bottom-3">
        <p class="text-xs opacity-50 font-semibold">Darius Brown / Linh Nguyen</p>
    </div>
  </div>

  <!-- Playing Page -->
  <div v-show="playingPage">
    <!-- NOTE: Delete for prod-->
    <button v-show="buttonsForTesting" @click="togglePlayingPage()" class="absolute top-72 left-72">BACK TO START PAGE</button>

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
    <div class="absolute left-9 top-9 text-xs opacity-50 font-semibold drop-shadow-[0_4px_4px_rgba(0,0,0,0.25)]">
        <p>PLAY ▶<br>VOL IIIIIIII</p>
    </div>

    <!-- TR: Now Playing, Song title, Artist name -->
    <div class="absolute right-9 top-9 text-right drop-shadow-[0_4px_4px_rgba(0,0,0,0.25)]">
        <p class="text-xs opacity-50 font-semibold">NOW PLAYING</p>
        <p id="song-name" class="text-[22px]">Dancing Droplets</p>
        <p id="artist-name" class="text-[22px] font-semibold">Leavv</p>
    </div>

    <!-- BL: Current Time & Date -->
    <div class="absolute left-9 bottom-9 text-xs opacity-50 font-semibold drop-shadow-[0_4px_4px_rgba(0,0,0,0.25)]">
        <DateTime></DateTime>
    </div>

    <!-- BR: Time on song -->
    <div class="absolute right-9 bottom-9 text-xs opacity-50 font-semibold drop-shadow-[0_4px_4px_rgba(0,0,0,0.25)]">
        <p id="play-time">0:00 / 3:14</p>
    </div>
  </div>
  
</template>

<style scoped>
</style>
