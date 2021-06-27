<template>
  <div>
    <h1>index</h1>
    <TodoItem v-for="(todo, idx) in todos" :key="idx" :todo-data="todo"/>
  </div>
</template>

<script>
import TodoItem from '@/components/TodoItem.vue'

export default {
  name: 'Index',
  components: {
    TodoItem
  },
  data: function () {
    return {
      
    }
  },
  props: {
    todos: Array
  }
}
</script>

<style>

</style>