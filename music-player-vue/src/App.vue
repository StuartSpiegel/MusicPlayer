<template>
  <div class="App">
    <h1>Music Player</h1>
    <audio controls>
      <source :src="files/test.mp3" type="audio/mpeg" />
      Your browser does not support the audio element.
    </audio>
  </div>
</template>

<script>
export default {
  name: 'App',
  computed: {
    audioUrl() {
      return '/play';
    },
  },
};
</script>
