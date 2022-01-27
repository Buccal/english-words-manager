<template>
  <el-container>
    <el-header>
      <TheHeader />
    </el-header>
    <el-main>
      <el-row>
        <el-col :span="12" :offset="6">
          <router-view></router-view>
        </el-col>
      </el-row>
    </el-main>
    <el-footer>
      <TheFooter />
    </el-footer>
  </el-container>
</template>

<script setup>
import TheHeader from './components/TheHeader'
import TheFooter from './components/TheFooter'
</script>

<style lang="scss" scoped>
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

.el-header {
  padding: 0;
}
</style>
