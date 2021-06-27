<template>
  <div>
    <h1>List</h1>
      <VideoListItem
       v-for="video in videos"
       :key="video.etag"
       :video="video"
       @select-video="onSelectVideo"
       />
  </div>
</template>

<script>
import VideoListItem from '@/components/VideoListItem.vue'

export default {
  name: 'VideoList',
  props: {
    videos: Array,
  },
  components: {
    VideoListItem
  },
  methods: {
    onSelectVideo: function (video) {
      this.$emit('select-video', video)
    }
  }
}
</script>

<style>

</style>