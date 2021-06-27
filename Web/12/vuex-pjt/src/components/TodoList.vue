<template>
  <div>
    <li v-for="(todo, idx) in $store.state.todos" :key='idx'>
      <span :class="{ complete: todo.isCompleted }" @click="updateTodo(todo)">{{ todo.title }}</span>
    <button @click="deleteTodo(todo)">Delete</button>
    </li>
    
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'TodoList',
  methods: {
    // deleteTodo: function (todo) {
    //   // console.log(todo)
    //   this.$store.dispatch('deleteTodo', todo)
    // },
    // updateTodo: function (todo) {
    //   // console.log('UPDATE')
    //   this.$store.dispatch('updateTodo', todo)
    // },
    ...mapActions([
      'deleteTodo',
      'updateTodo',
    ])
  },
}
</script>

<style>
  .complete {
    text-decoration: line-through;
  }
</style>