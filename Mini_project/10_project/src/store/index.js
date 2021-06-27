import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

const API_URL = 'https://gist.githubusercontent.com/eduChange-hphk/d9acb9fcfaa6ece53c9e8bcddd64131b/raw/9c8bc58a99e2ea77d42abd41376e5e1becabea69/movies.json'

export default new Vuex.Store({
  state: {
    movies: [],
    mymovies: [],
  },
  mutations: {
    CREATE_MY_MOVIE: function (state, input) {
      state.mymovies.push(input)
    },
    LOAD_MOVIES: function (state, movies) {
      state.movies = movies
    }
  },
  actions: {
    createMyMovie: function ({ commit }, input) {
      commit('CREATE_MY_MOVIE', input)
    },
    loadMovies: function () {
      axios({
        method: 'get',
        url: API_URL,
      })
      .then((res) => {
        this.commit('LOAD_MOVIES', res.data)
      })
    }
  },
  getters: {
    pickMovie: function (state) {
      return state.movies.map((movie) => {
        return movie.title
      })
    }
  },

  modules: {
  }
})
