color_data = {
    "colors": {
    "0": ["#FF0000","#00FF00","#0000FF","#FFFF00","#FF00FF","#00FFFF","#800080","#FFA500","#FFC0CB","#A52A2A"],
    "1": ["#FFB3B3","#B3FFB3","#B3B3FF","#FFFFB3","#FFB3FF","#B3FFFF","#D1B3D1","#FFD1B3","#FFD1D1","#D1A3A3"],
    "2": ["#FF073A","#39FF14","#1B03A3","#FFFF33","#FF33FF","#33FFFF","#9400D3","#FF4500","#FF69B4","#964B00"],
    "3": ["#4EAB35", "#1845F5", "#ED3833", "#FACD48", "#FFFFFF"],
    "4": ["#F8D349", "#47B8F7", "#EFC2ED", "#6B6BC2", "#909090"],
    "5": ["#ACDAD8", "#EF6C38", "#76D1EA", "#ED893B", "#E1E4CA"],
    "6": ["#5C7D7F", "#E9CF68", "#B92C42", "#512538", "#D55F3F"],
    "7": ["#61CEC5", "#BE4F59", "#CBF048", "#EF6D68", "#556272"],
    "8": ["#FFDE00","#FF6347","#FF4040","#3CB371","#1E90FF","#C71585","#FF69B4","#8A2BE2","#20B2AA","#FFA07A","#800000","#008000","#0000FF","#FF0000","#000080","#FFC0CB","#A52A2A","#008080","#800080","#FFFF00","#FFC0CB","#DC143C","#A52A2A","#DEB887","#5F9EA0","#7FFF00","#D2691E","#FF7F50","#6495ED","#FFD700","#DAA520","#FFBF00","#ADFF2F","#FF69B4","#CD5C5C","#4B0082","#F0E68C","#7CFC00","#ADD8E6","#F08080","#90EE90","#FFB6C1","#FFA07A","#20B2AA","#87CEFA","#B0C4DE","#00FF00","#32CD32","#FF00FF","#800000","#66CDAA","#0000CD","#BA55D3","#9370DB","#3CB371","#7B68EE","#00FA9A","#48D1CC","#C71585","#191970","#FFE4B5","#000080","#808000","#6B8E23","#FFA500","#FF4500","#DA70D6","#EEE8AA","#98FB98","#AFEEEE","#DB7093","#CD853F","#FFC0CB","#DDA0DD","#800080","#663399","#FF0000","#BC8F8F","#4169E1","#8B4513","#FA8072","#F4A460","#2E8B57","#A0522D","#87CEEB","#6A5ACD","#00FF7F","#4682B4","#D2B48C","#008080","#D8BFD8","#FF6347","#40E0D0","#EE82EE","#9ACD32","#BF9B30"] 
 }
}

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dragon Colors</title>
    <style>
        body {{ font-family: Arial, sans-serif; }}
        .color-container {{ margin-bottom: 20px; }}
        .color-swatch {{ display: inline-block; width: 100px; height: 100px; margin-right: 10px; border: 1px solid #000; }}
        .color-name {{ padding-top: 110px; display: block; }}
    </style>
</head>
<body>
    <h1>Dragon Colors</h1>
    {}
</body>
</html>
"""

parts_html = ""

for part, colors in color_data["colors"].items():
    part_html = f'<div class="color-container"><h2>{part.capitalize()}</h2>'
    for color in colors:
        part_html += f'<div class="color-swatch" style="background-color: {color};"><span class="color-name">{color}</span></div>'
    part_html += '</div>'
    parts_html += part_html

html_content = html_template.format(parts_html)

with open("pixales_colors.html", "w") as file:
    file.write(html_content)

print("HTML page generated successfully.")
