<template>
  <div id="app">
    <div id="nav">
      <!-- Router -->
      <div class="d-flex justify-content-center">
        <router-link :to="{ name: 'Home' }" class="fs-3 text-decoration-none">Home</router-link>
        <h2 class="mx-2 text-secondary">|</h2>
        <router-link :to="{ name: 'Random' }" class="fs-3 text-decoration-none">Random</router-link>
        <h2 class="mx-2 text-secondary">|</h2>
        <router-link :to="{ name: 'MyMovieList' }" class="fs-3 text-decoration-none">My Movie</router-link>
      </div>

    </div>
    <router-view/>
  </div>
</template>

<style>
@font-face {
    font-family: 'NanumBarunpen';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_two@1.0/NanumBarunpen.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}
body {
  font-family: 'NanumBarunpen';
}
#center {
  text-align: center;
}

#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
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
  text-decoration-line: underline;
}
</style>
