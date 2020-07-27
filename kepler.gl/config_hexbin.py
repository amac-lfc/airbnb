config = {
  "version": "v1",
  "config": {
    "visState": {
      "filters": [],
      "layers": [
        {
          "id": "t1iqcrb",
          "type": "hexagon",
          "config": {
            "dataId": "Chicago",
            "label": "Point",
            "color": [
              237,
              200,
              0
            ],
            "columns": {
              "lat": "latitude",
              "lng": "longitude"
            },
            "isVisible": True,
            "visConfig": {
              "opacity": 0.8,
              "worldUnitSize": 1,
              "resolution": 8,
              "colorRange": {
                "name": "ColorBrewer YlOrRd-6",
                "type": "sequential",
                "category": "ColorBrewer",
                "colors": [
                  "#ffffb2",
                  "#fed976",
                  "#feb24c",
                  "#fd8d3c",
                  "#f03b20",
                  "#bd0026"
                ]
              },
              "coverage": 1,
              "sizeRange": [
                0,
                694.03
              ],
              "percentile": [
                0,
                100
              ],
              "elevationPercentile": [
                0,
                100
              ],
              "elevationScale": 15.4,
              "colorAggregation": "average",
              "sizeAggregation": "count",
              "enable3d": True
            },
            "hidden": False,
            "textLabel": []
          },
          "visualChannels": {
            "colorField": {
              "name": "price",
              "type": "integer"
            },
            "colorScale": "quantile",
            "sizeField": None,
            "sizeScale": "linear"
          }
        },
        {
          "id": "0mrmks",
          "type": "geojson",
          "config": {
            "dataId": "Boundaries",
            "label": "Boundaries",
            "color": [
              119,
              110,
              87
            ],
            "columns": {
              "geojson": "geometry"
            },
            "isVisible": True,
            "visConfig": {
              "opacity": 0.8,
              "strokeOpacity": 0.41,
              "thickness": 1,
              "strokeColor": [
                233,
                246,
                250
              ],
              "colorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#5A1846",
                  "#900C3F",
                  "#C70039",
                  "#E3611C",
                  "#F1920E",
                  "#FFC300"
                ]
              },
              "strokeColorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#5A1846",
                  "#900C3F",
                  "#C70039",
                  "#E3611C",
                  "#F1920E",
                  "#FFC300"
                ]
              },
              "radius": 10,
              "sizeRange": [
                0,
                10
              ],
              "radiusRange": [
                0,
                50
              ],
              "heightRange": [
                0,
                500
              ],
              "elevationScale": 5,
              "stroked": True,
              "filled": False,
              "enable3d": False,
              "wireframe": False
            },
            "hidden": False,
            "textLabel": [
              {
                "field": None,
                "color": [
                  255,
                  255,
                  255
                ],
                "size": 18,
                "offset": [
                  0,
                  0
                ],
                "anchor": "start",
                "alignment": "center"
              }
            ]
          },
          "visualChannels": {
            "colorField": None,
            "colorScale": "quantile",
            "sizeField": None,
            "sizeScale": "linear",
            "strokeColorField": None,
            "strokeColorScale": "quantile",
            "heightField": None,
            "heightScale": "linear",
            "radiusField": None,
            "radiusScale": "linear"
          }
        }
      ],
      "interactionConfig": {
        "tooltip": {
          "fieldsToShow": {
            "Chicago": [
              {
                "name": "accommodates",
                "type": "integer",
                "format": "",
                "analyzerType": "INT",
                "id": "accommodates",
                "tableFieldIndex": 5
              },
              {
                "name": "bathrooms",
                "type": "real",
                "format": "",
                "analyzerType": "FLOAT",
                "id": "bathrooms",
                "tableFieldIndex": 6
              },
              {
                "name": "price",
                "type": "integer",
                "format": "",
                "analyzerType": "INT",
                "id": "price",
                "tableFieldIndex": 7
              }
            ],
            "Boundaries": [
              {
                "name": "pri_neigh",
                "type": "string",
                "format": "",
                "analyzerType": "STRING",
                "id": "pri_neigh",
                "tableFieldIndex": 1
              }
            ]
          },
          "compareMode": False,
          "compareType": "absolute",
          "enabled": True
        },
        "brush": {
          "size": 0.5,
          "enabled": False
        },
        "geocoder": {
          "enabled": False
        },
        "coordinate": {
          "enabled": False
        }
      },
      "layerBlending": "normal",
      "splitMaps": [],
      "animationConfig": {
        "currentTime": None,
        "speed": 1
      }
    },
    "mapState": {
      "bearing": 24,
      "dragRotate": True,
      "latitude": 41.880855781373825,
      "longitude": -87.72628069597286,
      "pitch": 50,
      "zoom": 9.130198681903842,
      "isSplit": False
    },
    "mapStyle": {
      "styleType": "dark",
      "topLayerGroups": {},
      "visibleLayerGroups": {
        "label": True,
        "road": True,
        "border": False,
        "building": True,
        "water": True,
        "land": True,
        "3d building": False
      },
      "threeDBuildingColor": [
        9.665468314072013,
        17.18305478057247,
        31.1442867897876
      ],
      "mapStyles": {}
    }
  }
}