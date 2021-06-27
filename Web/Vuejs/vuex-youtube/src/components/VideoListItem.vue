<template>
  <div @click="selectVideo">
    <img :src="videoImg" alt="">
    <p>{{ videoTitle }}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'VideoListItem',
  props: {
    video: {},
  },
  computed: {
    videoTitle: function () {
      return _.unescape(this.video.snippet.title)
    },
    videoImg: function () {
      return this.video.snippet.thumbnails.default.url
    },
  },
  methods: {
    selectVideo: function () {
      // console.log('click')
      this.$store.dispatch('selectVideo', this.video)
    }
  },
}
</script>

<style>

</style>