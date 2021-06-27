<template>
  <div>
    <div class="d-flex justify-content-between">
      <div :class="{ completed: movie.completed }">
        <input type="checkbox" class="me-1">
        {{ movie.title }}
      </div>
      <div class="btn btn-sm">X</div>
    </div>
    
  </div>
</template>

<script>
export default {
  name: 'MyListItem',
  props: {
    movie: {
      type: Object,
    }
  },
  methods: {
    deleteMovie: function () {
      this.$store.dispatch('deleteMovie', this.movie)
    },
  },
}
</script>

<style>

</style>