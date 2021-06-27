<template>
  <div style="margin-top: 7%;" id="center">
    <h1 class="mt-5">영화 추천</h1>
    <div class="col-2 btn btn-lg btn-success my-3" @click="pickMovie">CLICK</div>
    <h2 class="mt-5">{{ selectedMovie }}</h2>

  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'Random',
  data: function () {
    return {
      movie: [],
      selectedMovie: '',
    }
  },

  methods: {
    pickMovie: function () {
      this.selectedMovie = _.sample(this.movieTitles)
    },
  },
  computed: {
    movieTitles: function () {
      return this.$store.getters.pickMovie
    }
  },
}
</script>

<style>

</style>