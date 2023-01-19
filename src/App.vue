<script>
export default {
    data() {
        return {
            startPage: true,
            playingPage: false
        }
    },
    methods: {
        togglePlayingPage(){
            this.startPage = !this.startPage;
            this.playingPage = !this.playingPage;
        }
    }
};
</script>

<template>
    <!-- Start Page -->
    <!-- Main container -->
    <div v-show="startPage" class="flex items-center justify-center h-screen shadow-[inset_0_0px_0px_1000px_rgba(217,217,217,0.2)]">
        <!-- vibe beyond title -->
        <h1 class="text-[64px] drop-shadow-[0_4px_4px_rgba(0,0,0,0.25)]">
            <b class="font-light">vibe </b><b>beyond.</b>
        </h1>

        <!-- play button + text -->
        <button @click="togglePlayingPage()" id="play-button" class="absolute bottom-52 drop-shadow-[0_4px_4px_rgba(0,0,0,0.25)]">
            <p class="text-2xl text-[#4F3247] opacity-80 tracking-wider text-center relative bottom-4">play</p>            
        </button>

        <!-- Darius / Linh -->
        <div class ="absolute right-5 bottom-3">
            <p class="text-xs opacity-50 font-semibold">Darius Brown / Linh Nguyen</p>
        </div>
    </div>

    <div v-show="playingPage">
        <button @click="togglePlayingPage()">BLOOP</button>
    </div>
</template>

<style scoped>
</style>
