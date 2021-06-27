<template>
  <div>
    <h1>create</h1>
    <input type="text" v-model="userInput" @keyup.enter="addTodo">
  </div>
</template>

<script>
export default {
  name: 'Create',
  data: function () {
    return {
      userInput: ''
    }
  },
  methods: {
    addTodo: function () {
      this.$emit('add-todo', this.userInput)
      // console.log(this.userInput)
      this.userInput = ''
    }
  }
}
</script>

<style>

</style>