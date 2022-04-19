<template>
  <el-row class="login">
    <el-col
      :span="12"
      :offset="6"
    >
      <el-tabs type="border-card" v-model="data.activeName">
        <el-tab-pane label="登录" name="login">
          <el-form
            label-width="120px"
            ref="loginForm"
            :model="form"
            :rules="rules"
            class="form"
          >
            <el-form-item
              label="账号："
              prop="username"
            >
              <el-input
                v-model="form.username"
                type="text"
              ></el-input>
            </el-form-item>
            <el-form-item
              label="密码："
              prop="password"
            >
              <el-input
                v-model="form.password"
                type="password"
                @keydown.enter="handleLogin"
              ></el-input>
            </el-form-item>
            <div style="text-align: center">
              <el-button
                type="primary"
                @click="handleLogin()"
              >登录</el-button>
            </div>
          </el-form>
        </el-tab-pane>
        <el-tab-pane label="注册"  name="register">
          <el-form
            label-width="120px"
            ref="registerForm"
            :model="form"
            :rules="rules"
            class="form"
          >
            <el-form-item
              label="账号："
              prop="username"
            >
              <el-input
                v-model="form.username"
                type="text"
              ></el-input>
            </el-form-item>
            <el-form-item
              label="密码："
              prop="password"
            >
              <el-input
                v-model="form.password"
                type="password"
                @keydown.enter="handleRegister"
              ></el-input>
            </el-form-item>
            <div style="text-align: center">
              <el-button
                type="primary"
                @click="handleRegister()"
              >注册</el-button>
            </div>
          </el-form>
        </el-tab-pane>
      </el-tabs>
    </el-col>
  </el-row>
</template>

<script setup>
import { reactive } from 'vue'
import router from '@/router/index.js'
import store from '@/store/index'
import { register, login } from '@/api'
import { encrypt } from '@/utils/jsencrypt'
import { setToken, setTokenType } from '@/utils/auth'
import { ElMessage } from 'element-plus'

let data = reactive({
  activeName: "login"
})

const form = reactive({
  username: '',
  password: '',
})

const rules = reactive({
  username: [{
    required: true,
    message: '请输入用户名',
    trigger: 'blur'
  }],
  password: [{
    required: true,
    message: '请输入密码',
    trigger: 'blur'
  }],
})

const handleRegister = () => {
  register({
    username: form.username,
    password: encrypt(form.password)
  }).then(() => {
    ElMessage.success("注册成功")
    data.activeName = "login"
  }).catch(err=>{
    ElMessage.error('注册失败，原因为：' + err.msg)
  })
}

const handleLogin = () => {
  login({
    username: form.username,
    password: encrypt(form.password)
  }).then((res) => {
    store.commit('$_setStorage', res.data)
    setToken(res.data.access_token)
    setTokenType(res.data.token_type)
    ElMessage.success("登录成功")
    router.push('/')
  }).catch(err => {
    console.log(err)
    debugger
    ElMessage.error('登录失败，原因为：' + err.msg)
  })
}
</script>

<style lang="scss" scoped>
.login {
  margin-top: 100px;

  & .form {
    margin-top: 25px;

    & .el-input {
      width: 280px;
    }
  }
}
</style>
