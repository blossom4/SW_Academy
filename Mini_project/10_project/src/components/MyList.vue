<template>
  <div>
    <MyListItem
    v-for="(movie, idx) in this.$store.state.mymovies" 
    :key="idx"
    :movie="movie"
    />
  </div>
</template>

<script>
import MyListItem from '@/components/MyListItem'

export default {
  name: 'MyList',
  components: {
    MyListItem,
  },
}
</script>

<style>

</style>