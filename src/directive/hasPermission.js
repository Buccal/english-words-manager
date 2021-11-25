import Vue from 'vue'
import store from "@/store/index";

const permiList = {
  visitor: [],
  user: ["frequency-operater", "words-manager", "user-info"],
  vip: ["frequency-operater", "words-manager", "user-info"],
  admin: ["frequency-operater", "words-manager", "user-info"],
};

function changeHasPermission(el, binding) {
  if (permiList[getUserRole()].indexOf(binding.value) === -1) {
    el.parentNode && el.parentNode.removeChild(el)
  }

  function getUserRole() {
    if (store.getters.loginStatus){
      return "user";
    }else{
      return "visitor";
    }
  }
}

export default {
  install(Vue){
    Vue.directive('hasPermi', {
      mounted(el, binding) {
        changeHasPermission(el, binding);
      }
    })
  }
};
