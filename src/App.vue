<template>
  <div id="nav">
    <router-link to="/">Home</router-link> |
    <router-link to="/frequency">Word Frequency</router-link>
    <router-link to="/knownWordsManager">Known Words Manager</router-link>
    <router-link to="/login">Login</router-link>
  </div>
  <div class="body">
    <router-view />
  </div>
</template>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}

.body {
  width: 65%;
  margin: 0 auto;
}
</style>
