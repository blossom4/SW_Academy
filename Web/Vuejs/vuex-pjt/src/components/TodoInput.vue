<template>
  <div>
    <input v-model="input" type="text" @keyup.enter="createTodo">
  </div>
</template>

<script>
export default {
  name: 'TodoInput',
  data: function () {
    return {
      input: '',
    }
  },
  methods: {
    createTodo: function () {
      // console.log(this.$store)
      this.$store.dispatch('createTodo', this.input)
      this.input = ''
    }
  }
}
</script>

<style>

</style>