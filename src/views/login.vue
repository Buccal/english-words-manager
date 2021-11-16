<template>
  <el-form ref="form" :model="form" label-width="120px" class="register">
    <el-form-item label="账号：">
      <el-input v-model="form.account" type="text"></el-input>
    </el-form-item>
    <el-form-item label="密码：">
      <el-input v-model="form.password" type="password"></el-input>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="handleRegister">注册</el-button>
      <el-button type="primary" @click="handleLogin">登录</el-button>
    </el-form-item>
  </el-form>
</template>

<script>
import { register, login } from "@/api/index"
export default {
  data() {
    return {
      form: {
        account: "",
        password: "",
      },
    }
  },
  methods: {
    handleRegister() {
      register(this.form).then(res => {
        if(res.code === 200 && res.data){
          localStorage.setItem("user_id", res.data);
          this.$router.push("/");
        }else{
          alert("注册失败，原因为：" + res.msg);
        }
      });
    },
    handleLogin() {
      login(this.form).then(res => {
        if(res.code === 200 && res.data){
          localStorage.setItem("user_id", res.data);
          this.$router.push("/");
        }else{
          alert("登录失败，原因为：" + res.msg);
        }
      });
    }
  },
  created() {
  }
}
</script>

<style lang="scss" scoped>
</style>