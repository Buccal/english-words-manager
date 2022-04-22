import store from '@/store/index'

const permissionList = {
  visitor: [],
  user: ['frequency-management', 'words-manager', 'user-info'],
  vip: ['frequency-management', 'words-manager', 'user-info'],
  admin: ['frequency-management', 'words-manager', 'user-info']
}

function changeHasPermission (el, binding) {
  if (permissionList[getUserRole()].indexOf(binding.value) === -1) {
    el.parentNode && el.parentNode.removeChild(el)
  }

  function getUserRole () {
    if (store.getters.loginStatus) {
      return 'user'
    } else {
      return 'visitor'
    }
  }
}

export default {
  install (Vue) {
    Vue.directive('hasPermi', {
      mounted (el, binding) {
        changeHasPermission(el, binding)
      }
    })
  }
}
