import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    todos: [],
  },
  mutations: {
    CREATE_TODO: function (state, input) {
      state.todos.push(input)
    },
    UPDATE_TODO: function (state, input) {
      console.log(state)
      state.todos = state.todos.map((todo) => {
        if (todo === input) {
          return { ...todo, completed: !todo.completed }
        }
        return todo
      })
    },
    DELETE_TODO: function (state, input) { 
      const index = state.todos.indexOf(input)
      state.todos.splice(index, 1)
    },
  },
  actions: {
    createTodo: function (context, input) {
      context.commit('CREATE_TODO', input)
    },
    updateTodo: function (context, input) {
      context.commit('UPDATE_TODO', input)
    },
    deleteTodo: function ({ commit }, input) {
      commit('DELETE_TODO', input)
    },
  },
  modules: {
  }
})
