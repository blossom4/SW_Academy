<template>
  <div>
    <p>ID</p>
    <input type="text" v-model="credential.username">
    <p>PASSWORD</p>
    <input type="password" v-model="credential.password">
    <br>
    <button @click="login()">login</button>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Login',
  data: function () {
    return {
      credential: {
        username: '',
        password: '',
      },
    }
  },
  methods: {
    login: function () {
      axios({
        method: 'post',
        url: `${SERVER_URL}/accounts/api-token-auth/`,
        data: this.credential
      })
        .then ((res) => {
          console.log(res)
        })
        .catch ((err) => {
          console.log(err)
        })
    }
  }
}
</script>
