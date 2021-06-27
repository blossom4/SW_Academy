<template>
  <div>
    <div class="card" style="width: 18rem;">
      <img :src="posterURL" class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">{{ movie.title }}</h5>
        <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
      </div>
    </div>
   
  </div>
</template>

<script>


export default {
  name: 'MovieCard',
  props: {
    movie: {
      type: Object,
    }
  },
  computed: {
    posterURL () {
      return `https://image.tmdb.org/t/p/w500/${this.movie.poster_path}`
    }
  }

    
  

}
</script>

<style>

</style>