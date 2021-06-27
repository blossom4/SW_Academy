import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    todos: [

    ],
  },
  mutations: {
    CREATE_TODO: function (state, input) {
      const todo = {
        title: input,
        isCompleted: false
      }
      state.todos.push(todo)
    },
    DELETE_TODO: function (state, todo) {

      const index = state.todos.indexOf(todo)
      state.todos.splice(index, 1)
    },
    UPDATE_TODO: function (state, target_todo) {
      // console.log(state, todo)
      state.todos = state.todos.map((todo) => {
        if (todo === target_todo) {
          return {...todo, isCompleted: !todo.isCompleted}
        }
        return todo
      })
    }
  },
  actions: {
    createTodo: function (context, input) {
      // console.log(context, input)
      context.commit('CREATE_TODO', input)
    },
    deleteTodo: function ({ commit }, todo) {
      commit('DELETE_TODO', todo)
    },
    updateTodo: function ({ commit }, todo) {
      commit('UPDATE_TODO', todo)
    },
  },
  getters: {
    completeTodoCount: function (state) {
      return state.todos.filter((todo) => {
        return todo.isCompleted
      }).length
    },
    uncompleteTodoCount: function (state) {
      return state.todos.filter((todo) => {
        return !todo.isCompleted
      }).length
    }
  },
  modules: {
  }
})
