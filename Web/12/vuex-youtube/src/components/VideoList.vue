<template>
  <div>
    <VideoListItem
    v-for="video in $store.state.searchResult"
    :key="video.etag"
    :video="video"
    />
 
  </div>
</template>

<script>
import VideoListItem from '@/components/VideoListItem'

export default {
  name: 'VideoList',
  components: {
    VideoListItem,
  },
}
</script>

<style>

</style>