// 引入axios
import axios from 'axios'

// 【非必要】 引入错误提示语
import errorCode from '@/utils/errorCode'

//设置默认请求头
axios.defaults.headers['Content-Type'] = 'application/json';

// 设置默认请求地址
axios.defaults.baseURL = 'http://127.0.0.1:8000/';

//设置默认的请求超时时间
axios.defaults.timeout = 10000;

const server = axios.create()

// 请求拦截器
server.interceptors.request.use(
	config => {
		// 获取token
		let token = localStorage.getItem("header");
		// 判断是否存在token
		if (token) {
			// 每个http header都加上token
			config.headers.token = `${token}`;
		}

		// get请求映射params参数
		if (config.method === 'get' && config.params) {
			// 拼接请求地址
			let url = config.url + '?';
			for (const propName of Object.keys(config.params)) {
				const value = config.params[propName];
				var part = encodeURIComponent(propName) + "=";
				if (value !== null && typeof(value) !== "undefined") {
					if (typeof value === 'object') {
						for (const key of Object.keys(value)) {
							let params = propName + '[' + key + ']';
							var subPart = encodeURIComponent(params) + "=";
							url += subPart + encodeURIComponent(value[key]) + "&";
						}
					} else {
						url += part + encodeURIComponent(value) + "&";
					}
				}
			}
			url = url.slice(0, -1);
			config.params = {};
			config.url = url;
		}

		return config;
	},
	err => {
		this.$router.push("/login")
		return Promise.reject(err);
	});

// 响应拦截器
server.interceptors.response.use(function(res) {
	let rtn = res.data;

	rtn.code = res.status;

	// 映射错误信息
	rtn.msg = rtn.msg || res.data.msg || errorCode[rtn.code] || errorCode['default'] || res.statusText;

	if (rtn.code >= 400) {
		// 删除已经失效或过期的token（不删除也可以，因为登录后覆盖）
		localStorage.clear();
		router.replace({
			// 跳转到登录页重新获取token
			path: '/login',
			query: {
				// 登陆后回到当前页面
				redirect: router.currentRoute.fullPath
			}
		})
	} else if (rtn.code !== 200) {
		return Promise.reject(new Error(rtn.msg))
	}
	return rtn
}, function(error) {
	let { message } = error;
	if (message == "Network Error") {
		message = "后端接口连接异常";
	} else if (message.includes("timeout")) {
		message = "系统接口请求超时";
	} else if (message.includes("Request failed with status code")) {
		message = "系统接口" + message.substr(message.length - 3) + "异常";
	}
	return Promise.reject(error)
})

export default server