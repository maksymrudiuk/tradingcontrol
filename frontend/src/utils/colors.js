function rgbGenerate() {
  const color = Object
  var rgbcolor = [Math.floor(Math.random()*256), Math.floor(Math.random()*256), Math.floor(Math.random()*256)]
  color.rgba = 'rgba(' + rgbcolor.join(', ') + ', .75)'
  color.rgb = 'rgb(' + rgbcolor.join(', ') + ')'
  return color
}

export default rgbGenerate
