<template>
  <div>
    <iframe :src="videoURL" frameborder="0"></iframe>
    <h5>{{ videoTitle }}</h5>
    <p>{{ videoDescription }}</p>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'VideoDetail',
  computed: {
    ...mapGetters([
      'videoURL',
      'videoTitle',
      'videoDescription',
    ])
  },
}
</script>

<style>

</style>