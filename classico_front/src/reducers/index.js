import { KO, JP, EN, REQ, FEAST } from '../actions'
import { combineReducers } from 'redux'

// S: index page // 
// check default language
let saved_lang = localStorage.getItem('setine_lang')
let language = ''

if (saved_lang === null) {
  language = navigator.languages ? navigator.languages[0] : (navigator.language || navigator.userLanguage)
  localStorage.setItem('setine_lang', language)
} else {
  language = saved_lang
}

const languageInitialState = {
  value: language
}

const lang = (state = languageInitialState, action) => {
  switch (action.type) {
    case KO:
      return Object.assign({}, state, {
        value: 'ko'
      })
    case JP:
      return Object.assign({}, state, {
        value: 'jp'
      })
    case EN:
      return Object.assign({}, state, {
        value: 'en'
      })
    case REQ:
      localStorage.setItem('setine_lang', action.req)
      return Object.assign({}, state, {
        value: action.req
      })      
    default:
      return state
  }
}
// E: index page // 

// S: rank pages //
function getToday() {
  let today = new Date()
  let dd = checkNumber(today.getDate())
  let mm = checkNumber(today.getMonth() + 1)
  let yyyy = today.getFullYear()

  let target = yyyy + mm + dd
  return target
}

function checkNumber(val) {
  if (val < 10) val = "0" + val
  return val
}

const rankInitialState = {
  date: getToday()
}

const rank = (state = rankInitialState, action) => {
  switch (action.type) {
    case FEAST:
      return Object.assign({}, state, {
        date: action.date
      })      
    default:
      return state
  }
}
// E: rank pages //

const setineApp = combineReducers({
  lang,
  rank
})

export default setineApp
