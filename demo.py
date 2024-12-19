# This is a sample program to demo features of PixelGrapher

import pixelgraph as px
from pixelgraph import backandforth

px.init(100, 400, 30)

while True:
    px.clear()

    px.vertical(px.backandforth)
    px.horizontal(px.backandforth)

    px.vertical(px.res - px.backandforth)
    px.horizontal(px.res - px.backandforth)

    px.update()
