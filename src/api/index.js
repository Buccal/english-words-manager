import request from '@/utils/request'

// 用户相关

// 注册
// 参数：account、password
// 默认创建熟词库
export function register (data) {
  return request({
    url: '/user/register',
    method: 'post',
    data: data
  })
}

// 登陆
// 参数：account、password
// 返回：userId
export function login (data) {
  return request({
    url: '/user/login',
    method: 'post',
    data: data
  })
}

// 注销（todo）
// 参数：account、password、userId
export function deleteAccount (userId) {
  return request({
    url: '/user/delete' + userId,
    method: 'delete'
  })
}

// 关闭（todo）
// 参数：account、password、userId
export function close (data) {
  return request({
    url: '/user/close',
    method: 'post',
    data: data
  })
}

// 清空重置（todo）
// 参数：account、password、userId
export function reset (data) {
  return request({
    url: '/user/reset',
    method: 'post',
    data: data
  })
}

// 词频计算
export function wordfrequency (data) {
  return request({
    url: '/wordfrequency',
    method: 'post',
    data: data
  })
}

// 词语管理

// 添加熟词
export function add (data) {
  return request({
    url: '/user_words/set_known',
    method: 'post',
    data: data
  })
}

// 获取熟词列表
export function getKnownWords (userId) {
  return request({
    url: '/user_words/known_list/' + userId,
    method: 'get'
  })
}

// 移除熟词（todo）
export function remove (data) {
  return request({
    url: '/word/remove',
    method: 'delete',
    data: data
  })
}

// 将生词保存为单词本（todo）
// 参数：用户id、单词本名称、单词列表、来源文本（可选项）
export function create (data) {
  return request({
    url: '/book/create',
    method: 'post',
    data: data
  })
}

// 获取所有单词本（todo）
// 参数：用户id
export function getBooks (userId) {
  return request({
    url: '/book/list' + userId,
    method: 'get'
  })
}

// 获取模板单词列表
export function getTemplateWords (userId, level) {
  return request({
    url: '/user_words/template_list/' + userId + '/' + level,
    method: 'get'
  })
}
