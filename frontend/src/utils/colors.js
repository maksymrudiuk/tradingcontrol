function getColor (value) {
  const color = Object
  var rgbcolor = null
  if (value >= 60) {
    rgbcolor = [173, 255, 47]
  } if (value >= 40 && value < 60) {
    rgbcolor = [255, 255, 51]
  } if (value >= 0 && value < 40) {
    rgbcolor = [255, 99, 71]
  }
  color.rgba = 'rgba(' + rgbcolor.join(', ') + ', .75)'
  color.rgb = 'rgb(' + rgbcolor.join(', ') + ')'
  return color
}
export default getColor
