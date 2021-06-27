<template>
  <div id="app">
    <p>Completed Todos: {{ completeTodoCount }}</p>
    <p>unCompleted Todos: {{ uncompleteTodoCount }}</p>
    <TodoInput/>
    <TodoList/>
  </div>
</template>

<script>
import TodoList from '@/components/TodoList'
import TodoInput from '@/components/TodoInput'
import { mapGetters } from 'vuex'

export default {
  name: 'App',
  components: {
    TodoList,
    TodoInput,
  },
  computed: {
    // completeTodoCount: function () {
    //   return this.$store.getters.completeTodoCount
    // },
    // uncompleteTodoCount: function () {
    //   return this.$store.getters.uncompleteTodoCount
    // },
    ...mapGetters([
      'completeTodoCount',
      'uncompleteTodoCount',
    ])
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
