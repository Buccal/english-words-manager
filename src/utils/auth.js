import Cookies from 'js-cookie'

const TokenKey = 'token'

const TokenType = "token-type"

export function getToken() {
  return Cookies.get(TokenKey)
}

export function setToken(token) {
  return Cookies.set(TokenKey, token)
}

export function removeToken() {
  return Cookies.remove(TokenKey)
}

export function getTokenType() {
  return Cookies.get(TokenType)
}

export function setTokenType(tokenType) {
  return Cookies.set(TokenType, tokenType)
}

export function removeTokenType() {
  return Cookies.remove(TokenType)
}

