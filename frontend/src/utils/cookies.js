function getCookie (name) {
  var matches = document.cookie.match(new RegExp(
    // eslint-disable-next-line
    '(?:^|; )' + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + '=([^;]*)'
  ))
  return matches
    ? decodeURIComponent(matches[1])
    : false
}

export default getCookie
