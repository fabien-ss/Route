import tkinter as tk
import folium
from shapely.geometry import MultiLineString
import tkinterhtml as tkhtml

class PanneauLalanaSimba(tk.Frame):
    def __init__(self, parent,valeurCalculees, tableauCoordonnee, mls):
        tk.Frame.__init__(self, parent)
        self.valuerCalculees = valeurCalculees
        self.tableauCoordonnee = tableauCoordonnee
        #sprint(tableauCoordonnee)
        self.LabelFrame = tk.Label(self, text= "Prix de reviens "+str(self.valuerCalculees[0])+"Ar")
        self.LabelFrame1 = tk.Label(self, text= "Jour de reparation "+str(self.valuerCalculees[1])+"heures")
        self.mls = mls

        start = mls.geoms[0].coords[0]
        print(start)
        mark_style = {'color':'red', 'icon': 'info-sign'}
        m = folium.Map(location=[mls.centroid.y, mls.centroid.x], zoom_start=13)
        folium.Marker(location=start, icon=folium.Icon(**mark_style)).add_to(m)
        folium.GeoJson(data=mls.__geo_interface__).add_to(m)        
        
        folium.Marker(location=start, icon=folium.Icon(**mark_style)).add_to(m)
        
        m.save('test.html')
        label = self.LabelFrame
        label2 = self.LabelFrame1
        label.grid(row=0, column=0)
        label2.grid(row=1, column=0)
        
    def getId(self):
        print("OK NBOSS")
      