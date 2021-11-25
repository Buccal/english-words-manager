<template>
  <el-row class="login">
    <el-col :span="12" :offset="6">
      <el-tabs type="border-card">
        <el-tab-pane label="登录">
          <el-form
            label-width="120px"
            ref="ruleform"
            :model="form"
            class="form"
          >
            <el-form-item
              label="账号："
              prop="account"
            >
              <el-input
                v-model="form.account"
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
        <el-tab-pane label="注册">
          <el-form
            label-width="120px"
            ref="ruleform"
            :model="form"
            class="form"
          >
            <el-form-item
              label="账号："
              prop="account"
            >
              <el-input
                v-model="form.account"
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
import { ref, reactive, toRefs } from "vue";
import router from "@/router/index.js";
import store from "@/store/index";
import { register, login } from "@/api/index";

const ruleform = ref(null);

const form = reactive({
  account: "",
  password: "",
});

// const { account, password } = toRefs(form)

const handleRegister = () => {
  register(form).then((res) => {
    if (res.code === 200 && res.data) {
      store.commit('$_setStorage', { user_id: res.data });
      router.push("/");
    } else {
      alert("注册失败，原因为：" + res.msg);
    }
  });
};

const handleLogin = () => {
  login(form).then((res) => {
    if (res.code === 200 && res.data) {
      store.commit('$_setStorage', { user_id: res.data });
      router.push("/");
    } else {
      alert("登录失败，原因为：" + res.msg);
    }
  });
};
</script>

<style lang="scss" scoped>
.login {
  margin-top: 100px;

  & .form {
    margin: 50px 100px;

    & .el-input {
      width: 280px;
    }
  }
}
</style>
