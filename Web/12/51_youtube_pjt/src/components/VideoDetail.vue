<template>
  <div>
    <iframe v-if="video" :src="videoURL" frameborder="0"></iframe>
  </div>
</template>

<script>


export default {
  name: 'VideoDetail',
  props: {
    video: {},
  },
  computed: {
    videoURL: function () {
      const videoId = this.video.id.videoId
      return `https://www.youtube.com/embed/${videoId}`
    }
  },
}
</script>

<style>

</style>