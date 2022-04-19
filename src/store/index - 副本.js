import { createStore } from 'vuex'

// 创建一个新的 store 实例
const store = createStore({
  state () {
    // 单一状态树
    // 唯一数据源 (SSOT)
    return {
      count: 0,
      todos: [
        { id: 1, text: '...', done: true },
        { id: 2, text: '...', done: false }
      ]
      /*
      get: 放在计算属性中：return this.$store.state.count
      批量get:使用mapState批量创建计算属性
      import { mapState } from 'vuex'
      computed: mapState({
        count: state => state.count,
        countAlias: 'count', // 传字符串参数 'count' 等同于 `state => state.count`
        doneCount: 'doneTodosCount', //重命名，把 `this.doneCount` 映射为 `this.$store.getters.doneTodosCount`
        countPlusLocalState (state) {
          return stathis.$te.count + this.localCount; //非箭头函数this
        }
      })
      computed: mapState(['count', 'num']) // 名称相同可以简写
      localComputed () { ... }, ...mapState({ ... }) // 使用对象展开运算符将此对象混入到外部对象中
      set: 使用方法，以便更明确地追踪到状态的变化
       */
    }
  },
  // 类似store的计算属性，从 Vue 3.0 开始，getter 的结果不再像计算属性一样会被缓存起来。这是一个已知的问题，将会在 3.2 版本中修复。
  getters: {
    doneTodos: (state) => {
      return state.todos.filter(todo => todo.done)
    },
    // 可以接受getter作为参数
    doneTodosCount (state, getters) {
      return getters.doneTodos.length
    },
    // 返回一个可以查询store里数据的函数，这种情况下不会缓存结果
    getTodoById: (state) => (id) => {
      return state.todos.find(todo => todo.id === id)
    }
    /*
    访问：放在计算属性中：return this.$store.getters.doneTodos
     */
  },
  mutations: {
    // 必须是同步函数
    increment (state, payload) {
      state.count += payload.amount
    },
    /*
    传参叫提交载荷（payload），一般是个对象，更易读
    call:
      this.$store.commit('increment', { amount: 10 }); // 载荷形式
      this.$store.commit({ type: 'increment', amount: 10 }); // 对象形式
     */
  },
  actions: {
    // 可以包含异步操作，返回一个mutations
    // 默认参数是store，等价于{ commit } = store
    incrementAsync ({ commit }) {
      setTimeout(() => {
        commit('increment', { amount: 10 });
      }, 1000);
    }
    /*
    call:
      this.$store.dispatch('incrementAsync', { amount: 10 }) // 载荷形式
      this.$store.dispatch({ type: 'incrementAsync', amount: 10 }) // 对象形式
    */
  }
});

export default store;
