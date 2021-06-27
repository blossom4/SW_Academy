<template>
  <div>
    <input type="checkbox" :class="{ completed: todo.completed }"  @click="updateTodo()">
    <span :class="{ completed: todo.completed }" @click="updateTodo()">{{ todo.content }}</span>
    <button @click="deleteTodo()">Delete</button>
  </div>
</template>

<script>
export default {
  name: 'TodoListItem',
  props: {
    todo: {
      type: Object,
    },
  },
  methods: {
    updateTodo: function () {
        this.$store.dispatch('updateTodo', this.todo)
    },
    deleteTodo: function () {
      this.$store.dispatch('deleteTodo', this.todo)
    }
  },
  
}
</script>

<style>
  .completed {
    text-decoration-line: line-through;
  }
</style>