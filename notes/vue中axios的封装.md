## vue中axios的封装
在vue项目和后端交互获取数据时，通常使用axios库，[官方文档](https://links.jianshu.com/go?to=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Faxios)。
浅谈在项目中axios的简单二次封装

### 安装
```bash
	npm install axios; //安装axios
	//cnpm install axios;//或者使用镜像下载.
```

#### 引入组件
**通常情况下，在项目src目录下创建request文件夹，然后创建http.js和api.js文件。**
- http.js用来二次封装axios；
- api.js用来统一管理后端接口；

## 在http.js文件中
- 引入axios；
- 引入qs，用于序列化post类型的数据。
- 引入ui提示框，根据自己u进行修改；**[[推荐elementui文档\]](https://links.jianshu.com/go?to=https%3A%2F%2Felement.eleme.cn%2F%23%2Fzh-CN%2Fcomponent%2Fmessage)**

### 环境切换
在http.js的文件中的axios.defaults.baseURL可以设置axios的默认请求地址。配合不同的运行指令进行开发不同环境的数据。
另附配置[[vue不同环境配置不同打包命令]](https://links.jianshu.com/go?to=https%3A%2F%2Fwww.liangzl.com%2Fget-article-detail-13554.html)

#### 环境的切换
```
	if (process.env.NODE_ENV == 'development') {  
		  axios.defaults.baseURL = 'https://www.baidu.com';}
	else if (process.env.NODE_ENV == 'debug') {  
		  axios.defaults.baseURL = 'https://www.ceshi.com';
	}
	else if (process.env.NODE_ENV == 'production') {  
	   axios.defaults.baseURL = 'https://www.production.com';
	}
```

### 请求默认值的设置
#### 通过axios.defaults.timeout设置默认的请求超时时间。
```
    //设置默认的请求超时时间
    axios.defaults.timeout = 10000;
```

#### 设置默认请求头和token
```
    //设置post的请求头
    axios.defaults.headers.post['Content-Type'] = 'application/json';
    //设置默认token 一般有权限不在这里设置
    //axios.defaults.headers.Authorization=token;
```
### 请求拦截
#### token拦截
一般情况下，发送请求必须带有token进行验证。做权限的话这里需要注意。
```
axios.interceptors.request.use(
    config => {
        let token = localStorage.getItem("header");
        if (token) { // 判断是否存在token，如果存在的话，则每个http header都加上token
            config.headers.token = `${token}`;
        }
        return config;
    },
    err => {
        this.$router.push("/login")
        return Promise.reject(err);
    });
```

#### 响应拦截
*这里需要根据后端协商，根据后端返回状态码进行处理*
```
    axios.interceptors.response.use(function(response) {
        if (response.status >= 400) {
            localStorage.clear(); // 删除已经失效或过期的token（不删除也可以，因为登录后覆盖）
            router.replace({
                path: '/login', // 到登录页重新获取token
                query: {
                    //回到当前页面
                    redirect: router.currentRoute.fullPath
                }
            })
        }
        return response
    }, function(error) {
        if (error.response) {
            if (error.response.status === 403) {
                Message({
                    showClose: true,
                    message: '登录过期',
                    type: 'error'
                });
                localStorage.clear();
                Cookies.set("user", "", -10);
                router.replace({
                    path: '/login' // 到登录页重新获取token
                })
            } else if (error.response.status === 405) {
                Message({
                    showClose: true,
                    message: '权限不足,请联系管理员',
                    type: 'warning'
                });
                router.replace({
                    path: '/error',
                })
            } else if (error.response.status === 500) {
                Message({
                    showClose: true,
                    message: '服务器异常',
                    type: 'error'
                });
            }
        }
        return Promise.reject(error)
    })
```

### 封装get和post方法
*axios封装的方法有很多，比如get,post,delete,put等方法。这里简单介绍get和post的封装。*

#### post
```
	/**
	 * post方法，对应post请求
	 * @param {String} url [请求的url地址]
	 * @param {Object} params [请求时携带的参数]
	 */
	export function post(url, params) {
	  return new Promise((resolve, reject) => {
	    axios.post(url, params)
	      .then(res => {
	        resolve(res.data);
	      })
	      .catch(err => {
	        reject(err.data)
	      })
	  });
	}
```

#### get
```
	/**
	 * get方法，对应get请求
	 * @param {String} url [请求的url地址]
	 * @param {Object} params [请求时携带的参数]
	 */
	export function get(url, params) {
	  return new Promise((resolve, reject) => {
	    axios.get(url, {
	      params: params
	    }).then(res => {
	      resolve(res.data);
	    }).catch(err => {
	      reject(err.data)
	    })
	  });
	}
```

# vue中api的封装
*首先在api.js中引入在http.js中封装的get和post两种方法。*
```
	import { get, post } from './http'
```

#### 不同参数的封装接口方法
```
	export const Login = p => get('/api/admin/login', p);
	export const Registry = p => post('/api/admin/registry', p);
```

#### 路径参数封装
```
	export const Api= p => post('/api/'+ p);
```

#### 多参数封装
```
	export const Api=（ p，q ）=> post('/api/'+ p+“/"+q);
```

#### 页面中使用方法
```
	import { Login,Registry } from "@/request/api"
	export default {
		name:"app",
		data(){
			return{
				message:{
					uname:"",
					upwd:""
				}
			}
		},
		methods:{
			login(){
				Login(this.message).then(res=>{
					....请求成功的处理
				})
			}
		}
	}
```

例外附上：
1.[[gulp安装与使用\]](https://links.jianshu.com/go?to=https%3A%2F%2Fblog.csdn.net%2FGenius_cxx%2Farticle%2Fdetails%2F97399942)
2.[[搭建基于webpack的vue环境\]](https://links.jianshu.com/go?to=https%3A%2F%2Fblog.csdn.net%2FGenius_cxx%2Farticle%2Fdetails%2F97399524)
3.[[浅谈Vue项目优化心得\]](https://links.jianshu.com/go?to=https%3A%2F%2Fblog.csdn.net%2FGenius_cxx%2Farticle%2Fdetails%2F97397268)
4.[[总结：搭建Vue项目心得\]](https://links.jianshu.com/go?to=https%3A%2F%2Fblog.csdn.net%2FGenius_cxx%2Farticle%2Fdetails%2F96484202)
5. [[总结：vue中Axios的封装-API接口的管理\]](https://links.jianshu.com/go?to=https%3A%2F%2Fblog.csdn.net%2FGenius_cxx%2Farticle%2Fdetails%2F97788044)