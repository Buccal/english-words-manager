<template>
  <el-menu
    :default-active="router.currentRoute._value.path"
    :ellipsis="false"
    mode="horizontal"
    menu-trigger="hover"
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

    <el-sub-menu index="language">
      <template #title>语言</template>
      <el-menu-item index="zh-CN">中文</el-menu-item>
      <el-menu-item index="en-US">English</el-menu-item>
      <el-menu-item index="ru-RU">русский язык</el-menu-item>
      <el-sub-menu index="2-4">
        <template #title>其他</template>
        <el-menu-item index="de-DE">Deutsch</el-menu-item>
        <el-menu-item index="fr-FR">Français</el-menu-item>
        <el-menu-item index="es-ES">Español</el-menu-item>
        <el-menu-item index="ja-JP">日本語</el-menu-item>
        <el-menu-item index="ko-KR">한국어 공부 해요</el-menu-item>
      </el-sub-menu>
    </el-sub-menu>
    <el-menu-item index="/login" v-if="showLogin">登录</el-menu-item>

    <el-sub-menu index="5" v-if="!showLogin">
      <template #title>
        <el-avatar
          src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"
        ></el-avatar>
      </template>
      <el-menu-item index="5-1">设置</el-menu-item>
      <el-menu-item :index="router.currentRoute._value.path">登出</el-menu-item>
    </el-sub-menu>
  </el-menu>
</template>

<script setup>
import { defineComponent, computed } from 'vue'
import router from "@/router/index";
import store from "@/store/index";

const showLogin = computed(() => {
  return !store.getters.loginStatus
});

const handleSelect = (key, keyPath) => {
  if(key === router.currentRoute._value.path){
    store.commit('$_removeStorage');
    window.location.reload();
  }
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