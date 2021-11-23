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
    if(!localStorage.localStorage.getItem("user_id")){
      return "visitor";
    }else{
      return "user";
      // return localStorage.localStorage.getItem("role");
    }
  }
}



const install = function(Vue) {
  Vue.directive('hasPermi', {
    bind: function(el, binding, vnode) {
      changeHasPermission(el, binding)
    },
    update(el, binding, vnode) {
      changeHasPermission(el, binding)
    }
  })
}
