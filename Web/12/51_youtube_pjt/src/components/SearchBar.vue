<template>
  <div>
    <input class="form-control" type="text" @keyup.enter="onInputKeyword" v-model="inputValue">
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
  data: function() {
    return {
      inputValue: '',
    }
  },
  methods: {
    onInputKeyword: function (event) {
      this.$emit('input-change', this.inputValue)
      console.log(event.target.value)
    }
  }
}
</script>

<style>

</style>