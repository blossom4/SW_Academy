<template>
  <div>
    <li class="d-flex align-items-center border rounded my-1" @click="selectVideo">
      <img :src="video.snippet.thumbnails.default.url" alt="">
      <p class="text-center w-100">{{ video.snippet.title | stringUnescape }}</p>
    </li>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'VideoListItem',
  props: {
    video: Object,
  },
  methods: {
    selectVideo: function() {
      this.$emit('select-video', this.video)
    }
  },
  filters: {
  stringUnescape: function (rowText) {
    return _.unescape(rowText)
    }
  }
}
</script>

<style>

</style>