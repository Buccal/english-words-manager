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
- 多个单词：防止与未来html元素冲突 #A
- PascalCase（有助自动补全；大小写不敏感系统出问题）或kebab-case #B
- 基础（展示类的、无逻辑的或无状态的）组件名添加前缀（Base、App或V） #B
  BaseButton.vue、AppButton.vue、VButton.vue
- 单例（只有单个活跃实例）组件以The前缀命名，以示其唯一性，每个页面只能用一次


组件属性
- 尽量详细，至少指定类型 #A
  - type
  - required
  - validator

语法
- 始终为v-for设置key值：以便维护内部组件及其子树的状态 #A
- 永远不要在一个元素上同时使用v-if和v-for #A
- 为单文件组件样式设置作用域：配合组件库的class覆盖样式 #A
- 私有property名称 #A
  - 添加$_前缀 #A
  - 使用闭包 #A
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