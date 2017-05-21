export const KO = 'KO'
export const JP = 'JP'
export const EN = 'EN'
export const REQ = 'REQ'
export const FEAST = 'FEAST'

export function setKorean () {
  return {
    type: KO
  }
}

export function setJapanese () {
  return {
    type: JP
  }
}

export function setEnglish () {
  return {
    type: EN
  }
}

export function setRequest(value) {
    return {
        type: REQ,
        req: value
    };
}

export function getFeast(value) {
    return {
        type: FEAST,
        date: value
    };
}
