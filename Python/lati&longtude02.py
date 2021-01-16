import gmplot

#Input latitude and longtitude, and zoom value
gmap1 = gmplot.GoogleMapPlotter(53.4630621, -2.2935288, 13)

#download it automatic to your file or to foler path (C:\\users\\inf\\Desktop\\test.html")
#only works for html, NOT any image folder like png, jpg or ect.
gmap1.draw("test.html")
