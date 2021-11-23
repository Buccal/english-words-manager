import Vue from 'vue'

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
    if(!localStorage.getItem("user_id")){
      return "visitor";
    }else{
      return "user";
      // return localStorage.getItem("role");
    }
  }
}

export default {
  install(Vue){
    Vue.directive('hasPermi', {
      mounted(el, binding) {
        debugger
        changeHasPermission(el, binding);
      }
    })
  }
};
