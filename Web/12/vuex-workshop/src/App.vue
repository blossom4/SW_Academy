<template>
  <div id="app">
    <input type="text" @keyup.enter="createTodo" v-model="input">
    <button @click="createTodo">Enter</button>
    <TodoList/>
  </div>
</template>

<script>

import TodoList from '@/components/TodoList'


export default {
  name: 'App',
  data: function () {
    return {
      input: '',
    }
  },
  components: {
    TodoList,
  },
  methods: {
    createTodo: function () {
      const todoItem = {
        content: this.input,
        completed: false,
      }
      if (todoItem.content.trim()) {
        this.$store.dispatch('createTodo', todoItem)
      }
      this.input = ''
    }
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
