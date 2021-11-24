<template>
  <el-menu
    :default-active="activeIndex"
    mode="horizontal"
    :ellipsis="false"
    @select="handleSelect"
    router
  >
<!--       background-color="#fff"
    text-color="#000"
    active-text-color="#409EFF" -->
    <el-menu-item index="/" id="logo">logo</el-menu-item>

    <el-menu-item index="/frequency">词频</el-menu-item>

    <el-sub-menu index="1" v-hasPermi="'words-manager'">
      <template #title>管理</template>
      <el-menu-item index="known-words-manager">熟词</el-menu-item>
      <el-menu-item index="1-1">单词本</el-menu-item>
    </el-sub-menu>

    <el-sub-menu index="2">
      <template #title>语言</template>
      <el-menu-item index="2-1">zh-CN</el-menu-item>
      <el-menu-item index="2-2">en-US</el-menu-item>
      <el-menu-item index="2-3">zh-MO</el-menu-item>
      <el-sub-menu index="2-4">
        <template #title>其他</template>
        <el-menu-item index="2-4-1">zh-TW</el-menu-item>
        <el-menu-item index="2-4-2">zh-HK</el-menu-item>
      </el-sub-menu>
    </el-sub-menu>

    <el-menu-item index="/login">登录</el-menu-item>
  </el-menu>
</template>

<script setup>
import { defineComponent, ref } from 'vue'

const activeIndex = ref('/')

const handleSelect = (key, keyPath) => {
  console.log(key, keyPath)
}
</script>

<style lang="scss" scoped>
.el-menu {
  justify-content: flex-end;
}

#logo {
  margin-right: auto;
}
</style>