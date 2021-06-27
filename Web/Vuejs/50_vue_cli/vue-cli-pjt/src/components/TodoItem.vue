<template>
  <li>
    <input type="checkbox" v-model="todoData.isCompleted">
    {{ todoData.content }}
  </li>
</template>

<script>
export default {
  name: 'TodoItem',
  props: {
    todoData: Object
  },
}
</script>

<style>

</style>