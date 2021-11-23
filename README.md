# new-words-frequency

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).


[webpack搭建vue项目](https://www.jianshu.com/p/d56425fc6c23)
[总结：vue中Axios的封装-API接口的管理](https://www.jianshu.com/p/5e578b046577)


1. 分词时态
2. 结果改为表格，可添加到熟词列表，或一键添加
3. 生词列表保存

实现效果：
1. 将要阅读的文本粘贴到输入框
2. 后端分词，筛掉熟词，计算生词词频
3. 生成生词列表展示在页面中
4. 可以将生词添加到熟词列表中
5. 可以管理熟词列表
6. 可以文本和将生词列表绑定保存（左侧文本，右侧生词）



图标咋用的？没搞懂

Collection

<el-icon><folder-add /></el-icon>
<el-icon><plus /></el-icon>





https://fastapi.tiangolo.com/zh/tutorial/query-params/
http://127.0.0.1:8000/docs#/default/get_book_list_book_get
http://127.0.0.1:8000/redoc#operation/root__get


https://element-plus.gitee.io/zh-CN/component/pagination.html#%E9%99%84%E5%8A%A0%E5%8A%9F%E8%83%BD


vue3
代码规范

大量文本，上传txt进行词频分析


权限
1. 游客
	首页就是词频计算页
		词频计算用户输入
			输入框、
			计算按钮：只统计词频
		词频统计结果
			表格（序号、词语[可排序]、词频[可排序]）
			搜索结果（搜索框、按钮）
			导出（表格，txt）
		右上角，登陆按钮
2. 普通用户
	首页词频计算页
		词频计算用户输入
			输入框
			计算按钮：默认只统计生词的词频，可取消
		词频统计结果
			表格（序号、词语[可排序]、词频[可排序]、是否生词[可选择、可筛选]）
			保存选择的熟词到熟词库
			保存生词到生词本（可关联文本）
			搜索结果（搜索框、按钮）
			导出（表格，txt）
		右上角，登出按钮
	熟词管理页
	生词本管理页
	设置页



报错
- 
登陆注册页，点击输入框，报错runtime-core.esm-bundler.js?5c40:6584
[Vue warn]: Invalid event arguments: event validation failed for event "keydown".




[vue3语法参考](https://juejin.cn/post/7031086963214483492)


文本域无法输入是因为表单的ref和v-model一致

ref定义的变量，要使用.value改变值
reactive定义的变量，集中包装到一个对象里，对象.变量改变值
用let定义的变量，重新赋值会覆盖ref和reactive


## 代码规范
单文件组件名称
- 使用多个单词：防止与未来html元素冲突 #A
- 使用PascalCase或kebab-case格式 #B
  - 单文件组件和字符串模板：PascalCase
    - 编辑器可以在模板里自动补全组件名称
    - 视觉上更能够和单个单词的 HTML 元素区别开
    - 视觉上更能够和非Vue的自定义元素区别开
  - DOM模板：kebab-case
    - HTML 、是大小写不敏感的
  - 单文件组件、字符串模板、DOM模板：kebab-case
  - JS/JSX：PascalCase（在较为简单的应用中，只使用app.component进行全局组件注册时，可以使用kebab-case字符串）
    - app.component('MyComponent' / 'my-component'
    - import 'MyComponent' from
    - export default { name: 'MyComponent'
- 基础（展示类的、无逻辑的或无状态的）组件名添加前缀（Base、App或V） #B
  BaseButton.vue、AppButton.vue、VButton.vue
- 单例（只有单个活跃实例，每个页面只能用一次，永远不接受任何prop）组件以The前缀命名，以示其唯一性 #B
- 与父组件紧密耦合的子组件应该以父组件名作为前缀命名 #B
  - TodoList、TodoListItem
  - SearchSidebar、SearchSidebarNavigation
- 组件名称应该以高阶的 (通常是一般化描述的) 单词开头，并以描述性的修饰词结尾 #B
  - SearchButtonClear.vue
  - SearchButtonRun.vue
  - SearchInputQuery.vue
  - SearchInputExcludeGlob.vue
  - SettingsCheckboxTerms.vue
  - SettingsCheckboxLaunchOnStartup.vue
- 组件名称应该倾向于完整的单词，而不是缩写 #B
  编辑器中的自动补全已经让书写长命名的代价非常之低了，而其带来的明确性却是非常宝贵的。不常用的缩写尤其应该避免。


组件属性
- 尽量详细，至少指定类型 #A
  - type
  - required
  - validator
- 声明用camelCase，模板和JSX中用kebab-case #B
  - props: { greetingText: String }
  - <WelcomeMessage greeting-text="hi"/>
- 多个attribute的元素应该分多行撰写，每个attribute一行 #B
- 组件密集或难以阅读时，属性之间添加空行，在一些编辑器里还可以通过键盘快速导航 #C

语法
- 始终为v-for设置key值：以便维护内部组件及其子树的状态 #A
- 永远不要在一个元素上同时使用v-if和v-for #A
- 为单文件组件样式设置作用域：配合组件库的class覆盖样式 #A
- 私有property名称 #A
  - 添加$_前缀
  - 使用闭包
```
methods: {
  $_myPrivateFunction() {
    // ...
  }

  publicMethod() {
    myPrivateFunction()
  }
}
```
- 分为单文件组件 #B
- 在单文件组件、字符串模板和JSX中，没有内容的组件应该是自闭合的——但在DOM模板里永远不要这样做 #B
  - 自闭合组件表示它们不仅没有内容，而且是刻意没有内容。
- 组件模板应该只包含简单的表达式，复杂的表达式则应该重构为计算属性或方法 #B
- 应该把复杂计算属性尽可能多地分割为更简单的计算属性 #B
- 非空HTML属性的值应该始终带有单/双引号，不要用attr=xxx或attr={xxx} #B
- 指令缩写要么始终使用，要么始终不使用 #B
  - 用 : 表示 v-bind:
  - 用 @ 表示 v-on:
  - 用 # 表示 v-slot
- 元素选择器应该避免在scoped中出现，用类选择器替换 #D
- 应该优先通过prop和事件进行父子组件之间的通信，而不是通过this.$parent或对prop做出变更 #D
  一个理想的Vue应用是prop向下传递，事件向上传递的。遵循这一约定会让你的组件更易于理解。
- 应该优先通过Vuex管理全局状态，而不是通过this.$root或一个全局事件总线 #D


组件/实例选项顺序 #C
1. **全局感知** (要求在组件以外被感知)
  - `name`
2. **模板编译选项** (改变模板编译的方式)
  - `compilerOptions`
3. **模板依赖** (模板内使用的资源)
  - `components`
  - `directives`
4. **组合** (合并 property 至选项内)
  - `extends`
  - `mixins`
  - `provide`/`inject`
5. **接口** (组件的接口)
  - `inheritAttrs`
  - `props`
  - `emits`
  - `expose`
6. **组合式 API** (使用组合式 API 的入口点)
  - `setup`
7. **本地状态** (本地的响应式 property)
  - `data`
  - `computed`
8. **事件** (通过响应式事件触发的回调)
  - `watch`
  - 生命周期事件 (按照它们被调用的顺序)
    - `beforeCreate`
    - `created`
    - `beforeMount`
    - `mounted`
    - `beforeUpdate`
    - `updated`
    - `activated`
    - `deactivated`
    - `beforeUnmount`
    - `unmounted`
    - `errorCaptured`
    - `renderTracked`
    - `renderTriggered`
9. **非响应式的 property** (不依赖响应性系统的实例 property)
  - `methods`
10. **渲染** (组件输出的声明式描述)
   - `template`/`render`

元素属性的顺序 #C
1. **定义** (提供组件的选项)
  - `is`
2. **列表渲染** (创建相同元素的多个变体)
  - `v-for`
3. **条件** (元素是否渲染/显示)
  - `v-if`
  - `v-else-if`
  - `v-else`
  - `v-show`
  - `v-cloak`
4. **渲染修饰符** (改变元素的渲染方式)
  - `v-pre`
  - `v-once`
5. **全局感知** (要求在组件以外被感知)
  - `id`
6. **唯一性 Attribute** (需要唯一值的 attribute)
  - `ref`
  - `key`
7. **双向绑定** (结合了绑定与事件)
  - `v-model`
8. **其他 Attribute** (所有普通的、绑定或未绑定的 attribute)
9. **事件** (组件事件监听器)
  - `v-on`
10. **内容** (覆写元素的内容)
   - `v-html`
   - `v-text`

单文件组件的顶级元素的顺序
始终保持 <script>、<template> 和 <style> 标签的顺序一致 #C

## 名词解释
字符串模板：写在vue实例定义组件时，如template: 'blabla'
JSX
DOM模板：写在html文件中


## 图标
Avatar、Stamp、UserFilled 用户
BrushFilled、Brush 主题
Histogram 词频

HomeFilled、House 主页

InfoFilled 更多信息
QuestionFilled 问题

MoonNight、Moon 月亮
Sunrise、Sunny 太阳

Management 单词本

Setting、Tools 设置
Share 分享

Sugar

https://www.cnblogs.com/BlueCc/p/14339424.html