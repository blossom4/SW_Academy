<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Index</router-link> |
      <router-link to="/create">Create</router-link>
    </div>
    <router-view :todos="todosApp" @add-todo="createTodo"/>
  </div>
</template>

<script>
export default {
  name: 'App',
  data: function () {
    return {
      todosApp: [
        {content: '공부하기', isCompleted: false},
        {content: '저녁먹기', isCompleted: true},
      ]
    }
  },
  methods: {
    createTodo: function (input) {
      // console.log(input)
      const todo = {
        content: input,
        isCompleted: false
      }

      this.todosApp.push(todo)
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
