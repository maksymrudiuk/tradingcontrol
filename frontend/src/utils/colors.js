function rgbGenerate () {
  const color = Object
  var rgbcolor = [Math.floor(Math.random() * 256), Math.floor(Math.random() * 256), Math.floor(Math.random() * 256)]
  color.rgba = 'rgba(' + rgbcolor.join(', ') + ', .75)'
  color.rgb = 'rgb(' + rgbcolor.join(', ') + ')'
  return color
}

function getColor (value) {
  const color = Object
  if (value >= 60) {
    var rgbcolor = [173, 255, 47]
  } if (value >= 40 && value < 60) {
    var rgbcolor = [255, 255, 51]
  } if (value >= 0 && value < 40) {
    var rgbcolor = [255, 99, 71]
  }
  color.rgba = 'rgba(' + rgbcolor.join(', ') + ', .75)'
  color.rgb = 'rgb(' + rgbcolor.join(', ') + ')'
  return color
}
export default getColor
