<template>
  <div class="d-fle">
    <MovieCard
    v-for="(movie, idx) in this.$store.state.movies" 
    :key="idx"
    :movie="movie"
    />
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard'

export default {
  name: 'Home',
  components: {
    MovieCard,
  },
  methods: {
    loadMovies: function () {
      this.$store.dispatch('loadMovies')
    },
  },
  created: function () {
    this.loadMovies()
  }
}
</script>

<style>

</style>