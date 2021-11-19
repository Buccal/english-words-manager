<template>
  <el-form ref="ruleform" :model="form" label-width="120px" class="register">
    <el-form-item label="账号：" prop="account">
      <el-input v-model="form.account" type="text"></el-input>
    </el-form-item>
    <el-form-item label="密码：" prop="password">
      <el-input v-model="form.password" type="password"></el-input>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="handleRegister()">注册</el-button>
      <el-button type="primary" @click="handleLogin()">登录</el-button>
    </el-form-item>
  </el-form>
</template>

<script setup>
import { ref, reactive, toRefs } from "vue";
import router from '@/router/index.js'
import { register, login } from "@/api/index"

const ruleform = ref(null);

const form = reactive({
  account: "",
  password: "",
});

// const { account, password } = toRefs(form)

const handleRegister = () => {
  register(form).then(res => {
    if(res.code === 200 && res.data){
      localStorage.setItem("user_id", res.data);
      router.push("/");
    }else{
      alert("注册失败，原因为：" + res.msg);
    }
  });
};

const handleLogin = () => {
  login(form).then(res => {
    if(res.code === 200 && res.data){
      localStorage.setItem("user_id", res.data);
      router.push("/");
    }else{
      alert("登录失败，原因为：" + res.msg);
    }
  });
}
</script>

<style lang="scss" scoped>
</style>

