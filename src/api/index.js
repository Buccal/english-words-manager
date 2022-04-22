import request from '@/utils/request'

// 用户相关

/**
 * 用户注册
 * @param {Object} data - 请求的url地址
 * @param {String} data.account - 账号
 * @param {String} data.password - 密码
 */
export function register (data) {
  return request({
    url: '/user/register',
    method: 'post',
    data: data
  })
}


/**
 * 用户登录
 * @param {Object} data - 请求的url地址
 * @param {String} data.account - 账号
 * @param {String} data.password - 密码
 * @returns {Object} res
 * @returns {Number} res.userId
 */
export function login (data) {
  return request({
    url: '/user/login',
    method: 'post',
    data: data
  })
}

/**
 * 获取用户的基本信息
 * @returns {Object} res
 * @returns {String} res.data.account
 * @returns {String} res.data.email
 * @returns {Boolean} res.data.disabled
 */
export function getUserInfo () {
  return request({
    url: '/user/info',
    method: 'get',
  })
}

// 注销（Todo）
// 参数：account、password、userId
export function deleteAccount (userId) {
  return request({
    url: '/user/delete' + userId,
    method: 'delete'
  })
}

// 关闭（Todo）
// 参数：account、password、userId
export function close (data) {
  return request({
    url: '/user/close',
    method: 'post',
    data: data
  })
}

// 清空重置（Todo）
// 参数：account、password、userId
export function reset (data) {
  return request({
    url: '/user/reset',
    method: 'post',
    data: data
  })
}

/**
 * 计算词频
 * @param {Object} data
 * @param {String} data.content - 英文文本
 */
export function wordFrequency (data) {
  return request({
    url: '/wordFrequency',
    method: 'post',
    data: data
  })
}

// 词语管理

/**
 * 添加已认识的单词
 * @param {Object} data
 * @param {String} data.content - 英文文本
 */
export function add (data) {
  return request({
    url: '/user_words/set_known',
    method: 'post',
    data: data
  })
}

// 移除熟词（Todo）
export function remove (data) {
  return request({
    url: '/word/remove',
    method: 'delete',
    data: data
  })
}

// 将生词保存为单词本（Todo）
// 参数：用户id、单词本名称、单词列表、来源文本（可选项）
export function create (data) {
  return request({
    url: '/book/create',
    method: 'post',
    data: data
  })
}

// 获取所有单词本（Todo）
// 参数：用户id
export function getBooks (userId) {
  return request({
    url: '/book/list' + userId,
    method: 'get'
  })
}

// 获取模板单词列表
export function getTemplateWords (level) {
  return request({
    url: '/templateWords/' + level,
    method: 'get'
  })
}
