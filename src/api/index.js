import request from '@/utils/request'

// 用户相关

// 注册
// 参数：account、password
// 默认创建熟词库
export function register(data) {
  return request({
    url: '/user/register',
    method: 'post',
    data: data
  })
}

// 登陆
// 参数：account、password
// 返回：user_id
export function login(data) {
  return request({
    url: '/user/login',
    method: 'post',
    data: data
  })
}

// 注销（todo）
// 参数：account、password、user_id
export function delete_account(user_id) {
  return request({
    url: '/user/delete' + user_id,
    method: 'delete',
  })
}

// 关闭（todo）
// 参数：account、password、user_id
export function close(data) {
  return request({
    url: '/user/close',
    method: 'post',
    data: data
  })
}

// 清空重置（todo）
// 参数：account、password、user_id
export function reset(data) {
  return request({
    url: '/user/reset',
    method: 'post',
    data: data
  })
}

// 词频计算
export function wordfrequency(data) {
  return request({
    url: '/wordfrequency',
    method: 'post',
    data: data
  })
}

// 词语管理

// 添加熟词
export function add(data) {
  return request({
    url: '/known_word/add',
    method: 'post',
    data: data,
  })
}

// 获取熟词列表
export function getKnownWords(user_id) {
  return request({
    url: '/known_word/list/' + user_id,
    method: 'get',
  })
}

// 移除熟词（todo）
export function remove(data) {
  return request({
    url: '/word/remove',
    method: 'delete',
    data: data,
  })
}

// 将生词保存为单词本（todo）
// 参数：用户id、单词本名称、单词列表、来源文本（可选项）
export function create(data) {
  return request({
    url: '/book/create',
    method: 'post',
    data: data,
  })
}

// 获取所有单词本（todo）
// 参数：用户id
export function getBooks(user_id) {
  return request({
    url: '/book/list' + user_id,
    method: 'get',
  })
}

// 获取模板单词列表
export function getTemplateWords(level) {
  return request({
    url: '/template_word/list/' + level,
    method: 'get',
  })
}