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

// 注销
// 参数：account、password、user_id
export function delete_account(user_id) {
  return request({
    url: '/user/delete' + user_id,
    method: 'delete',
  })
}

// 关闭
// 参数：account、password、user_id
export function close(user_id) {
  return request({
    url: '/user/close' + user_id,
    method: 'post',
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

// 移除熟词
export function remove(data) {
  return request({
    url: '/word/remove',
    method: 'delete',
    data: data,
  })
}

// 获取熟词列表
export function getwords(user_id) {
  return request({
    url: '/word/list' + user_id,
    method: 'get',
  })
}

// 将生词保存为单词本
// 参数：用户id、单词本名称、单词列表、来源文本（可选项）
export function create(data) {
  return request({
    url: '/book/create',
    method: 'post',
    data: data,
  })
}

// 获取所有单词本
// 参数：用户id
export function getBooks(user_id) {
  return request({
    url: '/book/list' + user_id,
    method: 'get',
  })
}
