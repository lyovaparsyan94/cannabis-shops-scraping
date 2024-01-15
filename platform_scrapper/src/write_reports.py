import os
import json
import pprint


def clean_data(list_of_circle_sections, store="aaa", address='bb'):
    final_data = {}
    for item in list_of_circle_sections:
        if str(item)[0].isdigit():
            if type(list_of_circle_sections[item]) is list:
                final_data[item] = list_of_circle_sections[item]
        if type(item) is dict:
            # if type(list_of_circle_sections[item]) is dict:
            for key, value in item.items():
                if key:
                    for k1, v1 in value.items():
                        max_distance = max(v1.keys())
                        if key not in final_data:
                            final_data[key] = {}
                        if k1 not in final_data[key]:
                            final_data[key][k1] = {}
                        final_data[key][k1][max_distance] = v1[max_distance]
    res = {}
    for price in final_data:
        if type(final_data[price]) is list:
            res = final_data
            break
        if price not in res:
            res[price] = []
            for degree in final_data[price]:
                for km in final_data[price][degree]:
                    res[price].append(final_data[price][degree][km])

    filename = str(store) + str(address)
    with open(f"gd_{filename}.json", 'w') as file:
        json.dump(res, file)
    pprint.pprint(res)
    return res


def write_report(global_data, store, address, status, url, ecom_provider, service_options, index):
    store_l = str(store).capitalize()
    address_l = str(address).capitalize()
    filename = store_l + address_l
    liner = f"\n{60 * '-'}\n"
    with open(f"{index}glob.txt", "w") as file:
        if not global_data:
            result = f"Delivery info for {store} at address {address} NOT Found from {ecom_provider} ecommerse provider's server"
            json.dump(result, file, indent=2)
        else:
            json.dump(global_data, file, indent=2)
    with open(f"{index}{filename}.txt", "a") as f:
        report = f"Store - {store}{liner}Address - {address}{liner}{status}{liner}URL {url}{liner}Platform - {ecom_provider}{liner}Service options\n{service_options}{liner}Delivery Zones according to the price\nfirst number is the price, and in brackets are the coordinates of area according to that price \n"
        f.write(report)
        with open(f'{index}glob.txt', 'r') as glob_file:
            for line in glob_file:
                f.write(line)
    os.remove(f'{index}glob.txt')


x = [
  {
    "5.0": {
      "0": {
        "0.5": [
          [
            46.58311721313598,
            -81.1986488
          ]
        ]
      },
      "15": {
        "0.5": [
          [
            46.58296393806229,
            -81.19696038918546
          ]
        ]
      },
      "30": {
        "0.5": [
          [
            46.58251456075017,
            -81.19538706772674
          ]
        ]
      },
      "45": {
        "0.5": [
          [
            46.581799712257705,
            -81.1940360746072
          ]
        ]
      },
      "60": {
        "0.5": [
          [
            46.580868117530414,
            -81.1929994849917
          ]
        ],
        "0.9": [
          [
            46.584915785938755,
            -81.18282996113938
          ],
          "min order - 0"
        ]
      }
    }
  },
  {
    "5.0": {
      "72": {
        "0.5": [
          [
            46.580009063764486,
            -81.19244490231677
          ]
        ],
        "0.9": [
          [
            46.582510395418204,
            -81.18127737289447
          ],
          "min order - 0"
        ]
      },
      "87": {
        "0.5": [
          [
            46.57885451721586,
            -81.19213471397953
          ]
        ],
        "0.9": [
          [
            46.57927764111373,
            -81.18040926790293
          ],
          "min order - 0"
        ]
      },
      "102": {
        "0.5": [
          [
            46.5776839529057,
            -81.19226845546274
          ]
        ],
        "0.9": [
          [
            46.576000071568814,
            -81.18078419076465
          ],
          "min order - 0"
        ]
      },
      "117": {
        "0.5": [
          [
            46.57657714136539,
            -81.1928369849576
          ]
        ],
        "0.9": [
          [
            46.572901041443444,
            -81.18237642473265
          ],
          "min order - 0"
        ]
      },
      "132": {
        "0.5": [
          [
            46.575609503977105,
            -81.19380153644796
          ]
        ],
        "0.9": [
          [
            46.57019171930024,
            -81.18507733085617
          ],
          "min order - 0"
        ],
        "1.3": [
          [
            46.56236580782227,
            -81.17247751265177
          ],
          "min order - 0"
        ]
      }
    },
    "10.0": {
      "117": {
        "1.3": [
          [
            46.567590808274964,
            -81.16726820114789
          ]
        ],
        "1.7000000000000002": [
          [
            46.560646248676825,
            -81.14751381421608
          ],
          "min order - 35.0"
        ],
        "2.1": [
          [
            46.55206716830588,
            -81.12311518153962
          ],
          "min order - 35.0"
        ]
      }
    }
  },
  {
    "5.0": {
      "144": {
        "0.5": [
          [
            46.57498034498992,
            -81.19481493480933
          ]
        ],
        "0.9": [
          [
            46.568430127640966,
            -81.18791480822712
          ],
          "min order - 0"
        ],
        "1.3": [
          [
            46.55896855580681,
            -81.17794969132176
          ],
          "min order - 0"
        ]
      },
      "159": {
        "0.5": [
          [
            46.5744201092487,
            -81.19631134724399
          ]
        ],
        "0.9": [
          [
            46.56686152372204,
            -81.19210451673628
          ],
          "min order - 0"
        ]
      },
      "174": {
        "0.5": [
          [
            46.57414602134741,
            -81.1979670171736
          ]
        ],
        "0.9": [
          [
            46.566094107993216,
            -81.19673998968065
          ],
          "min order - 0"
        ]
      },
      "189": {
        "0.5": [
          [
            46.57417675560066,
            -81.19966913827575
          ]
        ],
        "0.9": [
          [
            46.56618016039852,
            -81.20150547726892
          ],
          "min order - 0"
        ]
      },
      "204": {
        "0.5": [
          [
            46.5745102180182,
            -81.20130174165764
          ]
        ],
        "0.9": [
          [
            46.56711381870322,
            -81.20607638753313
          ],
          "min order - 0"
        ]
      }
    }
  },
  {
    "5.0": {
      "216": {
        "0.5": [
          [
            46.57498034498992,
            -81.20248266519067
          ]
        ],
        "0.9": [
          [
            46.568430127640966,
            -81.20938279177288
          ],
          "min order - 0"
        ],
        "1.7000000000000002": [
          [
            46.546595533016976,
            -81.23237625422837
          ],
          "min order - 0"
        ],
        "2.1": [
          [
            46.53131095852591,
            -81.24846557750624
          ],
          "min order - 0"
        ]
      },
      "231": {
        "0.5": [
          [
            46.57578855741737,
            -81.20371785728685
          ]
        ],
        "0.9": [
          [
            46.57069305555513,
            -81.21284130588413
          ],
          "min order - 0"
        ]
      },
      "246": {
        "0.5": [
          [
            46.57678967770005,
            -81.20460765420893
          ]
        ],
        "0.9": [
          [
            46.573496132649254,
            -81.21533294246242
          ],
          "min order - 0"
        ],
        "1.7000000000000002": [
          [
            46.56251646923048,
            -81.25107846155629
          ],
          "min order - 0"
        ]
      },
      "261": {
        "0.5": [
          [
            46.577915489631685,
            -81.20509140511123
          ]
        ]
      },
      "276": {
        "0.5": [
          [
            46.579089276178486,
            -81.20513611978183
          ]
        ]
      }
    },
    "10.0": {
      "216": {
        "1.3": [
          [
            46.55896855580681,
            -81.21934790867824
          ]
        ]
      },
      "231": {
        "1.3": [
          [
            46.563332644760315,
            -81.22601783817525
          ]
        ],
        "1.7000000000000002": [
          [
            46.55370717287009,
            -81.24324564145455
          ],
          "min order - 35.0"
        ],
        "2.1": [
          [
            46.54181648527889,
            -81.26452239899767
          ],
          "min order - 35.0"
        ]
      },
      "246": {
        "1.3": [
          [
            46.56873846382072,
            -81.23082367093794
          ]
        ],
        "2.1": [
          [
            46.5548299459978,
            -81.27609555245947
          ],
          "min order - 35.0"
        ],
        "2.5": [
          [
            46.545678690405225,
            -81.30587279863812
          ],
          "min order - 35.0"
        ]
      },
      "261": {
        "0.9": [
          [
            46.576648369538894,
            -81.21668782421351
          ]
        ],
        "1.3": [
          [
            46.57481770721112,
            -81.23343764375909
          ],
          "min order - 35.0"
        ],
        "1.7000000000000002": [
          [
            46.572423270048084,
            -81.2553402900556
          ],
          "min order - 35.0"
        ],
        "2.1": [
          [
            46.569464825386994,
            -81.28239502926593
          ],
          "min order - 35.0"
        ],
        "2.5": [
          [
            46.56594214052967,
            -81.31460096743224
          ],
          "min order - 35.0"
        ]
      },
      "276": {
        "0.9": [
          [
            46.57993496831936,
            -81.21681347697294
          ]
        ],
        "1.3": [
          [
            46.58115614076827,
            -81.2336811494611
          ],
          "min order - 35.0"
        ],
        "1.7000000000000002": [
          [
            46.58275255774418,
            -81.25573952258821
          ],
          "min order - 35.0"
        ],
        "2.1": [
          [
            46.58472398332091,
            -81.28298908909959
          ],
          "min order - 35.0"
        ],
        "2.5": [
          [
            46.58707018140888,
            -81.31543044910394
          ],
          "min order - 35.0"
        ],
        "2.9": [
          [
            46.5897909157368,
            -81.353064310044
          ],
          "min order - 35.0"
        ]
      }
    },
    "15.0": {
      "276": {
        "3.3": [
          [
            46.59288594983331,
            -81.39589148667767
          ]
        ],
        "3.6999999999999997": [
          [
            46.596355047008714,
            -81.44391290106978
          ],
          "min order - 35.0"
        ]
      }
    }
  },
  {
    "5.0": {
      "288": {
        "0.5": [
          [
            46.580009063764486,
            -81.20485269768324
          ]
        ],
        "1.7000000000000002": [
          [
            46.59084689395928,
            -81.25324963101454
          ],
          "min order - 0"
        ]
      },
      "303": {
        "0.5": [
          [
            46.58106890870057,
            -81.20411969230419
          ]
        ],
        "1.3": [
          [
            46.59184644157936,
            -81.22819523625469
          ],
          "min order - 0"
        ],
        "1.7000000000000002": [
          [
            46.60017401919959,
            -81.24680280730107
          ],
          "min order - 0"
        ]
      },
      "318": {
        "0.5": [
          [
            46.581961817941455,
            -81.20301380542801
          ]
        ],
        "1.3": [
          [
            46.59666840695959,
            -81.22222376853375
          ],
          "min order - 0"
        ],
        "1.7000000000000002": [
          [
            46.608032243662926,
            -81.23707190576353
          ],
          "min order - 0"
        ]
      },
      "333": {
        "0.5": [
          [
            46.58262693178937,
            -81.20161039704823
          ]
        ]
      },
      "348": {
        "0.5": [
          [
            46.58301891494061,
            -81.20000511712087
          ]
        ]
      }
    },
    "10.0": {
      "288": {
        "0.9": [
          [
            46.582510395418204,
            -81.21602022710553
          ]
        ],
        "1.3": [
          [
            46.586123078050804,
            -81.23215217458224
          ],
          "min order - 35.0"
        ]
      },
      "303": {
        "0.9": [
          [
            46.585478013283826,
            -81.21396809684309
          ]
        ]
      },
      "318": {
        "0.9": [
          [
            46.587978225334325,
            -81.21087168446924
          ]
        ]
      },
      "333": {
        "0.9": [
          [
            46.58984060667687,
            -81.20694197892466
          ]
        ]
      }
    }
  }
]

clean_data(x)
# clean_data(null, "null31 CELINA ST", "The Peace Pipe")
