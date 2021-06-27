<template>
  <div>
    <input type="text" v-model="query">
    <button @click="onSearch">Search</button>
  </div>
</template>

<script>
export default {
  name: 'VideoSearchBar',
  data: function () {
    return {
      query: '',
    }
  },
  methods: {
    onSearch: function () {
      // console.log(this.query)
      this.$store.dispatch('onSearch', this.query)
      this.query = ''
    }
  },
}
</script>

<style>

</style>